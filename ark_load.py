#!/usr/bin/python3
import sys
import struct

class ARK_savegame_reader:
	START_OFFSET = 6

	def __init__(self, file_name, debug=False):
		self.f = open(file_name, 'rb')
		self.debug = debug
		self.read_PrimalItemConsumable_X_C = lambda: self.read_regular_indexed(1, 1, 1, 9)
		self.read_Thatch_Floor_C = lambda: self.read_regular_indexed(0, 1, 1, 15)
		self.read_Thatch_Wall_Small_C = lambda: self.read_regular_indexed(0, 1, 1, 15)
		self.read_Campfire_C = lambda: self.read_regular_indexed(0, 1, 0, 15)
		self.read_PrimalItemArmor_X_C = lambda: self.read_regular_indexed(1, 1, 1, 9)
		self.read_PrimalItemConsumable_X_C = lambda: self.read_regular_indexed(1, 1, 1, 9)
		self.read_LadderBP_C = lambda: self.read_regular_indexed(0, 1, 1, 15)

	def readUint32(self):
		uint_bytes = self.f.read(4)
		return struct.unpack('I', uint_bytes)[0]

	def peekUint32(self):
		pos = self.f.tell()
		uint = self.readUint32()
		self.seek(pos)
		return uint

	def readEntry(self, size_multiplier = 1):
		size = self.readUint32()
		return self.f.read(size * size_multiplier)

	def readString(self):
		string = self.readEntry()[:-1] # omit trailing null terminator
		try:
			return string.decode('utf-8')
		except:
			return string

	def peekString(self):
		pos = self.f.tell()
		string = self.readString()
		self.f.seek(pos)
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

	def readUint32_equals(self, expected_value):
		read_value = self.readUint32()
		assert read_value == expected_value, '{0} == {1}'.format(read_value, expected_value)

	def readBytes_equals(self, expected_value):
		read_value = self.f.read(len(expected_value))
		assert read_value == expected_value, '{0} == {1}'.format(read_value, expected_value)

	def readString_equals(self, expected_value):
		read_value = self.readString()
		assert read_value == expected_value, '"{0}" == "{1}"'.format(read_value, expected_value)

	def read_regular_indexed(self, expected_value_of_first_uint, 
					expected_value_of_second_uint,
			   		descriptor_index,
					number_of_trailing_words):
		character = self.readString()
		descriptor = character.split('_')[descriptor_index]
		self.readUint32_equals(expected_value_of_first_uint)
		self.readUint32_equals(expected_value_of_second_uint)
		indexed = self.readString()
		index = int(indexed.split('_')[-1])
		self.f.read(number_of_trailing_words * 4)
		return (descriptor, index)

		

	def read_ShooterGameState(self):
		self.readString_equals('ShooterGameState')
		self.readUint32_equals(0)
		number_of_game_states = self.readUint32()
		# so far only encountered 1 here
		assert(number_of_game_states == 1)
		for i in range(number_of_game_states):
			self.readString_equals('ShooterGameState_{0}'.format(i))
			self.f.read(9 * 4)

	def read_InstancedFoliageActor(self):
		self.readString_equals('InstancedFoliageActor')
		self.readUint32_equals(0)
		number_of_actors = self.readUint32()
		# only encountered value 1
		assert(number_of_actors == 1)
		for i in range(number_of_actors):
			self.readString_equals('InstancedFoliageActor_{0}'.format(i))
			self.f.read(15 * 4)

	def read_MatineeActor(self):
		self.readString_equals('MatineeActor')
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		self.readString_equals('Matinee_DayTime')
		self.f.read(15*4)

	def read_DinoCharacterStatusComponent_BP_X_C(self, X):
		fixup = {'Megalodon':'Mega'}
		if X in fixup:
			X = fixup[X]
		if X == 'Coel':
			self.readString_equals('DinoCharacterStatusComponent_BP_C'.format(X))
			self.readUint32_equals(0)
			self.readUint32_equals(2)
			s = self.readString()
			assert s.startswith('DinoCharacterStatus_BP_C'.format(X)), s
		else:
			self.readString_equals('DinoCharacterStatusComponent_BP_{0}_C'.format(X))
			self.readUint32_equals(0)
			self.readUint32_equals(2)
			s = self.readString()
			fixup = {'Ankylo':'Anklyo', }
			if X in fixup:
				X = fixup[X]
			assert s.startswith('DinoCharacterStatus_BP_{0}_C'.format(X)), s
			
		
	def read_X_Character_BP_C(self):
		character = self.readString()
		dino = character.split('_')[0]
		self.readUint32_equals(0)
		number = self.readUint32()
		indexed = self.readString() #
		index = int(indexed.split('_')[-1])
		self.f.read(15 * 4)
		self.read_DinoCharacterStatusComponent_BP_X_C(dino)
		self.readString_equals(indexed)
		self.f.read(9 * 4)
		return (dino, index)
	
	def read_X_Character_C(self):
		character = self.readString()
		dino = character.split('_')[0]
		self.readUint32_equals(0)
		number = self.readUint32()
		indexed = self.readString() #
		index = int(indexed.split('_')[-1])
		self.f.read(15 * 4)
		self.read_DinoCharacterStatusComponent_BP_X_C(dino)
		self.readString_equals(indexed)
		self.f.read(9 * 4)
		return (dino, index)


	def read_DinoTamedInventoryComponent_X_C(self):
		character = self.readString()
		dino = character.split('_')[1]
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		self.readString_equals(character+'_0')
		dino_name_index = self.readString()
		self.f.read(9 * 4)
		return (dino_name_index, 'TamedInventory')


	def read_PrimalInventoryBP_Campfire_C(self):
		character = 'PrimalInventoryBP_Campfire_C'
		self.readString_equals(character)
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		self.readString_equals(character + '1')
		indexed = self.readString()
		index = int(indexed.split('_')[-1])
		assert indexed.startswith('Campfire_C'), indexed
		self.f.read(9 * 4)
		return ('campfire inventory', index)


	def get_Component_read_function(self, string):
		read_Function = getattr(self, 'read_' + string, None)
		if not read_Function:
			read_Function = getattr(self, 'read_' + string.split('_')[0] + '_X_C', None)
		if not read_Function:
			read_Function = getattr(self, 'read_X_' + '_'.join(string.split('_')[1:]), None)
		if read_Function:
			return read_Function

	def read_Component(self):
		string = self.peekString()
		read_Function = self.get_Component_read_function(string)
		if read_Function:
			return read_Function()
		else:
			assert not "Unknown component", string
		

	def readFile(self):
		self.f.seek(ARK_savegame_reader.START_OFFSET)
		numberOfInitialEntries = self.readUint32()
		initialEntries = [self.readString() for i in range(numberOfInitialEntries)]
		print(initialEntries)
		numberOfCells = self.readUint32()
		cells = [self.readRegion() for i in range(numberOfCells)]	
		print(cells)
		self.readUint32_equals(0)
		changingNumber = self.readUint32()
		print(changingNumber)
		self.readBytes_equals(b'}@=6\xf6\xef\x00I\xba\x95\xc8\xa6\xc8\xdc(\xdf')
		#761fc
		mod_name = self.readString()
		print(mod_name)
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		propertyName = self.readString()
		print(propertyName)
		self.readUint32_equals(0)
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		self.readBytes_equals(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xB6\xF9\x1B\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
		self.read_ShooterGameState()
		self.read_InstancedFoliageActor()
		self.read_MatineeActor()
		self.read_ShooterGameState()
		for i in range(100000):
			print(self.read_Component())


if len(sys.argv) < 1:
	print("Call {0} <path-to-savefile>".format(sys.argv[0]))
	exit(-1)
else:
	reader = ARK_savegame_reader(sys.argv[1])
	reader.readFile()
