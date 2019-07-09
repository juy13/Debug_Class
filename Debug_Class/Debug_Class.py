import os
import sys
from accessify import protected

class Debug:

	def __init__(self, file_came, debug_came=True):
		self.debug = debug_came
		self.file = file_came

	@protected
	def log_in_file(self, log_info):
		if self.debug == True:
			with open(self.file, 'a') as handle:
				handle.write(log_info + '\n')
		else:
			pass

	@protected
	def log_on_screen(self, log_info):
		if self.debug == True:
			print(log_info)
		else:
			pass

	@protected
	def log_lambda(self):
		return lambda log_info: print(log_info) if self.debug == True else 0

