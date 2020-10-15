// Auto-generated. Do not edit!

// (in-package testing.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class array {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.int_array = null;
    }
    else {
      if (initObj.hasOwnProperty('int_array')) {
        this.int_array = initObj.int_array
      }
      else {
        this.int_array = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type array
    // Serialize message field [int_array]
    bufferOffset = _arraySerializer.int32(obj.int_array, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type array
    let len;
    let data = new array(null);
    // Deserialize message field [int_array]
    data.int_array = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.int_array.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'testing/array';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '026155ab21538c65a83bb475fd218b8c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] int_array
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new array(null);
    if (msg.int_array !== undefined) {
      resolved.int_array = msg.int_array;
    }
    else {
      resolved.int_array = []
    }

    return resolved;
    }
};

module.exports = array;
