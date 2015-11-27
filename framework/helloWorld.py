#!/usr/bin/env python3

# try to import the cocos module
try:
  import cocos
except:
  print('Cannot import cocos. Did you run \'pip install cocos2d\' ?')

# import helper Class and methods
import helpers

# Set text on screen
msg = "Hello, world! This is text!!!!111!!11!!!1"

# Set font size
fontSize = 42

# Set screen size
size = (800,600)

# our main function
def main():
  # We initialize the director, that takes care of our main window
  cocos.director.director.init(width=size[0], height=size[1], autoscale=True, resizable=True)

  # We instantiate hello_layer with our HelloWorld() class
  hello_layer = helpers.HelloWorld(msg=msg, fontSize=fontSize)
  # Now we create a .Scene and pass our HelloWorld() object stored in hello_layer, as a child
  main_scene = cocos.scene.Scene(hello_layer)
  # All setup now. Let's run our main_scene
  cocos.director.director.run(main_scene)
  # The above could have been compacted to:
  # cocos.director.director.run(cocos.scene.Scene(helpers.HelloWorld()))

if __name__ == '__main__': main()