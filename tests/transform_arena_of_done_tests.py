from .context import content
import os
import unittest
from content import transform


def _get_practice():
    filename = os.path.join(os.path.dirname(
        __file__), 'examples/arena_of_done/practice.md')
    with open(filename) as file:
        markdown = file.read()
    return transform.markdown2practice(markdown)


class SilentGroupMindMappingTestCase(unittest.TestCase):
    practice = _get_practice()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_read_practice_from_file(self):
        assert self.practice.name == 'Arena of Done'

    def test_can_read_practice_description(self):
        assert self.practice.description.startswith(
            'In incremental product delivery, you deliver a working, ')

    def test_contains_two_guides(self):
        assert len(self.practice.guides) == 2

    def test_can_read_guide_titles(self):
        g1 = self.practice.guides[0]
        assert g1.title == 'Prepare the "Arena of Done" event'
        g2 = self.practice.guides[1]
        assert g2.title == 'The Arena of Done'

    def test_can_read_guide_description(self):
        g = self.practice.guides[1]
        assert g.description.startswith(
            'The Arena of Done is an interactive, collaborative event that')

    def test_guide_has_steps(self):
        g = self.practice.guides[1]
        assert len(g.steps) == 13


if __name__ == '__main__':
    unittest.main()
