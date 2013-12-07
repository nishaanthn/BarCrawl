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
			barTwitterID = lineContents[2]
			barFBid = lineContents[3]
			#bar4SquareID = lineContents[4]
			
			barCornerLocs = []
			
			for i in range(5,13):
				if not lineContents[i]:
					lineContents.append(9999999)
				if lineContents[i] == "":
					lineContents[i] = 9999999

			swCorner = (float(lineContents[5]), float(lineContents[6]))
			nwCorner = (float(lineContents[7]), float(lineContents[8]))
			neCorner = (float(lineContents[9]), float(lineContents[10]))
			seCorner = (float(lineContents[11]), float(lineContents[12]))


			barCornerLocs.append(swCorner)
			barCornerLocs.append(nwCorner)
			barCornerLocs.append(neCorner)
			barCornerLocs.append(seCorner)

			barCenter = (float(lineContents[13]), float(lineContents[14]))

			# --- Create Variable and Store it  **** Change As Necessary for DB **** 
			bar = Bar(barName, barCenter, barCornerLocs, barTwitterHandle, barTwitterID, barFBid, "USA", "College Station")
			barList.append(bar)

		# --- Printing Bar Data (for testing)
		#for bar in barList:
			#bar.printBarData()


if __name__ == "__main__":
	loadAllBarData("BarData.csv", bars)