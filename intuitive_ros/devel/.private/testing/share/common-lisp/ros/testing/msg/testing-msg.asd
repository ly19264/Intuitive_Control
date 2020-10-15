
(cl:in-package :asdf)

(defsystem "testing-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "array" :depends-on ("_package_array"))
    (:file "_package_array" :depends-on ("_package"))
  ))