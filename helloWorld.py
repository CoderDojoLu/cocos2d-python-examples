#!/usr/bin/env python3

# try to import the cocos module
try:
	import cocos
except:
	print('Cannot import cocos. Did you run \'pip install cocos2d\' ?')

# define a simple HelloWorld() class that inherits from cocos.layer.Layer (making it a sub-class of it)
class HelloWorld(cocos.layer.Layer):
	# __init__ is run every time you instantiate the class
	def __init__(self):
		# Always call super in the constructor
		super(HelloWorld, self).__init__()
		# label will become an object with all the necessary to display a text, with font TimesNewRoman and it will be center-anchored
		# Note: .Label is a subclass of CocosNode
		label = cocos.text.Label('Hello, world', font_name='Times New Roman', font_size=32, anchor_x='center', anchor_y='center')
		# set the position of our text to x:320 y:240
		label.position = (320, 240)
		# add our label as a child. It is a CocosNode object, which know how to render themselves.
		self.add(label)

# our main function
def main():
	# We initialize the director, that takes care of our main window
	cocos.director.director.init()
	# We instantiate hello_layer with our HelloWorld() class
	hello_layer = HelloWorld()
	# Now we create a .Scene and pass our HelloWorld() object stored in hello_layer, as a child
	main_scene = cocos.scene.Scene(hello_layer)
	# All setup now. Let's run our main_scene
	cocos.director.director.run(main_scene)
	# The above could have been compacted to:
	# cocos.director.director.run(cocos.scene.Scene(HelloWorld()))

if __name__ == '__main__': main()