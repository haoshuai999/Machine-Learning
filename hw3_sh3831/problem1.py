from visualize import visualize_scatter
import pandas as pd
import sys

def calculate_weight(df):
	weights = [0,0,0]
	convergence = 0
	count = 0
	all_weights = []

	while convergence != 3:
		weights_copy = weights[:]
		all_weights.append(weights_copy)
		convergence = 0
		for i, row in df.iterrows():
			sum_weight = weights[0]*row[0] + weights[1]*row[1] + weights[2]
			
			if row[2] * sum_weight <= 0:
				weights[0] += row[2] * row[0]
				weights[1] += row[2] * row[1]
				weights[2] += row[2]
		for j in range(len(weights)):
			if weights[j] == all_weights[count][j]:
				convergence += 1
		count += 1

	return all_weights


if __name__ == "__main__":
	# Get input
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	#======== INPUT1.CSV =======#
	print("Visualizing input1.csv")

	# Import input1.csv, without headers for easier indexing
	data = pd.read_csv(input_file, header=None)
	result_weights = calculate_weight(data)
	result = result_weights[-1]

	# Draw the line
	visualize_scatter(data, weights=result)

	# Write to file
	df = pd.DataFrame(result_weights)
	df.to_csv(path_or_buf=output_file, header=['weight_1','weight_2','b'], index=False)