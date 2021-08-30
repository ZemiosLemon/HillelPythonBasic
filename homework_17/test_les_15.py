import unittest

import les_15_task_2


class Lesson15Test(unittest.TestCase):
    def test_result_lesson6(self):
        self.assertEqual(les_15_task_2.format_number("380502852124"), "(+38) 050-285-21-24")
