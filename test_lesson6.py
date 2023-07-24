import unittest
from unittest import TestCase

import lesson6


class TestColorPosition(TestCase):

    def test_upper(self):
        p = lesson6.ColorSwitcher()
        self.assertEqual(p.current_color().get_color(), lesson6.Colors.RED)
        self.assertEqual(p.current_color().get_position(), 2)


if __name__ == '__main__':
    unittest.main()
    pass
