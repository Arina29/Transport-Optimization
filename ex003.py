from pprint import pprint
import math
import glob
import copy
import matplotlib.pyplot as plt
import numpy as np
from graph import*

def subtract(station_graph, troll_list, passengers_nr):
	for station in station_graph:
		if(len(troll_list) == 1):
			if troll_list[0] in station_graph[station]['trolleybuses']:
				station_graph[station]['passengers'] -= passengers_nr
		else:
			if troll_list[0] in station_graph[station]['trolleybuses'] and troll_list[1] in station_graph[station]['trolleybuses']:
				station_graph[station]['passengers'] -= passengers_nr

	return station_graph


def update_station_graph(station_graph, final_stations):
	for final in final_stations:
		for station in station_graph:
			if(final == station):
				if(len(station_graph[station]['trolleybuses']) == 1):
					subtract(station_graph, station_graph[station]['trolleybuses'],station_graph[station]['passengers'])
				else:
					subtract(station_graph, station_graph[station]['trolleybuses'][:],station_graph[station]['passengers'])
	return station_graph

def find_neccessary_trol_nr(station_graph, final_stations):
	max_passengers = 70
	d = {}
	for final in final_stations:
		for station in station_graph:
			if(final == station):
				if(len(station_graph[station]['trolleybuses']) == 1):
					d[station_graph[station]['trolleybuses'][0]] = math.ceil(station_graph[station]['passengers']/max_passengers)
				else:
					d[station_graph[station]['trolleybuses'][0]] = math.ceil(station_graph[station]['passengers']/(2*max_passengers))
					d[station_graph[station]['trolleybuses'][1]] = math.ceil(station_graph[station]['passengers']/(2*max_passengers))
	
	modified_station_graph = update_station_graph(station_graph, final_stations)
	for station in modified_station_graph:
		if modified_station_graph[station]['passengers'] > 0:
			d[station] = math.ceil(station_graph[station]['passengers']/max_passengers)
	return d

if __name__ == "__main__":
	result = {}
	result = find_neccessary_trol_nr(get_station_graph(), get_terminal_stations())
	for key in result:
		if isinstance(key, int):
			print('trolleybus {} - nr of trolleybuses: {}'.format(key, result[key]))
		else:
			print('additional trolleybuses at: {} - nr of trolleybuses: {}' .format(key, result[key]))
