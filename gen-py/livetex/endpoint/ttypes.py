# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import livetex.livetex_service.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Endpoint:
  """
  Точка входа в сервис.


  serv: сервис.

  host: адрес хоста.

  port: порт.

  protocol: используемый протокол.

  path: путь.

  Attributes:
   - serv
   - host
   - port
   - protocol
   - path
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'serv', None, None, ), # 1
    (2, TType.STRING, 'host', None, None, ), # 2
    (3, TType.I16, 'port', None, None, ), # 3
    (4, TType.STRING, 'protocol', None, None, ), # 4
    (5, TType.STRING, 'path', None, None, ), # 5
  )

  def __init__(self, serv=None, host=None, port=None, protocol=None, path=None,):
    self.serv = serv
    self.host = host
    self.port = port
    self.protocol = protocol
    self.path = path

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
          self.serv = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.host = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.port = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.protocol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.path = iprot.readString();
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
    oprot.writeStructBegin('Endpoint')
    if self.serv is not None:
      oprot.writeFieldBegin('serv', TType.I32, 1)
      oprot.writeI32(self.serv)
      oprot.writeFieldEnd()
    if self.host is not None:
      oprot.writeFieldBegin('host', TType.STRING, 2)
      oprot.writeString(self.host)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I16, 3)
      oprot.writeI16(self.port)
      oprot.writeFieldEnd()
    if self.protocol is not None:
      oprot.writeFieldBegin('protocol', TType.STRING, 4)
      oprot.writeString(self.protocol)
      oprot.writeFieldEnd()
    if self.path is not None:
      oprot.writeFieldBegin('path', TType.STRING, 5)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serv is None:
      raise TProtocol.TProtocolException(message='Required field serv is unset!')
    if self.host is None:
      raise TProtocol.TProtocolException(message='Required field host is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
