import unittest
import les_11_task_2
import les_15_task_2
import les_6_task_1
import les_7_task_2


class Lesson6Test(unittest.TestCase):
    def test_lesson6(self):
        coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
        code = ('BTC', 'ETH', 'XRP', 'LTC')
        self.assertEqual(les_6_task_1.list_dict(coin, code),
                         {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'})


class Lesson7Test(unittest.TestCase):
    def test_lesson7_cel(self):
        self.assertEqual(les_7_task_2.celsius(293.15, 'K'), 20)

    def test_lesson7_far(self):
        self.assertEqual(les_7_task_2.fahrenheit(20, 'C'), 68)

    def test_lesson7_kel(self):
        self.assertEqual(les_7_task_2.kelvin(20, 'C'), 293.15)


class Lesson11Test(unittest.TestCase):
    def test_lessons_11(self):
        poli_list = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', 'ЛЕД', '13231', 'T E N E T', 'ШАБАШ']
        self.assertEqual(les_11_task_2.verification(poli_list), True)


class Lesson15Test(unittest.TestCase):
    def test_lessons_15(self):
        self.assertEqual(les_15_task_2.format_number('063-999-99-99'), '(+38) 063 999-99-99')
