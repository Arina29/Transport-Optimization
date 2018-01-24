import numpy as np 
import matplotlib.pyplot as plt 
import os


def graphic(stations_dict, title):
	xy_axes_values = {}
	y_values, y_ticks = [], []
	for i, station_name in enumerate(sorted(stations_dict.keys())):
		y_ticks.append(i+0.25)
		y_values.append(station_name[:-4])
		for trolleybus, time in stations_dict[station_name].items():
			if trolleybus not in xy_axes_values.keys():
				xy_axes_values[trolleybus] = {'x':[], 'y':[]}
				for minutes in time:
					xy_axes_values[trolleybus]['x'].append(minutes)
					xy_axes_values[trolleybus]['y'].append(i+0.25)

			else:
				for minutes in time:
					xy_axes_values[trolleybus]['x'].append(minutes)
					xy_axes_values[trolleybus]['y'].append(i+0.25)

	fig = plt.figure(figsize=(15,4))
	ax = fig.add_subplot(111)
	ax.set_yticks(y_ticks)
	ax.set_yticklabels(y_values)

	colors = gen_colors(len(xy_axes_values.keys()))

	for i, trolleybus in enumerate(xy_axes_values.keys()):
		point = ax.plot(xy_axes_values[trolleybus]['x'], xy_axes_values[trolleybus]['y'], 'o', color = colors[i])
	
	ax.legend(labels = xy_axes_values.keys(), loc ='upper right')
	for i in y_ticks:
		ax.axhline(y = i, color = 'black', linewidth = 1)
		#print(y_values)
	#print(y_ticks)
	plt.title(title)
	#plt.show()

# Generate n differant colors
def gen_colors(n):
    cmap = plt.get_cmap('gist_rainbow')
    colors = cmap(np.linspace(0,1,n))
    return colors