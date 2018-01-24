import os
from pprint import pprint

import glob

def readfile(file):
	trolleybuses = {}
	time = []
	file = open(file, "r")
	for line in file:
		trol = line.split()[0][:-1]
		times = line.split()[1:]
		list_time = []
		for time in times:
			if not time.isalnum():
				time_ = time[:-1].split(":")
				time_Sec = int(time_[0]) * 60 + int(time_[1])
				list_time.append(time_Sec)
		trolleybuses[trol] = list_time
	file.close()
	return trolleybuses

def read_all_files():
	stations = {}

	station_name = os.listdir('sources')
	for name in station_name:
		if(name) != "station_graph.txt":
			stations[name] = readfile('sources/' + name)
	return stations

def calc_sum(trolleybus):
	sum_= 0
	for i in range(1, len(trolleybus)):
		sum_ += (trolleybus[i] - trolleybus[i-1]) ** 2
	return sum_

def add_one(trolleybuses, trolleybus_for_adding):
	_sum = []
	for t in trolleybuses:
		if trolleybuses[t] != trolleybus_for_adding:
			_sum += trolleybuses[t]

	trolleybus_for_adding = [x+1 for x in trolleybus_for_adding]
	_sum += trolleybus_for_adding
	return _sum
