from .context import google
from google import guide_reports
import unittest


class OkCounterTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_ok(self):
        s = '''
        Marijn: OK
        Dov: OK
        Hugo: OK
        '''
        assert 3 == guide_reports.count_oks_in(s)

    def test_one_ok(self):
        s = '''
        Hugo: OK'''
        assert 1 == guide_reports.count_oks_in(s)

    def test_one_ok_much_whitespace(self):
        s = '''
        Hugo:     OK'''
        assert 1 == guide_reports.count_oks_in(s)

    def test_one_ok_two_not_ok(self):
        s = '''
        Marijn: OK
        Dov: not OK
        Hugo: not OK
        '''
        assert 1 == guide_reports.count_oks_in(s)

    def test_ok_is_case_insensitive(self):
        s = '''
        Marijn: Ok
        Dov: ok
        Hugo: OK
        John: oK
        '''
        assert 4 == guide_reports.count_oks_in(s)


if __name__ == '__main__':
    unittest.main()
