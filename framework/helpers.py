# try to import the cocos module
try:
  import cocos
except:
  print('Cannot import cocos. Did you run \'pip install cocos2d\' ?')

# define a simple HelloWorld() class that inherits from cocos.layer.Layer (making it a sub-class of it)
class HelloWorld(cocos.layer.Layer):
  # __init__ is run every time you instantiate the class
  def __init__(self, msg='Hello, world!', fontName='Times New Roman', fontSize=32, color='white'):
    # Always call super in the constructor
    super(HelloWorld, self).__init__()
    # label will become an object with all the necessary to display a text, with font TimesNewRoman and it will be center-anchored
    # Note: .Label is a subclass of CocosNode
    label = cocos.text.Label(msg , font_name=fontName, font_size=fontSize, anchor_x='center', anchor_y='center')
    # set the position of our text to x:320 y:240
    label.position = (320, 240)
    # add our label as a child. It is a CocosNode object, which know how to render themselves.
    self.add(label)

def main():
  print("This is a module, please import me")

if __name__ == '__main__':
      main()