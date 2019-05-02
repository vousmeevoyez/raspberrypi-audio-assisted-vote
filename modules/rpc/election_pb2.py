# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: election.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rpc.candidate_pb2 as candidate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='election.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x65lection.proto\x1a\x0f\x63\x61ndidate.proto\"\x95\x01\n\x0c\x45lectionInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06images\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x12\n\ncreated_at\x18\x06 \x01(\t\x12\"\n\ncandidates\x18\x07 \x03(\x0b\x32\x0e.CandidateInfo\"\xcc\x01\n\x15\x43reateElectionRequest\x12-\n\x06header\x18\x01 \x01(\x0b\x32\x1d.CreateElectionRequest.Header\x12)\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x1b.CreateElectionRequest.Body\x1a\x1e\n\x06Header\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x1a\x39\n\x04\x42ody\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06images\x18\x03 \x01(\x0c\"a\n\x16\x43reateElectionResponse\x12*\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x1c.CreateElectionResponse.Body\x1a\x1b\n\x04\x42ody\x12\x13\n\x0b\x65lection_id\x18\x01 \x01(\t\"u\n\x12GetElectionRequest\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.GetElectionRequest.Header\x1a\x33\n\x06Header\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x13\n\x0b\x65lection_id\x18\x02 \x01(\t\"2\n\x13GetElectionResponse\x12\x1b\n\x04\x62ody\x18\x01 \x01(\x0b\x32\r.ElectionInfo\"\xe1\x01\n\x15UpdateElectionRequest\x12-\n\x06header\x18\x01 \x01(\x0b\x32\x1d.UpdateElectionRequest.Header\x12)\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x1b.UpdateElectionRequest.Body\x1a\x33\n\x06Header\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x13\n\x0b\x65lection_id\x18\x02 \x01(\t\x1a\x39\n\x04\x42ody\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06images\x18\x03 \x01(\x0c\"(\n\x16UpdateElectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"{\n\x15RemoveElectionRequest\x12-\n\x06header\x18\x01 \x01(\x0b\x32\x1d.RemoveElectionRequest.Header\x1a\x33\n\x06Header\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x13\n\x0b\x65lection_id\x18\x02 \x01(\t\"(\n\x16RemoveElectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"b\n\x13GetElectionsRequest\x12+\n\x06header\x18\x01 \x01(\x0b\x32\x1b.GetElectionsRequest.Header\x1a\x1e\n\x06Header\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"3\n\x14GetElectionsResponse\x12\x1b\n\x04\x62ody\x18\x01 \x03(\x0b\x32\r.ElectionInfo2\xd4\x02\n\x08\x45lection\x12\x43\n\x0e\x43reateElection\x12\x16.CreateElectionRequest\x1a\x17.CreateElectionResponse\"\x00\x12:\n\x0bGetElection\x12\x13.GetElectionRequest\x1a\x14.GetElectionResponse\"\x00\x12\x43\n\x0eUpdateElection\x12\x16.UpdateElectionRequest\x1a\x17.UpdateElectionResponse\"\x00\x12\x43\n\x0eRemoveElection\x12\x16.RemoveElectionRequest\x1a\x17.RemoveElectionResponse\"\x00\x12=\n\x0cGetElections\x12\x14.GetElectionsRequest\x1a\x15.GetElectionsResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[candidate__pb2.DESCRIPTOR,])




_ELECTIONINFO = _descriptor.Descriptor(
  name='ElectionInfo',
  full_name='ElectionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ElectionInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ElectionInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ElectionInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='ElectionInfo.images', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ElectionInfo.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='ElectionInfo.created_at', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candidates', full_name='ElectionInfo.candidates', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=185,
)


_CREATEELECTIONREQUEST_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='CreateElectionRequest.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='CreateElectionRequest.Header.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=333,
)

_CREATEELECTIONREQUEST_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='CreateElectionRequest.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateElectionRequest.Body.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='CreateElectionRequest.Body.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='CreateElectionRequest.Body.images', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=392,
)

