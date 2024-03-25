# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.inboxes_inbox_id_teammates.post import AddTeammateAccessRaw
from front_core_python_sdk.paths.inboxes.post import CreateDefaultTeamInboxRaw
from front_core_python_sdk.paths.teams_team_id_inboxes.post import CreateTeamInboxRaw
from front_core_python_sdk.paths.inboxes_inbox_id.get import GetInboxRaw
from front_core_python_sdk.paths.inboxes_inbox_id_channels.get import ListChannelsRaw
from front_core_python_sdk.paths.inboxes_inbox_id_conversations.get import ListConversationsInboxRaw
from front_core_python_sdk.paths.inboxes.get import ListInboxesRaw
from front_core_python_sdk.paths.teams_team_id_inboxes.get import ListTeamInboxesRaw
from front_core_python_sdk.paths.inboxes_inbox_id_teammates.get import ListTeammatesAccessRaw
from front_core_python_sdk.paths.inboxes_inbox_id_teammates.delete import RemoveAccessRaw


class InboxesApiRaw(
    AddTeammateAccessRaw,
    CreateDefaultTeamInboxRaw,
    CreateTeamInboxRaw,
    GetInboxRaw,
    ListChannelsRaw,
    ListConversationsInboxRaw,
    ListInboxesRaw,
    ListTeamInboxesRaw,
    ListTeammatesAccessRaw,
    RemoveAccessRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass