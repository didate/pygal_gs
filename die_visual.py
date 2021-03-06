from die import Die
import pygal

die_1 = Die()

results = []
for roll_num in range(1000):
    results.append(die_1.roll())

# Analyze the results
frequencies = []
for value in range(1, die_1.sides + 1):
    frequencies.append(results.count(value))

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual_svg')
