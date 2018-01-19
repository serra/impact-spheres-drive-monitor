from context import content
import os
import unittest
from content import guides

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
        guide = guides.find_guide(BIG_WALL_GUIDE_ID)

    def test_can_search_guides(self):
        result = guides.search_guides('wall')
        all = list(result)
        assert len(all) > 0

    def test_search_can_return_no_guides(self):
        result = guides.search_guides('thiz guide duz not exizt')
        all = list(result)
        assert len(all) == 0

    def test_can_retrieve_id_title_description(self):
        result = guides.search_guides('big wall')
        all = list(result)
        assert len(all) > 0

        guide = all[0]

        assert guide['id']
        assert guide['title']
        assert guide['description']
