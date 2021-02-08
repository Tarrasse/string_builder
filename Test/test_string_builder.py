import unittest

from StringBuilder.string_builder import StringBuilder


class TestStringBuilder(unittest.TestCase):
    def setUp(self):
        self.string_builder = StringBuilder()
        self.test_list = ['this', 'is', 'a', 'test', 'case']
        self.string_builder.append(self.test_list[0])
        self.string_builder.append(self.test_list[1])
        self.string_builder.append(self.test_list[2])
        self.string_builder.append(self.test_list[3])
        self.string_builder.append(self.test_list[4])

    def test_append(self):
        self.assertLessEqual(self.string_builder.length, len(''.join(self.test_list)))

        self.string_builder.capacity = 17
        self.assertEqual(self.string_builder.append("   "), False)

        self.assertEqual(self.string_builder.length, 15)

    def test_delete_all_before(self):
        self.string_builder.delete(end=4)
        self.assertEqual(self.string_builder.length, 11)
        self.assertEqual(self.string_builder.build(), "isatestcase")

        self.string_builder._delete_all_before(5)
        self.assertEqual(self.string_builder.build(), "stcase")

    def test_delete_all_after(self):
        self.string_builder.delete(start=4)
        self.assertEqual(self.string_builder.length, 5)

        self.string_builder._delete_all_after(3)
        self.assertEqual(self.string_builder.length, 4)

    def test_replace(self):
        s = self.string_builder.build()

        self.string_builder.replace('s', "X")

        self.assertNotEqual(self.string_builder.build(), s)
        self.assertEqual(self.string_builder.build(), "thiXiXateXtcaXe")

    def test_delete_subset(self):
        self.string_builder._delete_subset(2, 8)
        self.assertEqual(self.string_builder.build(), "thestcase")

    def test_delete_subset2(self):
        builder = StringBuilder()
        builder.append("THISISATESTCASE")
        builder._delete_subset(2, 5)
        self.assertEqual("THSATESTCASE", builder.build())

    def test_method_chaining(self):
        builder = StringBuilder()
        self.assertEquals("HJK", builder.append("H").append("J").append("K").build())

if __name__ == '__main__':
    unittest.main()
