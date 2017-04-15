import Series as s
import SVGHelperFunctions



xdat = [50,100]
ydat = [50,100]


series = s.Series(xdat, ydat, "test")

series.svg.save()