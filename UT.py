#!/usr/bin/env python3

import unittest
import ptp


class TestConversionMethods(unittest.TestCase):
    def test_colon_to_sec(self):
        self.assertEqual(ptp.colon_to_sec(''), 0)
        self.assertEqual(ptp.colon_to_sec(' '), 0)
        self.assertEqual(ptp.colon_to_sec('   '), 0)
        self.assertEqual(ptp.colon_to_sec('     '), 0)
        self.assertEqual(ptp.colon_to_sec(':'), 0)
        self.assertEqual(ptp.colon_to_sec(':::'), 0)
        self.assertEqual(ptp.colon_to_sec(':::::'), 0)
        self.assertEqual(ptp.colon_to_sec('0'), 0)
        self.assertEqual(ptp.colon_to_sec(' 0 '), 0)
        self.assertEqual(ptp.colon_to_sec('   0   '), 0)
        self.assertEqual(ptp.colon_to_sec('     0     '), 0)
        self.assertEqual(ptp.colon_to_sec('0:'), 0)
        self.assertEqual(ptp.colon_to_sec(':0'), 0)
        self.assertEqual(ptp.colon_to_sec(':0:'), 0)
        self.assertEqual(ptp.colon_to_sec(':::0:::'), 0)
        self.assertEqual(ptp.colon_to_sec(':::::0:::::'), 0)
        self.assertEqual(ptp.colon_to_sec('1'), 1)
        self.assertEqual(ptp.colon_to_sec(' 1 '), 1)
        self.assertEqual(ptp.colon_to_sec('   1   '), 1)
        self.assertEqual(ptp.colon_to_sec('     1     '), 1)
        self.assertEqual(ptp.colon_to_sec('1:'), 1)
        self.assertEqual(ptp.colon_to_sec(':1'), 1)
        self.assertEqual(ptp.colon_to_sec(':1:'), 1)
        self.assertEqual(ptp.colon_to_sec(':::1:::'), 1)
        self.assertEqual(ptp.colon_to_sec(':::::1:::::'), 1)
        self.assertEqual(ptp.colon_to_sec('0:1'), 1)
        self.assertEqual(ptp.colon_to_sec(':0:1:'), 1)
        self.assertEqual(ptp.colon_to_sec('0:0:1'), 1)
        self.assertEqual(ptp.colon_to_sec(':0:0:1:'), 1)
        self.assertEqual(ptp.colon_to_sec('0:0:0:0:1'), 1)
        self.assertEqual(ptp.colon_to_sec(':0:0:0:0:1:'), 1)
        self.assertEqual(ptp.colon_to_sec('1:0'), 60)
        self.assertEqual(ptp.colon_to_sec('0:1:0'), 60)
        self.assertEqual(ptp.colon_to_sec('1:0:0'), 3600)
        self.assertEqual(ptp.colon_to_sec('0:1:0:0'), 3600)
        self.assertEqual(ptp.colon_to_sec('1:1:0'), 3660)
        self.assertEqual(ptp.colon_to_sec('1:1:1'), 3661)
        self.assertEqual(ptp.colon_to_sec('1:2:3'), 3723)
        self.assertEqual(ptp.colon_to_sec('2:0:0'), 7200)
        self.assertEqual(ptp.colon_to_sec('3:0:0'), 10800)
        self.assertEqual(ptp.colon_to_sec('3:2:1'), 10921)
        self.assertEqual(ptp.colon_to_sec('1:2:3:4:5:6'), 804182706)
        self.assertEqual(ptp.colon_to_sec('6:5:4:3:2:1'), 4731274921)

    def test_sec_to_colon(self):
        self.assertEqual(ptp.sec_to_colon(1), '0:1')
        self.assertEqual(ptp.sec_to_colon(2), '0:2')
        self.assertEqual(ptp.sec_to_colon(3), '0:3')
        self.assertEqual(ptp.sec_to_colon(5), '0:5')
        self.assertEqual(ptp.sec_to_colon(10), '0:10')
        self.assertEqual(ptp.sec_to_colon(60), '0:1:0')
        self.assertEqual(ptp.sec_to_colon(61), '0:1:1')
        self.assertEqual(ptp.sec_to_colon(3600), '0:1:0:0')
        self.assertEqual(ptp.sec_to_colon(3661), '0:1:1:1')
        self.assertEqual(ptp.sec_to_colon(7200), '0:2:0:0')
        self.assertEqual(ptp.sec_to_colon(10800), '0:3:0:0')
        self.assertEqual(ptp.sec_to_colon(3723), '0:1:2:3')
        self.assertEqual(ptp.sec_to_colon(10921), '0:3:2:1')

    def test_sec_colon_sec(self):
        for sec in [0, 1, 2, 3, 4, 5, 3600, 3661, 1234, 4312, 666, 10800, 390, 4090]:
            self.assertEqual(ptp.colon_to_sec(ptp.sec_to_colon(sec)), sec)

    def test_colon_sec_colon(self):
        for colon in ['0', '0:1', '0:2', '0:3', '0:1:2:3:3', '0:3:2:1:0:0:0', '0:1:4:8', '0:1:2:23:44']:
            self.assertEqual(ptp.sec_to_colon(ptp.colon_to_sec(colon)), colon)


if __name__ == '__main__':
    unittest.main()
