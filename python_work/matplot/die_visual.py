from die import Die
import pygal

die = Die()

results = []

for roll_num in range(100):
	result = die.roll()
	results.append(result)
	
print(results)

frequenies = []

for value in range(1, die.num_size+1):
	frequency = results.count(value)
	frequenies.append(frequency)
	
print(frequenies)

hist = pygal.Bar()

hist.x_labels = ["1", "2","3","4,","5","6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequenies)
hist.render_to_file("die_visual.svg")
