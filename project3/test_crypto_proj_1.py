import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0x3182c3c1f37f18e7d5125a6bc599b27a', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('hellokitty', password)
        self.assertEqual('pookie', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0x35001fe32427381', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0xa3e10cb9eb3ff20f77759051e16ffdb36aac9c22d037fad28a1ce369eda5c46475afd55334fb20807f7478b9b24d0249132c466d84babd0e8e2f6206d2800b55a456e1bd87bb63a9633078b06b3b31d356e394be08e0ef77f09bdd75294cbf9501c1c7d3e60b6a58bc8a54a417ac9d9b0e7b746e216cb6cbba2c94f72d9a34d1', d)
        self.assertEqual('3a7382f2174cf47162dbdf5c8ce1e7fcf3e5122214e359082e6de87b', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('They are the egg men. I am the walrus. Goo goo g\'joob.', msg)


if __name__ == '__main__':
    unittest.main()
