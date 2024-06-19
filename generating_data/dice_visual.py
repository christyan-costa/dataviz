from die import Die
import pygal

# Create two D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyze the results.
frequencies = []
min_result = 2
max_result = die_1.num_sides + die_2.num_sides

for value in range(min_result, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = "Result"
hist._y_title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
