import os
import math
import json

import numpy as np
from sklearn.cluster import KMeans

class Config(object):

	def __init__(self):

		self.sourcePath = "./cycle_Dataset/data_splitted/"
		self.newDataPath = "./cycleData_Merged"
		self.featuresPath = "./feautures"

def getFileList(path):
	fileList = []
	for myFile in os.listdir(path):
		fileList.append(myFile)
	return fileList

def createDir(path):
	if os.path.isdir(path):
		pass
	else:
		os.makedirs(path)

def dataMerge():
	config = Config()
	dirList = getFileList(config.sourcePath)
	createDir(config.newDataPath)

	for myDir in dirList:
		if myDir[-1] == '1':
			continue

		commomDirName = myDir[ : -1]
		newDir = os.path.join(config.newDataPath, commomDirName)
		createDir(newDir)
		fileList_0 = getFileList(os.path.join(config.sourcePath, commomDirName + '0'))
		fileList_1 = getFileList(os.path.join(config.sourcePath, commomDirName + '1'))

		for myFile in fileList_0:
			os.system("cp {0} {1}".format(os.path.join(config.sourcePath, commomDirName + '0', myFile), os.path.join(config.newDataPath, commomDirName, myFile)))

		for myFile in fileList_1:
			os.system("cp {0} {1}".format(os.path.join(config.sourcePath, commomDirName + '1', myFile), os.path.join(config.newDataPath, commomDirName, str(int(myFile) + len(fileList_0)))))

def getMean(x):
	array = np.array(x)
	return np.mean(array)

def getStd(x):
	return np.std(x)

def getRms(x):
	rootSum = 0
	for x_ in x:
		rootSum = rootSum + x_ * x_

	rms = math.sqrt(rootSum / float(len(x)))
	return rms

def featuresExtraction():
	config = Config()
	createDir(config.featuresPath)
	dirList = getFileList(config.newDataPath)

	count = 1

	for myDir in dirList:
		fileList = getFileList(os.path.join(config.newDataPath, myDir))
		createDir(os.path.join(config.featuresPath, myDir))

		for myFile in fileList:
			dataList = [[], [], [], []]

			with open(os.path.join(config.newDataPath, myDir, myFile), "r") as f:
				for line in f:
					tmp = line.split(",")
					dataList[0].append(float(tmp[0]))
					dataList[1].append(float(tmp[1]))
					dataList[2].append(float(tmp[2]))
					dataList[3].append(math.sqrt(float(tmp[0]) * float(tmp[0]) + float(tmp[1]) * float(tmp[1]) + float(tmp[2]) * float(tmp[2])))

			feauture = []
			for i in range(4):
				feauture.append(getMean(dataList[i]))
				feauture.append(getStd(dataList[i]))
				feauture.append(max(dataList[i]))
				feauture.append(min(dataList[i]))
				feauture.append(getRms(dataList[i]))

			with open(os.path.join(config.featuresPath, myDir, myFile), "w+") as f:
				f.write(json.dumps(feauture))

		print(str(count) + ". " + myDir + " OK")
		count = count + 1

def kmeansAnalysis():
	config = Config()
	dirList = getFileList(config.featuresPath)

	featureList = []
	for myDir in dirList:
		fileList = getFileList(os.path.join(config.featuresPath, myDir))

		for myFile in fileList:
			with open(os.path.join(config.featuresPath, myDir, myFile), "r") as f:
				featureList.append(json.loads(f.read()))

	X = np.array(featureList)
	for i in range(744):
		kmeans = KMeans(n_clusters = i + 1, random_state = 0).fit(X)
		with open("log.txt", "a+") as f:
			f.write(str(i + 1) + " " + str(kmeans.inertia_ / float(745)) + "\n")
		print("cluster number: " + str(i + 1) + " OK")

if __name__ == '__main__':
	#dataMerge()
	# featuresExtraction()
	kmeansAnalysis()