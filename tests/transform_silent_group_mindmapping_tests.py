from .context import content
import os
import unittest
from content import transform


def _get_practice():
    filename = os.path.join(os.path.dirname(
        __file__), 'examples/silent_group_mind_mapping/practice.md')
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
        assert self.practice.name == 'Silent Group Mind Mapping'

    def test_can_read_practice_description(self):
        assert self.practice.description.startswith(
            'This is a technique that allows everyone to talk at once with no one')
        assert self.practice.description.endswith(
            'https://lifehacker.com/how-to-use-mind-maps-to-unleash-your-brains-creativity-1348869811\n')

    def test_contains_one_guide(self):
        assert len(self.practice.guides) == 1

    def test_can_read_guide_title(self):
        g = self.practice.guides[0]
        assert g.title == 'Silent Group Mind Mapping'

    def test_can_read_guide_description(self):
        g = self.practice.guides[0]
        assert g.description.startswith(
            'The goal is to capture and display a collaborative ')
        assert g.description.endswith('brainstorming, mindmap, group\n')

    def test_guide_has_steps(self):
        g = self.practice.guides[0]
        assert len(g.steps) == 9

    def test_step_has_instruction(self):
        g = self.practice.guides[0]
        assert g.steps[0].instruction == 'Prepare the exercise'

    def test_step_has_explanation(self):
        g = self.practice.guides[0]
        assert g.steps[0].explanation.startswith(
            'Hang a large roll of paper/whiteboard or several flip-ch')

    def test_steps_have_numbers(self):
        g = self.practice.guides[0]
        assert g.steps[0].number == 1
        assert g.steps[2].number == 3
        assert g.steps[7].number == 8


if __name__ == '__main__':
    unittest.main()
