# Name: Population Reproduction Calculator
# Author: William Engel
# Date: Jan 18, 2021

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

data = []
plot_data = [[],[]]

start_pop = int(input("Population at start: "))
child_rate = float(input("Rate of replacement: "))
generations = int(input("Generations: "))

if start_pop != 2:
	data.append({
		'kids' : int(start_pop*0.2),
		'adults' : int(start_pop*0.325),
		'middleage' : int(start_pop*0.325),
		'senior' : int(start_pop*0.15),
		'population' : 0
		})
elif start_pop == 2:
	data.append({
		'kids' : 0,
		'adults' : start_pop,
		'middleage' : 0,
		'senior' : 0,
		'population' : 0
		})

for gen in range(generations):
	couples = int(data[gen-1]['adults']/2)
	new_kids = int(couples*child_rate)

	new_adults = data[gen-1]['kids']
	new_seniors = data[gen-1]['middleage']
	new_middle_age = data[gen-1]['adults']

	data.append({
		'kids' : new_kids,
		'adults' : new_adults,
		'middleage' : new_middle_age,
		'senior' : new_seniors
	})

	population = 0
	for age in range(len(list(data[gen].keys()))):
		ar = list(data[gen].keys())
		population += data[gen][ar[age]]
	data[gen]['population'] = population

	'''
	print("Gen ", gen+1)
	print("|         Kids:    ", data[gen]['kids'])
	print("|       Adults:    ", data[gen]['adults'])
	print("|  Middle Aged:    ", data[gen]['middleage'])
	print("|      Seniors:    ", data[gen]['senior'])
	print("Population:    ", data[gen]['population'])
	print()'''

for l in range(len(data)-1):
	plot_data[0].append(l)
	plot_data[1].append(data[l]['population'])

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(plot_data[0], plot_data[1]);  # Plot some data on the axes.
plt.show()
