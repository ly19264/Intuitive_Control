; Auto-generated. Do not edit!


(cl:in-package testing-msg)


;//! \htmlinclude array.msg.html

(cl:defclass <array> (roslisp-msg-protocol:ros-message)
  ((int_array
    :reader int_array
    :initarg :int_array
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass array (<array>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <array>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'array)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name testing-msg:<array> is deprecated: use testing-msg:array instead.")))

(cl:ensure-generic-function 'int_array-val :lambda-list '(m))
(cl:defmethod int_array-val ((m <array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader testing-msg:int_array-val is deprecated.  Use testing-msg:int_array instead.")
  (int_array m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <array>) ostream)
  "Serializes a message object of type '<array>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'int_array))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'int_array))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <array>) istream)
  "Deserializes a message object of type '<array>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'int_array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'int_array)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<array>)))
  "Returns string type for a message object of type '<array>"
  "testing/array")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'array)))
  "Returns string type for a message object of type 'array"
  "testing/array")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<array>)))
  "Returns md5sum for a message object of type '<array>"
  "026155ab21538c65a83bb475fd218b8c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'array)))
  "Returns md5sum for a message object of type 'array"
  "026155ab21538c65a83bb475fd218b8c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<array>)))
  "Returns full string definition for message of type '<array>"
  (cl:format cl:nil "int32[] int_array~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'array)))
  "Returns full string definition for message of type 'array"
  (cl:format cl:nil "int32[] int_array~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <array>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'int_array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <array>))
  "Converts a ROS message object to a list"
  (cl:list 'array
    (cl:cons ':int_array (int_array msg))
))
