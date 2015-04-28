# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groupexp.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='groupexp.proto',
  package='',
  serialized_pb='\n\x0egroupexp.proto\"N\n\x0b\x46olderParam\x12\x12\n\nfoldername\x18\x01 \x02(\t\x12\x12\n\noutput_loc\x18\x02 \x02(\t\x12\x17\n\x0f\x64\x65ploy_net_name\x18\x03 \x02(\t\"f\n\tFileParam\x12\x10\n\x08\x66ile_loc\x18\x01 \x03(\t\x12\x12\n\noutput_loc\x18\x02 \x02(\t\x12\x1a\n\x0bis_modified\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x0f\x64\x65ploy_net_name\x18\x04 \x02(\t\"\x1f\n\x05Param\x12\x16\n\x03net\x18\x01 \x03(\x0b\x32\t.NetParam\"\xba\x01\n\x08NetParam\x12\x12\n\ncaffe_root\x18\x08 \x02(\t\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x11\n\tprotopath\x18\x02 \x02(\t\x12\x11\n\tmodelpath\x18\x03 \x02(\t\x12\x17\n\x08has_mean\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x08meanpath\x18\x05 \x01(\t\x12\x14\n\x0c\x63hannel_swap\x18\x06 \x01(\x08\x12\x11\n\traw_scale\x18\x07 \x01(\r\x12\x12\n\x03gpu\x18\t \x01(\x08:\x05\x66\x61lse')




_FOLDERPARAM = _descriptor.Descriptor(
  name='FolderParam',
  full_name='FolderParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foldername', full_name='FolderParam.foldername', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_loc', full_name='FolderParam.output_loc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deploy_net_name', full_name='FolderParam.deploy_net_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=18,
  serialized_end=96,
)


_FILEPARAM = _descriptor.Descriptor(
  name='FileParam',
  full_name='FileParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_loc', full_name='FileParam.file_loc', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_loc', full_name='FileParam.output_loc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_modified', full_name='FileParam.is_modified', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deploy_net_name', full_name='FileParam.deploy_net_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=98,
  serialized_end=200,
)


_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='net', full_name='Param.net', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=202,
  serialized_end=233,
)


_NETPARAM = _descriptor.Descriptor(
  name='NetParam',
  full_name='NetParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='caffe_root', full_name='NetParam.caffe_root', index=0,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='NetParam.name', index=1,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protopath', full_name='NetParam.protopath', index=2,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modelpath', full_name='NetParam.modelpath', index=3,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_mean', full_name='NetParam.has_mean', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meanpath', full_name='NetParam.meanpath', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_swap', full_name='NetParam.channel_swap', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_scale', full_name='NetParam.raw_scale', index=7,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu', full_name='NetParam.gpu', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=236,
  serialized_end=422,
)

_PARAM.fields_by_name['net'].message_type = _NETPARAM
DESCRIPTOR.message_types_by_name['FolderParam'] = _FOLDERPARAM
DESCRIPTOR.message_types_by_name['FileParam'] = _FILEPARAM
DESCRIPTOR.message_types_by_name['Param'] = _PARAM
DESCRIPTOR.message_types_by_name['NetParam'] = _NETPARAM

class FolderParam(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOLDERPARAM

  # @@protoc_insertion_point(class_scope:FolderParam)

class FileParam(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEPARAM

  # @@protoc_insertion_point(class_scope:FileParam)

class Param(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARAM

  # @@protoc_insertion_point(class_scope:Param)

class NetParam(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NETPARAM

  # @@protoc_insertion_point(class_scope:NetParam)


# @@protoc_insertion_point(module_scope)
