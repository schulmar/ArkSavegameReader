#!/usr/bin/python3
import sys
import struct
import string

class ARK_savegame_reader:
	START_OFFSET = 6
	WORD_SIZE = 4

	def __init__(self, file_name, debug=False):
		self.f = open(file_name, 'rb') if file_name else None
		self.debug = debug
		self.nesting_depth = 0
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
		self.f.seek(pos)
		return uint

	def readUint64(self):
		uint_bytes = self.f.read(8)
		return struct.unpack('Q', uint_bytes)[0]

	def readFloat(self):
		float_bytes = self.f.read(4)
		return struct.unpack('f', float_bytes)[0]

	def readDouble(self):
		double_bytes = self.f.read(8)
		return struct.unpack('d', double_bytes)[0]

	def readBool(self):
		bool_byte = self.f.read(1)
		return struct.unpack('?', bool_byte)[0]

	def readInt8(self):
		int8_byte = self.f.read(1)
		return struct.unpack('c', int8_byte)[0]

	def readInt16(self):
		int16_bytes = self.f.read(2)
		return struct.unpack('h', int16_bytes)[0]

	def readInt32(self):
		int32_bytes = self.f.read(4)
		return struct.unpack('i', int32_bytes)[0]
	
	def readUint16(self):
		uint16_bytes = self.f.read(2)
		return struct.unpack('H', uint16_bytes)[0]

	def readEntry(self, size_multiplier = 1):
		size = self.readUint32()
		return self.f.read(size * size_multiplier)

	def peekEntry(self, size_multiplier = 1):
		pos = self.tell()
		result = self.readEntry(size_multiplier)
		self.seek(pos)
		return result

	def readString(self, min_string_length = 4, max_string_length = 1000):
		length = self.readUint32()
		if not (min_string_length <= length <= max_string_length):
			return None
		b = self.f.read(length)
		#if b[-1] != b'\x00':
		#	return None
		string = b[:-1] # omit trailing null terminator
		try:
			return string.decode('utf-8')
		except:
			return string

	def is_at_string_begin(self, max_string_length = 1000):
		pos = self.f.tell()
		length = self.readUint32()
		is_valid_string = False
		if 4 < length <= max_string_length:
			self.f.seek(length - 1, 1)
			nullterminator = self.f.read(1)
			is_valid_string = (nullterminator == b'\x00')
		self.f.seek(pos)
		s = self.peekString()
		return is_valid_string and isinstance(s, str) and all(c in string.printable for c in s)


	def peekString(self):
		pos = self.f.tell()
		string = self.readString()
		self.f.seek(pos)
		return string


	def readRegion(self):
		cell_name = self.readString()
		if self.debug:
			self.print("Reading region {0}".format(cell_name))
		number_of_entry_batches = self.readUint32()
		# so far only encountered 0 and 1
		assert(number_of_entry_batches <= 1)
		for entry_batch_index in range(number_of_entry_batches):
			number_of_entries = self.readUint32()
			for i in range(number_of_entries):
				entry = self.readEntry(4)
				if self.debug:
					self.print('Read entry of size {0}'.format(len(entry)))
		return cell_name

	def readUint32_equals(self, expected_value):
		read_value = self.readUint32()
		if isinstance(expected_value, list):
			assert read_value in expected_value, ('{0} in {1}'.format(read_value, expected_value), self.f.tell())
		else:
			assert read_value == expected_value, ('{0} == {1}'.format(read_value, expected_value), self.f.tell())

	def readBytes_equals(self, expected_value):
		read_value = self.f.read(len(expected_value))
		assert read_value == expected_value, ('{0} == {1}'.format(read_value, expected_value), self.f.tell())

	def readString_equals(self, expected_value):
		read_value = self.readString()
		assert read_value == expected_value, ('"{0}" == "{1}"'.format(read_value, expected_value), self.f.tell())

	def read_regular_indexed(self, descriptor_index, number_of_trailing_words):
		character = self.readString()
		if descriptor_index is None:
			descriptor = character
		else:
			if isinstance(descriptor_index, list):
				split = character.split('_')
				descriptor = ' '.join([split[i] for i in descriptor_index])
			else:
				descriptor = character.split('_')[descriptor_index]
		self.readUint32_equals([0, 1])
		second_uint = self.readUint32()
		indexed = self.readString()
		index = None
		try:
			index = int(indexed.split('_')[-1])
		except:
			pass
		secondString = self.readString() if second_uint == 2 else None
		d = self.f.read(number_of_trailing_words * ARK_savegame_reader.WORD_SIZE)
		unpacked_floats = struct.unpack('f'*number_of_trailing_words, d)
		unpacked_ints = struct.unpack('I'*number_of_trailing_words, d)
		properties = []
		if number_of_trailing_words > 9:
			properties = self.read_properties_at(unpacked_ints[9], None)
		else:
			properties = self.read_properties_at(unpacked_ints[3], None)
		return (descriptor, index, secondString, properties)

	def get_Component_read_function(self, string):
		'''
		>>> ARK_savegame_reader(None).get_Component_read_function('DinoCharacterStatusComponent_BP_Monkey_C')
		'''
		read_function = getattr(self, 'read_' + string, None)
		components = string.split('_')
		#import pdb; pdb.set_trace()
		if not read_function:
			for i in range(len(components)):
				func_name = 'read_{0}_C'.format(
					'_'.join(components[0:i-1] + ['X'] + components[i+1:-2]))
				read_function = getattr(self, func_name, None)
				if read_function != None:
					return read_function
		return read_function

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
			return 'self.read_{0}(self):\n\t\t self.read_regular_indexed({0}, {1})'.format(string_c, length)
		return (string_c, 'following string is no _C string:', next_string )

	def try_read_component(self):
		errors = []
		# try shortest first to not read over following components
		for length in [9, 11, 15]:
			oldPos = self.f.tell()
			try:
				result = self.read_regular_indexed(None, length)
				if self.is_at_string_begin():
					return result
				else:
					print('Not %0: %1'%(length, self.f.read(10)))
					self.f.seek(oldPos)
			except Exception as e:
				self.f.seek(oldPos)
				errors.append((length, e))
				continue
		raise Exception("Don't know how to read component:", errors)

	def read_Component(self):
		string = self.peekString()
		if not string == None:
			read_Function = self.get_Component_read_function(string)
			if read_Function:
				return read_Function()
			else:
				try:
					return self.try_read_component()
				except AssertionError:
					raise
				except Exception as e:
					pos = self.f.tell()
					string = self.get_regular_indexed_parameter(string)
					raise Exception("Unknown component", string, e, pos)
		else:
			assert not "Not at string begin", (self.f.tell(), )

	def read_ObjectProperty(self, final_element = None):
		return ('ObjectProperty', self.readUint32(), self.readUint32())

	def read_IntProperty(self, name = None):
		return self.readInt32()

	def read_FloatProperty(self, name = None):
		return ('FloatProperty', self.readFloat())


	def read_DoubleProperty(self, name = None):
		return self.readDouble()

	def read_BoolProperty(self, name = None):
		return self.readBool()

	def read_ByteProperty(self, name = None):
		type_name = self.readString()
		if type_name == 'None':
			value = self.f.read(1)
		else:
			value = self.readString()
		return ('ByteProperty', value)

	def read_UInt32Property(self, name = None):
		return self.readUint32()

	def read_NameProperty(self, name = None):
		return self.readString()

	def read_Int8Property(self, name = None):
		return ('Int8Property', self.readInt8())

	def read_Int16Property(self, name = None):
		return ('Int16Property', self.readInt16())
	
	def read_StrProperty(self, name = None):
		return ('StrProperty', self.readString())

	def read_UInt16Property(self, name = None):
		return ('UInt16Property', self.readUint16())

	def read_UInt64Property(self, name = None):
		return ('UInt64Property', self.readUint64)

	def read_ArrayProperty(self, name = None):
		property_type = self.readString()
		number_of_entries = self.readUint32()
		read_property_func = getattr(self, 'read_' + property_type, None)
		entries = [read_property_func(None) for i in range(number_of_entries)]
		return ('ArrayProperty', entries)

	def read_StructProperty(self, name = None):
		name = self.readString()
		entries = []
		while self.peekString() != 'None':
			name_and_property = self.read_NameAndProperty()
			entries.append(name_and_property)
		return ('StructProperty', name, entries)
		
	def read_XPropertyTypeAndValue(self, name, property_type):
		read_property_func = getattr(self, 'read_' + property_type, None)
		assert read_property_func is not None, ("No property func for ",property_type, self.f.tell())
		final_element = {'MyCharacterStatusComponent' : 'LastInAllyRangeTime',
				'GameState' : 'LastInAllyRangeTime',
				'MyInventoryComponent' : 'InventoryItems',
				'InventoryItems' : 'EquippedItems',
				'EquippedItems' : 'ItemId'}
		return read_property_func(final_element[name] if name in final_element else None)

	def read_bytes_until_next_string_begin(self):
		b = b''
		while not self.is_at_string_begin():
			b += self.f.read(1)
		return b


	def read_NameAndProperty(self):
		name = self.readString()
		b = None
		if name is None:
			b = self.read_bytes_until_next_string_begin()
			name = self.readString()
		if name == 'None':
			return ('None', None)
		else:
			property_type = self.readString()
			assert property_type != None, ("Could not read property type of ", name, self.f.tell())
			assert property_type.endswith('Property'), ("Property type name does not end with 'Property'", name, property_type, self.f.tell())
			size = self.readUint32()
			if property_type == 'BoolProperty' and size == 0:
				size = 1
			index = self.readUint32()
			next_pos = self.f.tell() + size
			if property_type in ['ArrayProperty', 'ByteProperty']:
				next_pos += len(self.peekString()) + 1
			result = (name, b, index, self.read_XPropertyTypeAndValue(name, property_type))
			self.f.seek(next_pos)
			return result

	def read_property_at(self, location):
		oldpos = self.f.tell()
		try:
			self.f.seek(location)
			result = self.read_NameAndProperty()
			return result
		finally:
			self.f.seek(oldpos)

	"""
	If count == None then read until a None is hit
	"""
	def read_properties_at(self, location, count):
		oldpos = self.f.tell()
		try:
			self.f.seek(location)
			if count == None:
				result = []
				while self.peekString() != None:
					result.append(self.read_NameAndProperty())
				return result
			else:
				return [self.read_NameAndProperty() for _ in range(count)]
		finally:
			self.f.seek(oldpos)
	

	def read_Setting(self):
		self.readUint32_equals(1)
		name = self.readString()
		assert name.endswith('_settings'), ("Setting does not end with _settings", name, self.f.tell())
		value = self.read_NameAndProperty()
		self.print(value)
		self.readString_equals('None')
		self.readUint32_equals(0)
		return (name, value)

	def readFile(self):
		self.f.seek(ARK_savegame_reader.START_OFFSET)
		numberOfInitialEntries = self.readUint32()
		initialEntries = [self.readString() for i in range(numberOfInitialEntries)]
		if self.debug:
			print('Initial entries: {0}'.format(initialEntries))
		number_of_regions = self.readUint32()
		print('{0} regions'.format(number_of_regions))
		cells = [self.readRegion() for i in range(number_of_regions)]
		if self.is_at_string_begin():
			self.readString_equals('Matinee_WorldEnd')
		else:
			unknown_number= self.readUint32()
			print('unknown_number:'+str(unknown_number))
		number_of_entries = self.readUint32()
		randomBytes = self.f.read(16)
		components = []
		for i in range(number_of_entries):
			loc = self.f.tell()
			# sometimes the trailing entry does not fit?
			try:
				components.append(self.read_Component())
			except AssertionError as e:
				raise Exception(e, loc)
			except Exception as e:
				print("Could not read component at ", self.f.tell(), ":", e)
				break
		dino_status_component_count = 0
		files = {}
		for x in components:
			if len(x) >= 4 and isinstance(x[3], dict) and 'pos' in x[3]:
				pos = x[3]['pos']
				name = x[0]
				if name not in files:
					files[name] = open(name+'.txt', 'w')
				files[name].write('{0}\t{1}\t{2}\n'.format(pos['x'], pos['y'], pos['z']))
			elif 'CharacterStatusComponent' in x[0]:
				dino_status_component_count += 1
		for f in files.values():
			f.close()
		for component in components: 
			print(component)
		print("#Components:", len(components), ", expected:", number_of_entries)

	def readLocalPlayerArkProfile(self):
		self.readUint32_equals(1)
		self.readUint32_equals(1)
		self.readUint32_equals(0)
		self.readUint32_equals(0)
		components = [self.read_Component() for i in range(1)]
		print(components)


	def print(self, *args, **kwargs):
		print(sys._getframe(2).f_code.co_firstlineno, ':', self.nesting_depth, self.f.tell(), *args, **kwargs)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Call {0} <path-to-savefile>".format(sys.argv[0]))
		exit(-1)
	elif sys.argv[1] == 'doctest':
		import doctest
		doctest.testmod()
	else:
		filename = sys.argv[1]
		debug = False
		if len(sys.argv) > 2 and sys.argv[1] == "debug":
			filename = sys.argv[2]
			debug = True
		reader = ARK_savegame_reader(filename, debug)
		if filename.endswith('arkprofile'):
			reader.readLocalPlayerArkProfile()	
		else:
			reader.readFile()
