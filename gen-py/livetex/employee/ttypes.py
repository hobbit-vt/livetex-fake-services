# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import livetex.url.ttypes
import livetex.options.ttypes
import livetex.status.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Employee:
  """
  Оператор.


  id: уникальный идентификатор оператора.

  status: актуальный статус оператора.

  firstname: имя оператора.

  lastname: фамилия оператора.

  avatar: URL аватара оператора.

  phone: телефон оператора.

  email: email оператора.

  options: опциональные аттрибуты оператора.

  Attributes:
   - EmployeeId
   - status
   - firstname
   - lastname
   - avatar
   - phone
   - email
   - options
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'EmployeeId', None, None, ), # 1
    (2, TType.STRING, 'status', None, None, ), # 2
    (3, TType.STRING, 'firstname', None, None, ), # 3
    (4, TType.STRING, 'lastname', None, None, ), # 4
    (5, TType.STRING, 'avatar', None, None, ), # 5
    (6, TType.STRING, 'phone', None, None, ), # 6
    (7, TType.STRING, 'email', None, None, ), # 7
    (8, TType.MAP, 'options', (TType.STRING,None,TType.STRING,None), None, ), # 8
  )

  def __init__(self, EmployeeId=None, status=None, firstname=None, lastname=None, avatar=None, phone=None, email=None, options=None,):
    self.EmployeeId = EmployeeId
    self.status = status
    self.firstname = firstname
    self.lastname = lastname
    self.avatar = avatar
    self.phone = phone
    self.email = email
    self.options = options

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
          self.EmployeeId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.status = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.firstname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.lastname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.avatar = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.phone = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.email = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.MAP:
          self.options = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString();
            _val6 = iprot.readString();
            self.options[_key5] = _val6
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
    oprot.writeStructBegin('Employee')
    if self.EmployeeId is not None:
      oprot.writeFieldBegin('EmployeeId', TType.STRING, 1)
      oprot.writeString(self.EmployeeId)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRING, 2)
      oprot.writeString(self.status)
      oprot.writeFieldEnd()
    if self.firstname is not None:
      oprot.writeFieldBegin('firstname', TType.STRING, 3)
      oprot.writeString(self.firstname)
      oprot.writeFieldEnd()
    if self.lastname is not None:
      oprot.writeFieldBegin('lastname', TType.STRING, 4)
      oprot.writeString(self.lastname)
      oprot.writeFieldEnd()
    if self.avatar is not None:
      oprot.writeFieldBegin('avatar', TType.STRING, 5)
      oprot.writeString(self.avatar)
      oprot.writeFieldEnd()
    if self.phone is not None:
      oprot.writeFieldBegin('phone', TType.STRING, 6)
      oprot.writeString(self.phone)
      oprot.writeFieldEnd()
    if self.email is not None:
      oprot.writeFieldBegin('email', TType.STRING, 7)
      oprot.writeString(self.email)
      oprot.writeFieldEnd()
    if self.options is not None:
      oprot.writeFieldBegin('options', TType.MAP, 8)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.options))
      for kiter7,viter8 in self.options.items():
        oprot.writeString(kiter7)
        oprot.writeString(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.EmployeeId is None:
      raise TProtocol.TProtocolException(message='Required field EmployeeId is unset!')
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    if self.firstname is None:
      raise TProtocol.TProtocolException(message='Required field firstname is unset!')
    if self.lastname is None:
      raise TProtocol.TProtocolException(message='Required field lastname is unset!')
    if self.avatar is None:
      raise TProtocol.TProtocolException(message='Required field avatar is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
