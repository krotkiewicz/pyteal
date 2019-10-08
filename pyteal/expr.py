#!/usr/bin/env python3

"""
An expression language for TEAL.

"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import ClassVar, List

from .util import TealType

     
class Expr(ABC):

     @abstractmethod
     def type_of(self) -> TealType:
          """Returns a TealType enum describing the expression's return type
          """
          pass

     @abstractmethod
     def __str__(self) -> str:
          """Returns the string representation of the experssion
          """
          pass
     
     def __lt__(self, other):
          from .ops import Lt
          return Lt(self, other)

     def __gt__(self, other):
          from .ops import Gt
          return Gt(self, other)
     
     def __eq__(self, other):
          from .ops import Eq
          return Eq(self, other)

     # logic and
     def And(self, other):
          from .ops import And
          return And(self, other)

     # logic or
     def Or(self, other):
          from .ops import Or
          return Or(self, other)


class BinaryExpr(Expr):
     left: ClassVar[Expr]
     right: ClassVar[Expr]
    

class UnaryExpr(Expr):
     child: ClassVar[Expr]

class NaryExpr(Expr):
     args: ClassVar[List[Expr]]

class LeafExpr(Expr):
     pass

