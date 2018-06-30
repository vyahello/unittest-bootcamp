from unittest import TestCase


def setUpModule():
    """ Setup for a test module """

    print('setUpModule is calling before all test cases in a test module.')

    global module_string
    module_string = 'module string'


def tearDownModule():
    """ Teardown for a test module """

    print('tearDownModule is calling after all test cases in a test module.')


class TestStringMethods(TestCase):
    """ This test case is verifying basic string data type methods for truth. """

    @classmethod
    def setUpClass(cls) -> None:
        """ Setup for current test case. """

        print('setUpClass is calling once before all test methods.')
        cls.class_string: str = 'class string'

    @classmethod
    def tearDownClass(cls) -> None:
        """ Teardown for current test case. """

        print('tearDownClass is calling once after all test methods.')
        del cls.class_string

    def setUp(self):
        """ Setup for every test method. """

        print('setUp is calling before every test method.')
        self.method_string: str = 'method string'

    def tearDown(self) -> None:
        """ Teardown for every test method. """

        print('tearDown is calling after every test method.')
        del self.method_string

    def test_is_title(self) -> None:
        """ Test checks if given string is in titled case """

        print('calling test_is_title')

        titled_module_string: str = module_string.title()
        titled_class_string: str = self.class_string.title()
        titled_method_string: str = self.method_string.title()

        self.assertTrue(titled_module_string.title())
        self.assertTrue(titled_class_string.title())
        self.assertTrue(titled_method_string.istitle())

    def test_is_lower(self) -> None:
        """ Test checks if string is in lower case """

        print('calling test_is_lower')

        lower_module_string: str = module_string.lower()
        lower_class_string: str = self.class_string.lower()
        lower_method_string: str = self.method_string.lower()

        self.assertTrue(lower_module_string.islower())
        self.assertTrue(lower_class_string.islower())
        self.assertTrue(lower_method_string.islower())

    def test_is_upper(self) -> None:
        """ Test checks if string is in upper case """

        print('calling test_is_upper')

        upper_module_string: str = module_string.upper()
        upper_class_string: str = self.class_string.upper()
        upper_method_string: str = self.method_string.upper()

        self.assertTrue(upper_module_string.isupper())
        self.assertTrue(upper_class_string.isupper())
        self.assertTrue(upper_method_string.isupper())
