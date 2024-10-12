import os
import numpy as np 
import matplotlib.pyplot as plt
import cantera as ct

gas = ct.Solution('gri30.xml')

Dict = {}

for line in open('Reduction_Parameters.txt'):
	if '#' not in line:
		key = line.split()[0]
		value_st = line.split()[2]
		value_end = line.split()[3]
		step = line.split()[4]

		value_st = float(value_st)
		value_end = float(value_end)
		step = int(step)

		all_values = np.linspace(value_st, value_end, step)
		Dict[key] = all_values

Temp = []
Press = []
Phi = []

Temp = Dict['Temperature']
Press = Dict['Pressure']
Press = [i*ct.one_atm for i in Press]
Phi = Dict['Equivalence_Ratio']

sim_time = 5 # 5 Seconds
t_step = 0.01
n_time = np.arange(0, sim_time, t_step)
t_len = len(n_time)

case = 1
for tp in Temp:
	for p in Press:
		for ph in Phi:
			initial_state = tp, p, {'CH4':1,'O2':2/ph,'N2':7.52/ph}

			# Finding the reference Ignition Delay and Maximum Temperature
			gas.TPX = initial_state
			r = ct.IdealGasConstPressureReactor(gas, name='R1')
			sim = ct.ReactorNet([r])

			for i in range(0,gas.n_reactions):
				r.add_sensitivity_reaction(i)

			# set the tolerances for the solution and the sensitivity co-efficients
			sim.rtol = 1.0e-6 # Realtive change in the solution < sim.rtol
			sim.atol = 1.0e-15 # Absolute change in the solution < sim.atol

			sim.rtol_sensitivity = 1.0e-6 #relative change in sensitivity < sim.rtol_sense
			sim.atol_sensitivity = 1.0e-6 #absolute change in sensitivity <sim.atol_sense

			s = np.zeros((t_len, gas.n_reactions))
			ctr = 0
			Smax = np.zeros(gas.n_reactions)

			T_old = tp
			Ignition_delay = []
			tmp = []
			time = 0.0 # Initial Time

			for time in n_time:

				sim.advance(time) # Advancing the reactor w.r.t the time step
				tmp.append(r.T)
				T_new = r.T
				#T_new = T_new[i-1]

				if ((T_new - T_old)>=400):

					Ignition_delay = time

				T_old = T_new
				#T_old = T_old[i-1]
				max_temp = max(tmp)

				for i in range(0,gas.n_reactions): # Sensitivity analysis with respect to temperature 
					s[ctr,i] = (sim.sensitivity(1, i))
					sens = abs(s[:,i])
					sens = max(sens)
				
					Smax[i] = np.maximum(Smax[i], sens)
				ctr += 1

			S = sorted(zip(Smax, gas.reactions()), key=lambda x: -x[0])

			print('\nCase = ' + str(case) + '\nFor Temperature = ' + str(tp) + ' Kelvin, ' + 'Pressure = ' + str(p) + ' bar, ' + 'Equivalence Ratio = ' + str(ph))
			print('\nReference Ignition Delay = ', Ignition_delay)
			print('Reference Maximum Temperature = ', max_temp)

			#Creating a new mechanism and re-run the ignition problem
			red_mech = np.arange(40, gas.n_reactions, 1)

			T_max = []
			ID_max = []
			for r_mech in red_mech:

				reactions = [r[1] for r in S[:r_mech]]

				spec = ct.Species.listFromFile('gri30.cti')

				# create the new reduced mechanism
				gas2 = ct.Solution(thermo='IdealGas', kinetics='GasKinetics',
									species=spec, reactions=reactions)


				# Re-run the ignition problem with the reduced mechanism
				gas2.TPX = initial_state
				r = ct.IdealGasConstPressureReactor(gas2)
				sim = ct.ReactorNet([r])

				time = 0.0 # Initial Time

				# States of Reactor which include all attribiutes of the reactor
				states = ct.SolutionArray(gas, extra = ['t_ms','t'])

				T_old = tp
				tmp = []
				Ignition_delay = []
				for time in n_time:

					sim.advance(time) # Advancing the reactor w.r.t the time step
					tmp.append(r.T)
					T_new = r.T
					#T_new = T_new[i-1]

					if ((T_new - T_old)>=400):

						Ignition_delay = time

					T_old = T_new
					#T_old = T_old[i-1]
					#max_temp = np.max(tmp)
				T_max.append(np.max(tmp))
				ID_max.append(Ignition_delay)

			for n,i in enumerate(ID_max):
				if i == []:
					ID_max[n] = 0

			plt.figure(figsize=(13.0, 7.0))
			plt.subplot(2,1,1)
			plt.title('Reaction Mechanism Reduction for Case ' + str(case))
			plt.plot(red_mech, ID_max, label= 'Reference Ignition Delay = ' + str(Ignition_delay) + 'sec' + '\n Temperature = ' + str(tp) + 'Kelvin' + '\n Pressure = ' + str(p) + 'bar' + '\n Equivalence Ratio = ' + str(ph))
			plt.xlabel('Number of Reactions')
			plt.ylabel('Ignition Delay [ms]')
			plt.legend(loc='best')

			plt.subplot(2,1,2)
			plt.plot(red_mech, T_max, color = 'red', label= 'Reference Maximum Temperature = ' + str(max_temp) + ' Kelvin' + '\n Temperature = ' + str(tp) + 'Kelvin' + '\n Pressure = ' + str(p) + 'bar' + '\n Equivalence Ratio = ' + str(ph))
			plt.xlabel('Number of Reactions')
			plt.ylabel('Maximum Temperature [K]')
			plt.legend(loc='best')
			plt.savefig(' Case '+ str(case) + '.png')
			plt.clf()
			case += 1			