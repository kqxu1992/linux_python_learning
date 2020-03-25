import matplotlib.pyplot as plt

#def show_matplot():

input_values = [1, 2,3,4,5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth = 5)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 24)
plt.ylabel("square of value", fontsize = 24)
plt.tick_params(axis="both", labelsize = 14)
plt.show()
	
#show_matplot()
