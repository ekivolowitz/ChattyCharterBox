__author__ = 'Kivolowitz'
import svgwrite
from svgwrite import base
from svgwrite import shapes
from svgwrite import mixins


def toString(svg):
	'''
	Returns the xml tree of the object and all its subelements, but not the elements
	that this object is a subelement of.
	'''
	return svg.tostring()

def circleDiameter(svg):
	return (svg['r'] * 2)


def boxheight(svg):
	'''
	Return the height attribute of the object, if applicable. There are certain objects that
	Do not have a height attribute, for example a line doesn't have a height attribute. 
	'''
	try:
		return svg['height']
	except:
		return -1


def boxwidth(svg):
	'''
	Retuns the width attribute of the object, if applicable.
	'''
	try:
		return svg['width']
	except:
		return -1

def svg(x = 0, y = 0, name="output",  size=("100%", "100%"), width = 0, height = 0, fill = '#FFF', **kwargs):
	'''
	Creates the outer-layer SVG Element
	This is the root element of the svg.
	@param string name - string name of the svg you're creating. Defaults to output (with svg append to it later.)
	@param int x - x location of the svg you're placing.
	@param int y - y location of the svg you're placing.
	@param tuple(string, string) - defaults to 100% size of image.
	@param int width - width of the object you're placing. If either width or height is
		less than or equal to 0, it will default to the size tuple for sizing.
	@param int height - height of the object you're placing. If either width or height is
		less than or equal to 0, it will default to the size tuple for sizing.
	@param **kwards - specifying that this function uses keyword arguments.
	@return svg object from svgwrite.Drawing 
	'''
	if ".svg" in name:
		name = name.strip(".svg")
	svgImg = None
	if width <= 0 or height <= 0:
		svgImg = svgwrite.Drawing(name + '.svg', size=size)
	else:
		svgImg = svgwrite.Drawing(name + '.svg', size=(width, height))
	svgImg['fill'] = fill
	return svgImg

def translate(svg, x):
	return svg.translate(x)

def rotateObject(svg, angle, center = (0,0)):
	'''
	Rotate any svg object by any amout in degrees. 
	@param svg - object to rotate
	@param angle - amount to rotate by in degrees. 
	@return void
	'''
	pass
	# svg.rotate(angle, center)


def addLine(svg, startPointTuple = (0, 0), endPointTuple = (500, 500), color = '#000'):
	return svg.line(start = startPointTuple, end = endPointTuple, fill = color)

def addCircle(svg, radius = 1, center=(0,0), color = '#000'):
	'''
	@param radius - integer value of the radius of the circle.
	@param center - tuple of integers (x,y) that form the center of the circle.
	@param color - string of the color in which to fill the shape. Defaults to red, however it accepts
				   '#HEXValue'
	@return circle SVG shape. 
	'''
	return svg.circle(center = center, r = radius, fill = color)
def addRectangle(svg, insertCoordinate = (0,0), rectSize = (0,0), color = '#000'):
	'''
	@param insert - tuple of integers (x,y) of the point to insert the shape at
	@param rectSize - tuple of integers (width, height) of how large to make the rectangle.
	@param color - string of hex for coloring. 
	'''
	return svg.rect(insert = insertCoordinate, size = rectSize, fill = color)

def addText(svg, text='None', insertLocation = (0,0), color='#000', fontSize = "10px"):
	return svg.text(text, insert = insertLocation, fill = color, font_size = fontSize)


def changeColorOfObject(svg = None, fill = "#000"):
	'''
	@param object - the object to change the color of.
	@param fill - the color to change the object to. Defaults to black. Must be given in hex
				  or the name of the color ie 'blue', 'red', 'green'.
	'''
	svg['fill'] = fill

# if __name__ == "__main__":
	'''
	Example usage of creating a backdrop and adding an element to it:
	
	# Background element must be created with svg(*stuff*)
	example = svg(0,0,name="test", width=500, height=500)

	# All subelements are created by passing example, and then returned by the function. This is done so that
	# we can modify attributes (rotation, color, etc) about the object without recreating it. Simply use
	# rotateObject(object, 45). This rotates any object passed to it by 45 degrees.	
	circle = addCircle(example, radius = 10, center = (250, 250), color = '#FF0000')
	
	Main object add another object. This can also be used to add subobjects to other subobjects.
	example.add(circle)
	
	

	#must be at the end of the file.
	example.save()

	'''




