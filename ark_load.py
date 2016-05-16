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

	def read_X_Character_DNA_Harvester_C(self):
                 return self.read_regular_indexed(0, 1, [0, 2, 3], 15)
	def read_X_Character_BP_DNAHarvest_C(self):
                 return self.read_regular_indexed(0, 1, [0, 3], 15)
	def read_X_Character_BP_DNA_Harvester_C(self):
                 return self.read_regular_indexed(0, 1, [0, 3, 4], 15)
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
	def read_PlayerPawnTest_X_C(self):
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
	def read_PrimalItemRaft_C(self):
		return self.read_regular_indexed(1, 1, 0, 9)
	def read_PrimalItemResource_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemSkin_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemWeaponAttachment_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_PrimalItemStructure_X_C(self):
		return self.read_regular_indexed(1, 1, 1, 9)
	def read_Raft_BP_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_Ramp_Wood_SM_New_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_RaptorNest_BP_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_Rounded_Ceiling_Stone_R_C(self):
		return self.read_regular_indexed(0, 1, [0, 2, 1, 3], 15)
	def read_Rounded_Ceiling_Stone_L_C(self):
		return self.read_regular_indexed(0, 1, [0, 2, 1, 3], 15)
	def read_Rounded_Doorframe_Stone_C(self):
		return self.read_regular_indexed(0, 1, [0, 2, 1], 15)
	def read_RoundedFloor_Stone_L_C(self):
		return self.read_regular_indexed(0, 1, [1,0,2], 15)
	def read_RoundedFloor_Stone_R_C(self):
		return self.read_regular_indexed(0, 1, [1,0,2], 15)
	def read_Rounded_Stone_Roof_BP_C(self):
		return self.read_regular_indexed(0, 1, [0, 1, 2], 15)
	def read_Rounded_Stone_Stairs_BP_C(self):
		return self.read_regular_indexed(0, 1, [0, 1, 2], 15)
	def read_Rounded_Wall_Stone_C(self):
		return self.read_regular_indexed(0, 1, [0, 2, 1], 15)
	def read_StoneRoof_SM_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
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
		first = self.readString()#'StructurePainting1')
		if first.startswith('StructurePainting_'):
			indexed_structure = first
			data = None
		else:
			indexed_structure = self.readString()
			data = self.f.read(9 * ARK_savegame_reader.WORD_SIZE)
		return ('StructurePaintingComponent', indexed_structure, data)
	def read_ThatchRoof_SM_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_Top_StoneM_C(self):
		return self.read_regular_indexed(0, 1, [0, 1], 15)
	def read_TrikeNest_BP_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_Wall_X_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_WaterPipe_X_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_WeapFists_Female_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_WindowRoundedWall_Stone_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_WindowWall_X_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_Window_Wood_BP_C(self):
		return self.read_regular_indexed(0, 1, [1, 0], 15)
	def read_WoodRoof_SM_C(self):
		return self.read_regular_indexed(0, 1, 0, 15)
	def read_WoodWall_Sloped_Left_SM_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)
	def read_WoodWall_Sloped_Right_SM_C(self):
		return self.read_regular_indexed(0, 1, [2, 1, 0], 15)

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

	def read_regular_indexed(self, expected_value_of_first_uint, 
					expected_value_of_second_uint,
			   		descriptor_index,
					number_of_trailing_words):
		character = self.readString()
		if descriptor_index is None:
			descriptor = character
		else:
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
		unpacked = struct.unpack('f'*number_of_trailing_words, d)
		return (descriptor, index, unpacked, d)

	def read_ShooterGameState(self):
		return self.read_regular_indexed(0, 1, 0, 9)

	def read_InstancedFoliageActor(self):
		return self.read_regular_indexed(0, 1, 0, 15)

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
		data = struct.unpack('I'*9, d)
		return ('DinoCharacterStatusComponent', X, data, d)
			
		
	def read_X_Character_BP_C(self):
		character = self.readString()
		dino = character.split('_')[0]
		self.readUint32_equals(0)
		number = self.readUint32()
		indexed = self.readString() #
		index = int(indexed.split('_')[-1])
		d = self.f.read(15 * ARK_savegame_reader.WORD_SIZE)
		data = struct.unpack('IIIffffffIIIIII', d)
		return (dino, index, number, {'pos': {'x' : data[3], 'y' : data[4], 'z' : data [5]}, 'rot' : {'x' :data[6], 'y' : data[7], 'z' : data[8]}}, data, d)
	
	def read_X_Character_C(self):
		character = self.readString()
		dino = character.split('_')[0]
		self.readUint32_equals(0)
		number = self.readUint32()
		indexed = self.readString() #
		index = int(indexed.split('_')[-1])
		d = self.f.read(15 * ARK_savegame_reader.WORD_SIZE)
		data = struct.unpack('f'*15, d)
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
				'Tap_C' : 'WaterTap_C_3',
				'RaptorNest_C' : 'RaptorNest_BP_C_2',
				'TrikeNest_C' : 'TrikeNest_BP_C_1' }
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

	def try_read_component(self):
		for args in [(0, 1, None, 15), (0, 1, None, 9)]:
			oldPos = self.f.tell()
			result = self.read_regular_indexed(*args)
			if self.is_at_string_begin():
				return result
			else:
				print('Not %0: %1'%(args[3], self.f.read(10)) )
			self.f.seek(oldPos)
		raise "Don't know how to read component"

	def read_Component(self):
		string = self.peekString()
		read_Function = self.get_Component_read_function(string)
		if read_Function:
			return read_Function()
		else:
			try:
				return self.try_read_component()
			except:
				string = self.get_regular_indexed_parameter(string)
				assert not "Unknown component", (string, self.f.tell())

	def read_GameState(self):
		self.readString_equals('GameState')
		return ('GameState', self.read_ObjectProperty('LastInAllyRangeTime'))
		
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

	def read_GameMode_X_C(self):
		game_component = self.readString()
		assert game_component.startswith('GameMode_'), (game_component, self.f.tell())
		game_name = game_component.split('_')[1]
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		return ('GameMode', game_name)

	def read_TestGameMode_C(self):
		self.readString_equals('TestGameMode_C')
		self.readUint32_equals(0)
		self.readUint32_equals(1)
		return ('TestGameMode', '(No mod?)')

	def read_XPropertyTypeAndValue(self, name, property_type):
		read_property_func = getattr(self, 'read_' + property_type, None)
		assert read_property_func is not None, (property_type, self.f.tell())
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
			assert property_type != None, (name, self.f.tell())
			assert property_type.endswith('Property'), (name, property_type, self.f.tell())
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

	def read_Setting(self):
		self.readUint32_equals(1)
		name = self.readString()
		assert name.endswith('_settings'), (name, self.f.tell())
		value = self.read_NameAndProperty()
		self.print(value)
		self.readString_equals('None')
		self.readUint32_equals(0)
		return (name, value)

	def readFile(self):
		self.f.seek(ARK_savegame_reader.START_OFFSET)
		numberOfInitialEntries = self.readUint32()
		initialEntries = [self.readString() for i in range(numberOfInitialEntries)]
		number_of_regions = self.readUint32()
		print('{0} regions'.format(number_of_regions))
		cells = [self.readRegion() for i in range(number_of_regions)]
		if self.is_at_string_begin():
			self.readString_equals('Matinee_WorldEnd')
		else:
			unknown_number= self.readUint32()
			print('unknown_number:'+str(unknown_number))
		number_of_components = self.readUint32()
		self.readBytes_equals(b'}@=6\xf6\xef\x00I\xba\x95\xc8\xa6\xc8\xdc(\xdf')
		print('{0} components'.format(number_of_components))
		#761fc
		components = [self.read_Component() for i in range(number_of_components)]
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
		# somehow the last entry (FoliageActor) has 4 Words less at the end?
		self.f.seek(-4 * ARK_savegame_reader.WORD_SIZE, 1)
		number_of_properties = 1878053
		print('{0} properties'.format(number_of_properties))
		properties = [self.read_NameAndProperty() for i in range(number_of_properties)]
		my_character_status_component_count = 0
		for p in properties:
			if 'CharacterStatusComponent' in p[0]:
				my_character_status_component_count += 1
		print(dino_status_component_count, my_character_status_component_count)
		self.readUint32_equals(0)
		number_of_settings = self.readUint32()
		print('{0} settings'.format(number_of_settings))
		self.readUint32_equals(0)
		self.readUint32_equals(0)
		for i in range(number_of_settings):
			self.print(i, self.read_Setting())

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
		reader = ARK_savegame_reader(sys.argv[1])
		if sys.argv[1].endswith('arkprofile'):
			reader.readLocalPlayerArkProfile()	
		else:
			reader.readFile()
