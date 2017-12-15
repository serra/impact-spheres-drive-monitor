from context import content
import unittest
from content import guides
from contentful.space import Space

BIG_WALL_GUIDE_ID = '1Cgku5owWkuaQAGo4oegOy'


class ContentfulGuideTestCase(unittest.TestCase):

    def setUp(self):
        self.client = guides.get_client()
        self.guide = self.client.entry(BIG_WALL_GUIDE_ID)

    def tearDown(self):
        pass

    def test_can_retrieve_space_name(self):
        assert self.guide.space, 'the space of the guide is not retrievable'
        space = self.guide.space.resolve(self.client)
        assert isinstance(space, Space)
        assert space.name == 'Guides', 'the name of the space is not "Guides"'

    def test_can_retrieve_guide_name(self):
        assert 'wall' in self.guide.description
        assert 'Wall' in self.guide.title
