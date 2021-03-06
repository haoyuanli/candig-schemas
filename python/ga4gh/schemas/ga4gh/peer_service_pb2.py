# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/peer_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.ga4gh import common_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2
from ga4gh.schemas.google.api import annotations_pb2 as ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/peer_service.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n&ga4gh/schemas/ga4gh/peer_service.proto\x12\x13ga4gh.schemas.ga4gh\x1a ga4gh/schemas/ga4gh/common.proto\x1a*ga4gh/schemas/google/api/annotations.proto\"9\n\x10ListPeersRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"V\n\x11ListPeersResponse\x12(\n\x05peers\x18\x01 \x03(\x0b\x32\x19.ga4gh.schemas.ga4gh.Peer\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\">\n\x13\x41nnouncePeerRequest\x12\'\n\x04peer\x18\x01 \x01(\x0b\x32\x19.ga4gh.schemas.ga4gh.Peer\"\\\n\x14\x41nnouncePeerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x33\n\nattributes\x18\x02 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"\x10\n\x0eGetInfoRequest\"`\n\x0fGetInfoResponse\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x33\n\nattributes\x18\x02 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"H\n\x04Peer\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x33\n\nattributes\x18\x02 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes2\xfa\x02\n\x0bPeerService\x12|\n\tListPeers\x12%.ga4gh.schemas.ga4gh.ListPeersRequest\x1a&.ga4gh.schemas.ga4gh.ListPeersResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v0.6.0a10/peers/list:\x01*\x12\x80\x01\n\x0c\x41nnouncePeer\x12(.ga4gh.schemas.ga4gh.AnnouncePeerRequest\x1a).ga4gh.schemas.ga4gh.AnnouncePeerResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/v0.6.0a10/announce\x12j\n\x04Info\x12#.ga4gh.schemas.ga4gh.GetInfoRequest\x1a$.ga4gh.schemas.ga4gh.GetInfoResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v0.6.0a10/infob\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LISTPEERSREQUEST = _descriptor.Descriptor(
  name='ListPeersRequest',
  full_name='ga4gh.schemas.ga4gh.ListPeersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.ListPeersRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.ListPeersRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=198,
)


_LISTPEERSRESPONSE = _descriptor.Descriptor(
  name='ListPeersResponse',
  full_name='ga4gh.schemas.ga4gh.ListPeersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='ga4gh.schemas.ga4gh.ListPeersResponse.peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.ListPeersResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=286,
)


_ANNOUNCEPEERREQUEST = _descriptor.Descriptor(
  name='AnnouncePeerRequest',
  full_name='ga4gh.schemas.ga4gh.AnnouncePeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='ga4gh.schemas.ga4gh.AnnouncePeerRequest.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=350,
)


_ANNOUNCEPEERRESPONSE = _descriptor.Descriptor(
  name='AnnouncePeerResponse',
  full_name='ga4gh.schemas.ga4gh.AnnouncePeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ga4gh.schemas.ga4gh.AnnouncePeerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.AnnouncePeerResponse.attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=444,
)


_GETINFOREQUEST = _descriptor.Descriptor(
  name='GetInfoRequest',
  full_name='ga4gh.schemas.ga4gh.GetInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=462,
)


_GETINFORESPONSE = _descriptor.Descriptor(
  name='GetInfoResponse',
  full_name='ga4gh.schemas.ga4gh.GetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='ga4gh.schemas.ga4gh.GetInfoResponse.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.GetInfoResponse.attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=560,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='ga4gh.schemas.ga4gh.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='ga4gh.schemas.ga4gh.Peer.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.Peer.attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=634,
)

_LISTPEERSRESPONSE.fields_by_name['peers'].message_type = _PEER
_ANNOUNCEPEERREQUEST.fields_by_name['peer'].message_type = _PEER
_ANNOUNCEPEERRESPONSE.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_GETINFORESPONSE.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_PEER.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
DESCRIPTOR.message_types_by_name['ListPeersRequest'] = _LISTPEERSREQUEST
DESCRIPTOR.message_types_by_name['ListPeersResponse'] = _LISTPEERSRESPONSE
DESCRIPTOR.message_types_by_name['AnnouncePeerRequest'] = _ANNOUNCEPEERREQUEST
DESCRIPTOR.message_types_by_name['AnnouncePeerResponse'] = _ANNOUNCEPEERRESPONSE
DESCRIPTOR.message_types_by_name['GetInfoRequest'] = _GETINFOREQUEST
DESCRIPTOR.message_types_by_name['GetInfoResponse'] = _GETINFORESPONSE
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPeersRequest = _reflection.GeneratedProtocolMessageType('ListPeersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPEERSREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ListPeersRequest)
  ))
_sym_db.RegisterMessage(ListPeersRequest)

ListPeersResponse = _reflection.GeneratedProtocolMessageType('ListPeersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPEERSRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ListPeersResponse)
  ))
_sym_db.RegisterMessage(ListPeersResponse)

AnnouncePeerRequest = _reflection.GeneratedProtocolMessageType('AnnouncePeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANNOUNCEPEERREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.AnnouncePeerRequest)
  ))
_sym_db.RegisterMessage(AnnouncePeerRequest)

AnnouncePeerResponse = _reflection.GeneratedProtocolMessageType('AnnouncePeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _ANNOUNCEPEERRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.AnnouncePeerResponse)
  ))
_sym_db.RegisterMessage(AnnouncePeerResponse)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINFOREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetInfoRequest)
  ))
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINFORESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetInfoResponse)
  ))
_sym_db.RegisterMessage(GetInfoResponse)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), dict(
  DESCRIPTOR = _PEER,
  __module__ = 'ga4gh.schemas.ga4gh.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Peer)
  ))
_sym_db.RegisterMessage(Peer)


# @@protoc_insertion_point(module_scope)
