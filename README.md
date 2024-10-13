# GRI Mechanism Reduction

The Python program performs a chemical reaction mechanism reduction using the Cantera library. This is an introductory code on reduction and its effects on different cases. 

It does the following:

1. **Parses Reduction Parameters:** It reads reduction parameters like temperature, pressure, and equivalence ratio from a file `Reduction_Parameters.txt`, storing these in a dictionary.
2. **Simulates Ignition Delay and Temperature:** For different initial conditions (temperature, pressure, and fuel mixture), it sets up a constant pressure reactor to simulate the ignition process,         calculates the ignition delay (time it takes for a significant temperature rise), and records the maximum temperature.
3. **Sensitivity Analysis:** The program uses sensitivity analysis for reactions in the mechanism to determine their importance.
4. **Mechanism Reduction:** It removes unimportant reactions to create a reduced chemical mechanism and reruns the simulation with this reduced mechanism.
5. **Plots Results:** It generates and saves plots comparing ignition delay and maximum temperature against the number of reactions for each test case.

The resulting test cases data is shown below:

| Case number | Temperature (Kelvin) | Pressure (Bar) | Equivalence Ratio (No Units) | Reduced mechanism for Ignition Delay (Number of reactions) | Reduced mechanism for Maximum Temperature (Number of reactions) |
|-------------|----------------------|----------------|-----------------------------|-------------------------------------------------------------|------------------------------------------------------------------|
| 1           | 950                  | 3              | 0.5                         | 72                                                          | 163                                                              |
| 2           | 950                  | 3              | 1                           | 62                                                          | 164                                                              |
| 3           | 950                  | 3              | 1.5                         | 63                                                          | 245                                                              |
| 4           | 950                  | 4              | 0.5                         | 71                                                          | 155                                                              |
| 5           | 950                  | 4              | 1                           | 65                                                          | 199                                                              |
| 6           | 950                  | 4              | 1.5                         | 58                                                          | 230                                                              |
| 7           | 950                  | 5              | 0.5                         | 65                                                          | 157                                                              |
| 8           | 950                  | 5              | 1                           | 67                                                          | 208                                                              |
| 9           | 950                  | 5              | 1.5                         | 60                                                          | 244                                                              |
| 10          | 1050                 | 3              | 0.5                         | 49                                                          | 180                                                              |
| 11          | 1050                 | 3              | 1                           | 43                                                          | 167                                                              |
| 12          | 1050                 | 3              | 1.5                         | 99                                                          | 218                                                              |
| 13          | 1050                 | 4              | 0.5                         | 57                                                          | 208                                                              |
| 14          | 1050                 | 4              | 1                           | 44                                                          | 164                                                              |
| 15          | 1050                 | 4              | 1.5                         | 63                                                          | 240                                                              |
| 16          | 1050                 | 5              | 0.5                         | 83                                                          | 147                                                              |
| 17          | 1050                 | 5              | 1                           | 52                                                          | 158                                                              |
| 18          | 1050                 | 5              | 1.5                         | 65                                                          | 231                                                              |
| 19          | 1150                 | 3              | 0.5                         | 50                                                          | 149                                                              |
| 20          | 1150                 | 3              | 1                           | 72                                                          | 257                                                              |
| 21          | 1150                 | 3              | 1.5                         | 66                                                          | 262                                                              |
| 22          | 1150                 | 4              | 0.5                         | 57                                                          | 192                                                              |
| 23          | 1150                 | 4              | 1                           | 57                                                          | 212                                                              |
| 24          | 1150                 | 4              | 1.5                         | 63                                                          | 261                                                              |
| 25          | 1150                 | 5              | 0.5                         | 48                                                          | 173                                                              |
| 26          | 1150                 | 5              | 1                           | 68                                                          | 226                                                              |
| 27          | 1150                 | 5              | 1.5                         | 69                                                          | 252                                                              |
