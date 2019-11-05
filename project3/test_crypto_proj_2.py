import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0x64a93e3f817db41d655a9b23fc2dc6c6', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('barcelona', password)
        self.assertEqual('frankie', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0x803370c3c0ee601', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0x3668cfa60c2ea502faa04aba5dd0b0a8540ff4dbc8af02eb36bf3a156d4ca23849ba2e349025f9058e9497a425bb9019d42626c37c717c10173e3848514a60bc32b3d61066fb6e4b7560b0ced98c9f97466e91ea06cd94496d52da53cd504620c64bdc6392b47257e7299c6b0d44a6c0cd37ea4d941dfd28c513241c3de6a19', d)
        self.assertEqual('ea142d85a98a5e1663bee3c7e49de60d69bc8444ff4c335b3c424d2c', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('I am the Lizard King, I can do anything!', msg)


if __name__ == '__main__':
    unittest.main()
