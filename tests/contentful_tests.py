from context import content
import unittest
from content import guides
import os

BIG_WALL_GUIDE_ID = '1Cgku5owWkuaQAGo4oegOy'

class ContentfulTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_access_access_token(self):
        token = os.environ['CONTENTFUL_TOKEN']

    #
    # def test_can_connect_to_space(self):
    #     client = guides.get_client()
    #     client.entries()

    def test_can_retrieve_guide(self):
        client = guides.get_client()
        guide = client.entry(BIG_WALL_GUIDE_ID)

