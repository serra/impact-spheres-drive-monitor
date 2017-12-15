from ..context import content
import unittest
from content import guides
import os

BIG_WALL_GUIDE_ID = '1Cgku5owWkuaQAGo4oegOy'
GUIDE_CONTENT_TYPE_ID = 'guide'

class ContentfulTestCase(unittest.TestCase):

    def setUp(self):
        self.client = guides.get_client()

    def tearDown(self):
        pass

    def test_can_access_access_token(self):
        token = os.environ['CONTENTFUL_TOKEN']

    def test_can_retrieve_guide(self):
        guide = self.client.entry(BIG_WALL_GUIDE_ID)

    def test_can_retrieve_content_types(self):
        types = self.client.content_types()
        assert len(types) > 0

    def test_can_search_guides(self):
        result = self.client.entries({'query': 'wall', 'content_type': 'guide', 'select': 'fields.title'})
        assert len(result.items) > 0

    def test_can_search_guides_2(self):
        result = guides.search_guides('big wall')
        assert len(list(result)) > 0