_CREATEELECTIONREQUEST = _descriptor.Descriptor(
  name='CreateElectionRequest',
  full_name='CreateElectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CreateElectionRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='CreateElectionRequest.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEELECTIONREQUEST_HEADER, _CREATEELECTIONREQUEST_BODY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=392,
)


_CREATEELECTIONRESPONSE_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='CreateElectionResponse.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='election_id', full_name='CreateElectionResponse.Body.election_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=491,
)

_CREATEELECTIONRESPONSE = _descriptor.Descriptor(
  name='CreateElectionResponse',
  full_name='CreateElectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='CreateElectionResponse.body', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEELECTIONRESPONSE_BODY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=491,
)


_GETELECTIONREQUEST_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='GetElectionRequest.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='GetElectionRequest.Header.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='election_id', full_name='GetElectionRequest.Header.election_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=610,
)

_GETELECTIONREQUEST = _descriptor.Descriptor(
  name='GetElectionRequest',
  full_name='GetElectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='GetElectionRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETELECTIONREQUEST_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=610,
)


_GETELECTIONRESPONSE = _descriptor.Descriptor(
  name='GetElectionResponse',
  full_name='GetElectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='GetElectionResponse.body', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=612,
  serialized_end=662,
)


_UPDATEELECTIONREQUEST_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='UpdateElectionRequest.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='UpdateElectionRequest.Header.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='election_id', full_name='UpdateElectionRequest.Header.election_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=610,
)

_UPDATEELECTIONREQUEST_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='UpdateElectionRequest.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UpdateElectionRequest.Body.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='UpdateElectionRequest.Body.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='UpdateElectionRequest.Body.images', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=392,
)

_UPDATEELECTIONREQUEST = _descriptor.Descriptor(
  name='UpdateElectionRequest',
  full_name='UpdateElectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='UpdateElectionRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='UpdateElectionRequest.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEELECTIONREQUEST_HEADER, _UPDATEELECTIONREQUEST_BODY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=890,
)


_UPDATEELECTIONRESPONSE = _descriptor.Descriptor(
  name='UpdateElectionResponse',
  full_name='UpdateElectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='UpdateElectionResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=932,
)


_REMOVEELECTIONREQUEST_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='RemoveElectionRequest.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='RemoveElectionRequest.Header.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='election_id', full_name='RemoveElectionRequest.Header.election_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=610,
)

_REMOVEELECTIONREQUEST = _descriptor.Descriptor(
  name='RemoveElectionRequest',
  full_name='RemoveElectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='RemoveElectionRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REMOVEELECTIONREQUEST_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=934,
  serialized_end=1057,
)


_REMOVEELECTIONRESPONSE = _descriptor.Descriptor(
  name='RemoveElectionResponse',
  full_name='RemoveElectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RemoveElectionResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1059,
  serialized_end=1099,
)


_GETELECTIONSREQUEST_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='GetElectionsRequest.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='GetElectionsRequest.Header.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=333,
)

_GETELECTIONSREQUEST = _descriptor.Descriptor(
  name='GetElectionsRequest',
  full_name='GetElectionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='GetElectionsRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETELECTIONSREQUEST_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1101,
  serialized_end=1199,
)


_GETELECTIONSRESPONSE = _descriptor.Descriptor(
  name='GetElectionsResponse',
  full_name='GetElectionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='GetElectionsResponse.body', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1201,
  serialized_end=1252,
)

