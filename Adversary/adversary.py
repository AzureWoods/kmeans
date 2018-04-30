'''
@description: This code is used to generate different samples for attacks on different classifiers using kmeans++ method.
@author: MeL0dy
@date: 2018/5/1
'''
import random

class Adversary(object):

	def __init__(self, cl_name, data):
		'''
		@cl_name: Name of the classifier you want to attack
		@data: All data used to attack
		'''

		self.classifier = cl_name
		self.dataSet = data

	def getMean(self):
		'''
		Calculate the mean vector of all data used to attack.
		'''
		mean_vector = []
		num = len(self.dataSet)
		featureLength = len(self.dataSet[0])

		for i in range(featureLength):
			mean_vector.append(0)

		for i in range(num):
			for j in range(featureLength):
				mean_vector[j] = mean_vector[j] + self.dataSet[i][j]

		for i in range(featureLength):
			mean_vector[i] = mean_vector[i] / float(num)

		return mean_vector

	def Authentication(self, attack):
		'''
		@attack: Sample used to attack

		TODO: According to different classifiers which the user wants to attack, 
		call different functions for authentication and get results back.

		Need fixed: Here I need the interfaces of all the classifier code you guys developed.
		'''

		Auth = False

		# if attack == "...":
		# 	Auth = ...
		# elif attack == "...":
		# 	Auth = ...
		# ...
		# else Auth = ...

		return Auth

	def calNearestDist(self, data, allSample):
		'''
		@data: A single sample vector.
		@allSample: All samples which have been used as attack-samples before.
	
		TODO: Calculate the square of distances between the single sample and all attack samples used, then return the smallest one.
		'''
		dist = []
		featureLength = len(data)

		for sample in allSample:

			curDist = 0
			for i in range(featureLength):
				curDist = curDist + (data[i] - sample[i]) * (data[i] - sample[i])

			dist.append(curDist)

		dist.sort(reverse = True)
		return dist[0]

	def binarySearch(self, k, Seq):
		'''
		@k: Value to search.
		@Seq: Sequence used for searching.

		TODO: Find the position of the biggest number in the sequence whose value is smaller than k.
		'''
		l = 0
		r = len(Seq) - 1
		while r - l >= 2:
			mid = (l + r) >> 1
			# print("({0}, {1})".format(l, r))
			if(Seq[mid] <= k):
				l = mid
			else:
				r = mid

		return l

	def attackProcess(self, limitedNum):
		'''
		@limitedNum: The upper bound of the number to make tries.

		TODO: Generate attack samples for authentication and return the index of the first successful attempt.(-1 means all tries on attacks failed.)
		'''

		attackSample = []
		mean_sample = getMean()
		attackSample.append(mean_sample)

		Auth = False
		tryNum = 1
		dataNum = len(self.dataSet)

		while tryNum <= limitedNum:

			if Authentication(attackSample[tryNum - 1]) == True:
				Auth = True
				break

			distance = []
			for i in range(dataNum):
				distance.append(calNearestDist(self.dataSet[i], attackSample))

			probDist = []
			totalDist = sum(distance)
			for i in range(dataNum):
				distance[i] = distance[i] / totalDist

			probDist.append(0.0)
			for i in range(dataNum - 1):
				tmp = probDist[i]
				probDist.append(tmp + distance[i])
			probDist.append(1.0)
			
			roll = random.random()
			pos = binarySearch(roll, probDist)

			attackSample.append(self.dataSet[pos])
			tryNum = tryNum + 1

		if Auth == True:
			return tryNum - 1
		else:
			return -1