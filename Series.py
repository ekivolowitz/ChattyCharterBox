import SVGHelperFunctions
import math

class Series():
	def __init__(self, xData = [], yData = [], name = "Series"):
		self.svg = SVGHelperFunctions.svg(name = name, width = 500, height = 500)
		self._xData = xData
		self._yData = yData
		self._minX = min(xData)
		self._maxX = max(xData)
		self._minY = min(yData)
		self._maxY = max(yData)
		self.addXAxis()
		self.addYAxis()
		self.drawData()

	def addXAxis(self, text = "Time"):
		line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (50,450), rectSize =(440, 1))
		text = SVGHelperFunctions.addText(self.svg, text = text, insertLocation = (SVGHelperFunctions.boxwidth(self.svg) / 2, 470))
		startDate = SVGHelperFunctions.addText(self.svg, text = str(self._minX), insertLocation = (50, 452))
		startDate.rotate(90, center = (50,452))
		self.svg.add(startDate)
		self.svg.add(text)
		self.svg.add(line)

	def addYAxis(self, text = "Y Axis"):
		line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (50,50), rectSize =(1, 400))
		text = SVGHelperFunctions.addText(self.svg, text = text, insertLocation = (30, SVGHelperFunctions.boxheight(self.svg) / 2))
		
		x = 10
		while x < 400:
			
			tick = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (47, 450 - x), rectSize = (3, 1))
			
			if x == 100:
				yText = SVGHelperFunctions.addText(self.svg, text = str(self._maxY / 4), insertLocation = (35, 450 - int(400 * x / self._maxY)))
				self.svg.add(yText)
			elif x == 200:
				yText = SVGHelperFunctions.addText(self.svg, text = str(2 * self._maxY / 4), insertLocation = (35, 450 - int(400 * x / self._maxY)))
				self.svg.add(yText)
			elif x == 300:
				yText = SVGHelperFunctions.addText(self.svg, text = str(3 * self._maxY / 4), insertLocation = (35, 450 - int(400 * x / self._maxY)))
				self.svg.add(yText)
			elif x == 400:
				yText = SVGHelperFunctions.addText(self.svg, text = str(self._maxY), insertLocation = (35, 450 - int(400 * x / self._maxY)))
				self.svg.add(yText)
			self.svg.add(tick)
			x += 10


		text.rotate(90, (30, SVGHelperFunctions.boxheight(self.svg) / 2))
		self.svg.add(text)
		self.svg.add(line)

	def drawData(self, borderLineWidth = 1):
		previousDataPoint = (0,0)

		for i,xVal in enumerate(self._xData):
			temp_yData = self._yData[i]

			print("xVal before normalization " + str(xVal))
			xVal = 400 * (xVal / self._maxX)
			print("xVal after normalization " + str(xVal))
			print("yVal before normalization " + str(temp_yData))
			temp_yData = 400 * (temp_yData / self._maxY)
			print("yVal after normalization " + str(temp_yData))
			if previousDataPoint[0] == 0:
				previousDataPoint = (xVal, temp_yData)
			else:
				point1 = previousDataPoint
				point2 = (xVal, temp_yData)
	
				point1B = (50, 450)
				
				point2B = (point2[0] - point1[0] + 50, point2[1] + (450 - point1[1]))
				

				hyp = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
				
				
				x = (hyp, 0)
				y = (point2B[0], point2B[1])
				cos = ((point2B[0] - 50) / hyp)
				line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (point1[0] + 50 , 450 - point1[1]), rectSize = (1, hyp), color = "#FF0000")
  				# print(str(previousDataPoint))
				if point1[1] > point2[1]:
					line.rotate(-90 + math.degrees(math.acos(cos)), (line['x'],line['y']))
				else:
					line.rotate(-90 - math.degrees(math.acos(cos)), (line['x'],line['y']))
				previousDataPoint = point2
				self.svg.add(line)

