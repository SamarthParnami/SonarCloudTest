from unittest import TestCase


class FunctionATest(TestCase):

    def test1(self):
        from .source import functionA
        functionA()



class FunctionDTest(TestCase):

    def test1(self):
        from .source import functionD
        functionD()


class FunctionETest(TestCase):

    def test1(self):
        from .source import functionE
        functionE()


class FunctionKTest(TestCase):

    def test1(self):
        from .source import functionK
        functionK()