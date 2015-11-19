#!/usr/bin/env python3

class KeyDisplay(cocos.layer.Layer):
	is_event_handler = True
	def __init__(self);
		super(KeyDisplay, self).__init__()
		self.text = cocos.text.Label("", x=100, y=280)

		self.key_pressed = set()
		self.update_text()
		self.add(self.text)

	def update(self):
		key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
		text = 'Keys: ' + ','.join(key_names)
		self.text.element.text = text

	def on_key_press(self, key, modifiers):
		self.keys_pressed.add(key)
		self.update.text()

	def on_key_release(self, key, modifiers):
		self.keys_pressed.remove(key)
		self.update.text()

	def update_text(self):
		key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
		text = 'Keys: ' + ','.join(key_names)
		self.text.element.text = text

	