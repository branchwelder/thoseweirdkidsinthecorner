"""
basic echo server right now; prints data received from phone.
the person who wrote "https://docs.python.org/2/howto/sockets.html" is a great human being.
"""

import socket
import sys
import string
import math


class EchoSocket(object):
	"""
	Basic socket, to echo some sort of input/output.
	"""

	def __init__(self, port=8888):
		#============ Socket setup ===============================
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.host = ''
		self.port = port #this is an arbitrary number right now.
		print "Binding socket to ", self.host, " : ", self.port
		self.sock.bind((self.host, self.port))
		self.sock.listen(5)
		self.all_results = []

	def read_socket(self, msg_bytes=32):
		"""
		reads msg_bytes bytes from self.sock
		"""
		while True:
			c, addr = self.sock.accept()
			print "got connection from ", addr
			buf = c.recv(64)
			if len(buf) > 0:
				print "Received: ", str(buf)
				self.all_results.append(buf)
				break
		c.close()
		return buf

if __name__ == "__main__":
	es = EchoSocket()
	while True:
		es.read_socket()
		print es.all_results