from context import google
from google import guide_reports
import logging

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)


class GoogleLibrary:

    def __init__(sefl):
        pass

    def can_access_review_folder(self):
        guide_reports.to_review()
