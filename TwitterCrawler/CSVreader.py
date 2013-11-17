from BarCrawlClasses import Bar as Bar

# --- Global Variable
bars = []				# Temporary storage, Change as necessary


def loadAllBarData(fileName, barList):
		inputFile = open(fileName)

		for line in inputFile:
			# --- Split the Line at the Comma
			lineContents = line.split(',')

			# --- Remove WhiteSpace From Each lineContent
			for piece in lineContents:
				piece = piece.strip()

			# --- Save the Contents of the Line
			barName = lineContents[0]
			barTwitterHandle = lineContents[1]
			barFBid = lineContents[2]
			#bar4SquareID = lineContents[3]
			
			barCornerLocs = []
			swCorner = (float(lineContents[4]), float(lineContents[5]))
			nwCorner = (float(lineContents[6]), float(lineContents[7]))
			neCorner = (float(lineContents[8]), float(lineContents[9]))
			seCorner = (float(lineContents[10]), float(lineContents[11]))

			barCornerLocs.append(swCorner)
			barCornerLocs.append(nwCorner)
			barCornerLocs.append(neCorner)
			barCornerLocs.append(seCorner)

			barCenter = (float(lineContents[12]), float(lineContents[13]))

			# --- Create Variable and Store it  **** Change As Necessary for DB **** 
			bar = Bar(barName, barCenter, barCornerLocs, barTwitterHandle, barFBid, "USA", "College Station")
			barList.append(bar)

		# --- Printing Bar Data (for testing)
		for bar in barList:
			bar.printBarData()


if __name__ == "__main__":
	loadAllBarData("BarData.csv", bars)