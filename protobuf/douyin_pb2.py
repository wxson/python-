# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: douyin.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x64ouyin.proto\x12\x04test\x1a\x1fgoogle/protobuf/timestamp.proto\"(\n\nPushHeader\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xc0\x01\n\tPushFrame\x12\r\n\x05SeqID\x18\x01 \x01(\x04\x12\r\n\x05LogID\x18\x02 \x01(\x04\x12\x0f\n\x07service\x18\x03 \x01(\x05\x12\x0e\n\x06method\x18\x04 \x01(\x05\x12!\n\x07headers\x18\x05 \x03(\x0b\x32\x10.test.PushHeader\x12\x18\n\x10payload_encoding\x18\x06 \x01(\t\x12\x14\n\x0cpayload_type\x18\x07 \x01(\t\x12\x0f\n\x07payload\x18\x08 \x01(\x0c\x12\x10\n\x08LodIDNew\x18\t \x01(\t\"\xa1\x01\n\x07Message\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x0e\n\x06msg_id\x18\x03 \x01(\x04\x12\x10\n\x08msg_type\x18\x04 \x01(\x05\x12\x0e\n\x06offset\x18\x05 \x01(\x04\x12\x17\n\x0fneed_wrds_store\x18\x06 \x01(\x08\x12\x14\n\x0cwrds_version\x18\x07 \x01(\x04\x12\x14\n\x0cwrds_sub_key\x18\x08 \x01(\t\"\xfc\x02\n\x08Response\x12\x1f\n\x08messages\x18\x01 \x03(\x0b\x32\r.test.Message\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\x12\x16\n\x0e\x66\x65tch_interval\x18\x03 \x01(\x04\x12\x0b\n\x03now\x18\x04 \x01(\x04\x12\x14\n\x0cinternal_ext\x18\x05 \x01(\t\x12\x12\n\nfetch_type\x18\x06 \x01(\x05\x12\x35\n\x0croute_params\x18\x07 \x03(\x0b\x32\x1f.test.Response.RouteParamsEntry\x12\x1a\n\x12heartbeat_duration\x18\x08 \x01(\x04\x12\x10\n\x08need_ack\x18\t \x01(\x08\x12\x13\n\x0bpush_server\x18\n \x01(\t\x12\x13\n\x0blive_cursor\x18\x0b \x01(\t\x12\x17\n\x0fhistory_no_more\x18\x0c \x01(\x08\x12\x14\n\x0cproxy_server\x18\r \x01(\t\x1a\x32\n\x10RouteParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x83\x01\n\x0b\x43hatMessage\x12\x18\n\x04user\x18\x02 \x01(\x0b\x32\n.test.User\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x19\n\x11visible_to_sender\x18\x04 \x01(\x08\x12.\n\nevent_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"F\n\x0bGiftMessage\x12\x18\n\x04user\x18\x07 \x01(\x0b\x32\n.test.User\x12\x1d\n\x03gif\x18\x0f \x01(\x0b\x32\x10.test.GiftStruct\"5\n\x04User\x12\n\n\x02id\x18\x04 \x01(\x04\x12\x0f\n\x07shortId\x18\x02 \x01(\x04\x12\x10\n\x08nickName\x18\x03 \x01(\t\"8\n\nGiftStruct\x12\x10\n\x08\x64\x65scribe\x18\x02 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\x04\x12\x0c\n\x04name\x18\x10 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'douyin_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RESPONSE_ROUTEPARAMSENTRY']._options = None
  _globals['_RESPONSE_ROUTEPARAMSENTRY']._serialized_options = b'8\001'
  _globals['_PUSHHEADER']._serialized_start=55
  _globals['_PUSHHEADER']._serialized_end=95
  _globals['_PUSHFRAME']._serialized_start=98
  _globals['_PUSHFRAME']._serialized_end=290
  _globals['_MESSAGE']._serialized_start=293
  _globals['_MESSAGE']._serialized_end=454
  _globals['_RESPONSE']._serialized_start=457
  _globals['_RESPONSE']._serialized_end=837
  _globals['_RESPONSE_ROUTEPARAMSENTRY']._serialized_start=787
  _globals['_RESPONSE_ROUTEPARAMSENTRY']._serialized_end=837
  _globals['_CHATMESSAGE']._serialized_start=840
  _globals['_CHATMESSAGE']._serialized_end=971
  _globals['_GIFTMESSAGE']._serialized_start=973
  _globals['_GIFTMESSAGE']._serialized_end=1043
  _globals['_USER']._serialized_start=1045
  _globals['_USER']._serialized_end=1098
  _globals['_GIFTSTRUCT']._serialized_start=1100
  _globals['_GIFTSTRUCT']._serialized_end=1156
# @@protoc_insertion_point(module_scope)