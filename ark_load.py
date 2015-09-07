#!/usr/bin/python3
import sys
import struct

class ARK_savegame_reader:
	START_OFFSET = 6

	def __init__(self, file_name, debug=False):
		self.f = open(file_name, 'rb')
		self.debug = debug

	def readUint32(self):
		uint_bytes = self.f.read(4)
		return struct.unpack('I', uint_bytes)[0]

	def readEntry(self, size_multiplier = 1):
		size = self.readUint32()
		return self.f.read(size * size_multiplier)

	def readString(self):
		string = self.readEntry()
		try:
			return string.decode('utf-8')
		except:
			return string

	def readRegion(self):
		cell_name = self.readString()
		if self.debug:
			print("Reading region {0}".format(cell_name))
		number_of_entry_batches = self.readUint32()
		# so far only encountered 0 and 1
		assert(number_of_entry_batches <= 1)
		for entry_batch_index in range(number_of_entry_batches):
			number_of_entries = self.readUint32()
			for i in range(number_of_entries):
				entry = self.readEntry(4)
				if self.debug:
					print('Read entry of size {0}'.format(len(entry)))
		return cell_name
			
	
	def readFile(self):
		self.f.seek(ARK_savegame_reader.START_OFFSET)
		numberOfInitialEntries = self.readUint32()
		initialEntries = [self.readString() for i in range(numberOfInitialEntries)]
		print(initialEntries)
		numberOfCells = self.readUint32()
		cells = [self.readRegion() for i in range(numberOfCells)]	
		print(cells)
		alwaysZero = self.readUint32()
		# so far only encountered 0
		assert(alwaysZero == 0)
		changingNumber = self.readUint32()
		gibberish = self.f.read(16)
		assert(gibberish == b'}@=6\xf6\xef\x00I\xba\x95\xc8\xa6\xc8\xdc(\xdf')
		print(self.readString()) 
		

if len(sys.argv) < 1:
	print("Call {0} <path-to-savefile>".format(sys.argv[0]))
	exit(-1)
else:
	reader = ARK_savegame_reader(sys.argv[1])
	reader.readFile()
