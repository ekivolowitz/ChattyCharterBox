import SVGHelperFunctions
import math

class Series():
	def __init__(self, xData = [], yData = [], name = "Series"):
		self.svg = SVGHelperFunctions.svg(name = name, width = 500, height = 500)
		self._xData = xData
		self._yData = [500 - x for x in yData]
		self._minX = min(self._xData)
		self._maxX = max(self._xData)
		self._minY = min(self._yData)
		self._maxY = max(self._yData)
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
		text.rotate(90, (30, SVGHelperFunctions.boxheight(self.svg) / 2))
		self.svg.add(text)
		self.svg.add(line)

	def drawData(self, borderLineWidth = 1):
		previousDataPoint = (0,0)
		for i,xVal in enumerate(self._xData):
			temp_yData = self._yData[i] + 50
			
			print(xVal)
			print(self._maxX)

			xVal = 400 * (xVal / self._maxX)
			xVal += 50

			temp_yData = 400 * temp_yData / self._maxY
			print("xVal is " + str(xVal))
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
				line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (point1[0], point1[1]), rectSize = (1, hyp), color = "#FF0000")
				print(str(previousDataPoint))
				if point1[1] < point2[1]:
					line.rotate(-90 + math.degrees(math.acos(cos)), (line['x'],line['y']))
				else:
					line.rotate(-90 - math.degrees(math.acos(cos)), (line['x'],line['y']))
				previousDataPoint = point2
				self.svg.add(line)




				# point1 = SVGHelperFunctions.addCircle(self.svg, radius = 3, center = (50 + 10, 500-50-180))
				# point2 = SVGHelperFunctions.addCircle(self.svg, radius = 3, center = (50 + 150, 500-50-275))

				# self.svg.add(point1)
				# self.svg.add(point2)

				# point1B = SVGHelperFunctions.addCircle(self.svg, radius = 3, center = (50, 500-50), color = "#FF0000")
				# point2B = SVGHelperFunctions.addCircle(self.svg, radius = 3, center = (point2['cx'] - (point1['cx'] - 50), point2['cy'] + (500 - point1['cy'] - 50) ), color = "#FF0000")
				# # self.svg.add(point1B)
				# # self.svg.add(point2B)

				# hyp = math.sqrt((point1['cx'] - point2['cx']) ** 2 + (point1['cy'] - point2['cy']) ** 2)
				# # print(hyp)

				# x = (hyp, 0)
				# y = (point2B['cx'], point2B['cy'])
				# # print("Point2B x coordinate " + str(point2B['cx']))
				# cos = ((point2B['cx'] - 50) / hyp)
				# print(math.degrees(math.acos(cos)))
				# line = SVGHelperFunctions.addRectangle(self.svg, insertCoordinate = (point1['cx'], point1['cy']), rectSize = (1, hyp), color = "#FF0000")
				# # pprint(vars(line))
				# if point1['cy'] < point2['cy']:
				# 	line.rotate(-90 + math.degrees(math.acos(cos)), (line['x'],line['y']))
				# else:
				# 	line.rotate(-90 - math.degrees(math.acos(cos)), (line['x'],line['y']))
				# self.svg.add(line)
