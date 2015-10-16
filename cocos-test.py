#!/usr/bin/env python3
# Python Cocos2d Game Development
# Part 1: Getting Started

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-1/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)

# Imports
import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director

# Screen size
size = (800,600)

# Arbitrary variable we include later in out text label, attention to the scope!
deltaTime = 42

# Player class called Me() <--- Needs better name
class Me(actions.Move):

  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    super(Me, self).step(dt) # Run step function on the parent class.
    # Determine velocity based on keyboard inputs.
    velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
    velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])

    # Set the object's velocity.
    self.target.velocity = (velocity_x, velocity_y)

# Main class
def main():
  global keyboard # Declare this as global so it can be accessed within class methods.
  # Initialize the window
  director.init(width=size[0], height=size[1], autoscale=True, resizable=True)

  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()
  molecule = sprite.Sprite('sprites/molecule.png')
  molecule.scale = 2
  player_layer.add(molecule, z=1)
  scale = actions.ScaleBy(3, duration=2)

  # Add a Label, because we can.
  label = cocos.text.Label('Hello, world@' + str(deltaTime), font_name='Times New Roman', font_size=32, anchor_x='left', anchor_y='center')
  label.position = 0, size[1]/2
  label.velocity = 0, 0
  player_layer.add(label)

  # Set initial position and velocity.
  molecule.position = (size[0]/2, size[1]/2)
  molecule.velocity = (0, 0)

  # Set the sprite's movement class and run some actions.
  molecule.do(actions.Repeat(scale + actions.Reverse(scale)))
  
  label.do(Me())

  # Rotate the entire player_layer (includes ALL nodes, will rotate ONCE)
  player_layer.do(actions.RotateBy(360, duration=10))
  
  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer)

  # Set the sprite's movement class.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
  main()
