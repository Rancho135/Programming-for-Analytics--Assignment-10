
#****************************************************************
#Name:Goodnews Agbadu


#ANA1001 Assignment 10
#****************************************************************

#Plotting 5 cubes:
from matplotlib import pyplot as plt
# Define data.
x_values = [1,2,3,4,5]
y_values = [1, 8, 27, 64, 125]

#Style change
plt.style.use("seaborn")
fig, ax = plt.subplots()

# Make plot.
ax.scatter(x_values, y_values, s=40)

# Customize plot.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value of Cube', fontsize=14)

#set a tick label size
ax.tick_params(axis='both', labelsize=14)

# Save plot.
plt.savefig("cubes.jpg")

#Plotting 5000 cubes:
# Define data.
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

#Style change
plt.style.use("seaborn")
fig, ax = plt.subplots()

# Make plot.
ax.scatter(x_values, y_values, s=40)

# Customize plot.
ax.set_title("Cubes5000", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value of Cube', fontsize=14)

#set a tick label size
ax.tick_params(axis='both', labelsize=14)

# Save plot.
plt.savefig("cubes5000.jpg")

#Apply a colormap to your cubes plot.
#Plotting 5000 cubes:
# Define data.
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

#Style change
plt.style.use("seaborn")
fig, ax = plt.subplots()

# Make plot.
ax.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, s=40)

# Customize plot.
ax.set_title("Cubes5000", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value of Cube', fontsize=14)

#set a tick label size
ax.tick_params(axis='both', labelsize=14)

# Save plot.
plt.savefig("cubes5000cmap.jpg")

'''Create a simulation showing what happens when you roll two eight-sided dice 1000 times. Try to picture what you think the visualization will look like before you run the simulation; then see if your intuition was correct. Gradually increase the number of rolls until you start to see the limits of your system’s capabilities.'''

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D8 dice.
die1 = Die(num_sides=8)
die2 = Die(num_sides=8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    result = die1.roll() + die2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results for rolling two D8 dice 1,000,000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')


'''If you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18. Create a visualization that shows what happens when you roll three D6 dice.'''

from die import Die
# Create three D6 dice.
die1 = Die(num_sides=6)
die2 = Die(num_sides=6)
die3 = Die(num_sides=6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results for rolling 3 D6 dice 1,000,000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')


'''When you roll two dice, you usually add the two numbers together to get the result. Create a visualization that shows what happens if you multiply these numbers instead.'''

# Create two D6 dice.
from die import Die
die1 = Die(num_sides=6)
die2 = Die(num_sides=6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    result = die1.roll() * die2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die1.num_sides * die2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
        title='Results for multiplying 2 D6 dice.',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6*d6.html')