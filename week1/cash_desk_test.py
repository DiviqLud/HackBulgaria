import unittest

from cash_desk import CashDesk


class CashDeskTest(unittest.TestCase):

    def test_total_zero_when_new_instance_made(self):
        new_cash_desk = CashDesk()
        self.assertEqual(0, new_cash_desk.total())

    def test_total_after_take_money(self):
        new_cash_desk = CashDesk()
        new_cash_desk.take_money({1: 2, 100: 3})
        self.assertEqual(302, new_cash_desk.total())

    def test_can_withdraw_all_money(self):
        new_cash_desk = CashDesk()
        new_cash_desk.take_money({1: 2, 100: 3})
        self.assertTrue(new_cash_desk.can_withdraw_money(302))

    

if __name__ == '__main__':
    unittest.main()
