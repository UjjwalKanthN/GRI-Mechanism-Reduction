# GRI Mechanism Reduction

The Python program performs a chemical reaction mechanism reduction using the Cantera library. It does the following:

1. Reads Reduction Parameters: It reads reduction parameters like temperature, pressure, and equivalence ratio from a file (Reduction_Parameters.txt), storing these in a dictionary.
2. Simulates Ignition Delay and Temperature: For different initial conditions (temperature, pressure, and fuel mixture), it sets up a constant pressure reactor to simulate the ignition process,         calculates the ignition delay (time it takes for a significant temperature rise), and records the maximum temperature.
3. Sensitivity Analysis: The program uses sensitivity analysis for reactions in the mechanism to determine their importance.
4. Mechanism Reduction: It removes unimportant reactions to create a reduced chemical mechanism and reruns the simulation with this reduced mechanism.
5. Plots Results: It generates and saves plots comparing ignition delay and maximum temperature against the number of reactions for each test case.

 
![Reduced Mechanisms Table](https://github.com/user-attachments/assets/e4378593-e37d-4fa0-be26-99f642f065c1)
