# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from franka_control/SetForceTorqueCollisionBehaviorRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetForceTorqueCollisionBehaviorRequest(genpy.Message):
  _md5sum = "af37de8897f6124b6b82b8dad5d5a876"
  _type = "franka_control/SetForceTorqueCollisionBehaviorRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64[7] lower_torque_thresholds_nominal
float64[7] upper_torque_thresholds_nominal
float64[6] lower_force_thresholds_nominal
float64[6] upper_force_thresholds_nominal
"""
  __slots__ = ['lower_torque_thresholds_nominal','upper_torque_thresholds_nominal','lower_force_thresholds_nominal','upper_force_thresholds_nominal']
  _slot_types = ['float64[7]','float64[7]','float64[6]','float64[6]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lower_torque_thresholds_nominal,upper_torque_thresholds_nominal,lower_force_thresholds_nominal,upper_force_thresholds_nominal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetForceTorqueCollisionBehaviorRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.lower_torque_thresholds_nominal is None:
        self.lower_torque_thresholds_nominal = [0.] * 7
      if self.upper_torque_thresholds_nominal is None:
        self.upper_torque_thresholds_nominal = [0.] * 7
      if self.lower_force_thresholds_nominal is None:
        self.lower_force_thresholds_nominal = [0.] * 6
      if self.upper_force_thresholds_nominal is None:
        self.upper_force_thresholds_nominal = [0.] * 6
    else:
      self.lower_torque_thresholds_nominal = [0.] * 7
      self.upper_torque_thresholds_nominal = [0.] * 7
      self.lower_force_thresholds_nominal = [0.] * 6
      self.upper_force_thresholds_nominal = [0.] * 6

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_7d().pack(*self.lower_torque_thresholds_nominal))
      buff.write(_get_struct_7d().pack(*self.upper_torque_thresholds_nominal))
      buff.write(_get_struct_6d().pack(*self.lower_force_thresholds_nominal))
      buff.write(_get_struct_6d().pack(*self.upper_force_thresholds_nominal))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 56
      self.lower_torque_thresholds_nominal = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 56
      self.upper_torque_thresholds_nominal = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 48
      self.lower_force_thresholds_nominal = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 48
      self.upper_force_thresholds_nominal = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(self.lower_torque_thresholds_nominal.tostring())
      buff.write(self.upper_torque_thresholds_nominal.tostring())
      buff.write(self.lower_force_thresholds_nominal.tostring())
      buff.write(self.upper_force_thresholds_nominal.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 56
      self.lower_torque_thresholds_nominal = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=7)
      start = end
      end += 56
      self.upper_torque_thresholds_nominal = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=7)
      start = end
      end += 48
      self.lower_force_thresholds_nominal = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=6)
      start = end
      end += 48
      self.upper_force_thresholds_nominal = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=6)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from franka_control/SetForceTorqueCollisionBehaviorResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetForceTorqueCollisionBehaviorResponse(genpy.Message):
  _md5sum = "45872d25d65c97743cc71afc6d4e884d"
  _type = "franka_control/SetForceTorqueCollisionBehaviorResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool success
string error


"""
  __slots__ = ['success','error']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,error

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetForceTorqueCollisionBehaviorResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.error is None:
        self.error = ''
    else:
      self.success = False
      self.error = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.success
      buff.write(_get_struct_B().pack(_x))
      _x = self.error
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.error = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.error = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.success
      buff.write(_get_struct_B().pack(_x))
      _x = self.error
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.error = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.error = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SetForceTorqueCollisionBehavior(object):
  _type          = 'franka_control/SetForceTorqueCollisionBehavior'
  _md5sum = 'b1e592d1b6960bc05e6e3cba1eb02349'
  _request_class  = SetForceTorqueCollisionBehaviorRequest
  _response_class = SetForceTorqueCollisionBehaviorResponse
