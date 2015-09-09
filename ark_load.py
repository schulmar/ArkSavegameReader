#!/usr/bin/python3
import sys
import struct

class ARK_savegame_reader:
	START_OFFSET = 6

	def __init__(self, file_name, debug=False):
		self.f = open(file_name, 'rb')
		self.debug = debug
		self.read_PrimalItemConsumable_X_C = lambda: self.read_regular_indexed(1, 1, 1, 9)
		#self.read_Thatch_Floor_C = lambda: self.read_regular_indexed(0, 1, 1, 15)
		#self.read_Thatch_Wall_Small_C = lambda: self.read_regular_indexed(0, 1, 1, 15)
		self.read_Campfire_C = lambda: self.read_regular_indexed(0, 1, 0, 15)
		self.read_PrimalItemArmor_X_C = lambda: self.read_regular_indexed(1, 1, 1, 9)
		self.read_PrimalItemConsumable_X_C = lambda: self.read_regular_indexed(1, 1, 1, 9)
		self.read_LadderBP_C = lambda: self.read_regular_indexed(0, 1, 1, 15)
		self.read_StorageBox_Large_C = lambda: self.read_regular_indexed(0, 1, [0,1], 15)
		self.read_SimpleBed_C = lambda: self.read_regular_indexed(0, 1, 0, 15)
		self.read_StandingTorch_C = lambda: self.read_regular_indexed(0, 1, 0, 15)
		self.read_Wall_Wood_Small_SM_New_C = lambda: self.read_regular_indexed(0, 1, [2, 1, 0], 15)
		self.read_Ceiling_Wood_SM_C = lambda: self.read_regular_indexed(0, 1, [1, 0], 15)
		self.read_StorageBox_AnvilBench_C = lambda: self.read_regular_indexed(0, 1, [1, 0], 15)
		self.read_FenceFoundation_Wood_SM_C = lambda: self.read_regular_indexed(0, 1, [1, 0], 15)
		self.read_WindowWall_Wood_SM_New_C = lambda: self.read_regular_indexed(0, 1, [1, 0], 15)

	def peekBytes(self, number):
		pos = self.f.tell()
		result = self.f.read(number)
		self.f.seek(pos)
		return result 


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

	def peekEntry(self, size_multiplier = 1):
		pos = self.tell()
		result = self.readEntry(size_multiplier)
		self.seek(pos)
		return result

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
		if isinstance(descriptor_index, list):
			split = character.split('_')
			descriptor = ' '.join([split[i] for i in descriptor_index])
		else:
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


	def read_PrimalInventoryBP_X_C(self):
		character = self.readString()
		name = ' '.join(character.split('_')[1:-1])
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		C1_string = self.readString()
		assert C1_string.startswith(character + '1')
		indexed = self.readString()
		index = int(indexed.split('_')[-1])
		assert indexed.startswith('_'.join(character.split('_')[1:])), indexed
		self.f.read(9 * 4)
		return (name, index)

	def read_Thatch_X_C(self):
		return self.read_regular_indexed(0, 1, [0, 1], 15)
				
	def read_X_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)

	def get_Component_read_function(self, string):
		read_Function = getattr(self, 'read_' + string, None)
		if not read_Function and len(string.split('_')) == 2:
			read_Function = self.read_X_C
		if not read_Function:
			read_Function = getattr(self, 'read_' + string.split('_')[0] + '_X_C', None)
		if not read_Function:
			read_Function = getattr(self, 'read_X_' + '_'.join(string.split('_')[1:]), None)
		if read_Function:
			return read_Function

	def is_at_string_begin(self, max_string_length = 1000):
		pos = self.f.tell()
		length = self.readUint32()
		is_valid_string = False
		if 0 < length <= max_string_length:
			self.f.seek(length - 1, 1)
			nullterminator = self.f.read(1)
			is_valid_string = (nullterminator == b'\x00')
		self.f.seek(pos)
		string = self.peekString()
		return is_valid_string and isinstance(string, str)

	def get_regular_indexed_parameter(self, string_c):
		self.readString_equals(string_c)
		first_number = self.readUint32()
		second_number = self.readUint32()
		if not self.is_at_string_begin():
			return (string_c, 'no string at indexed string position')
		indexed = self.readString()
		if not indexed.startswith(string_c):
			return (string_c, 'no indexed string', indexed)
		pos = self.f.tell()
		# seek for the next string in word steps
		for i in range(20):
			if self.is_at_string_begin():
				length = i
				break
			self.f.seek(4,1)
		if not self.is_at_string_begin():
			return (string_c, 'no following string')
		next_string = self.readString()
		if next_string and next_string.endswith('_C'):
			return 'self.read_{2} = lambda: self.read_regular_indexed({0}, {1}, {2}, {3})'.format(first_number, second_number, string_c, length)
		return (string_c, 'following string is no _C string')

	def read_Component(self):
		string = self.peekString()
		read_Function = self.get_Component_read_function(string)
		if read_Function:
			return read_Function()
		else:
			string = self.get_regular_indexed_parameter(string)
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
