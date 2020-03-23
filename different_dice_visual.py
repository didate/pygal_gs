from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    results.append(die_1.roll()+die_2.roll())

# Analyze the results
frequencies = []
for value in range(1, die_1.sides+die_2.sides + 1):
    frequencies.append(results.count(value))

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
