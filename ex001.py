from pprint import pprint
import utils
import matplotlib.pyplot as plt 
import os

def minimize(filename):
	
	trolleybuses = utils.readfile(filename)
	minimum_prec, minimum = 15000000000, 10000000000
	max_interval = 20

	while(minimum_prec > minimum):
		T_prime, alpha = {}, {}
		trolleybus = []
		for key in trolleybuses.keys():
			T_prime[key] = utils.add_one(trolleybuses, trolleybuses[key])
		for key in T_prime.keys():	
			T_prime[key].sort()
			alpha[key] = utils.calc_sum(T_prime[key])
		print(alpha)
		
		minimum_key = min(alpha, key = alpha.get)
		minimum_prec = minimum
		minimum = alpha[minimum_key]

		print(minimum_key, minimum)
		trolleybuses[minimum_key] = [x+1 for x in trolleybuses[minimum_key]]

	visualise(trolleybuses)
	plt.title("New time-table")
	visualise(utils.readfile("sources/stefan_cel_mare.txt"))
	plt.title("Old time-table")
	plt.show()
	return trolleybuses

def visualise(trolleybuses):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	for key in trolleybuses.keys():
		y = []
		for i in range(len(trolleybuses[key])):
			y.append(1)
		ax.plot(trolleybuses[key], y, 'o')
	ax.legend(trolleybuses)

def maximum_interval(trolleybuses):
	all_trolleybuses, interval = [], []
	for key in trolleybuses.keys():
		all_trolleybuses += trolleybuses[key]
	all_trolleybuses.sort()
	for i in range(1, len(all_trolleybuses)):
		interval.append(all_trolleybuses[i] - all_trolleybuses[i-1])
	return max(interval)
		


if __name__ == "__main__":
	minimize("sources/stefan_cel_mare.txt")
	