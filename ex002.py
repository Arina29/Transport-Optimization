from pprint import pprint
import utils
import visualize_data
import matplotlib.pyplot as plt 
import os

def minimize(filename, station_dict):
	minimum_prec, minimum = 15000000000, 10000000000
	trolleybuses = utils.readfile(filename)
	T_prime, alpha = {}, {}
	troleibus =[]

	while(minimum_prec > minimum):
		troleibus=[]
		for key in trolleybuses.keys():
			T_prime[key] = utils.add_one(trolleybuses, trolleybuses[key])
		for key in T_prime.keys():	
			T_prime[key].sort()
			alpha[key] = utils.calc_sum(T_prime[key])

		minimum_key = min(alpha, key=alpha.get)
		minimum_prec = minimum
		minimum = alpha[minimum_key]

		for key in station_dict:
			for bus in station_dict[key]:
				if(minimum_key == bus):
					station_dict[key][bus] = [x+1 for x in station_dict[key][bus]]

	return station_dict

def minimize_all(station_dict):
	station_name = os.listdir('sources')
	for name in station_name:
		if(name) != "station_graph.txt":
			new_time_table = minimize('sources/' + name, station_dict)
	visualize_data.graphic(utils.read_all_files(), 'OLD TIME TABLE')
	visualize_data.graphic(station_dict, 'NEW TIME TABLE')
	plt.show()
	return new_time_table

if __name__ == "__main__":
	station_dict = utils.read_all_files()
	minimize_all(station_dict)