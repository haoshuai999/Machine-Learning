from visualize import visualize_3d
import pandas as pd
import sys

def calculate_weight(df):
	df1 = df.loc[:,[0,1]]
	n = len(df1)
	alpha = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 1]
	weights = []

	for column in df1:
		mean = df1.mean(axis = 0)[column]
		std = df1.std(axis = 0)[column]
		for i in range(n):
			df1[column][i] = (df1[column][i] - mean) / std

	df.loc[:,[0,1]] = df1

	for i in range(len(alpha)):
		beta = [0,0,0]
		iteration = 0
		while iteration < 100:
			tempR = 0
			tempbeta = [0,0,0]
			iteration += 1
			for j, row in df.iterrows():
				diff_weight = beta[0] + (beta[1]*row[0]) + (beta[2]*row[1]) - row[2]
				tempR += pow(diff_weight,2) 	
				# beta[0] -= (alpha[i] / n) * diff_weight
				# beta[1] -= (alpha[i] / n) * diff_weight * row[0]
				# beta[2] -= (alpha[i] / n) * diff_weight * row[1]
				tempbeta[0] += diff_weight
				tempbeta[1] += diff_weight * row[0]
				tempbeta[2] += diff_weight * row[1]


			
			R = tempR / (2 * n)
			beta[0] -= (alpha[i] / n) * tempbeta[0]
			beta[1] -= (alpha[i] / n) * tempbeta[1]
			beta[2] -= (alpha[i] / n) * tempbeta[2]
			#print([R,alpha[i]])
		if i == 9:
			while iteration < 200:
				tempR = 0
				tempbeta = [0,0,0]
				iteration += 1
				for j, row in df.iterrows():
					diff_weight = beta[0] + (beta[1]*row[0]) + (beta[2]*row[1]) - row[2]
					tempR += pow(diff_weight,2) 	
					# beta[0] -= (alpha[i] / n) * diff_weight
					# beta[1] -= (alpha[i] / n) * diff_weight * row[0]
					# beta[2] -= (alpha[i] / n) * diff_weight * row[1]
					tempbeta[0] += diff_weight
					tempbeta[1] += diff_weight * row[0]
					tempbeta[2] += diff_weight * row[1]


				
				R = tempR / (2 * n)
				beta[0] -= (alpha[i] / n) * tempbeta[0]
				beta[1] -= (alpha[i] / n) * tempbeta[1]
				beta[2] -= (alpha[i] / n) * tempbeta[2]
				print([R,alpha[i]])

		weights.append([alpha[i],iteration,beta[0],beta[1],beta[2]])

	return weights


if __name__ == "__main__":
	# Get input
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	#======== INPUT2.CSV =======#
	print("Visualizing input2.csv")

	# Import input1.csv, without headers for easier indexing
	data = pd.read_csv(input_file, header=None)

	# Process the data
	result_weights = calculate_weight(data)
	

	# Draw the line
	for i in range(len(result_weights)):
		result = result_weights[i]
		visualize_3d(data, lin_reg_weights=result[2:], alpha=result[0])

	# Write to file
	df = pd.DataFrame(result_weights)
	df.to_csv(path_or_buf=output_file, header=['alpha','num_iters','bias','b_age','b_weight'], index=False)