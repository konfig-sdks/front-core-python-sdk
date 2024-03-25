# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

import unittest
from unittest.mock import patch

import urllib3

import front_core_python_sdk
from front_core_python_sdk.paths.conversations_conversation_id_drafts import post
from front_core_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestConversationsConversationIdDrafts(ApiTestMixin, unittest.TestCase):
    """
    ConversationsConversationIdDrafts unit test stubs
        Create draft reply
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
