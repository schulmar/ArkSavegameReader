#!/usr/bin/python3
import sys
import struct

class ARK_savegame_reader:
	START_OFFSET = 6
	WORD_SIZE = 4

	def __init__(self, file_name, debug=False):
		self.f = open(file_name, 'rb') if file_name else None
		self.debug = debug
	def read_Bigfoot_Character_BP_DNA_Harvester_C(self):
                 self.read_regular_indexed(0, 1, [4, 0], 15)
	def read_Ceiling_Door_Wood_SM_New_C(self):
		return self.read_regular_indexed(0, 1, [2, 0, 1], 15)
	def read_Ceiling_Doorway_Wood_SM_New_C(self):
		return self.read_regular_indexed(0, 1, [2, 0, 1], 15)
	def read_Ceiling_X_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_CropPlotMedium_SM_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_Door_X_C(self):
		return self.read_regular_indexed(0, 1, [0, 1], 15)		
	def read_Doorframe_X_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_FenceFoundation_Wood_SM_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_Fence_StoneM_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_FenceFoundation_Stone_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_Floor_X_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_Gate_X_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_GateFrame_X_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_Monkey_Character_BP_DNA_Harvester_C(self):
		return self.read_regular_indexed(0, 1, [4, 0, 1], 15)
	def read_Pillar_Wood_SM_New_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_PlayerPawnTest_Female_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_PrimalItem_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemAmmo_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemArmor_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemConsumable_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemConsumableBuff_Parachute_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemConsumableMiracleGro_C(self):
		return self.read_regular_indexed(1, 1, 0, 9)
	def read_PrimalItemConsumableRespecSoup_C(self):
		return self.read_regular_indexed(1, 1, 0, 9)
	def read_PrimalItemDye_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemRadio_C(self):
		return self.read_regular_indexed(1, 1, 0, 9)
	def read_PrimalItemResource_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemSkin_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemWeaponAttachment_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemStructure_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_Ramp_Wood_SM_New_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_StoneWall_Sloped_Right_SM_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_StoneWall_Sloped_Left_SM_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_StorageBox_X_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_StructurePaintingComponent(self):
		self.readString_equals('StructurePaintingComponent')
		number = self.readUint32()
		self.readUint32_equals(2)
		self.readString_equals('StructurePainting1')
		indexed_structure = self.readString()
		return ('StructurePaintingComponent', indexed_structure, self.f.read(9 * ARK_savegame_reader.WORD_SIZE))
	def read_ThatchRoof_SM_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_Wall_X_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_WaterPipe_X_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_WeapFists_Female_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_WindowWall_X_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)

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
		d = self.f.read(number_of_trailing_words * ARK_savegame_reader.WORD_SIZE)
		return (descriptor, index, d)

		

	def read_ShooterGameState(self):
		self.readString_equals('ShooterGameState')
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		self.readString_equals('ShooterGameState_0')
		d = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		return 'ShooterGameState', d

	def read_InstancedFoliageActor(self):
		self.readString_equals('InstancedFoliageActor')
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		indexed = self.readString()
		assert indexed.startswith('InstancedFoliageActor_'), (indexed, self.f.tell())
		index = int(indexed.split('_')[-1])
		d = self.f.read(15 * ARK_savegame_reader.WORD_SIZE)
		return ('InstanceFoliageActor', index, d)

	def read_MatineeActor(self):
		self.readString_equals('MatineeActor')
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		self.readString_equals('Matinee_DayTime')
		d = self.f.read(15*ARK_savegame_reader.WORD_SIZE)
		return 'MatineeActor', d

	def read_DinoCharacterStatusComponent_BP_X_C(self, X = None):
		if X is None:
			string = self.peekString()
			transform = {'C':'Coel'}
			X = string.split('_')[2]
			if X in transform:
				X = transform[X]
		fixup = {'Megalodon':'Mega'}
		if X in fixup:
			X = fixup[X]
		if X == 'Coel':
			self.readString_equals('DinoCharacterStatusComponent_BP_C'.format(X))
			self.readUint32_equals(0)
			self.readUint32_equals(2)
			s = self.readString()
			assert s.startswith('DinoCharacterStatus_BP_C'.format(X)), (s, self.f.tell())
		else:
			self.readString_equals('DinoCharacterStatusComponent_BP_{0}_C'.format(X))
			self.readUint32_equals(0)
			self.readUint32_equals(2)
			s = self.readString()
			fixup = {'Ankylo':'Anklyo', }
			if X in fixup:
				X = fixup[X]
			assert s.startswith('DinoCharacterStatus_BP_{0}_C'.format(X)), (s, self.f.tell())
		instance = self.readString()
		#assert instance.startswith(X + '_Character'), (instance, X) Anklyo Ankylo problem
		d = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		return ('DinoCharacterStatusComponent', X, d)
			
		
	def read_X_Character_BP_C(self):
		character = self.readString()
		dino = character.split('_')[0]
		self.readUint32_equals(0)
		number = self.readUint32()
		indexed = self.readString() #
		index = int(indexed.split('_')[-1])
		d = self.f.read(15 * ARK_savegame_reader.WORD_SIZE)
		return (dino, index, d)
	
	def read_X_Character_C(self):
		character = self.readString()
		dino = character.split('_')[0]
		self.readUint32_equals(0)
		number = self.readUint32()
		indexed = self.readString() #
		index = int(indexed.split('_')[-1])
		d = self.f.read(15 * ARK_savegame_reader.WORD_SIZE)
		return (dino, index, d)


	def read_DinoTamedInventoryComponent_X_C(self):
		character = self.readString()
		dino = character.split('_')[1]
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		inventory_indexed = self.readString()
		assert inventory_indexed.startswith((character)), (inventory_indexed, character, self.f.tell())
		dino_name_index = self.readString()
		d = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		return (dino_name_index, 'TamedInventory', d)


	def read_PrimalInventoryBP_X_C(self):
		character = self.readString()
		name = ' '.join(character.split('_')[1:-1])
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		C1_string = self.readString()
		assert C1_string.startswith(character + '1'), (C1_string, character, self.f.tell())
		indexed = self.readString()
		index = int(indexed.split('_')[-1])
		expected_indexed = '_'.join(character.split('_')[1:])
		translation = {'AnvilBench_C' : 'StorageBox_AnvilBench_C',
				'CropPlot_Medium_C' : 'CropPlotMedium_SM_C',
				'WaterTank_C' : 'WaterTankBaseBP_C',
				'Tap_C' : 'WaterTap_C_3' }
		if expected_indexed in translation:
			expected_indexed = translation[expected_indexed]
		assert indexed.startswith(expected_indexed), (indexed, expected_indexed, self.f.tell())
		d = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		return (name, index, d)

	def read_Thatch_X_C(self):
		return self.read_regular_indexed(0, 1, [0, 1], 15)
				
	def read_X_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)

	def read_PlayerCharacterStatusComponent_BP_C(self):
		self.readString_equals('PlayerCharacterStatusComponent_BP_C')
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		self.readString_equals('PlayerCharacterStatus')
		string = self.readString()
		string.startswith('PlayerPawnTest_')
		d = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		c = self.read_PrimalInventoryComponent()
		return 'PlayerCharacterStatusComponent', string, d, c
		
	def read_PrimalInventoryComponent(self):
		self.readString_equals('PrimalInventoryComponent')
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		self.readString_equals('PrimalInventory1')
		string = self.readString()
		d = self.f.read(9*ARK_savegame_reader.WORD_SIZE)
		return 'PrimalInventoryComponent', string, d

	def get_Component_read_function(self, string):
		'''
		>>> ARK_savegame_reader(None).get_Component_read_function('DinoCharacterStatusComponent_BP_Monkey_C')
		'''
		read_Function = getattr(self, 'read_' + string, None)
		components = string.split('_')
		#import pdb; pdb.set_trace()
		if not read_Function and len(components) == 2:
			read_Function = self.read_X_C
		if not read_Function:
			read_Function = getattr(self, 'read_' + components[0] + '_X_C', None)
		if not read_Function:
			read_Function = getattr(self, 'read_' + '_'.join(components[0:2]) + '_X_C', None)
		if not read_Function:
			read_Function = getattr(self, 'read_X_' + '_'.join(components[1:]), None)
		return read_Function

	def is_at_string_begin(self, max_string_length = 1000):
		pos = self.f.tell()
		length = self.readUint32()
		is_valid_string = False
		if 4 < length <= max_string_length:
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
			return 'self.read_{2}(self):\n\t\t self.read_regular_indexed({0}, {1}, {2}, {3})'.format(first_number, second_number, string_c, length)
		return (string_c, 'following string is no _C string:', next_string )

	def read_Component(self):
		string = self.peekString()
		read_Function = self.get_Component_read_function(string)
		if read_Function:
			return read_Function()
		else:
			string = self.get_regular_indexed_parameter(string)
			assert not "Unknown component", (string, self.f.tell())

	def read_GameState(self):
		self.readString_equals('GameState')
		return ('GameState', self.read_ObjectProperty())
		
	def read_ObjectProperty(self):
		self.readString_equals('ObjectProperty')
		object_type = self.readUint32()
		n = None
		if object_type == 8:
			self.readUint32_equals(0)
			self.readUint32_equals(0)
			n = self.readUint32()
		elif object_type == 7:
			v = []	
			for i in range(7):
				self.readUint32_equals(0)
				v.append(self.readUint32())
		elif object_type == 4:
			self.readUint32_equals(0)
			v1 = self.readUint32()#5v
		elif object_type == 2:
			self.readUint32_equals(0)
			v1 = self.readUint32()#6v
			self.readUint32_equals(0)
			v2 = self.readUint32()#7v
		elif object_type == 1:
			self.readUint32_equals(0)
			v1 = self.readUint32()#8v
		else:
			assert not "Unknown value", (object_type, self.f.tell())
		values = {}
		last_property_was_none = False
		while self.is_at_string_begin():
			name_and_property = self.read_NameAndProperty()
			self.print(name_and_property)
			values[name_and_property[0]] = name_and_property[1]
		self.readUint32_equals([0, 1])
		return ('ObjectProperty', n, values)

	def read_DayNumber(self):
		self.readString_equals('DayNumber')
		return ('DayNumber', self.read_IntProperty())
	def read_PlayRate(self):
		self.readString_equals('PlayRate')
		return ('PlayRate', self.read_FloatProperty())

	def read_IntProperty(self):
		self.readString_equals('IntProperty')
		# 4 bytes per int?
		self.readUint32_equals(4) 
		self.readUint32_equals(0) #little endian 8byte int?
		i = self.readUint32()
		return i

	def read_FloatProperty(self):
		self.readString_equals('FloatProperty')
		# 4 bytes per float?
		self.readUint32_equals(4)
		i = self.readUint32()
		return ('FloatProperty', i, self.readFloat())


	def read_DoubleProperty(self):
		self.readString_equals('DoubleProperty')
		# 8 bytes per double?
		self.readUint32_equals(8)
		self.readUint32_equals(0)
		return self.readDouble()

	def read_BoolProperty(self):
		self.readString_equals('BoolProperty')
		# 1 bytes per bool but 0 as vaule?
		self.readUint32_equals(0)
		self.readUint32_equals(0)
		return self.readBool()

	def read_None(self):
		self.readString_equals('None')
		self.readUint32_equals(0)
		return ('None', None)

	def read_NoneProperty(self):
		return self.read_None()

	def read_ByteProperty(self):
		self.readString_equals('ByteProperty')
		self.readUint32_equals(1)
		index = self.readUint32()
		self.readString_equals('None')
		return ('ByteProperty', index, self.f.read(1))

	def read_UInt32Property(self):
		self.readString_equals('UInt32Property')
		self.readUint32_equals(4)
		self.readUint32_equals(0)
		return self.readUint32()

	def read_NameProperty(self):
		self.readString_equals('NameProperty')
		self.readUint32_equals([0x14, 0x15, 0x16, 0x17])
		self.readUint32_equals(0)
		return self.readString()

	def read_Int8Property(self):
		self.readString_equals('Int8Property')
		# number of bytes?
		self.readUint32_equals(1)
		self.readUint32_equals(1)
		return ('Int8Property', self.readInt8())
	
	def read_StrProperty(self):
		self.readString_equals('StrProperty')
		self.readUint32_equals([9, 0xC, 0xd])
		self.readUint32_equals(0)
		return ('StrProperty', self.readString())

	def read_UInt16Property(self):
		self.readString_equals('UInt16Property')
		self.readUint32_equals(2)
		self.readUint32_equals(0)
		return ('UInt16Property', self.readUint16())

	def read_ArrayProperty(self):
		self.readString_equals('ArrayProperty')
		number_of_entries = self.readUint32()
		self.readUint32_equals(0)
		entries = [self.read_XPropertyTypeAndValue() for i in range(number_of_entries)]
		return ('ArrayProperty', entries)

	def read_StructProperty(self):
		self.readString_equals('StructProperty')
		number_of_entries = self.readUint32()
		self.readUint32_equals(0)
		name = self.readString()
		entries = {}
		while self.peekString() != 'None':
			name_and_property = self.read_NameAndProperty()
			entries[name_and_property[0]] = name_and_property[1:]
		self.readString_equals('None')
		return ('StructProperty', name, entries)
		

	def read_NetworkTime(self):
		self.readString_equals('NetworkTime')
		return ('NetworkTime', self.read_DoubleProperty())

	def read_OriginalCreationTime(self):
		self.readString_equals('OriginalCreationTime')
		return ('OriginalCreationTime', self.read_DoubleProperty())
		

	def read_StaticMeshComponent(self):
		character = self.readString()
		self.readUint32_equals(0)
		self.readUint32_equals(2)
		indexed = self.readString()
		assert indexed.startswith(character), (indexed, character, self.f.tell())
		contains_indexed = self.readString()
		d = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		return ('StaticMeshCompoment', contains_indexed, d)

	def read_ArkGameMode(self):
		self.readString_equals('ArkGameMode')
		self.readUint32_equals(0)
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		d = self.f.read(12 * ARK_savegame_reader.WORD_SIZE)#b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xB6\xF9\x1B\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
		return ('ArkGameMode', d)

	def read_TestGameMode_X_C(self):
		mod_component = self.readString()
		assert mod_component.startswith('TestGameMode_'), (mod_component, self.f.tell())
		mod_name = mod_component.split('_')[1]
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		return ('TestGameMode', mod_name)

	def read_TestGameMode_C(self):
		self.readString_equals('TestGameMode_C')
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		return ('TestGameMode', '(No mod?)')

	def read_XPropertyTypeAndValue(self):
		propertyType = self.peekString() #e.g. FloatProperty
		read_property_func = getattr(self, 'read_' + propertyType, None)
		assert read_property_func is not None, (propertyType, self.f.tell())
		return read_property_func()

	def read_NameAndProperty(self):
		name = self.peekString()
		if name == 'None':
			return self.read_None()
		else:
			self.readString_equals(name)
			return (name, self.read_XPropertyTypeAndValue())

	def readFile(self):
		self.f.seek(ARK_savegame_reader.START_OFFSET)
		numberOfInitialEntries = self.readUint32()
		initialEntries = [self.readString() for i in range(numberOfInitialEntries)]
		numberOfCells = self.readUint32()
		cells = [self.readRegion() for i in range(numberOfCells)]
		if self.is_at_string_begin():
			self.readString_equals('Matinee_WorldEnd')
		else:
			unknown_number= self.readUint32()
		number_of_entries = self.readUint32()
		self.readBytes_equals(b'}@=6\xf6\xef\x00I\xba\x95\xc8\xa6\xc8\xdc(\xdf')
		#761fc
		l = [self.read_Component() for i in range(number_of_entries)]
		# somehow the last entry (FoliageActor) has 4 Words less at the end?
		self.f.seek(-4 * ARK_savegame_reader.WORD_SIZE, 1)
		self.print('==== Reading properties ====')
		# 011E:BDF0
		for i in range(1000000):
			self.print(i, self.read_NameAndProperty())

	def print(self, *args, **kwargs):
		print(sys._getframe(2).f_code.co_firstlineno, ':', self.f.tell(), *args, **kwargs)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Call {0} <path-to-savefile>".format(sys.argv[0]))
		exit(-1)
	elif sys.argv[1] == 'doctest':
		import doctest
		doctest.testmod()
	else:
		reader = ARK_savegame_reader(sys.argv[1])
		reader.readFile()