_ELECTIONINFO.fields_by_name['candidates'].message_type = candidate__pb2._CANDIDATEINFO
_CREATEELECTIONREQUEST_HEADER.containing_type = _CREATEELECTIONREQUEST
_CREATEELECTIONREQUEST_BODY.containing_type = _CREATEELECTIONREQUEST
_CREATEELECTIONREQUEST.fields_by_name['header'].message_type = _CREATEELECTIONREQUEST_HEADER
_CREATEELECTIONREQUEST.fields_by_name['body'].message_type = _CREATEELECTIONREQUEST_BODY
_CREATEELECTIONRESPONSE_BODY.containing_type = _CREATEELECTIONRESPONSE
_CREATEELECTIONRESPONSE.fields_by_name['body'].message_type = _CREATEELECTIONRESPONSE_BODY
_GETELECTIONREQUEST_HEADER.containing_type = _GETELECTIONREQUEST
_GETELECTIONREQUEST.fields_by_name['header'].message_type = _GETELECTIONREQUEST_HEADER
_GETELECTIONRESPONSE.fields_by_name['body'].message_type = _ELECTIONINFO
_UPDATEELECTIONREQUEST_HEADER.containing_type = _UPDATEELECTIONREQUEST
_UPDATEELECTIONREQUEST_BODY.containing_type = _UPDATEELECTIONREQUEST
_UPDATEELECTIONREQUEST.fields_by_name['header'].message_type = _UPDATEELECTIONREQUEST_HEADER
_UPDATEELECTIONREQUEST.fields_by_name['body'].message_type = _UPDATEELECTIONREQUEST_BODY
_REMOVEELECTIONREQUEST_HEADER.containing_type = _REMOVEELECTIONREQUEST
_REMOVEELECTIONREQUEST.fields_by_name['header'].message_type = _REMOVEELECTIONREQUEST_HEADER
_GETELECTIONSREQUEST_HEADER.containing_type = _GETELECTIONSREQUEST
_GETELECTIONSREQUEST.fields_by_name['header'].message_type = _GETELECTIONSREQUEST_HEADER
_GETELECTIONSRESPONSE.fields_by_name['body'].message_type = _ELECTIONINFO
DESCRIPTOR.message_types_by_name['ElectionInfo'] = _ELECTIONINFO
DESCRIPTOR.message_types_by_name['CreateElectionRequest'] = _CREATEELECTIONREQUEST
DESCRIPTOR.message_types_by_name['CreateElectionResponse'] = _CREATEELECTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetElectionRequest'] = _GETELECTIONREQUEST
DESCRIPTOR.message_types_by_name['GetElectionResponse'] = _GETELECTIONRESPONSE
DESCRIPTOR.message_types_by_name['UpdateElectionRequest'] = _UPDATEELECTIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateElectionResponse'] = _UPDATEELECTIONRESPONSE
DESCRIPTOR.message_types_by_name['RemoveElectionRequest'] = _REMOVEELECTIONREQUEST
DESCRIPTOR.message_types_by_name['RemoveElectionResponse'] = _REMOVEELECTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetElectionsRequest'] = _GETELECTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetElectionsResponse'] = _GETELECTIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ElectionInfo = _reflection.GeneratedProtocolMessageType('ElectionInfo', (_message.Message,), dict(
  DESCRIPTOR = _ELECTIONINFO,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:ElectionInfo)
  ))
_sym_db.RegisterMessage(ElectionInfo)

CreateElectionRequest = _reflection.GeneratedProtocolMessageType('CreateElectionRequest', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _CREATEELECTIONREQUEST_HEADER,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:CreateElectionRequest.Header)
    ))
  ,

  Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), dict(
    DESCRIPTOR = _CREATEELECTIONREQUEST_BODY,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:CreateElectionRequest.Body)
    ))
  ,
  DESCRIPTOR = _CREATEELECTIONREQUEST,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:CreateElectionRequest)
  ))
_sym_db.RegisterMessage(CreateElectionRequest)
_sym_db.RegisterMessage(CreateElectionRequest.Header)
_sym_db.RegisterMessage(CreateElectionRequest.Body)

CreateElectionResponse = _reflection.GeneratedProtocolMessageType('CreateElectionResponse', (_message.Message,), dict(

  Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), dict(
    DESCRIPTOR = _CREATEELECTIONRESPONSE_BODY,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:CreateElectionResponse.Body)
    ))
  ,
  DESCRIPTOR = _CREATEELECTIONRESPONSE,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:CreateElectionResponse)
  ))
_sym_db.RegisterMessage(CreateElectionResponse)
_sym_db.RegisterMessage(CreateElectionResponse.Body)

GetElectionRequest = _reflection.GeneratedProtocolMessageType('GetElectionRequest', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _GETELECTIONREQUEST_HEADER,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:GetElectionRequest.Header)
    ))
  ,
  DESCRIPTOR = _GETELECTIONREQUEST,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:GetElectionRequest)
  ))
