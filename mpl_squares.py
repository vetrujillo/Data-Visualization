#Importing module as alias 'plt'
import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#Variable 'fig' represents entire figure or collection of plots
#Variable 'ax' represents a single plot in the figure and is most used variable
#subplots() generate one or more plots in same figure
fig, ax = plt.subplots()

#plot() method tries to plot data given
ax.plot(input_values, squares, linewidth=3)

#Set chart and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

#Opens Matplotlib's viewer and displays plot
plt.show()