import matplotlib.pyplot as plt

input_values = [1, 2,3,4,5]
squares = [1, 4, 9, 16, 25]

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, edgecolor="none", s=80)
#plt.scatter(input_values, squares,c ="red", edgecolor="none", s=80)
#plt.scatter(input_values, squares,c =(0,1,0), edgecolor="none", s=80)
plt.scatter(input_values, squares,c =squares, cmap=plt.cm.Blues, edgecolor="none", s=80)
#plt.axis([0,1100,0,1100000])
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 24)
plt.ylabel("square of value", fontsize = 24)
plt.tick_params(axis="both", which="major", labelsize = 14)
plt.show()
plt.savefig("square_scatter.png", bbox_inches="tight")
