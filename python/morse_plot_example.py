# -*- coding: utf-8 -*-
"""
An example of how to plot with morseplotlib
"""

# The usual imports
import numpy as np
import matplotlib.pyplot as plt


# This import adds the `morse_plot` function to Matplotlib
# Nothing more to do !
import morseplot.morse_plot




# Create some data to plot
x = np.linspace(0, 10, 1000)
y = np.cos(x)


# The usual plot
plt.plot(x, y)

# Plot with some morse code
plt.morse_plot(x, y+1, morse_text='AB ')


# We can also do it from the axis !
# Get the axis
ax = plt.gca()
# Morse plot. We also added some extra args
ax.morse_plot(x, y+2, morse_text='CD ', label='Morse !', color='k') 
# And finally a line with a prosign
ax.morse_plot(x, y+3, morse_text='~SK~ SK ', label='~SK~ prosign vs SK')


plt.legend()


