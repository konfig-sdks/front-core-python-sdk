# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.links.post import CreateLink
from front_core_python_sdk.paths.links_link_id.get import GetLink
from front_core_python_sdk.paths.links.get import ListByIdAndType
from front_core_python_sdk.paths.links_link_id_conversations.get import ListConversations
from front_core_python_sdk.paths.links_link_id.patch import UpdateLink
from front_core_python_sdk.apis.tags.links_api_raw import LinksApiRaw


class LinksApi(
    CreateLink,
    GetLink,
    ListByIdAndType,
    ListConversations,
    UpdateLink,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LinksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LinksApiRaw(api_client)