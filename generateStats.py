def genStats():
	downloadStats = []
	

	count = 0
	with open("data/dat", 'r') as f:
		for line in f:
			if count == 0:
				startDate = line.split("_")[0]
				startDate = startDate.replace("-", "/")
			downloadStats.append(int(line.split(" ")[1].replace(",", "")))
			endDate = line.split("_")[0]
			endDate = endDate.replace("-", "/")

	print(str(downloadStats))
	print("Start date is " + startDate)
	print("End date is " + endDate)
	ts = plt.Series(downloadStats, index=date_range(startDate, periods = len(downloadStats)))
	ts.plot()



















if __name__ == "__main__":
	genStats()