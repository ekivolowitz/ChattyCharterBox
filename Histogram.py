import sys
import math
import SVGHelperFunctions




class Histogram():
	def __init__(self, data = [], name = "Histogram", binAccuracy = 0.2):
		self.svg = SVGHelperFunctions.svg(name = name, width = 500, height = 500)
		self._bins = {}
		self._binAccuracy = binAccuracy
		self._toDecimalPoint = self.toDecimalPoint()
		self._minData = min(data)
		self._maxData = max(data)
		self.generateBins(self._minData, self._maxData, binAccuracy)
		self.parseData(data)
		self.drawData()
	def save(self):
		self.svg.save()

	def generateBins(self, _min, _max, step):
		current = _min
		while current <= _max:
			self._bins[round(current, self._toDecimalPoint)] = 0
			current += step

	def toDecimalPoint(self):
		toDecimalPlace = 0
		accuracyAsString = str(self._binAccuracy)
		splitAccuracy = accuracyAsString.split(".")
		if len(splitAccuracy) > 1:
			toDecimalPlace = len(splitAccuracy[1])
		return toDecimalPlace

	def parseData(self, data):
		for elem in data:
			x = round(elem / self._binAccuracy) * self._binAccuracy
			x = round(x, self._toDecimalPoint)
			try:
				self._bins[x] += 1
			except:
				print(str(x) + " failed to find a key in self._bins in the Histogram you tried to generate.")

	
	def addXAxis(self, text = "X Axis"):
		line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (50,450), rectSize =(440, 1))
		text = SVGHelperFunctions.addText(self.svg, text = text, insertLocation = (SVGHelperFunctions.boxwidth(self.svg) / 2, 470))
		self.svg.add(text)
		self.svg.add(line)

	def addYAxis(self, text = "Y Axis"):
		line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (50,50), rectSize =(1, 400))
		text = SVGHelperFunctions.addText(self.svg, text = text, insertLocation = (30, SVGHelperFunctions.boxheight(self.svg) / 2))
		SVGHelperFunctions.rotateObject(text, 90, (30, SVGHelperFunctions.boxheight(self.svg) / 2))
		self.svg.add(text)
		self.svg.add(line)


	def addTitle(self, text = "Title"):
		text = SVGHelperFunctions.addText(self.svg, text = text, insertLocation = (SVGHelperFunctions.boxwidth(self.svg) / 2 - 20, 30), fontSize = "30px")
		self.svg.add(text)

	def drawData(self, borderLineWidth = 1):
		mode = 0
		for key in self._bins.keys():
			if self._bins[key] > mode:
				mode = self._bins[key]
		binWidth = math.floor((SVGHelperFunctions.boxwidth(self.svg) - 60) / len(self._bins))
		
		currentX = 51
		for key in self._bins.keys():
			binHeight = 400/mode * self._bins[key]
			square = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (currentX, 450 - binHeight), rectSize = (binWidth, binHeight), color = '#FF0000')
			currentX += binWidth
			leftLine = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (currentX - binWidth, 450 - binHeight), rectSize = (borderLineWidth, binHeight), color = '#000')
			rightLine = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (currentX - binWidth, 450 - binHeight), rectSize = (binWidth, borderLineWidth), color = '#000')
			topLine = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (currentX  - borderLineWidth, 450 - binHeight), rectSize = (borderLineWidth, binHeight), color = '#000')
			self.svg.add(square)
			self.svg.add(leftLine)
			self.svg.add(rightLine)
			self.svg.add(topLine)


