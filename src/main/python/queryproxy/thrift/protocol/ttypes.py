#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class QueryType:
  SOLR = 1
  SQL = 2

  _VALUES_TO_NAMES = {
    1: "SOLR",
    2: "SQL",
  }

  _NAMES_TO_VALUES = {
    "SOLR": 1,
    "SQL": 2,
  }


class QueryParams:
  """
  Attributes:
   - type
   - table
   - paramList
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'table', None, None, ), # 2
    (3, TType.LIST, 'paramList', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, type=None, table=None, paramList=None,):
    self.type = type
    self.table = table
    self.paramList = paramList

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
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.table = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.paramList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.paramList.append(_elem5)
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
    oprot.writeStructBegin('QueryParams')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.table is not None:
      oprot.writeFieldBegin('table', TType.STRING, 2)
      oprot.writeString(self.table)
      oprot.writeFieldEnd()
    if self.paramList is not None:
      oprot.writeFieldBegin('paramList', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.paramList))
      for iter6 in self.paramList:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryResult:
  """
  Attributes:
   - offset
   - length
   - results
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'offset', None, None, ), # 1
    (2, TType.I32, 'length', None, None, ), # 2
    (3, TType.LIST, 'results', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, offset=None, length=None, results=None,):
    self.offset = offset
    self.length = length
    self.results = results

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
          self.offset = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.length = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.results = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString();
            self.results.append(_elem12)
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
    oprot.writeStructBegin('QueryResult')
    if self.offset is not None:
      oprot.writeFieldBegin('offset', TType.I32, 1)
      oprot.writeI32(self.offset)
      oprot.writeFieldEnd()
    if self.length is not None:
      oprot.writeFieldBegin('length', TType.I32, 2)
      oprot.writeI32(self.length)
      oprot.writeFieldEnd()
    if self.results is not None:
      oprot.writeFieldBegin('results', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.results))
      for iter13 in self.results:
        oprot.writeString(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryFailureException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

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
          self.message = iprot.readString();
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
    oprot.writeStructBegin('QueryFailureException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
