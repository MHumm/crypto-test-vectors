#!/usr/bin/env python3

import unittest
from kdf import *


class KDFTests(unittest.TestCase):
    def test_kdf_vector_one(self):
        """Test vector #1, ANSI X9.63
            [SHA-256]
            [shared secret length = 192]
            [SharedInfo length = 0]
            [key data length = 128]
        """
        known_ss1 = "96c05619d56c328ab95fe84b18264b08725b85e33fd34f08"
        known_kdp1 = ""
        known_key1 = "443024c3dae66b95e6f5670601558f71"
        dl = len(known_key1) // 2
        kdf_out = sha256_kdf(known_ss1, known_kdp1, dl)
        self.assertEqual(kdf_out, known_key1)

    def test_kdf_vector_two(self):
        """Test vector #2, ANSI X9.63
            [SHA-256]
            [shared secret length = 192]
            [SharedInfo length = 0]
            [key data length = 128]
        """
        known_ss2 = "96f600b73ad6ac5629577eced51743dd2c24c21b1ac83ee4"
        known_kdp2 = ""
        known_key2 = "b6295162a7804f5667ba9070f82fa522"
        dl = len(known_key2) // 2
        kdf_out = sha256_kdf(known_ss2, known_kdp2, dl)
        self.assertEqual(kdf_out, known_key2)

    def test_kdf_vector_three(self):
        """Test vector #3, ANSI X9.63
            [SHA-256]
            [shared secret length = 192]
            [SharedInfo length = 128]
            [key data length = 1024]
        """
        known_ss3 = "22518b10e70f2a3f243810ae3254139efbee04aa57c7af7d"
        known_kdp3 = "75eef81aa3041e33b80971203d2c0c52"
        known_key3 = "c498af77161cc59f2962b9a713e2b215152d139766ce34a776df11866a69bf2e52a13d9c7c6fc878c50c5ea0bc7b00e0da2447cfd874f6cf92f30d0097111485500c90c3af8b487872d04685d14c8d1dc8d7fa08beb0ce0ababc11f0bd496269142d43525a78e5bc79a17f59676a5706dc54d54d4d1f0bd7e386128ec26afc21"
        dl = len(known_key3) // 2
        kdf_out = sha256_kdf(known_ss3, known_kdp3, dl)
        self.assertEqual(kdf_out, known_key3)

    def test_kdf_vector_four(self):
        """Test vector #4, ANSI X9.63
            [SHA-256]
            [shared secret length = 192]
            [SharedInfo length = 128]
            [key data length = 1024]
        """
        known_ss4 = "7e335afa4b31d772c0635c7b0e06f26fcd781df947d2990a"
        known_kdp4 = "d65a4812733f8cdbcdfb4b2f4c191d87"
        known_key4 = "c0bd9e38a8f9de14c2acd35b2f3410c6988cf02400543631e0d6a4c1d030365acbf398115e51aaddebdc9590664210f9aa9fed770d4c57edeafa0b8c14f93300865251218c262d63dadc47dfa0e0284826793985137e0a544ec80abf2fdf5ab90bdaea66204012efe34971dc431d625cd9a329b8217cc8fd0d9f02b13f2f6b0b"
        dl = len(known_key4) // 2
        kdf_out = sha256_kdf(known_ss4, known_kdp4, dl)
        self.assertEqual(kdf_out, known_key4)


if __name__ == '__main__':
    unittest.main()
