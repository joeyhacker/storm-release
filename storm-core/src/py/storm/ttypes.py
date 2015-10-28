#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TopologyInitialStatus:
  ACTIVE = 1
  INACTIVE = 2

  _VALUES_TO_NAMES = {
    1: "ACTIVE",
    2: "INACTIVE",
  }

  _NAMES_TO_VALUES = {
    "ACTIVE": 1,
    "INACTIVE": 2,
  }

class TopologyStatus:
  ACTIVE = 1
  INACTIVE = 2
  REBALANCING = 3
  KILLED = 4

  _VALUES_TO_NAMES = {
    1: "ACTIVE",
    2: "INACTIVE",
    3: "REBALANCING",
    4: "KILLED",
  }

  _NAMES_TO_VALUES = {
    "ACTIVE": 1,
    "INACTIVE": 2,
    "REBALANCING": 3,
    "KILLED": 4,
  }

class NumErrorsChoice:
  ALL = 0
  NONE = 1
  ONE = 2

  _VALUES_TO_NAMES = {
    0: "ALL",
    1: "NONE",
    2: "ONE",
  }

  _NAMES_TO_VALUES = {
    "ALL": 0,
    "NONE": 1,
    "ONE": 2,
  }

class LogLevelAction:
  UNCHANGED = 1
  UPDATE = 2
  REMOVE = 3

  _VALUES_TO_NAMES = {
    1: "UNCHANGED",
    2: "UPDATE",
    3: "REMOVE",
  }

  _NAMES_TO_VALUES = {
    "UNCHANGED": 1,
    "UPDATE": 2,
    "REMOVE": 3,
  }


