# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import livetex.options.ttypes
import livetex.token.ttypes
import livetex.livetex_service.ttypes
import livetex.environment.ttypes
import livetex.endpoint.ttypes
import livetex.account.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class CheckTokenResult:
  """
  Ответ проверки токена.


  result: результат проверки токена на валидность.

  options: список опций доступных для клиента.

  Attributes:
   - result
   - services
   - serviceOptions
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'result', None, None, ), # 1
    (2, TType.MAP, 'services', (TType.I32,None,TType.STRUCT,(livetex.endpoint.ttypes.Endpoint, livetex.endpoint.ttypes.Endpoint.thrift_spec)), None, ), # 2
    (3, TType.STRUCT, 'serviceOptions', (livetex.livetex_service.ttypes.ServiceOptions, livetex.livetex_service.ttypes.ServiceOptions.thrift_spec), None, ), # 3
  )

  def __init__(self, result=None, services=None, serviceOptions=None,):
    self.result = result
    self.services = services
    self.serviceOptions = serviceOptions

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
        if ftype == TType.BOOL:
          self.result = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.services = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readI32();
            _val6 = livetex.endpoint.ttypes.Endpoint()
            _val6.read(iprot)
            self.services[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.serviceOptions = livetex.livetex_service.ttypes.ServiceOptions()
          self.serviceOptions.read(iprot)
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
    oprot.writeStructBegin('CheckTokenResult')
    if self.result is not None:
      oprot.writeFieldBegin('result', TType.BOOL, 1)
      oprot.writeBool(self.result)
      oprot.writeFieldEnd()
    if self.services is not None:
      oprot.writeFieldBegin('services', TType.MAP, 2)
      oprot.writeMapBegin(TType.I32, TType.STRUCT, len(self.services))
      for kiter7,viter8 in self.services.items():
        oprot.writeI32(kiter7)
        viter8.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.serviceOptions is not None:
      oprot.writeFieldBegin('serviceOptions', TType.STRUCT, 3)
      self.serviceOptions.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.result is None:
      raise TProtocol.TProtocolException(message='Required field result is unset!')
    if self.services is None:
      raise TProtocol.TProtocolException(message='Required field services is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
