from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
import warnings
import functools

def deprecated(func):
	"""This is a decorator which can be used to mark functions as deprecated.
	It will result in a warning being emitted when the function is used.
	"""
	@functools.wraps(func)
	def new_func(*args, **kwargs):
		warnings.warn_explicit(
			"You've called a deprecated function. Maybe this function needs updating to the new package. {}".format(func.__name__),
			category=DeprecationWarning,
			filename=func.__code__.co_filename,
			lineno=func.__code__.co_firstlineno + 1
		)
		return func(*args, **kwargs)
	return new_func