class JavaObjectArg:
  """
  Attributes:
   - int_arg
   - long_arg
   - string_arg
   - bool_arg
   - binary_arg
   - double_arg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'int_arg', None, None, ), # 1
    (2, TType.I64, 'long_arg', None, None, ), # 2
    (3, TType.STRING, 'string_arg', None, None, ), # 3
    (4, TType.BOOL, 'bool_arg', None, None, ), # 4
    (5, TType.STRING, 'binary_arg', None, None, ), # 5
    (6, TType.DOUBLE, 'double_arg', None, None, ), # 6
  )

  def __init__(self, int_arg=None, long_arg=None, string_arg=None, bool_arg=None, binary_arg=None, double_arg=None,):
    self.int_arg = int_arg
    self.long_arg = long_arg
    self.string_arg = string_arg
    self.bool_arg = bool_arg
    self.binary_arg = binary_arg
    self.double_arg = double_arg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.int_arg = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.long_arg = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.string_arg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.bool_arg = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.binary_arg = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.DOUBLE:
          self.double_arg = iprot.readDouble();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JavaObjectArg')
    if self.int_arg is not None:
      oprot.writeFieldBegin('int_arg', TType.I32, 1)
      oprot.writeI32(self.int_arg)
      oprot.writeFieldEnd()
    if self.long_arg is not None:
      oprot.writeFieldBegin('long_arg', TType.I64, 2)
      oprot.writeI64(self.long_arg)
      oprot.writeFieldEnd()
    if self.string_arg is not None:
      oprot.writeFieldBegin('string_arg', TType.STRING, 3)
      oprot.writeString(self.string_arg.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.bool_arg is not None:
      oprot.writeFieldBegin('bool_arg', TType.BOOL, 4)
      oprot.writeBool(self.bool_arg)
      oprot.writeFieldEnd()
    if self.binary_arg is not None:
      oprot.writeFieldBegin('binary_arg', TType.STRING, 5)
      oprot.writeString(self.binary_arg)
      oprot.writeFieldEnd()
    if self.double_arg is not None:
      oprot.writeFieldBegin('double_arg', TType.DOUBLE, 6)
      oprot.writeDouble(self.double_arg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.int_arg)
    value = (value * 31) ^ hash(self.long_arg)
    value = (value * 31) ^ hash(self.string_arg)
    value = (value * 31) ^ hash(self.bool_arg)
    value = (value * 31) ^ hash(self.binary_arg)
    value = (value * 31) ^ hash(self.double_arg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class JavaObject:
  """
  Attributes:
   - full_class_name
   - args_list
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'full_class_name', None, None, ), # 1
    (2, TType.LIST, 'args_list', (TType.STRUCT,(JavaObjectArg, JavaObjectArg.thrift_spec)), None, ), # 2
  )

  def __init__(self, full_class_name=None, args_list=None,):
    self.full_class_name = full_class_name
    self.args_list = args_list

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.full_class_name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.args_list = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = JavaObjectArg()
            _elem5.read(iprot)
            self.args_list.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JavaObject')
    if self.full_class_name is not None:
      oprot.writeFieldBegin('full_class_name', TType.STRING, 1)
      oprot.writeString(self.full_class_name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.args_list is not None:
      oprot.writeFieldBegin('args_list', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.args_list))
      for iter6 in self.args_list:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.full_class_name is None:
      raise TProtocol.TProtocolException(message='Required field full_class_name is unset!')
    if self.args_list is None:
      raise TProtocol.TProtocolException(message='Required field args_list is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.full_class_name)
    value = (value * 31) ^ hash(self.args_list)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NullStruct:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NullStruct')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GlobalStreamId:
  """
  Attributes:
   - componentId
   - streamId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'componentId', None, None, ), # 1
    (2, TType.STRING, 'streamId', None, None, ), # 2
  )

  def __init__(self, componentId=None, streamId=None,):
    self.componentId = componentId
    self.streamId = streamId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.componentId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.streamId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('GlobalStreamId')
    if self.componentId is not None:
      oprot.writeFieldBegin('componentId', TType.STRING, 1)
      oprot.writeString(self.componentId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.streamId is not None:
      oprot.writeFieldBegin('streamId', TType.STRING, 2)
      oprot.writeString(self.streamId.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.componentId is None:
      raise TProtocol.TProtocolException(message='Required field componentId is unset!')
    if self.streamId is None:
      raise TProtocol.TProtocolException(message='Required field streamId is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.componentId)
    value = (value * 31) ^ hash(self.streamId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Grouping:
  """
  Attributes:
   - fields
   - shuffle
   - all
   - none
   - direct
   - custom_object
   - custom_serialized
   - local_or_shuffle
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'fields', (TType.STRING,None), None, ), # 1
    (2, TType.STRUCT, 'shuffle', (NullStruct, NullStruct.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'all', (NullStruct, NullStruct.thrift_spec), None, ), # 3
    (4, TType.STRUCT, 'none', (NullStruct, NullStruct.thrift_spec), None, ), # 4
    (5, TType.STRUCT, 'direct', (NullStruct, NullStruct.thrift_spec), None, ), # 5
    (6, TType.STRUCT, 'custom_object', (JavaObject, JavaObject.thrift_spec), None, ), # 6
    (7, TType.STRING, 'custom_serialized', None, None, ), # 7
    (8, TType.STRUCT, 'local_or_shuffle', (NullStruct, NullStruct.thrift_spec), None, ), # 8
  )

  def __init__(self, fields=None, shuffle=None, all=None, none=None, direct=None, custom_object=None, custom_serialized=None, local_or_shuffle=None,):
    self.fields = fields
    self.shuffle = shuffle
    self.all = all
    self.none = none
    self.direct = direct
    self.custom_object = custom_object
    self.custom_serialized = custom_serialized
    self.local_or_shuffle = local_or_shuffle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.fields = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString().decode('utf-8')
            self.fields.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.shuffle = NullStruct()
          self.shuffle.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.all = NullStruct()
          self.all.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.none = NullStruct()
          self.none.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.direct = NullStruct()
          self.direct.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.custom_object = JavaObject()
          self.custom_object.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.custom_serialized = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRUCT:
          self.local_or_shuffle = NullStruct()
          self.local_or_shuffle.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Grouping')
    if self.fields is not None:
      oprot.writeFieldBegin('fields', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.fields))
      for iter13 in self.fields:
        oprot.writeString(iter13.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.shuffle is not None:
      oprot.writeFieldBegin('shuffle', TType.STRUCT, 2)
      self.shuffle.write(oprot)
      oprot.writeFieldEnd()
    if self.all is not None:
      oprot.writeFieldBegin('all', TType.STRUCT, 3)
      self.all.write(oprot)
      oprot.writeFieldEnd()
    if self.none is not None:
      oprot.writeFieldBegin('none', TType.STRUCT, 4)
      self.none.write(oprot)
      oprot.writeFieldEnd()
    if self.direct is not None:
      oprot.writeFieldBegin('direct', TType.STRUCT, 5)
      self.direct.write(oprot)
      oprot.writeFieldEnd()
    if self.custom_object is not None:
      oprot.writeFieldBegin('custom_object', TType.STRUCT, 6)
      self.custom_object.write(oprot)
      oprot.writeFieldEnd()
    if self.custom_serialized is not None:
      oprot.writeFieldBegin('custom_serialized', TType.STRING, 7)
      oprot.writeString(self.custom_serialized)
      oprot.writeFieldEnd()
    if self.local_or_shuffle is not None:
      oprot.writeFieldBegin('local_or_shuffle', TType.STRUCT, 8)
      self.local_or_shuffle.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.fields)
    value = (value * 31) ^ hash(self.shuffle)
    value = (value * 31) ^ hash(self.all)
    value = (value * 31) ^ hash(self.none)
    value = (value * 31) ^ hash(self.direct)
    value = (value * 31) ^ hash(self.custom_object)
    value = (value * 31) ^ hash(self.custom_serialized)
    value = (value * 31) ^ hash(self.local_or_shuffle)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StreamInfo:
  """
  Attributes:
   - output_fields
   - direct
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'output_fields', (TType.STRING,None), None, ), # 1
    (2, TType.BOOL, 'direct', None, None, ), # 2
  )

  def __init__(self, output_fields=None, direct=None,):
    self.output_fields = output_fields
    self.direct = direct

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.output_fields = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = iprot.readString().decode('utf-8')
            self.output_fields.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.direct = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StreamInfo')
    if self.output_fields is not None:
      oprot.writeFieldBegin('output_fields', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.output_fields))
      for iter20 in self.output_fields:
        oprot.writeString(iter20.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.direct is not None:
      oprot.writeFieldBegin('direct', TType.BOOL, 2)
      oprot.writeBool(self.direct)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.output_fields is None:
      raise TProtocol.TProtocolException(message='Required field output_fields is unset!')
    if self.direct is None:
      raise TProtocol.TProtocolException(message='Required field direct is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.output_fields)
    value = (value * 31) ^ hash(self.direct)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ShellComponent:
  """
  Attributes:
   - execution_command
   - script
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'execution_command', None, None, ), # 1
    (2, TType.STRING, 'script', None, None, ), # 2
  )

  def __init__(self, execution_command=None, script=None,):
    self.execution_command = execution_command
    self.script = script

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.execution_command = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.script = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ShellComponent')
    if self.execution_command is not None:
      oprot.writeFieldBegin('execution_command', TType.STRING, 1)
      oprot.writeString(self.execution_command.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.script is not None:
      oprot.writeFieldBegin('script', TType.STRING, 2)
      oprot.writeString(self.script.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.execution_command)
    value = (value * 31) ^ hash(self.script)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ComponentObject:
  """
  Attributes:
   - serialized_java
   - shell
   - java_object
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serialized_java', None, None, ), # 1
    (2, TType.STRUCT, 'shell', (ShellComponent, ShellComponent.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'java_object', (JavaObject, JavaObject.thrift_spec), None, ), # 3
  )

  def __init__(self, serialized_java=None, shell=None, java_object=None,):
    self.serialized_java = serialized_java
    self.shell = shell
    self.java_object = java_object

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.serialized_java = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.shell = ShellComponent()
          self.shell.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.java_object = JavaObject()
          self.java_object.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ComponentObject')
    if self.serialized_java is not None:
      oprot.writeFieldBegin('serialized_java', TType.STRING, 1)
      oprot.writeString(self.serialized_java)
      oprot.writeFieldEnd()
    if self.shell is not None:
      oprot.writeFieldBegin('shell', TType.STRUCT, 2)
      self.shell.write(oprot)
      oprot.writeFieldEnd()
    if self.java_object is not None:
      oprot.writeFieldBegin('java_object', TType.STRUCT, 3)
      self.java_object.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serialized_java)
    value = (value * 31) ^ hash(self.shell)
    value = (value * 31) ^ hash(self.java_object)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ComponentCommon:
  """
  Attributes:
   - inputs
   - streams
   - parallelism_hint
   - json_conf
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'inputs', (TType.STRUCT,(GlobalStreamId, GlobalStreamId.thrift_spec),TType.STRUCT,(Grouping, Grouping.thrift_spec)), None, ), # 1
    (2, TType.MAP, 'streams', (TType.STRING,None,TType.STRUCT,(StreamInfo, StreamInfo.thrift_spec)), None, ), # 2
    (3, TType.I32, 'parallelism_hint', None, None, ), # 3
    (4, TType.STRING, 'json_conf', None, None, ), # 4
  )

  def __init__(self, inputs=None, streams=None, parallelism_hint=None, json_conf=None,):
    self.inputs = inputs
    self.streams = streams
    self.parallelism_hint = parallelism_hint
    self.json_conf = json_conf

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.inputs = {}
          (_ktype22, _vtype23, _size21 ) = iprot.readMapBegin()
          for _i25 in xrange(_size21):
            _key26 = GlobalStreamId()
            _key26.read(iprot)
            _val27 = Grouping()
            _val27.read(iprot)
            self.inputs[_key26] = _val27
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.streams = {}
          (_ktype29, _vtype30, _size28 ) = iprot.readMapBegin()
          for _i32 in xrange(_size28):
            _key33 = iprot.readString().decode('utf-8')
            _val34 = StreamInfo()
            _val34.read(iprot)
            self.streams[_key33] = _val34
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.parallelism_hint = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.json_conf = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ComponentCommon')
    if self.inputs is not None:
      oprot.writeFieldBegin('inputs', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRUCT, TType.STRUCT, len(self.inputs))
      for kiter35,viter36 in self.inputs.items():
        kiter35.write(oprot)
        viter36.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.streams is not None:
      oprot.writeFieldBegin('streams', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.streams))
      for kiter37,viter38 in self.streams.items():
        oprot.writeString(kiter37.encode('utf-8'))
        viter38.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.parallelism_hint is not None:
      oprot.writeFieldBegin('parallelism_hint', TType.I32, 3)
      oprot.writeI32(self.parallelism_hint)
      oprot.writeFieldEnd()
    if self.json_conf is not None:
      oprot.writeFieldBegin('json_conf', TType.STRING, 4)
      oprot.writeString(self.json_conf.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.inputs is None:
      raise TProtocol.TProtocolException(message='Required field inputs is unset!')
    if self.streams is None:
      raise TProtocol.TProtocolException(message='Required field streams is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.inputs)
    value = (value * 31) ^ hash(self.streams)
    value = (value * 31) ^ hash(self.parallelism_hint)
    value = (value * 31) ^ hash(self.json_conf)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SpoutSpec:
  """
  Attributes:
   - spout_object
   - common
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'spout_object', (ComponentObject, ComponentObject.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'common', (ComponentCommon, ComponentCommon.thrift_spec), None, ), # 2
  )

  def __init__(self, spout_object=None, common=None,):
    self.spout_object = spout_object
    self.common = common

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.spout_object = ComponentObject()
          self.spout_object.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.common = ComponentCommon()
          self.common.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SpoutSpec')
    if self.spout_object is not None:
      oprot.writeFieldBegin('spout_object', TType.STRUCT, 1)
      self.spout_object.write(oprot)
      oprot.writeFieldEnd()
    if self.common is not None:
      oprot.writeFieldBegin('common', TType.STRUCT, 2)
      self.common.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.spout_object is None:
      raise TProtocol.TProtocolException(message='Required field spout_object is unset!')
    if self.common is None:
      raise TProtocol.TProtocolException(message='Required field common is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.spout_object)
    value = (value * 31) ^ hash(self.common)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Bolt:
  """
  Attributes:
   - bolt_object
   - common
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'bolt_object', (ComponentObject, ComponentObject.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'common', (ComponentCommon, ComponentCommon.thrift_spec), None, ), # 2
  )

  def __init__(self, bolt_object=None, common=None,):
    self.bolt_object = bolt_object
    self.common = common

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.bolt_object = ComponentObject()
          self.bolt_object.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.common = ComponentCommon()
          self.common.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Bolt')
    if self.bolt_object is not None:
      oprot.writeFieldBegin('bolt_object', TType.STRUCT, 1)
      self.bolt_object.write(oprot)
      oprot.writeFieldEnd()
    if self.common is not None:
      oprot.writeFieldBegin('common', TType.STRUCT, 2)
      self.common.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.bolt_object is None:
      raise TProtocol.TProtocolException(message='Required field bolt_object is unset!')
    if self.common is None:
      raise TProtocol.TProtocolException(message='Required field common is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.bolt_object)
    value = (value * 31) ^ hash(self.common)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StateSpoutSpec:
  """
  Attributes:
   - state_spout_object
   - common
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'state_spout_object', (ComponentObject, ComponentObject.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'common', (ComponentCommon, ComponentCommon.thrift_spec), None, ), # 2
  )

  def __init__(self, state_spout_object=None, common=None,):
    self.state_spout_object = state_spout_object
    self.common = common

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.state_spout_object = ComponentObject()
          self.state_spout_object.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.common = ComponentCommon()
          self.common.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StateSpoutSpec')
    if self.state_spout_object is not None:
      oprot.writeFieldBegin('state_spout_object', TType.STRUCT, 1)
      self.state_spout_object.write(oprot)
      oprot.writeFieldEnd()
    if self.common is not None:
      oprot.writeFieldBegin('common', TType.STRUCT, 2)
      self.common.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.state_spout_object is None:
      raise TProtocol.TProtocolException(message='Required field state_spout_object is unset!')
    if self.common is None:
      raise TProtocol.TProtocolException(message='Required field common is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.state_spout_object)
    value = (value * 31) ^ hash(self.common)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StormTopology:
  """
  Attributes:
   - spouts
   - bolts
   - state_spouts
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'spouts', (TType.STRING,None,TType.STRUCT,(SpoutSpec, SpoutSpec.thrift_spec)), None, ), # 1
    (2, TType.MAP, 'bolts', (TType.STRING,None,TType.STRUCT,(Bolt, Bolt.thrift_spec)), None, ), # 2
    (3, TType.MAP, 'state_spouts', (TType.STRING,None,TType.STRUCT,(StateSpoutSpec, StateSpoutSpec.thrift_spec)), None, ), # 3
  )

  def __init__(self, spouts=None, bolts=None, state_spouts=None,):
    self.spouts = spouts
    self.bolts = bolts
    self.state_spouts = state_spouts

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.spouts = {}
          (_ktype40, _vtype41, _size39 ) = iprot.readMapBegin()
          for _i43 in xrange(_size39):
            _key44 = iprot.readString().decode('utf-8')
            _val45 = SpoutSpec()
            _val45.read(iprot)
            self.spouts[_key44] = _val45
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.bolts = {}
          (_ktype47, _vtype48, _size46 ) = iprot.readMapBegin()
          for _i50 in xrange(_size46):
            _key51 = iprot.readString().decode('utf-8')
            _val52 = Bolt()
            _val52.read(iprot)
            self.bolts[_key51] = _val52
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.state_spouts = {}
          (_ktype54, _vtype55, _size53 ) = iprot.readMapBegin()
          for _i57 in xrange(_size53):
            _key58 = iprot.readString().decode('utf-8')
            _val59 = StateSpoutSpec()
            _val59.read(iprot)
            self.state_spouts[_key58] = _val59
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StormTopology')
    if self.spouts is not None:
      oprot.writeFieldBegin('spouts', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.spouts))
      for kiter60,viter61 in self.spouts.items():
        oprot.writeString(kiter60.encode('utf-8'))
        viter61.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.bolts is not None:
      oprot.writeFieldBegin('bolts', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.bolts))
      for kiter62,viter63 in self.bolts.items():
        oprot.writeString(kiter62.encode('utf-8'))
        viter63.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.state_spouts is not None:
      oprot.writeFieldBegin('state_spouts', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.state_spouts))
      for kiter64,viter65 in self.state_spouts.items():
        oprot.writeString(kiter64.encode('utf-8'))
        viter65.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.spouts is None:
      raise TProtocol.TProtocolException(message='Required field spouts is unset!')
    if self.bolts is None:
      raise TProtocol.TProtocolException(message='Required field bolts is unset!')
    if self.state_spouts is None:
      raise TProtocol.TProtocolException(message='Required field state_spouts is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.spouts)
    value = (value * 31) ^ hash(self.bolts)
    value = (value * 31) ^ hash(self.state_spouts)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AlreadyAliveException(TException):
  """
  Attributes:
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AlreadyAliveException')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.msg is None:
      raise TProtocol.TProtocolException(message='Required field msg is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NotAliveException(TException):
  """
  Attributes:
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NotAliveException')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.msg is None:
      raise TProtocol.TProtocolException(message='Required field msg is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthorizationException(TException):
  """
  Attributes:
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AuthorizationException')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.msg is None:
      raise TProtocol.TProtocolException(message='Required field msg is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InvalidTopologyException(TException):
  """
  Attributes:
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InvalidTopologyException')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.msg is None:
      raise TProtocol.TProtocolException(message='Required field msg is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ThrottlingException(TException):
  """
  Attributes:
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ThrottlingException')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.msg is None:
      raise TProtocol.TProtocolException(message='Required field msg is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TopologySummary:
  """
  Attributes:
   - id
   - name
   - num_tasks
   - num_executors
   - num_workers
   - uptime_secs
   - status
   - sched_status
   - owner
   - replication_count
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'num_tasks', None, None, ), # 3
    (4, TType.I32, 'num_executors', None, None, ), # 4
    (5, TType.I32, 'num_workers', None, None, ), # 5
    (6, TType.I32, 'uptime_secs', None, None, ), # 6
    (7, TType.STRING, 'status', None, None, ), # 7
    None, # 8
    None, # 9
    None, # 10
    None, # 11
    None, # 12
    None, # 13
    None, # 14
    None, # 15
    None, # 16
    None, # 17
    None, # 18
    None, # 19
    None, # 20
    None, # 21
    None, # 22
    None, # 23
    None, # 24
    None, # 25
    None, # 26
    None, # 27
    None, # 28
    None, # 29
    None, # 30
    None, # 31
    None, # 32
    None, # 33
    None, # 34
    None, # 35
    None, # 36
    None, # 37
    None, # 38
    None, # 39
    None, # 40
    None, # 41
    None, # 42
    None, # 43
    None, # 44
    None, # 45
    None, # 46
    None, # 47
    None, # 48
    None, # 49
    None, # 50
    None, # 51
    None, # 52
    None, # 53
    None, # 54
    None, # 55
    None, # 56
    None, # 57
    None, # 58
    None, # 59
    None, # 60
    None, # 61
    None, # 62
    None, # 63
    None, # 64
    None, # 65
    None, # 66
    None, # 67
    None, # 68
    None, # 69
    None, # 70
    None, # 71
    None, # 72
    None, # 73
    None, # 74
    None, # 75
    None, # 76
    None, # 77
    None, # 78
    None, # 79
    None, # 80
    None, # 81
    None, # 82
    None, # 83
    None, # 84
    None, # 85
    None, # 86
    None, # 87
    None, # 88
    None, # 89
    None, # 90
    None, # 91
    None, # 92
    None, # 93
    None, # 94
    None, # 95
    None, # 96
    None, # 97
    None, # 98
    None, # 99
    None, # 100
    None, # 101
    None, # 102
    None, # 103
    None, # 104
    None, # 105
    None, # 106
    None, # 107
    None, # 108
    None, # 109
    None, # 110
    None, # 111
    None, # 112
    None, # 113
    None, # 114
    None, # 115
    None, # 116
    None, # 117
    None, # 118
    None, # 119
    None, # 120
    None, # 121
    None, # 122
    None, # 123
    None, # 124
    None, # 125
    None, # 126
    None, # 127
    None, # 128
    None, # 129
    None, # 130
    None, # 131
    None, # 132
    None, # 133
    None, # 134
    None, # 135
    None, # 136
    None, # 137
    None, # 138
    None, # 139
    None, # 140
    None, # 141
    None, # 142
    None, # 143
    None, # 144
    None, # 145
    None, # 146
    None, # 147
    None, # 148
    None, # 149
    None, # 150
    None, # 151
    None, # 152
    None, # 153
    None, # 154
    None, # 155
    None, # 156
    None, # 157
    None, # 158
    None, # 159
    None, # 160
    None, # 161
    None, # 162
    None, # 163
    None, # 164
    None, # 165
    None, # 166
    None, # 167
    None, # 168
    None, # 169
    None, # 170
    None, # 171
    None, # 172
    None, # 173
    None, # 174
    None, # 175
    None, # 176
    None, # 177
    None, # 178
    None, # 179
    None, # 180
    None, # 181
    None, # 182
    None, # 183
    None, # 184
    None, # 185
    None, # 186
    None, # 187
    None, # 188
    None, # 189
    None, # 190
    None, # 191
    None, # 192
    None, # 193
    None, # 194
    None, # 195
    None, # 196
    None, # 197
    None, # 198
    None, # 199
    None, # 200
    None, # 201
    None, # 202
    None, # 203
    None, # 204
    None, # 205
    None, # 206
    None, # 207
    None, # 208
    None, # 209
    None, # 210
    None, # 211
    None, # 212
    None, # 213
    None, # 214
    None, # 215
    None, # 216
    None, # 217
    None, # 218
    None, # 219
    None, # 220
    None, # 221
    None, # 222
    None, # 223
    None, # 224
    None, # 225
    None, # 226
    None, # 227
    None, # 228
    None, # 229
    None, # 230
    None, # 231
    None, # 232
    None, # 233
    None, # 234
    None, # 235
    None, # 236
    None, # 237
    None, # 238
    None, # 239
    None, # 240
    None, # 241
    None, # 242
    None, # 243
    None, # 244
    None, # 245
    None, # 246
    None, # 247
    None, # 248
    None, # 249
    None, # 250
    None, # 251
    None, # 252
    None, # 253
    None, # 254
    None, # 255
    None, # 256
    None, # 257
    None, # 258
    None, # 259
    None, # 260
    None, # 261
    None, # 262
    None, # 263
    None, # 264
    None, # 265
    None, # 266
    None, # 267
    None, # 268
    None, # 269
    None, # 270
    None, # 271
    None, # 272
    None, # 273
    None, # 274
    None, # 275
    None, # 276
    None, # 277
    None, # 278
    None, # 279
    None, # 280
    None, # 281
    None, # 282
    None, # 283
    None, # 284
    None, # 285
    None, # 286
    None, # 287
    None, # 288
    None, # 289
    None, # 290
    None, # 291
    None, # 292
    None, # 293
    None, # 294
    None, # 295
    None, # 296
    None, # 297
    None, # 298
    None, # 299
    None, # 300
    None, # 301
    None, # 302
    None, # 303
    None, # 304
    None, # 305
    None, # 306
    None, # 307
    None, # 308
    None, # 309
    None, # 310
    None, # 311
    None, # 312
    None, # 313
    None, # 314
    None, # 315
    None, # 316
    None, # 317
    None, # 318
    None, # 319
    None, # 320
    None, # 321
    None, # 322
    None, # 323
    None, # 324
    None, # 325
    None, # 326
    None, # 327
    None, # 328
    None, # 329
    None, # 330
    None, # 331
    None, # 332
    None, # 333
    None, # 334
    None, # 335
    None, # 336
    None, # 337
    None, # 338
    None, # 339
    None, # 340
    None, # 341
    None, # 342
    None, # 343
    None, # 344
    None, # 345
    None, # 346
    None, # 347
    None, # 348
    None, # 349
    None, # 350
    None, # 351
    None, # 352
    None, # 353
    None, # 354
    None, # 355
    None, # 356
    None, # 357
    None, # 358
    None, # 359
    None, # 360
    None, # 361
    None, # 362
    None, # 363
    None, # 364
    None, # 365
    None, # 366
    None, # 367
    None, # 368
    None, # 369
    None, # 370
    None, # 371
    None, # 372
    None, # 373
    None, # 374
    None, # 375
    None, # 376
    None, # 377
    None, # 378
    None, # 379
    None, # 380
    None, # 381
    None, # 382
    None, # 383
    None, # 384
    None, # 385
    None, # 386
    None, # 387
    None, # 388
    None, # 389
    None, # 390
    None, # 391
    None, # 392
    None, # 393
    None, # 394
    None, # 395
    None, # 396
    None, # 397
    None, # 398
    None, # 399
    None, # 400
    None, # 401
    None, # 402
    None, # 403
    None, # 404
    None, # 405
    None, # 406
    None, # 407
    None, # 408
    None, # 409
    None, # 410
    None, # 411
    None, # 412
    None, # 413
    None, # 414
    None, # 415
    None, # 416
    None, # 417
    None, # 418
    None, # 419
    None, # 420
    None, # 421
    None, # 422
    None, # 423
    None, # 424
    None, # 425
    None, # 426
    None, # 427
    None, # 428
    None, # 429
    None, # 430
    None, # 431
    None, # 432
    None, # 433
    None, # 434
    None, # 435
    None, # 436
    None, # 437
    None, # 438
    None, # 439
    None, # 440
    None, # 441
    None, # 442
    None, # 443
    None, # 444
    None, # 445
    None, # 446
    None, # 447
    None, # 448
    None, # 449
    None, # 450
    None, # 451
    None, # 452
    None, # 453
    None, # 454
    None, # 455
    None, # 456
    None, # 457
    None, # 458
    None, # 459
    None, # 460
    None, # 461
    None, # 462
    None, # 463
    None, # 464
    None, # 465
    None, # 466
    None, # 467
    None, # 468
    None, # 469
    None, # 470
    None, # 471
    None, # 472
    None, # 473
    None, # 474
    None, # 475
    None, # 476
    None, # 477
    None, # 478
    None, # 479
    None, # 480
    None, # 481
    None, # 482
    None, # 483
    None, # 484
    None, # 485
    None, # 486
    None, # 487
    None, # 488
    None, # 489
    None, # 490
    None, # 491
    None, # 492
    None, # 493
    None, # 494
    None, # 495
    None, # 496
    None, # 497
    None, # 498
    None, # 499
    None, # 500
    None, # 501
    None, # 502
    None, # 503
    None, # 504
    None, # 505
    None, # 506
    None, # 507
    None, # 508
    None, # 509
    None, # 510
    None, # 511
    None, # 512
    (513, TType.STRING, 'sched_status', None, None, ), # 513
    (514, TType.STRING, 'owner', None, None, ), # 514
    (515, TType.I32, 'replication_count', None, None, ), # 515
  )

  def __init__(self, id=None, name=None, num_tasks=None, num_executors=None, num_workers=None, uptime_secs=None, status=None, sched_status=None, owner=None, replication_count=None,):
    self.id = id
    self.name = name
    self.num_tasks = num_tasks
    self.num_executors = num_executors
    self.num_workers = num_workers
    self.uptime_secs = uptime_secs
    self.status = status
    self.sched_status = sched_status
    self.owner = owner
    self.replication_count = replication_count

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.num_tasks = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.num_executors = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.num_workers = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.uptime_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.status = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 513:
        if ftype == TType.STRING:
          self.sched_status = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 514:
        if ftype == TType.STRING:
          self.owner = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 515:
        if ftype == TType.I32:
          self.replication_count = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TopologySummary')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.num_tasks is not None:
      oprot.writeFieldBegin('num_tasks', TType.I32, 3)
      oprot.writeI32(self.num_tasks)
      oprot.writeFieldEnd()
    if self.num_executors is not None:
      oprot.writeFieldBegin('num_executors', TType.I32, 4)
      oprot.writeI32(self.num_executors)
      oprot.writeFieldEnd()
    if self.num_workers is not None:
      oprot.writeFieldBegin('num_workers', TType.I32, 5)
      oprot.writeI32(self.num_workers)
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I32, 6)
      oprot.writeI32(self.uptime_secs)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRING, 7)
      oprot.writeString(self.status.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.sched_status is not None:
      oprot.writeFieldBegin('sched_status', TType.STRING, 513)
      oprot.writeString(self.sched_status.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.owner is not None:
      oprot.writeFieldBegin('owner', TType.STRING, 514)
      oprot.writeString(self.owner.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.replication_count is not None:
      oprot.writeFieldBegin('replication_count', TType.I32, 515)
      oprot.writeI32(self.replication_count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.num_tasks is None:
      raise TProtocol.TProtocolException(message='Required field num_tasks is unset!')
    if self.num_executors is None:
      raise TProtocol.TProtocolException(message='Required field num_executors is unset!')
    if self.num_workers is None:
      raise TProtocol.TProtocolException(message='Required field num_workers is unset!')
    if self.uptime_secs is None:
      raise TProtocol.TProtocolException(message='Required field uptime_secs is unset!')
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.num_tasks)
    value = (value * 31) ^ hash(self.num_executors)
    value = (value * 31) ^ hash(self.num_workers)
    value = (value * 31) ^ hash(self.uptime_secs)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.sched_status)
    value = (value * 31) ^ hash(self.owner)
    value = (value * 31) ^ hash(self.replication_count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SupervisorSummary:
  """
  Attributes:
   - host
   - uptime_secs
   - num_workers
   - num_used_workers
   - supervisor_id
   - version
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'host', None, None, ), # 1
    (2, TType.I32, 'uptime_secs', None, None, ), # 2
    (3, TType.I32, 'num_workers', None, None, ), # 3
    (4, TType.I32, 'num_used_workers', None, None, ), # 4
    (5, TType.STRING, 'supervisor_id', None, None, ), # 5
    (6, TType.STRING, 'version', None, "VERSION_NOT_PROVIDED", ), # 6
  )

  def __init__(self, host=None, uptime_secs=None, num_workers=None, num_used_workers=None, supervisor_id=None, version=thrift_spec[6][4],):
    self.host = host
    self.uptime_secs = uptime_secs
    self.num_workers = num_workers
    self.num_used_workers = num_used_workers
    self.supervisor_id = supervisor_id
    self.version = version

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.host = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.uptime_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.num_workers = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.num_used_workers = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.supervisor_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.version = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SupervisorSummary')
    if self.host is not None:
      oprot.writeFieldBegin('host', TType.STRING, 1)
      oprot.writeString(self.host.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I32, 2)
      oprot.writeI32(self.uptime_secs)
      oprot.writeFieldEnd()
    if self.num_workers is not None:
      oprot.writeFieldBegin('num_workers', TType.I32, 3)
      oprot.writeI32(self.num_workers)
      oprot.writeFieldEnd()
    if self.num_used_workers is not None:
      oprot.writeFieldBegin('num_used_workers', TType.I32, 4)
      oprot.writeI32(self.num_used_workers)
      oprot.writeFieldEnd()
    if self.supervisor_id is not None:
      oprot.writeFieldBegin('supervisor_id', TType.STRING, 5)
      oprot.writeString(self.supervisor_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 6)
      oprot.writeString(self.version.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.host is None:
      raise TProtocol.TProtocolException(message='Required field host is unset!')
    if self.uptime_secs is None:
      raise TProtocol.TProtocolException(message='Required field uptime_secs is unset!')
    if self.num_workers is None:
      raise TProtocol.TProtocolException(message='Required field num_workers is unset!')
    if self.num_used_workers is None:
      raise TProtocol.TProtocolException(message='Required field num_used_workers is unset!')
    if self.supervisor_id is None:
      raise TProtocol.TProtocolException(message='Required field supervisor_id is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.host)
    value = (value * 31) ^ hash(self.uptime_secs)
    value = (value * 31) ^ hash(self.num_workers)
    value = (value * 31) ^ hash(self.num_used_workers)
    value = (value * 31) ^ hash(self.supervisor_id)
    value = (value * 31) ^ hash(self.version)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NimbusSummary:
  """
  Attributes:
   - host
   - port
   - uptime_secs
   - isLeader
   - version
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'host', None, None, ), # 1
    (2, TType.I32, 'port', None, None, ), # 2
    (3, TType.I32, 'uptime_secs', None, None, ), # 3
    (4, TType.BOOL, 'isLeader', None, None, ), # 4
    (5, TType.STRING, 'version', None, None, ), # 5
  )

  def __init__(self, host=None, port=None, uptime_secs=None, isLeader=None, version=None,):
    self.host = host
    self.port = port
    self.uptime_secs = uptime_secs
    self.isLeader = isLeader
    self.version = version

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.host = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.uptime_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.isLeader = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.version = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NimbusSummary')
    if self.host is not None:
      oprot.writeFieldBegin('host', TType.STRING, 1)
      oprot.writeString(self.host.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 2)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I32, 3)
      oprot.writeI32(self.uptime_secs)
      oprot.writeFieldEnd()
    if self.isLeader is not None:
      oprot.writeFieldBegin('isLeader', TType.BOOL, 4)
      oprot.writeBool(self.isLeader)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 5)
      oprot.writeString(self.version.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.host is None:
      raise TProtocol.TProtocolException(message='Required field host is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    if self.uptime_secs is None:
      raise TProtocol.TProtocolException(message='Required field uptime_secs is unset!')
    if self.isLeader is None:
      raise TProtocol.TProtocolException(message='Required field isLeader is unset!')
    if self.version is None:
      raise TProtocol.TProtocolException(message='Required field version is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.host)
    value = (value * 31) ^ hash(self.port)
    value = (value * 31) ^ hash(self.uptime_secs)
    value = (value * 31) ^ hash(self.isLeader)
    value = (value * 31) ^ hash(self.version)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ClusterSummary:
  """
  Attributes:
   - supervisors
   - topologies
   - nimbuses
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'supervisors', (TType.STRUCT,(SupervisorSummary, SupervisorSummary.thrift_spec)), None, ), # 1
    None, # 2
    (3, TType.LIST, 'topologies', (TType.STRUCT,(TopologySummary, TopologySummary.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'nimbuses', (TType.STRUCT,(NimbusSummary, NimbusSummary.thrift_spec)), None, ), # 4
  )

  def __init__(self, supervisors=None, topologies=None, nimbuses=None,):
    self.supervisors = supervisors
    self.topologies = topologies
    self.nimbuses = nimbuses

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.supervisors = []
          (_etype69, _size66) = iprot.readListBegin()
          for _i70 in xrange(_size66):
            _elem71 = SupervisorSummary()
            _elem71.read(iprot)
            self.supervisors.append(_elem71)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.topologies = []
          (_etype75, _size72) = iprot.readListBegin()
          for _i76 in xrange(_size72):
            _elem77 = TopologySummary()
            _elem77.read(iprot)
            self.topologies.append(_elem77)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.nimbuses = []
          (_etype81, _size78) = iprot.readListBegin()
          for _i82 in xrange(_size78):
            _elem83 = NimbusSummary()
            _elem83.read(iprot)
            self.nimbuses.append(_elem83)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ClusterSummary')
    if self.supervisors is not None:
      oprot.writeFieldBegin('supervisors', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.supervisors))
      for iter84 in self.supervisors:
        iter84.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.topologies is not None:
      oprot.writeFieldBegin('topologies', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.topologies))
      for iter85 in self.topologies:
        iter85.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.nimbuses is not None:
      oprot.writeFieldBegin('nimbuses', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.nimbuses))
      for iter86 in self.nimbuses:
        iter86.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.supervisors is None:
      raise TProtocol.TProtocolException(message='Required field supervisors is unset!')
    if self.topologies is None:
      raise TProtocol.TProtocolException(message='Required field topologies is unset!')
    if self.nimbuses is None:
      raise TProtocol.TProtocolException(message='Required field nimbuses is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.supervisors)
    value = (value * 31) ^ hash(self.topologies)
    value = (value * 31) ^ hash(self.nimbuses)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ErrorInfo:
  """
  Attributes:
   - error
   - error_time_secs
   - host
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'error', None, None, ), # 1
    (2, TType.I32, 'error_time_secs', None, None, ), # 2
    (3, TType.STRING, 'host', None, None, ), # 3
    (4, TType.I32, 'port', None, None, ), # 4
  )

  def __init__(self, error=None, error_time_secs=None, host=None, port=None,):
    self.error = error
    self.error_time_secs = error_time_secs
    self.host = host
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.error = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.error_time_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.host = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ErrorInfo')
    if self.error is not None:
      oprot.writeFieldBegin('error', TType.STRING, 1)
      oprot.writeString(self.error.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.error_time_secs is not None:
      oprot.writeFieldBegin('error_time_secs', TType.I32, 2)
      oprot.writeI32(self.error_time_secs)
      oprot.writeFieldEnd()
    if self.host is not None:
      oprot.writeFieldBegin('host', TType.STRING, 3)
      oprot.writeString(self.host.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 4)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error is None:
      raise TProtocol.TProtocolException(message='Required field error is unset!')
    if self.error_time_secs is None:
      raise TProtocol.TProtocolException(message='Required field error_time_secs is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.error)
    value = (value * 31) ^ hash(self.error_time_secs)
    value = (value * 31) ^ hash(self.host)
    value = (value * 31) ^ hash(self.port)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BoltStats:
  """
  Attributes:
   - acked
   - failed
   - process_ms_avg
   - executed
   - execute_ms_avg
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'acked', (TType.STRING,None,TType.MAP,(TType.STRUCT,(GlobalStreamId, GlobalStreamId.thrift_spec),TType.I64,None)), None, ), # 1
    (2, TType.MAP, 'failed', (TType.STRING,None,TType.MAP,(TType.STRUCT,(GlobalStreamId, GlobalStreamId.thrift_spec),TType.I64,None)), None, ), # 2
    (3, TType.MAP, 'process_ms_avg', (TType.STRING,None,TType.MAP,(TType.STRUCT,(GlobalStreamId, GlobalStreamId.thrift_spec),TType.DOUBLE,None)), None, ), # 3
    (4, TType.MAP, 'executed', (TType.STRING,None,TType.MAP,(TType.STRUCT,(GlobalStreamId, GlobalStreamId.thrift_spec),TType.I64,None)), None, ), # 4
    (5, TType.MAP, 'execute_ms_avg', (TType.STRING,None,TType.MAP,(TType.STRUCT,(GlobalStreamId, GlobalStreamId.thrift_spec),TType.DOUBLE,None)), None, ), # 5
  )

  def __init__(self, acked=None, failed=None, process_ms_avg=None, executed=None, execute_ms_avg=None,):
    self.acked = acked
    self.failed = failed
    self.process_ms_avg = process_ms_avg
    self.executed = executed
    self.execute_ms_avg = execute_ms_avg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.acked = {}
          (_ktype88, _vtype89, _size87 ) = iprot.readMapBegin()
          for _i91 in xrange(_size87):
            _key92 = iprot.readString().decode('utf-8')
            _val93 = {}
            (_ktype95, _vtype96, _size94 ) = iprot.readMapBegin()
            for _i98 in xrange(_size94):
              _key99 = GlobalStreamId()
              _key99.read(iprot)
              _val100 = iprot.readI64();
              _val93[_key99] = _val100
            iprot.readMapEnd()
            self.acked[_key92] = _val93
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.failed = {}
          (_ktype102, _vtype103, _size101 ) = iprot.readMapBegin()
          for _i105 in xrange(_size101):
            _key106 = iprot.readString().decode('utf-8')
            _val107 = {}
            (_ktype109, _vtype110, _size108 ) = iprot.readMapBegin()
            for _i112 in xrange(_size108):
              _key113 = GlobalStreamId()
              _key113.read(iprot)
              _val114 = iprot.readI64();
              _val107[_key113] = _val114
            iprot.readMapEnd()
            self.failed[_key106] = _val107
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.process_ms_avg = {}
          (_ktype116, _vtype117, _size115 ) = iprot.readMapBegin()
          for _i119 in xrange(_size115):
            _key120 = iprot.readString().decode('utf-8')
            _val121 = {}
            (_ktype123, _vtype124, _size122 ) = iprot.readMapBegin()
            for _i126 in xrange(_size122):
              _key127 = GlobalStreamId()
              _key127.read(iprot)
              _val128 = iprot.readDouble();
              _val121[_key127] = _val128
            iprot.readMapEnd()
            self.process_ms_avg[_key120] = _val121
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.executed = {}
          (_ktype130, _vtype131, _size129 ) = iprot.readMapBegin()
          for _i133 in xrange(_size129):
            _key134 = iprot.readString().decode('utf-8')
            _val135 = {}
            (_ktype137, _vtype138, _size136 ) = iprot.readMapBegin()
            for _i140 in xrange(_size136):
              _key141 = GlobalStreamId()
              _key141.read(iprot)
              _val142 = iprot.readI64();
              _val135[_key141] = _val142
            iprot.readMapEnd()
            self.executed[_key134] = _val135
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.MAP:
          self.execute_ms_avg = {}
          (_ktype144, _vtype145, _size143 ) = iprot.readMapBegin()
          for _i147 in xrange(_size143):
            _key148 = iprot.readString().decode('utf-8')
            _val149 = {}
            (_ktype151, _vtype152, _size150 ) = iprot.readMapBegin()
            for _i154 in xrange(_size150):
              _key155 = GlobalStreamId()
              _key155.read(iprot)
              _val156 = iprot.readDouble();
              _val149[_key155] = _val156
            iprot.readMapEnd()
            self.execute_ms_avg[_key148] = _val149
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BoltStats')
    if self.acked is not None:
      oprot.writeFieldBegin('acked', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.acked))
      for kiter157,viter158 in self.acked.items():
        oprot.writeString(kiter157.encode('utf-8'))
        oprot.writeMapBegin(TType.STRUCT, TType.I64, len(viter158))
        for kiter159,viter160 in viter158.items():
          kiter159.write(oprot)
          oprot.writeI64(viter160)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.failed is not None:
      oprot.writeFieldBegin('failed', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.failed))
      for kiter161,viter162 in self.failed.items():
        oprot.writeString(kiter161.encode('utf-8'))
        oprot.writeMapBegin(TType.STRUCT, TType.I64, len(viter162))
        for kiter163,viter164 in viter162.items():
          kiter163.write(oprot)
          oprot.writeI64(viter164)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.process_ms_avg is not None:
      oprot.writeFieldBegin('process_ms_avg', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.process_ms_avg))
      for kiter165,viter166 in self.process_ms_avg.items():
        oprot.writeString(kiter165.encode('utf-8'))
        oprot.writeMapBegin(TType.STRUCT, TType.DOUBLE, len(viter166))
        for kiter167,viter168 in viter166.items():
          kiter167.write(oprot)
          oprot.writeDouble(viter168)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.executed is not None:
      oprot.writeFieldBegin('executed', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.executed))
      for kiter169,viter170 in self.executed.items():
        oprot.writeString(kiter169.encode('utf-8'))
        oprot.writeMapBegin(TType.STRUCT, TType.I64, len(viter170))
        for kiter171,viter172 in viter170.items():
          kiter171.write(oprot)
          oprot.writeI64(viter172)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.execute_ms_avg is not None:
      oprot.writeFieldBegin('execute_ms_avg', TType.MAP, 5)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.execute_ms_avg))
      for kiter173,viter174 in self.execute_ms_avg.items():
        oprot.writeString(kiter173.encode('utf-8'))
        oprot.writeMapBegin(TType.STRUCT, TType.DOUBLE, len(viter174))
        for kiter175,viter176 in viter174.items():
          kiter175.write(oprot)
          oprot.writeDouble(viter176)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.acked is None:
      raise TProtocol.TProtocolException(message='Required field acked is unset!')
    if self.failed is None:
      raise TProtocol.TProtocolException(message='Required field failed is unset!')
    if self.process_ms_avg is None:
      raise TProtocol.TProtocolException(message='Required field process_ms_avg is unset!')
    if self.executed is None:
      raise TProtocol.TProtocolException(message='Required field executed is unset!')
    if self.execute_ms_avg is None:
      raise TProtocol.TProtocolException(message='Required field execute_ms_avg is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.acked)
    value = (value * 31) ^ hash(self.failed)
    value = (value * 31) ^ hash(self.process_ms_avg)
    value = (value * 31) ^ hash(self.executed)
    value = (value * 31) ^ hash(self.execute_ms_avg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SpoutStats:
  """
  Attributes:
   - acked
   - failed
   - complete_ms_avg
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'acked', (TType.STRING,None,TType.MAP,(TType.STRING,None,TType.I64,None)), None, ), # 1
    (2, TType.MAP, 'failed', (TType.STRING,None,TType.MAP,(TType.STRING,None,TType.I64,None)), None, ), # 2
    (3, TType.MAP, 'complete_ms_avg', (TType.STRING,None,TType.MAP,(TType.STRING,None,TType.DOUBLE,None)), None, ), # 3
  )

  def __init__(self, acked=None, failed=None, complete_ms_avg=None,):
    self.acked = acked
    self.failed = failed
    self.complete_ms_avg = complete_ms_avg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.acked = {}
          (_ktype178, _vtype179, _size177 ) = iprot.readMapBegin()
          for _i181 in xrange(_size177):
            _key182 = iprot.readString().decode('utf-8')
            _val183 = {}
            (_ktype185, _vtype186, _size184 ) = iprot.readMapBegin()
            for _i188 in xrange(_size184):
              _key189 = iprot.readString().decode('utf-8')
              _val190 = iprot.readI64();
              _val183[_key189] = _val190
            iprot.readMapEnd()
            self.acked[_key182] = _val183
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.failed = {}
          (_ktype192, _vtype193, _size191 ) = iprot.readMapBegin()
          for _i195 in xrange(_size191):
            _key196 = iprot.readString().decode('utf-8')
            _val197 = {}
            (_ktype199, _vtype200, _size198 ) = iprot.readMapBegin()
            for _i202 in xrange(_size198):
              _key203 = iprot.readString().decode('utf-8')
              _val204 = iprot.readI64();
              _val197[_key203] = _val204
            iprot.readMapEnd()
            self.failed[_key196] = _val197
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.complete_ms_avg = {}
          (_ktype206, _vtype207, _size205 ) = iprot.readMapBegin()
          for _i209 in xrange(_size205):
            _key210 = iprot.readString().decode('utf-8')
            _val211 = {}
            (_ktype213, _vtype214, _size212 ) = iprot.readMapBegin()
            for _i216 in xrange(_size212):
              _key217 = iprot.readString().decode('utf-8')
              _val218 = iprot.readDouble();
              _val211[_key217] = _val218
            iprot.readMapEnd()
            self.complete_ms_avg[_key210] = _val211
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SpoutStats')
    if self.acked is not None:
      oprot.writeFieldBegin('acked', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.acked))
      for kiter219,viter220 in self.acked.items():
        oprot.writeString(kiter219.encode('utf-8'))
        oprot.writeMapBegin(TType.STRING, TType.I64, len(viter220))
        for kiter221,viter222 in viter220.items():
          oprot.writeString(kiter221.encode('utf-8'))
          oprot.writeI64(viter222)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.failed is not None:
      oprot.writeFieldBegin('failed', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.failed))
      for kiter223,viter224 in self.failed.items():
        oprot.writeString(kiter223.encode('utf-8'))
        oprot.writeMapBegin(TType.STRING, TType.I64, len(viter224))
        for kiter225,viter226 in viter224.items():
          oprot.writeString(kiter225.encode('utf-8'))
          oprot.writeI64(viter226)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.complete_ms_avg is not None:
      oprot.writeFieldBegin('complete_ms_avg', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.complete_ms_avg))
      for kiter227,viter228 in self.complete_ms_avg.items():
        oprot.writeString(kiter227.encode('utf-8'))
        oprot.writeMapBegin(TType.STRING, TType.DOUBLE, len(viter228))
        for kiter229,viter230 in viter228.items():
          oprot.writeString(kiter229.encode('utf-8'))
          oprot.writeDouble(viter230)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.acked is None:
      raise TProtocol.TProtocolException(message='Required field acked is unset!')
    if self.failed is None:
      raise TProtocol.TProtocolException(message='Required field failed is unset!')
    if self.complete_ms_avg is None:
      raise TProtocol.TProtocolException(message='Required field complete_ms_avg is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.acked)
    value = (value * 31) ^ hash(self.failed)
    value = (value * 31) ^ hash(self.complete_ms_avg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExecutorSpecificStats:
  """
  Attributes:
   - bolt
   - spout
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'bolt', (BoltStats, BoltStats.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'spout', (SpoutStats, SpoutStats.thrift_spec), None, ), # 2
  )

  def __init__(self, bolt=None, spout=None,):
    self.bolt = bolt
    self.spout = spout

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.bolt = BoltStats()
          self.bolt.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.spout = SpoutStats()
          self.spout.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ExecutorSpecificStats')
    if self.bolt is not None:
      oprot.writeFieldBegin('bolt', TType.STRUCT, 1)
      self.bolt.write(oprot)
      oprot.writeFieldEnd()
    if self.spout is not None:
      oprot.writeFieldBegin('spout', TType.STRUCT, 2)
      self.spout.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.bolt)
    value = (value * 31) ^ hash(self.spout)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExecutorStats:
  """
  Attributes:
   - emitted
   - transferred
   - specific
   - rate
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'emitted', (TType.STRING,None,TType.MAP,(TType.STRING,None,TType.I64,None)), None, ), # 1
    (2, TType.MAP, 'transferred', (TType.STRING,None,TType.MAP,(TType.STRING,None,TType.I64,None)), None, ), # 2
    (3, TType.STRUCT, 'specific', (ExecutorSpecificStats, ExecutorSpecificStats.thrift_spec), None, ), # 3
    (4, TType.DOUBLE, 'rate', None, None, ), # 4
  )

  def __init__(self, emitted=None, transferred=None, specific=None, rate=None,):
    self.emitted = emitted
    self.transferred = transferred
    self.specific = specific
    self.rate = rate

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.emitted = {}
          (_ktype232, _vtype233, _size231 ) = iprot.readMapBegin()
          for _i235 in xrange(_size231):
            _key236 = iprot.readString().decode('utf-8')
            _val237 = {}
            (_ktype239, _vtype240, _size238 ) = iprot.readMapBegin()
            for _i242 in xrange(_size238):
              _key243 = iprot.readString().decode('utf-8')
              _val244 = iprot.readI64();
              _val237[_key243] = _val244
            iprot.readMapEnd()
            self.emitted[_key236] = _val237
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.transferred = {}
          (_ktype246, _vtype247, _size245 ) = iprot.readMapBegin()
          for _i249 in xrange(_size245):
            _key250 = iprot.readString().decode('utf-8')
            _val251 = {}
            (_ktype253, _vtype254, _size252 ) = iprot.readMapBegin()
            for _i256 in xrange(_size252):
              _key257 = iprot.readString().decode('utf-8')
              _val258 = iprot.readI64();
              _val251[_key257] = _val258
            iprot.readMapEnd()
            self.transferred[_key250] = _val251
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.specific = ExecutorSpecificStats()
          self.specific.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.rate = iprot.readDouble();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ExecutorStats')
    if self.emitted is not None:
      oprot.writeFieldBegin('emitted', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.emitted))
      for kiter259,viter260 in self.emitted.items():
        oprot.writeString(kiter259.encode('utf-8'))
        oprot.writeMapBegin(TType.STRING, TType.I64, len(viter260))
        for kiter261,viter262 in viter260.items():
          oprot.writeString(kiter261.encode('utf-8'))
          oprot.writeI64(viter262)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.transferred is not None:
      oprot.writeFieldBegin('transferred', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.MAP, len(self.transferred))
      for kiter263,viter264 in self.transferred.items():
        oprot.writeString(kiter263.encode('utf-8'))
        oprot.writeMapBegin(TType.STRING, TType.I64, len(viter264))
        for kiter265,viter266 in viter264.items():
          oprot.writeString(kiter265.encode('utf-8'))
          oprot.writeI64(viter266)
        oprot.writeMapEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.specific is not None:
      oprot.writeFieldBegin('specific', TType.STRUCT, 3)
      self.specific.write(oprot)
      oprot.writeFieldEnd()
    if self.rate is not None:
      oprot.writeFieldBegin('rate', TType.DOUBLE, 4)
      oprot.writeDouble(self.rate)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.emitted is None:
      raise TProtocol.TProtocolException(message='Required field emitted is unset!')
    if self.transferred is None:
      raise TProtocol.TProtocolException(message='Required field transferred is unset!')
    if self.specific is None:
      raise TProtocol.TProtocolException(message='Required field specific is unset!')
    if self.rate is None:
      raise TProtocol.TProtocolException(message='Required field rate is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.emitted)
    value = (value * 31) ^ hash(self.transferred)
    value = (value * 31) ^ hash(self.specific)
    value = (value * 31) ^ hash(self.rate)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExecutorInfo:
  """
  Attributes:
   - task_start
   - task_end
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'task_start', None, None, ), # 1
    (2, TType.I32, 'task_end', None, None, ), # 2
  )

  def __init__(self, task_start=None, task_end=None,):
    self.task_start = task_start
    self.task_end = task_end

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.task_start = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.task_end = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ExecutorInfo')
    if self.task_start is not None:
      oprot.writeFieldBegin('task_start', TType.I32, 1)
      oprot.writeI32(self.task_start)
      oprot.writeFieldEnd()
    if self.task_end is not None:
      oprot.writeFieldBegin('task_end', TType.I32, 2)
      oprot.writeI32(self.task_end)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.task_start is None:
      raise TProtocol.TProtocolException(message='Required field task_start is unset!')
    if self.task_end is None:
      raise TProtocol.TProtocolException(message='Required field task_end is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.task_start)
    value = (value * 31) ^ hash(self.task_end)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExecutorSummary:
  """
  Attributes:
   - executor_info
   - component_id
   - host
   - port
   - uptime_secs
   - stats
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'executor_info', (ExecutorInfo, ExecutorInfo.thrift_spec), None, ), # 1
    (2, TType.STRING, 'component_id', None, None, ), # 2
    (3, TType.STRING, 'host', None, None, ), # 3
    (4, TType.I32, 'port', None, None, ), # 4
    (5, TType.I32, 'uptime_secs', None, None, ), # 5
    None, # 6
    (7, TType.STRUCT, 'stats', (ExecutorStats, ExecutorStats.thrift_spec), None, ), # 7
  )

  def __init__(self, executor_info=None, component_id=None, host=None, port=None, uptime_secs=None, stats=None,):
    self.executor_info = executor_info
    self.component_id = component_id
    self.host = host
    self.port = port
    self.uptime_secs = uptime_secs
    self.stats = stats

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.executor_info = ExecutorInfo()
          self.executor_info.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.component_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.host = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.uptime_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRUCT:
          self.stats = ExecutorStats()
          self.stats.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ExecutorSummary')
    if self.executor_info is not None:
      oprot.writeFieldBegin('executor_info', TType.STRUCT, 1)
      self.executor_info.write(oprot)
      oprot.writeFieldEnd()
    if self.component_id is not None:
      oprot.writeFieldBegin('component_id', TType.STRING, 2)
      oprot.writeString(self.component_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.host is not None:
      oprot.writeFieldBegin('host', TType.STRING, 3)
      oprot.writeString(self.host.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 4)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I32, 5)
      oprot.writeI32(self.uptime_secs)
      oprot.writeFieldEnd()
    if self.stats is not None:
      oprot.writeFieldBegin('stats', TType.STRUCT, 7)
      self.stats.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.executor_info is None:
      raise TProtocol.TProtocolException(message='Required field executor_info is unset!')
    if self.component_id is None:
      raise TProtocol.TProtocolException(message='Required field component_id is unset!')
    if self.host is None:
      raise TProtocol.TProtocolException(message='Required field host is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    if self.uptime_secs is None:
      raise TProtocol.TProtocolException(message='Required field uptime_secs is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.executor_info)
    value = (value * 31) ^ hash(self.component_id)
    value = (value * 31) ^ hash(self.host)
    value = (value * 31) ^ hash(self.port)
    value = (value * 31) ^ hash(self.uptime_secs)
    value = (value * 31) ^ hash(self.stats)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TopologyInfo:
  """
  Attributes:
   - id
   - name
   - uptime_secs
   - executors
   - status
   - errors
   - sched_status
   - owner
   - replication_count
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'uptime_secs', None, None, ), # 3
    (4, TType.LIST, 'executors', (TType.STRUCT,(ExecutorSummary, ExecutorSummary.thrift_spec)), None, ), # 4
    (5, TType.STRING, 'status', None, None, ), # 5
    (6, TType.MAP, 'errors', (TType.STRING,None,TType.LIST,(TType.STRUCT,(ErrorInfo, ErrorInfo.thrift_spec))), None, ), # 6
    None, # 7
    None, # 8
    None, # 9
    None, # 10
    None, # 11
    None, # 12
    None, # 13
    None, # 14
    None, # 15
    None, # 16
    None, # 17
    None, # 18
    None, # 19
    None, # 20
    None, # 21
    None, # 22
    None, # 23
    None, # 24
    None, # 25
    None, # 26
    None, # 27
    None, # 28
    None, # 29
    None, # 30
    None, # 31
    None, # 32
    None, # 33
    None, # 34
    None, # 35
    None, # 36
    None, # 37
    None, # 38
    None, # 39
    None, # 40
    None, # 41
    None, # 42
    None, # 43
    None, # 44
    None, # 45
    None, # 46
    None, # 47
    None, # 48
    None, # 49
    None, # 50
    None, # 51
    None, # 52
    None, # 53
    None, # 54
    None, # 55
    None, # 56
    None, # 57
    None, # 58
    None, # 59
    None, # 60
    None, # 61
    None, # 62
    None, # 63
    None, # 64
    None, # 65
    None, # 66
    None, # 67
    None, # 68
    None, # 69
    None, # 70
    None, # 71
    None, # 72
    None, # 73
    None, # 74
    None, # 75
    None, # 76
    None, # 77
    None, # 78
    None, # 79
    None, # 80
    None, # 81
    None, # 82
    None, # 83
    None, # 84
    None, # 85
    None, # 86
    None, # 87
    None, # 88
    None, # 89
    None, # 90
    None, # 91
    None, # 92
    None, # 93
    None, # 94
    None, # 95
    None, # 96
    None, # 97
    None, # 98
    None, # 99
    None, # 100
    None, # 101
    None, # 102
    None, # 103
    None, # 104
    None, # 105
    None, # 106
    None, # 107
    None, # 108
    None, # 109
    None, # 110
    None, # 111
    None, # 112
    None, # 113
    None, # 114
    None, # 115
    None, # 116
    None, # 117
    None, # 118
    None, # 119
    None, # 120
    None, # 121
    None, # 122
    None, # 123
    None, # 124
    None, # 125
    None, # 126
    None, # 127
    None, # 128
    None, # 129
    None, # 130
    None, # 131
    None, # 132
    None, # 133
    None, # 134
    None, # 135
    None, # 136
    None, # 137
    None, # 138
    None, # 139
    None, # 140
    None, # 141
    None, # 142
    None, # 143
    None, # 144
    None, # 145
    None, # 146
    None, # 147
    None, # 148
    None, # 149
    None, # 150
    None, # 151
    None, # 152
    None, # 153
    None, # 154
    None, # 155
    None, # 156
    None, # 157
    None, # 158
    None, # 159
    None, # 160
    None, # 161
    None, # 162
    None, # 163
    None, # 164
    None, # 165
    None, # 166
    None, # 167
    None, # 168
    None, # 169
    None, # 170
    None, # 171
    None, # 172
    None, # 173
    None, # 174
    None, # 175
    None, # 176
    None, # 177
    None, # 178
    None, # 179
    None, # 180
    None, # 181
    None, # 182
    None, # 183
    None, # 184
    None, # 185
    None, # 186
    None, # 187
    None, # 188
    None, # 189
    None, # 190
    None, # 191
    None, # 192
    None, # 193
    None, # 194
    None, # 195
    None, # 196
    None, # 197
    None, # 198
    None, # 199
    None, # 200
    None, # 201
    None, # 202
    None, # 203
    None, # 204
    None, # 205
    None, # 206
    None, # 207
    None, # 208
    None, # 209
    None, # 210
    None, # 211
    None, # 212
    None, # 213
    None, # 214
    None, # 215
    None, # 216
    None, # 217
    None, # 218
    None, # 219
    None, # 220
    None, # 221
    None, # 222
    None, # 223
    None, # 224
    None, # 225
    None, # 226
    None, # 227
    None, # 228
    None, # 229
    None, # 230
    None, # 231
    None, # 232
    None, # 233
    None, # 234
    None, # 235
    None, # 236
    None, # 237
    None, # 238
    None, # 239
    None, # 240
    None, # 241
    None, # 242
    None, # 243
    None, # 244
    None, # 245
    None, # 246
    None, # 247
    None, # 248
    None, # 249
    None, # 250
    None, # 251
    None, # 252
    None, # 253
    None, # 254
    None, # 255
    None, # 256
    None, # 257
    None, # 258
    None, # 259
    None, # 260
    None, # 261
    None, # 262
    None, # 263
    None, # 264
    None, # 265
    None, # 266
    None, # 267
    None, # 268
    None, # 269
    None, # 270
    None, # 271
    None, # 272
    None, # 273
    None, # 274
    None, # 275
    None, # 276
    None, # 277
    None, # 278
    None, # 279
    None, # 280
    None, # 281
    None, # 282
    None, # 283
    None, # 284
    None, # 285
    None, # 286
    None, # 287
    None, # 288
    None, # 289
    None, # 290
    None, # 291
    None, # 292
    None, # 293
    None, # 294
    None, # 295
    None, # 296
    None, # 297
    None, # 298
    None, # 299
    None, # 300
    None, # 301
    None, # 302
    None, # 303
    None, # 304
    None, # 305
    None, # 306
    None, # 307
    None, # 308
    None, # 309
    None, # 310
    None, # 311
    None, # 312
    None, # 313
    None, # 314
    None, # 315
    None, # 316
    None, # 317
    None, # 318
    None, # 319
    None, # 320
    None, # 321
    None, # 322
    None, # 323
    None, # 324
    None, # 325
    None, # 326
    None, # 327
    None, # 328
    None, # 329
    None, # 330
    None, # 331
    None, # 332
    None, # 333
    None, # 334
    None, # 335
    None, # 336
    None, # 337
    None, # 338
    None, # 339
    None, # 340
    None, # 341
    None, # 342
    None, # 343
    None, # 344
    None, # 345
    None, # 346
    None, # 347
    None, # 348
    None, # 349
    None, # 350
    None, # 351
    None, # 352
    None, # 353
    None, # 354
    None, # 355
    None, # 356
    None, # 357
    None, # 358
    None, # 359
    None, # 360
    None, # 361
    None, # 362
    None, # 363
    None, # 364
    None, # 365
    None, # 366
    None, # 367
    None, # 368
    None, # 369
    None, # 370
    None, # 371
    None, # 372
    None, # 373
    None, # 374
    None, # 375
    None, # 376
    None, # 377
    None, # 378
    None, # 379
    None, # 380
    None, # 381
    None, # 382
    None, # 383
    None, # 384
    None, # 385
    None, # 386
    None, # 387
    None, # 388
    None, # 389
    None, # 390
    None, # 391
    None, # 392
    None, # 393
    None, # 394
    None, # 395
    None, # 396
    None, # 397
    None, # 398
    None, # 399
    None, # 400
    None, # 401
    None, # 402
    None, # 403
    None, # 404
    None, # 405
    None, # 406
    None, # 407
    None, # 408
    None, # 409
    None, # 410
    None, # 411
    None, # 412
    None, # 413
    None, # 414
    None, # 415
    None, # 416
    None, # 417
    None, # 418
    None, # 419
    None, # 420
    None, # 421
    None, # 422
    None, # 423
    None, # 424
    None, # 425
    None, # 426
    None, # 427
    None, # 428
    None, # 429
    None, # 430
    None, # 431
    None, # 432
    None, # 433
    None, # 434
    None, # 435
    None, # 436
    None, # 437
    None, # 438
    None, # 439
    None, # 440
    None, # 441
    None, # 442
    None, # 443
    None, # 444
    None, # 445
    None, # 446
    None, # 447
    None, # 448
    None, # 449
    None, # 450
    None, # 451
    None, # 452
    None, # 453
    None, # 454
    None, # 455
    None, # 456
    None, # 457
    None, # 458
    None, # 459
    None, # 460
    None, # 461
    None, # 462
    None, # 463
    None, # 464
    None, # 465
    None, # 466
    None, # 467
    None, # 468
    None, # 469
    None, # 470
    None, # 471
    None, # 472
    None, # 473
    None, # 474
    None, # 475
    None, # 476
    None, # 477
    None, # 478
    None, # 479
    None, # 480
    None, # 481
    None, # 482
    None, # 483
    None, # 484
    None, # 485
    None, # 486
    None, # 487
    None, # 488
    None, # 489
    None, # 490
    None, # 491
    None, # 492
    None, # 493
    None, # 494
    None, # 495
    None, # 496
    None, # 497
    None, # 498
    None, # 499
    None, # 500
    None, # 501
    None, # 502
    None, # 503
    None, # 504
    None, # 505
    None, # 506
    None, # 507
    None, # 508
    None, # 509
    None, # 510
    None, # 511
    None, # 512
    (513, TType.STRING, 'sched_status', None, None, ), # 513
    (514, TType.STRING, 'owner', None, None, ), # 514
    (515, TType.I32, 'replication_count', None, None, ), # 515
  )

  def __init__(self, id=None, name=None, uptime_secs=None, executors=None, status=None, errors=None, sched_status=None, owner=None, replication_count=None,):
    self.id = id
    self.name = name
    self.uptime_secs = uptime_secs
    self.executors = executors
    self.status = status
    self.errors = errors
    self.sched_status = sched_status
    self.owner = owner
    self.replication_count = replication_count

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.uptime_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.executors = []
          (_etype270, _size267) = iprot.readListBegin()
          for _i271 in xrange(_size267):
            _elem272 = ExecutorSummary()
            _elem272.read(iprot)
            self.executors.append(_elem272)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.status = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.MAP:
          self.errors = {}
          (_ktype274, _vtype275, _size273 ) = iprot.readMapBegin()
          for _i277 in xrange(_size273):
            _key278 = iprot.readString().decode('utf-8')
            _val279 = []
            (_etype283, _size280) = iprot.readListBegin()
            for _i284 in xrange(_size280):
              _elem285 = ErrorInfo()
              _elem285.read(iprot)
              _val279.append(_elem285)
            iprot.readListEnd()
            self.errors[_key278] = _val279
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 513:
        if ftype == TType.STRING:
          self.sched_status = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 514:
        if ftype == TType.STRING:
          self.owner = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 515:
        if ftype == TType.I32:
          self.replication_count = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TopologyInfo')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I32, 3)
      oprot.writeI32(self.uptime_secs)
      oprot.writeFieldEnd()
    if self.executors is not None:
      oprot.writeFieldBegin('executors', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.executors))
      for iter286 in self.executors:
        iter286.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRING, 5)
      oprot.writeString(self.status.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.errors is not None:
      oprot.writeFieldBegin('errors', TType.MAP, 6)
      oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.errors))
      for kiter287,viter288 in self.errors.items():
        oprot.writeString(kiter287.encode('utf-8'))
        oprot.writeListBegin(TType.STRUCT, len(viter288))
        for iter289 in viter288:
          iter289.write(oprot)
        oprot.writeListEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.sched_status is not None:
      oprot.writeFieldBegin('sched_status', TType.STRING, 513)
      oprot.writeString(self.sched_status.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.owner is not None:
      oprot.writeFieldBegin('owner', TType.STRING, 514)
      oprot.writeString(self.owner.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.replication_count is not None:
      oprot.writeFieldBegin('replication_count', TType.I32, 515)
      oprot.writeI32(self.replication_count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.uptime_secs is None:
      raise TProtocol.TProtocolException(message='Required field uptime_secs is unset!')
    if self.executors is None:
      raise TProtocol.TProtocolException(message='Required field executors is unset!')
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    if self.errors is None:
      raise TProtocol.TProtocolException(message='Required field errors is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.uptime_secs)
    value = (value * 31) ^ hash(self.executors)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.errors)
    value = (value * 31) ^ hash(self.sched_status)
    value = (value * 31) ^ hash(self.owner)
    value = (value * 31) ^ hash(self.replication_count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class KillOptions:
  """
  Attributes:
   - wait_secs
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'wait_secs', None, None, ), # 1
  )

  def __init__(self, wait_secs=None,):
    self.wait_secs = wait_secs

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.wait_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('KillOptions')
    if self.wait_secs is not None:
      oprot.writeFieldBegin('wait_secs', TType.I32, 1)
      oprot.writeI32(self.wait_secs)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.wait_secs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RebalanceOptions:
  """
  Attributes:
   - wait_secs
   - num_workers
   - num_executors
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'wait_secs', None, None, ), # 1
    (2, TType.I32, 'num_workers', None, None, ), # 2
    (3, TType.MAP, 'num_executors', (TType.STRING,None,TType.I32,None), None, ), # 3
  )

  def __init__(self, wait_secs=None, num_workers=None, num_executors=None,):
    self.wait_secs = wait_secs
    self.num_workers = num_workers
    self.num_executors = num_executors

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.wait_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.num_workers = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.num_executors = {}
          (_ktype291, _vtype292, _size290 ) = iprot.readMapBegin()
          for _i294 in xrange(_size290):
            _key295 = iprot.readString().decode('utf-8')
            _val296 = iprot.readI32();
            self.num_executors[_key295] = _val296
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RebalanceOptions')
    if self.wait_secs is not None:
      oprot.writeFieldBegin('wait_secs', TType.I32, 1)
      oprot.writeI32(self.wait_secs)
      oprot.writeFieldEnd()
    if self.num_workers is not None:
      oprot.writeFieldBegin('num_workers', TType.I32, 2)
      oprot.writeI32(self.num_workers)
      oprot.writeFieldEnd()
    if self.num_executors is not None:
      oprot.writeFieldBegin('num_executors', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.I32, len(self.num_executors))
      for kiter297,viter298 in self.num_executors.items():
        oprot.writeString(kiter297.encode('utf-8'))
        oprot.writeI32(viter298)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.wait_secs)
    value = (value * 31) ^ hash(self.num_workers)
    value = (value * 31) ^ hash(self.num_executors)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Credentials:
  """
  Attributes:
   - creds
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'creds', (TType.STRING,None,TType.STRING,None), None, ), # 1
  )

  def __init__(self, creds=None,):
    self.creds = creds

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.creds = {}
          (_ktype300, _vtype301, _size299 ) = iprot.readMapBegin()
          for _i303 in xrange(_size299):
            _key304 = iprot.readString().decode('utf-8')
            _val305 = iprot.readString().decode('utf-8')
            self.creds[_key304] = _val305
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Credentials')
    if self.creds is not None:
      oprot.writeFieldBegin('creds', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.creds))
      for kiter306,viter307 in self.creds.items():
        oprot.writeString(kiter306.encode('utf-8'))
        oprot.writeString(viter307.encode('utf-8'))
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.creds is None:
      raise TProtocol.TProtocolException(message='Required field creds is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.creds)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SubmitOptions:
  """
  Attributes:
   - initial_status
   - creds
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'initial_status', None, None, ), # 1
    (2, TType.STRUCT, 'creds', (Credentials, Credentials.thrift_spec), None, ), # 2
  )

  def __init__(self, initial_status=None, creds=None,):
    self.initial_status = initial_status
    self.creds = creds

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.initial_status = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.creds = Credentials()
          self.creds.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SubmitOptions')
    if self.initial_status is not None:
      oprot.writeFieldBegin('initial_status', TType.I32, 1)
      oprot.writeI32(self.initial_status)
      oprot.writeFieldEnd()
    if self.creds is not None:
      oprot.writeFieldBegin('creds', TType.STRUCT, 2)
      self.creds.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.initial_status is None:
      raise TProtocol.TProtocolException(message='Required field initial_status is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.initial_status)
    value = (value * 31) ^ hash(self.creds)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SupervisorInfo:
  """
  Attributes:
   - time_secs
   - hostname
   - assignment_id
   - used_ports
   - meta
   - scheduler_meta
   - uptime_secs
   - version
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'time_secs', None, None, ), # 1
    (2, TType.STRING, 'hostname', None, None, ), # 2
    (3, TType.STRING, 'assignment_id', None, None, ), # 3
    (4, TType.LIST, 'used_ports', (TType.I64,None), None, ), # 4
    (5, TType.LIST, 'meta', (TType.I64,None), None, ), # 5
    (6, TType.MAP, 'scheduler_meta', (TType.STRING,None,TType.STRING,None), None, ), # 6
    (7, TType.I64, 'uptime_secs', None, None, ), # 7
    (8, TType.STRING, 'version', None, None, ), # 8
  )

  def __init__(self, time_secs=None, hostname=None, assignment_id=None, used_ports=None, meta=None, scheduler_meta=None, uptime_secs=None, version=None,):
    self.time_secs = time_secs
    self.hostname = hostname
    self.assignment_id = assignment_id
    self.used_ports = used_ports
    self.meta = meta
    self.scheduler_meta = scheduler_meta
    self.uptime_secs = uptime_secs
    self.version = version

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.time_secs = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.hostname = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.assignment_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.used_ports = []
          (_etype311, _size308) = iprot.readListBegin()
          for _i312 in xrange(_size308):
            _elem313 = iprot.readI64();
            self.used_ports.append(_elem313)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.meta = []
          (_etype317, _size314) = iprot.readListBegin()
          for _i318 in xrange(_size314):
            _elem319 = iprot.readI64();
            self.meta.append(_elem319)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.MAP:
          self.scheduler_meta = {}
          (_ktype321, _vtype322, _size320 ) = iprot.readMapBegin()
          for _i324 in xrange(_size320):
            _key325 = iprot.readString().decode('utf-8')
            _val326 = iprot.readString().decode('utf-8')
            self.scheduler_meta[_key325] = _val326
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.uptime_secs = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.version = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SupervisorInfo')
    if self.time_secs is not None:
      oprot.writeFieldBegin('time_secs', TType.I64, 1)
      oprot.writeI64(self.time_secs)
      oprot.writeFieldEnd()
    if self.hostname is not None:
      oprot.writeFieldBegin('hostname', TType.STRING, 2)
      oprot.writeString(self.hostname.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.assignment_id is not None:
      oprot.writeFieldBegin('assignment_id', TType.STRING, 3)
      oprot.writeString(self.assignment_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.used_ports is not None:
      oprot.writeFieldBegin('used_ports', TType.LIST, 4)
      oprot.writeListBegin(TType.I64, len(self.used_ports))
      for iter327 in self.used_ports:
        oprot.writeI64(iter327)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.meta is not None:
      oprot.writeFieldBegin('meta', TType.LIST, 5)
      oprot.writeListBegin(TType.I64, len(self.meta))
      for iter328 in self.meta:
        oprot.writeI64(iter328)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.scheduler_meta is not None:
      oprot.writeFieldBegin('scheduler_meta', TType.MAP, 6)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.scheduler_meta))
      for kiter329,viter330 in self.scheduler_meta.items():
        oprot.writeString(kiter329.encode('utf-8'))
        oprot.writeString(viter330.encode('utf-8'))
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I64, 7)
      oprot.writeI64(self.uptime_secs)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 8)
      oprot.writeString(self.version.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.time_secs is None:
      raise TProtocol.TProtocolException(message='Required field time_secs is unset!')
    if self.hostname is None:
      raise TProtocol.TProtocolException(message='Required field hostname is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.time_secs)
    value = (value * 31) ^ hash(self.hostname)
    value = (value * 31) ^ hash(self.assignment_id)
    value = (value * 31) ^ hash(self.used_ports)
    value = (value * 31) ^ hash(self.meta)
    value = (value * 31) ^ hash(self.scheduler_meta)
    value = (value * 31) ^ hash(self.uptime_secs)
    value = (value * 31) ^ hash(self.version)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NodeInfo:
  """
  Attributes:
   - node
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'node', None, None, ), # 1
    (2, TType.SET, 'port', (TType.I64,None), None, ), # 2
  )

  def __init__(self, node=None, port=None,):
    self.node = node
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.node = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.SET:
          self.port = set()
          (_etype334, _size331) = iprot.readSetBegin()
          for _i335 in xrange(_size331):
            _elem336 = iprot.readI64();
            self.port.add(_elem336)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NodeInfo')
    if self.node is not None:
      oprot.writeFieldBegin('node', TType.STRING, 1)
      oprot.writeString(self.node.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.SET, 2)
      oprot.writeSetBegin(TType.I64, len(self.port))
      for iter337 in self.port:
        oprot.writeI64(iter337)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.node is None:
      raise TProtocol.TProtocolException(message='Required field node is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.node)
    value = (value * 31) ^ hash(self.port)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Assignment:
  """
  Attributes:
   - master_code_dir
   - node_host
   - executor_node_port
   - executor_start_time_secs
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'master_code_dir', None, None, ), # 1
    (2, TType.MAP, 'node_host', (TType.STRING,None,TType.STRING,None), {
    }, ), # 2
    (3, TType.MAP, 'executor_node_port', (TType.LIST,(TType.I64,None),TType.STRUCT,(NodeInfo, NodeInfo.thrift_spec)), {
    }, ), # 3
    (4, TType.MAP, 'executor_start_time_secs', (TType.LIST,(TType.I64,None),TType.I64,None), {
    }, ), # 4
  )

  def __init__(self, master_code_dir=None, node_host=thrift_spec[2][4], executor_node_port=thrift_spec[3][4], executor_start_time_secs=thrift_spec[4][4],):
    self.master_code_dir = master_code_dir
    if node_host is self.thrift_spec[2][4]:
      node_host = {
    }
    self.node_host = node_host
    if executor_node_port is self.thrift_spec[3][4]:
      executor_node_port = {
    }
    self.executor_node_port = executor_node_port
    if executor_start_time_secs is self.thrift_spec[4][4]:
      executor_start_time_secs = {
    }
    self.executor_start_time_secs = executor_start_time_secs

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.master_code_dir = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.node_host = {}
          (_ktype339, _vtype340, _size338 ) = iprot.readMapBegin()
          for _i342 in xrange(_size338):
            _key343 = iprot.readString().decode('utf-8')
            _val344 = iprot.readString().decode('utf-8')
            self.node_host[_key343] = _val344
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.executor_node_port = {}
          (_ktype346, _vtype347, _size345 ) = iprot.readMapBegin()
          for _i349 in xrange(_size345):
            _key350 = []
            (_etype355, _size352) = iprot.readListBegin()
            for _i356 in xrange(_size352):
              _elem357 = iprot.readI64();
              _key350.append(_elem357)
            iprot.readListEnd()
            _val351 = NodeInfo()
            _val351.read(iprot)
            self.executor_node_port[_key350] = _val351
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.executor_start_time_secs = {}
          (_ktype359, _vtype360, _size358 ) = iprot.readMapBegin()
          for _i362 in xrange(_size358):
            _key363 = []
            (_etype368, _size365) = iprot.readListBegin()
            for _i369 in xrange(_size365):
              _elem370 = iprot.readI64();
              _key363.append(_elem370)
            iprot.readListEnd()
            _val364 = iprot.readI64();
            self.executor_start_time_secs[_key363] = _val364
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Assignment')
    if self.master_code_dir is not None:
      oprot.writeFieldBegin('master_code_dir', TType.STRING, 1)
      oprot.writeString(self.master_code_dir.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.node_host is not None:
      oprot.writeFieldBegin('node_host', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.node_host))
      for kiter371,viter372 in self.node_host.items():
        oprot.writeString(kiter371.encode('utf-8'))
        oprot.writeString(viter372.encode('utf-8'))
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.executor_node_port is not None:
      oprot.writeFieldBegin('executor_node_port', TType.MAP, 3)
      oprot.writeMapBegin(TType.LIST, TType.STRUCT, len(self.executor_node_port))
      for kiter373,viter374 in self.executor_node_port.items():
        oprot.writeListBegin(TType.I64, len(kiter373))
        for iter375 in kiter373:
          oprot.writeI64(iter375)
        oprot.writeListEnd()
        viter374.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.executor_start_time_secs is not None:
      oprot.writeFieldBegin('executor_start_time_secs', TType.MAP, 4)
      oprot.writeMapBegin(TType.LIST, TType.I64, len(self.executor_start_time_secs))
      for kiter376,viter377 in self.executor_start_time_secs.items():
        oprot.writeListBegin(TType.I64, len(kiter376))
        for iter378 in kiter376:
          oprot.writeI64(iter378)
        oprot.writeListEnd()
        oprot.writeI64(viter377)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.master_code_dir is None:
      raise TProtocol.TProtocolException(message='Required field master_code_dir is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.master_code_dir)
    value = (value * 31) ^ hash(self.node_host)
    value = (value * 31) ^ hash(self.executor_node_port)
    value = (value * 31) ^ hash(self.executor_start_time_secs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TopologyActionOptions:
  """
  Attributes:
   - kill_options
   - rebalance_options
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'kill_options', (KillOptions, KillOptions.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'rebalance_options', (RebalanceOptions, RebalanceOptions.thrift_spec), None, ), # 2
  )

  def __init__(self, kill_options=None, rebalance_options=None,):
    self.kill_options = kill_options
    self.rebalance_options = rebalance_options

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.kill_options = KillOptions()
          self.kill_options.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.rebalance_options = RebalanceOptions()
          self.rebalance_options.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TopologyActionOptions')
    if self.kill_options is not None:
      oprot.writeFieldBegin('kill_options', TType.STRUCT, 1)
      self.kill_options.write(oprot)
      oprot.writeFieldEnd()
    if self.rebalance_options is not None:
      oprot.writeFieldBegin('rebalance_options', TType.STRUCT, 2)
      self.rebalance_options.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.kill_options)
    value = (value * 31) ^ hash(self.rebalance_options)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StormBase:
  """
  Attributes:
   - name
   - status
   - num_workers
   - component_executors
   - launch_time_secs
   - owner
   - topology_action_options
   - prev_status
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.I32, 'status', None, None, ), # 2
    (3, TType.I32, 'num_workers', None, None, ), # 3
    (4, TType.MAP, 'component_executors', (TType.STRING,None,TType.I32,None), None, ), # 4
    (5, TType.I32, 'launch_time_secs', None, None, ), # 5
    (6, TType.STRING, 'owner', None, None, ), # 6
    (7, TType.STRUCT, 'topology_action_options', (TopologyActionOptions, TopologyActionOptions.thrift_spec), None, ), # 7
    (8, TType.I32, 'prev_status', None, None, ), # 8
  )

  def __init__(self, name=None, status=None, num_workers=None, component_executors=None, launch_time_secs=None, owner=None, topology_action_options=None, prev_status=None,):
    self.name = name
    self.status = status
    self.num_workers = num_workers
    self.component_executors = component_executors
    self.launch_time_secs = launch_time_secs
    self.owner = owner
    self.topology_action_options = topology_action_options
    self.prev_status = prev_status

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.status = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.num_workers = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.component_executors = {}
          (_ktype380, _vtype381, _size379 ) = iprot.readMapBegin()
          for _i383 in xrange(_size379):
            _key384 = iprot.readString().decode('utf-8')
            _val385 = iprot.readI32();
            self.component_executors[_key384] = _val385
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.launch_time_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.owner = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRUCT:
          self.topology_action_options = TopologyActionOptions()
          self.topology_action_options.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.prev_status = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StormBase')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 2)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.num_workers is not None:
      oprot.writeFieldBegin('num_workers', TType.I32, 3)
      oprot.writeI32(self.num_workers)
      oprot.writeFieldEnd()
    if self.component_executors is not None:
      oprot.writeFieldBegin('component_executors', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.I32, len(self.component_executors))
      for kiter386,viter387 in self.component_executors.items():
        oprot.writeString(kiter386.encode('utf-8'))
        oprot.writeI32(viter387)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.launch_time_secs is not None:
      oprot.writeFieldBegin('launch_time_secs', TType.I32, 5)
      oprot.writeI32(self.launch_time_secs)
      oprot.writeFieldEnd()
    if self.owner is not None:
      oprot.writeFieldBegin('owner', TType.STRING, 6)
      oprot.writeString(self.owner.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.topology_action_options is not None:
      oprot.writeFieldBegin('topology_action_options', TType.STRUCT, 7)
      self.topology_action_options.write(oprot)
      oprot.writeFieldEnd()
    if self.prev_status is not None:
      oprot.writeFieldBegin('prev_status', TType.I32, 8)
      oprot.writeI32(self.prev_status)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    if self.num_workers is None:
      raise TProtocol.TProtocolException(message='Required field num_workers is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.num_workers)
    value = (value * 31) ^ hash(self.component_executors)
    value = (value * 31) ^ hash(self.launch_time_secs)
    value = (value * 31) ^ hash(self.owner)
    value = (value * 31) ^ hash(self.topology_action_options)
    value = (value * 31) ^ hash(self.prev_status)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ClusterWorkerHeartbeat:
  """
  Attributes:
   - storm_id
   - executor_stats
   - time_secs
   - uptime_secs
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'storm_id', None, None, ), # 1
    (2, TType.MAP, 'executor_stats', (TType.STRUCT,(ExecutorInfo, ExecutorInfo.thrift_spec),TType.STRUCT,(ExecutorStats, ExecutorStats.thrift_spec)), None, ), # 2
    (3, TType.I32, 'time_secs', None, None, ), # 3
    (4, TType.I32, 'uptime_secs', None, None, ), # 4
  )

  def __init__(self, storm_id=None, executor_stats=None, time_secs=None, uptime_secs=None,):
    self.storm_id = storm_id
    self.executor_stats = executor_stats
    self.time_secs = time_secs
    self.uptime_secs = uptime_secs

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.storm_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.executor_stats = {}
          (_ktype389, _vtype390, _size388 ) = iprot.readMapBegin()
          for _i392 in xrange(_size388):
            _key393 = ExecutorInfo()
            _key393.read(iprot)
            _val394 = ExecutorStats()
            _val394.read(iprot)
            self.executor_stats[_key393] = _val394
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.time_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.uptime_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ClusterWorkerHeartbeat')
    if self.storm_id is not None:
      oprot.writeFieldBegin('storm_id', TType.STRING, 1)
      oprot.writeString(self.storm_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.executor_stats is not None:
      oprot.writeFieldBegin('executor_stats', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRUCT, TType.STRUCT, len(self.executor_stats))
      for kiter395,viter396 in self.executor_stats.items():
        kiter395.write(oprot)
        viter396.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.time_secs is not None:
      oprot.writeFieldBegin('time_secs', TType.I32, 3)
      oprot.writeI32(self.time_secs)
      oprot.writeFieldEnd()
    if self.uptime_secs is not None:
      oprot.writeFieldBegin('uptime_secs', TType.I32, 4)
      oprot.writeI32(self.uptime_secs)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.storm_id is None:
      raise TProtocol.TProtocolException(message='Required field storm_id is unset!')
    if self.executor_stats is None:
      raise TProtocol.TProtocolException(message='Required field executor_stats is unset!')
    if self.time_secs is None:
      raise TProtocol.TProtocolException(message='Required field time_secs is unset!')
    if self.uptime_secs is None:
      raise TProtocol.TProtocolException(message='Required field uptime_secs is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.storm_id)
    value = (value * 31) ^ hash(self.executor_stats)
    value = (value * 31) ^ hash(self.time_secs)
    value = (value * 31) ^ hash(self.uptime_secs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ThriftSerializedObject:
  """
  Attributes:
   - name
   - bits
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'bits', None, None, ), # 2
  )

  def __init__(self, name=None, bits=None,):
    self.name = name
    self.bits = bits

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.bits = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ThriftSerializedObject')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.bits is not None:
      oprot.writeFieldBegin('bits', TType.STRING, 2)
      oprot.writeString(self.bits)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.bits is None:
      raise TProtocol.TProtocolException(message='Required field bits is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.bits)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LocalStateData:
  """
  Attributes:
   - serialized_parts
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'serialized_parts', (TType.STRING,None,TType.STRUCT,(ThriftSerializedObject, ThriftSerializedObject.thrift_spec)), None, ), # 1
  )

  def __init__(self, serialized_parts=None,):
    self.serialized_parts = serialized_parts

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.serialized_parts = {}
          (_ktype398, _vtype399, _size397 ) = iprot.readMapBegin()
          for _i401 in xrange(_size397):
            _key402 = iprot.readString().decode('utf-8')
            _val403 = ThriftSerializedObject()
            _val403.read(iprot)
            self.serialized_parts[_key402] = _val403
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LocalStateData')
    if self.serialized_parts is not None:
      oprot.writeFieldBegin('serialized_parts', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.serialized_parts))
      for kiter404,viter405 in self.serialized_parts.items():
        oprot.writeString(kiter404.encode('utf-8'))
        viter405.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serialized_parts is None:
      raise TProtocol.TProtocolException(message='Required field serialized_parts is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serialized_parts)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LocalAssignment:
  """
  Attributes:
   - topology_id
   - executors
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'topology_id', None, None, ), # 1
    (2, TType.LIST, 'executors', (TType.STRUCT,(ExecutorInfo, ExecutorInfo.thrift_spec)), None, ), # 2
  )

  def __init__(self, topology_id=None, executors=None,):
    self.topology_id = topology_id
    self.executors = executors

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.topology_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.executors = []
          (_etype409, _size406) = iprot.readListBegin()
          for _i410 in xrange(_size406):
            _elem411 = ExecutorInfo()
            _elem411.read(iprot)
            self.executors.append(_elem411)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LocalAssignment')
    if self.topology_id is not None:
      oprot.writeFieldBegin('topology_id', TType.STRING, 1)
      oprot.writeString(self.topology_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.executors is not None:
      oprot.writeFieldBegin('executors', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.executors))
      for iter412 in self.executors:
        iter412.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.topology_id is None:
      raise TProtocol.TProtocolException(message='Required field topology_id is unset!')
    if self.executors is None:
      raise TProtocol.TProtocolException(message='Required field executors is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.topology_id)
    value = (value * 31) ^ hash(self.executors)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LSSupervisorId:
  """
  Attributes:
   - supervisor_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'supervisor_id', None, None, ), # 1
  )

  def __init__(self, supervisor_id=None,):
    self.supervisor_id = supervisor_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.supervisor_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LSSupervisorId')
    if self.supervisor_id is not None:
      oprot.writeFieldBegin('supervisor_id', TType.STRING, 1)
      oprot.writeString(self.supervisor_id.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.supervisor_id is None:
      raise TProtocol.TProtocolException(message='Required field supervisor_id is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.supervisor_id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LSApprovedWorkers:
  """
  Attributes:
   - approved_workers
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'approved_workers', (TType.STRING,None,TType.I32,None), None, ), # 1
  )

  def __init__(self, approved_workers=None,):
    self.approved_workers = approved_workers

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.approved_workers = {}
          (_ktype414, _vtype415, _size413 ) = iprot.readMapBegin()
          for _i417 in xrange(_size413):
            _key418 = iprot.readString().decode('utf-8')
            _val419 = iprot.readI32();
            self.approved_workers[_key418] = _val419
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LSApprovedWorkers')
    if self.approved_workers is not None:
      oprot.writeFieldBegin('approved_workers', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.I32, len(self.approved_workers))
      for kiter420,viter421 in self.approved_workers.items():
        oprot.writeString(kiter420.encode('utf-8'))
        oprot.writeI32(viter421)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.approved_workers is None:
      raise TProtocol.TProtocolException(message='Required field approved_workers is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.approved_workers)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LSSupervisorAssignments:
  """
  Attributes:
   - assignments
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'assignments', (TType.I32,None,TType.STRUCT,(LocalAssignment, LocalAssignment.thrift_spec)), None, ), # 1
  )

  def __init__(self, assignments=None,):
    self.assignments = assignments

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.assignments = {}
          (_ktype423, _vtype424, _size422 ) = iprot.readMapBegin()
          for _i426 in xrange(_size422):
            _key427 = iprot.readI32();
            _val428 = LocalAssignment()
            _val428.read(iprot)
            self.assignments[_key427] = _val428
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LSSupervisorAssignments')
    if self.assignments is not None:
      oprot.writeFieldBegin('assignments', TType.MAP, 1)
      oprot.writeMapBegin(TType.I32, TType.STRUCT, len(self.assignments))
      for kiter429,viter430 in self.assignments.items():
        oprot.writeI32(kiter429)
        viter430.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.assignments is None:
      raise TProtocol.TProtocolException(message='Required field assignments is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.assignments)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LSWorkerHeartbeat:
  """
  Attributes:
   - time_secs
   - topology_id
   - executors
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'time_secs', None, None, ), # 1
    (2, TType.STRING, 'topology_id', None, None, ), # 2
    (3, TType.LIST, 'executors', (TType.STRUCT,(ExecutorInfo, ExecutorInfo.thrift_spec)), None, ), # 3
    (4, TType.I32, 'port', None, None, ), # 4
  )

  def __init__(self, time_secs=None, topology_id=None, executors=None, port=None,):
    self.time_secs = time_secs
    self.topology_id = topology_id
    self.executors = executors
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.time_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.topology_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.executors = []
          (_etype434, _size431) = iprot.readListBegin()
          for _i435 in xrange(_size431):
            _elem436 = ExecutorInfo()
            _elem436.read(iprot)
            self.executors.append(_elem436)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LSWorkerHeartbeat')
    if self.time_secs is not None:
      oprot.writeFieldBegin('time_secs', TType.I32, 1)
      oprot.writeI32(self.time_secs)
      oprot.writeFieldEnd()
    if self.topology_id is not None:
      oprot.writeFieldBegin('topology_id', TType.STRING, 2)
      oprot.writeString(self.topology_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.executors is not None:
      oprot.writeFieldBegin('executors', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.executors))
      for iter437 in self.executors:
        iter437.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 4)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.time_secs is None:
      raise TProtocol.TProtocolException(message='Required field time_secs is unset!')
    if self.topology_id is None:
      raise TProtocol.TProtocolException(message='Required field topology_id is unset!')
    if self.executors is None:
      raise TProtocol.TProtocolException(message='Required field executors is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.time_secs)
    value = (value * 31) ^ hash(self.topology_id)
    value = (value * 31) ^ hash(self.executors)
    value = (value * 31) ^ hash(self.port)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GetInfoOptions:
  """
  Attributes:
   - num_err_choice
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'num_err_choice', None, None, ), # 1
  )

  def __init__(self, num_err_choice=None,):
    self.num_err_choice = num_err_choice

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.num_err_choice = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('GetInfoOptions')
    if self.num_err_choice is not None:
      oprot.writeFieldBegin('num_err_choice', TType.I32, 1)
      oprot.writeI32(self.num_err_choice)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.num_err_choice)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LogLevel:
  """
  Attributes:
   - action
   - target_log_level
   - reset_log_level_timeout_secs
   - reset_log_level_timeout_epoch
   - reset_log_level
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'action', None, None, ), # 1
    (2, TType.STRING, 'target_log_level', None, None, ), # 2
    (3, TType.I32, 'reset_log_level_timeout_secs', None, None, ), # 3
    (4, TType.I64, 'reset_log_level_timeout_epoch', None, None, ), # 4
    (5, TType.STRING, 'reset_log_level', None, None, ), # 5
  )

  def __init__(self, action=None, target_log_level=None, reset_log_level_timeout_secs=None, reset_log_level_timeout_epoch=None, reset_log_level=None,):
    self.action = action
    self.target_log_level = target_log_level
    self.reset_log_level_timeout_secs = reset_log_level_timeout_secs
    self.reset_log_level_timeout_epoch = reset_log_level_timeout_epoch
    self.reset_log_level = reset_log_level

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.action = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.target_log_level = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.reset_log_level_timeout_secs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.reset_log_level_timeout_epoch = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.reset_log_level = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LogLevel')
    if self.action is not None:
      oprot.writeFieldBegin('action', TType.I32, 1)
      oprot.writeI32(self.action)
      oprot.writeFieldEnd()
    if self.target_log_level is not None:
      oprot.writeFieldBegin('target_log_level', TType.STRING, 2)
      oprot.writeString(self.target_log_level.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.reset_log_level_timeout_secs is not None:
      oprot.writeFieldBegin('reset_log_level_timeout_secs', TType.I32, 3)
      oprot.writeI32(self.reset_log_level_timeout_secs)
      oprot.writeFieldEnd()
    if self.reset_log_level_timeout_epoch is not None:
      oprot.writeFieldBegin('reset_log_level_timeout_epoch', TType.I64, 4)
      oprot.writeI64(self.reset_log_level_timeout_epoch)
      oprot.writeFieldEnd()
    if self.reset_log_level is not None:
      oprot.writeFieldBegin('reset_log_level', TType.STRING, 5)
      oprot.writeString(self.reset_log_level.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.action is None:
      raise TProtocol.TProtocolException(message='Required field action is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.action)
    value = (value * 31) ^ hash(self.target_log_level)
    value = (value * 31) ^ hash(self.reset_log_level_timeout_secs)
    value = (value * 31) ^ hash(self.reset_log_level_timeout_epoch)
    value = (value * 31) ^ hash(self.reset_log_level)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LogConfig:
  """
  Attributes:
   - named_logger_level
  """

  thrift_spec = (
    None, # 0
    None, # 1
    (2, TType.MAP, 'named_logger_level', (TType.STRING,None,TType.STRUCT,(LogLevel, LogLevel.thrift_spec)), None, ), # 2
  )

  def __init__(self, named_logger_level=None,):
    self.named_logger_level = named_logger_level

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 2:
        if ftype == TType.MAP:
          self.named_logger_level = {}
          (_ktype457, _vtype458, _size456 ) = iprot.readMapBegin()
          for _i460 in xrange(_size456):
            _key461 = iprot.readString().decode('utf-8')
            _val462 = LogLevel()
            _val462.read(iprot)
            self.named_logger_level[_key461] = _val462
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LogConfig')
    if self.named_logger_level is not None:
      oprot.writeFieldBegin('named_logger_level', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.named_logger_level))
      for kiter463,viter464 in self.named_logger_level.items():
        oprot.writeString(kiter463.encode('utf-8'))
        viter464.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.named_logger_level)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class DRPCRequest:
  """
  Attributes:
   - func_args
   - request_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'func_args', None, None, ), # 1
    (2, TType.STRING, 'request_id', None, None, ), # 2
  )

  def __init__(self, func_args=None, request_id=None,):
    self.func_args = func_args
    self.request_id = request_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.func_args = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.request_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DRPCRequest')
    if self.func_args is not None:
      oprot.writeFieldBegin('func_args', TType.STRING, 1)
      oprot.writeString(self.func_args.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.request_id is not None:
      oprot.writeFieldBegin('request_id', TType.STRING, 2)
      oprot.writeString(self.request_id.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.func_args is None:
      raise TProtocol.TProtocolException(message='Required field func_args is unset!')
    if self.request_id is None:
      raise TProtocol.TProtocolException(message='Required field request_id is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.func_args)
    value = (value * 31) ^ hash(self.request_id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class DRPCExecutionException(TException):
  """
  Attributes:
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
  )

  def __init__(self, msg=None,):
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DRPCExecutionException')
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.msg is None:
      raise TProtocol.TProtocolException(message='Required field msg is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
