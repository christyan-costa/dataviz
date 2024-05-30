from die import Die

# Create a D6 (6 sided die).
die = Die()

# Make some rolls, and store the results in a list.
results = [die.roll() for _ in range(1000)]

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

