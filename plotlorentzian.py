# Use pyplot and numpy to design a graph corresponding to a Lorentzian oscillator
import matplotlib.pyplot as plt, numpy as np

N = 100 # Number of points in each axis

A = 1.0 # Gives a useful value to the constant in the equation below
omega_0 = 100.0 # Gives a value to the resonant frequency

min_omega = 0.0 # Defines the minimum acceptable frequency
max_omega = 200.0 # Defines the maximum acceptable frequency
omega_range =  np.linspace(
            min_omega,
            max_omega,
            N
    ) # Defines the whole range of acceptable frequncy values

epsilon_range = [
] # Initializes the list that will store all the permittivity values

# Loop through all frequency values and calculate the permittivity
for omega in omega_range:
    chi = A/(omega_0*omega_0 - omega*omega) # Susceptibility
    epsilon = 1 + chi # Permittivity
    epsilon_range.append(epsilon) # Stores the permittivity values to a list

plt.plot( # Uses pyplot to plot the permittivity vs the frequency
            omega_range,
            epsilon_range
    )

plt.show() # Generates the graph