_sym_db.RegisterMessage(GetElectionRequest)
_sym_db.RegisterMessage(GetElectionRequest.Header)

GetElectionResponse = _reflection.GeneratedProtocolMessageType('GetElectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETELECTIONRESPONSE,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:GetElectionResponse)
  ))
_sym_db.RegisterMessage(GetElectionResponse)

UpdateElectionRequest = _reflection.GeneratedProtocolMessageType('UpdateElectionRequest', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _UPDATEELECTIONREQUEST_HEADER,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:UpdateElectionRequest.Header)
    ))
  ,

  Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), dict(
    DESCRIPTOR = _UPDATEELECTIONREQUEST_BODY,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:UpdateElectionRequest.Body)
    ))
  ,
  DESCRIPTOR = _UPDATEELECTIONREQUEST,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:UpdateElectionRequest)
  ))
_sym_db.RegisterMessage(UpdateElectionRequest)
_sym_db.RegisterMessage(UpdateElectionRequest.Header)
_sym_db.RegisterMessage(UpdateElectionRequest.Body)

UpdateElectionResponse = _reflection.GeneratedProtocolMessageType('UpdateElectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEELECTIONRESPONSE,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:UpdateElectionResponse)
  ))
_sym_db.RegisterMessage(UpdateElectionResponse)

RemoveElectionRequest = _reflection.GeneratedProtocolMessageType('RemoveElectionRequest', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _REMOVEELECTIONREQUEST_HEADER,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:RemoveElectionRequest.Header)
    ))
  ,
  DESCRIPTOR = _REMOVEELECTIONREQUEST,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:RemoveElectionRequest)
  ))
_sym_db.RegisterMessage(RemoveElectionRequest)
_sym_db.RegisterMessage(RemoveElectionRequest.Header)

RemoveElectionResponse = _reflection.GeneratedProtocolMessageType('RemoveElectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEELECTIONRESPONSE,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:RemoveElectionResponse)
  ))
_sym_db.RegisterMessage(RemoveElectionResponse)

GetElectionsRequest = _reflection.GeneratedProtocolMessageType('GetElectionsRequest', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _GETELECTIONSREQUEST_HEADER,
    __module__ = 'election_pb2'
    # @@protoc_insertion_point(class_scope:GetElectionsRequest.Header)
    ))
  ,
  DESCRIPTOR = _GETELECTIONSREQUEST,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:GetElectionsRequest)
  ))
_sym_db.RegisterMessage(GetElectionsRequest)
_sym_db.RegisterMessage(GetElectionsRequest.Header)

GetElectionsResponse = _reflection.GeneratedProtocolMessageType('GetElectionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETELECTIONSRESPONSE,
  __module__ = 'election_pb2'
  # @@protoc_insertion_point(class_scope:GetElectionsResponse)
  ))
_sym_db.RegisterMessage(GetElectionsResponse)



_ELECTION = _descriptor.ServiceDescriptor(
  name='Election',
  full_name='Election',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1255,
  serialized_end=1595,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateElection',
    full_name='Election.CreateElection',
    index=0,
    containing_service=None,
    input_type=_CREATEELECTIONREQUEST,
    output_type=_CREATEELECTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetElection',
    full_name='Election.GetElection',
    index=1,
    containing_service=None,
    input_type=_GETELECTIONREQUEST,
    output_type=_GETELECTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateElection',
    full_name='Election.UpdateElection',
    index=2,
    containing_service=None,
    input_type=_UPDATEELECTIONREQUEST,
    output_type=_UPDATEELECTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveElection',
    full_name='Election.RemoveElection',
    index=3,
    containing_service=None,
    input_type=_REMOVEELECTIONREQUEST,
    output_type=_REMOVEELECTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetElections',
    full_name='Election.GetElections',
    index=4,
    containing_service=None,
    input_type=_GETELECTIONSREQUEST,
    output_type=_GETELECTIONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ELECTION)

DESCRIPTOR.services_by_name['Election'] = _ELECTION

# @@protoc_insertion_point(module_scope)
