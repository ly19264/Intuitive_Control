// Generated by gencpp from file testing/array.msg
// DO NOT EDIT!


#ifndef TESTING_MESSAGE_ARRAY_H
#define TESTING_MESSAGE_ARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace testing
{
template <class ContainerAllocator>
struct array_
{
  typedef array_<ContainerAllocator> Type;

  array_()
    : int_array()  {
    }
  array_(const ContainerAllocator& _alloc)
    : int_array(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _int_array_type;
  _int_array_type int_array;





  typedef boost::shared_ptr< ::testing::array_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::testing::array_<ContainerAllocator> const> ConstPtr;

}; // struct array_

typedef ::testing::array_<std::allocator<void> > array;

typedef boost::shared_ptr< ::testing::array > arrayPtr;
typedef boost::shared_ptr< ::testing::array const> arrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::testing::array_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::testing::array_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::testing::array_<ContainerAllocator1> & lhs, const ::testing::array_<ContainerAllocator2> & rhs)
{
  return lhs.int_array == rhs.int_array;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::testing::array_<ContainerAllocator1> & lhs, const ::testing::array_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace testing

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::testing::array_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::testing::array_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::testing::array_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::testing::array_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::testing::array_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::testing::array_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::testing::array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "026155ab21538c65a83bb475fd218b8c";
  }

  static const char* value(const ::testing::array_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x026155ab21538c65ULL;
  static const uint64_t static_value2 = 0xa83bb475fd218b8cULL;
};

template<class ContainerAllocator>
struct DataType< ::testing::array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "testing/array";
  }

  static const char* value(const ::testing::array_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::testing::array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32[] int_array\n"
;
  }

  static const char* value(const ::testing::array_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::testing::array_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.int_array);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct array_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::testing::array_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::testing::array_<ContainerAllocator>& v)
  {
    s << indent << "int_array[]" << std::endl;
    for (size_t i = 0; i < v.int_array.size(); ++i)
    {
      s << indent << "  int_array[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.int_array[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // TESTING_MESSAGE_ARRAY_H
