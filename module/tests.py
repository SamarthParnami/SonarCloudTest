from unittest import TestCase


class FunctionATest(TestCase):

    def test1(self):
        from .source import functionA
        functionA()