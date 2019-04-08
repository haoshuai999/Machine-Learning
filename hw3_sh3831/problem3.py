from sklearn.cluster import KMeans
from PIL import Image
import numpy as np

def calculate_cluster(data, cluster):
	kmeans = KMeans(n_clusters=cluster, random_state=0).fit(data)
	# print(kmeans.labels_)
	# print(kmeans.cluster_centers_)

	result = [kmeans.labels_,kmeans.cluster_centers_]

	return result

if __name__ == "__main__":

	# Read trees.png
	im = Image.open('trees.png')
	rgb_im = im.convert('RGB')
	data = np.array(rgb_im.getdata(band=None),dtype=object)

	# Process the data
	cluster_center = [2,6,50]
	for index in range(len(cluster_center)):
		result = calculate_cluster(data,cluster_center[index])

		# Output and visualize the data
		output = []
		for j in range(len(result[0])):
			for i in range(len(result[1])):
				if result[0][j] == i:
					convert_result = []
					temp_result = result[1][i].tolist()
					for item in temp_result:
						convert_result.append(int(item))
					output.append(tuple(convert_result))
					#output.append(result[1][i])

		# output = bytes(output)
		# Image.frombytes('RGB',(350,258),output).show()
		print("Show the image when k = %d" % cluster_center[index])
		im2 = Image.new('RGB',(350,258))
		im2.putdata(output)
		im2.show()