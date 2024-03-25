# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

import unittest

import os
from pprint import pprint
from front_core_python_sdk import FrontCore

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        frontcore = FrontCore(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(frontcore)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
