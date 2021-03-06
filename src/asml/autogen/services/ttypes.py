#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ComponentType:
  DATASTREAM = 1
  FEATGEN = 2
  LEARNER = 3
  DEPLOYER = 4

  _VALUES_TO_NAMES = {
    1: "DATASTREAM",
    2: "FEATGEN",
    3: "LEARNER",
    4: "DEPLOYER",
  }

  _NAMES_TO_VALUES = {
    "DATASTREAM": 1,
    "FEATGEN": 2,
    "LEARNER": 3,
    "DEPLOYER": 4,
  }

