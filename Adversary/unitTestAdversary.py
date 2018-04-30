from adversary import Adversary

def test_binarySearch(ad):
	Seq = [0.0, 0.13, 0.24, 0.31, 0.49, 0.56, 0.61, 0.77, 0.84, 0.98] 
	testItem = [0.0, 0.04, 0.13, 0.156, 0.24, 0.30, 0.31, 0.371, 0.49, 0.491, 0.56, 0.586, 0.61, 0.666, 0.77, 0.79, 0.84, 0.954, 0.98, 0.999]

	for i in testItem:
		pos = ad.binarySearch(i, Seq)
		print(pos)


if __name__ == '__main__':

	ad = Adversary("kmeans", [])
	test_binarySearch(ad)
