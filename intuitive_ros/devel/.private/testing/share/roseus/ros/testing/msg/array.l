;; Auto-generated. Do not edit!


(when (boundp 'testing::array)
  (if (not (find-package "TESTING"))
    (make-package "TESTING"))
  (shadow 'array (find-package "TESTING")))
(unless (find-package "TESTING::ARRAY")
  (make-package "TESTING::ARRAY"))

(in-package "ROS")
;;//! \htmlinclude array.msg.html


(defclass testing::array
  :super ros::object
  :slots (_int_array ))

(defmethod testing::array
  (:init
   (&key
    ((:int_array __int_array) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _int_array __int_array)
   self)
  (:int_array
   (&optional __int_array)
   (if __int_array (setq _int_array __int_array)) _int_array)
  (:serialization-length
   ()
   (+
    ;; int32[] _int_array
    (* 4    (length _int_array)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _int_array
     (write-long (length _int_array) s)
     (dotimes (i (length _int_array))
       (write-long (elt _int_array i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _int_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _int_array (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _int_array i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get testing::array :md5sum-) "026155ab21538c65a83bb475fd218b8c")
(setf (get testing::array :datatype-) "testing/array")
(setf (get testing::array :definition-)
      "int32[] int_array
")



(provide :testing/array "026155ab21538c65a83bb475fd218b8c")


