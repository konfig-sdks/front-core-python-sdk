# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.conversations_conversation_id_followers.post import AddFollowersRaw
from front_core_python_sdk.paths.conversations_conversation_id_links.post import AddLinkRaw
from front_core_python_sdk.paths.conversations_conversation_id_tags.post import AddTagsToConversationRaw
from front_core_python_sdk.paths.conversations.post import CreateDiscussionRaw
from front_core_python_sdk.paths.conversations_conversation_id.get import GetByIdRaw
from front_core_python_sdk.paths.conversations_conversation_id_events.get import ListEventsRaw
from front_core_python_sdk.paths.conversations_conversation_id_followers.get import ListFollowersRaw
from front_core_python_sdk.paths.conversations.get import ListInReverseChronologicalOrderRaw
from front_core_python_sdk.paths.conversations_conversation_id_inboxes.get import ListInboxesRaw
from front_core_python_sdk.paths.conversations_conversation_id_messages.get import ListMessagesInReverseChronologicalOrderRaw
from front_core_python_sdk.paths.conversations_conversation_id_followers.delete import RemoveFollowersRaw
from front_core_python_sdk.paths.conversations_conversation_id_links.delete import RemoveLinksRaw
from front_core_python_sdk.paths.conversations_conversation_id_tags.delete import RemoveTagRaw
from front_core_python_sdk.paths.conversations_search_query.get import SearchByQueryRaw
from front_core_python_sdk.paths.conversations_conversation_id_assignee.put import UpdateAssigneeRaw
from front_core_python_sdk.paths.conversations_conversation_id.patch import UpdateConversationByIdRaw
from front_core_python_sdk.paths.conversations_conversation_id_reminders.patch import UpdateRemindersRaw


class ConversationsApiRaw(
    AddFollowersRaw,
    AddLinkRaw,
    AddTagsToConversationRaw,
    CreateDiscussionRaw,
    GetByIdRaw,
    ListEventsRaw,
    ListFollowersRaw,
    ListInReverseChronologicalOrderRaw,
    ListInboxesRaw,
    ListMessagesInReverseChronologicalOrderRaw,
    RemoveFollowersRaw,
    RemoveLinksRaw,
    RemoveTagRaw,
    SearchByQueryRaw,
    UpdateAssigneeRaw,
    UpdateConversationByIdRaw,
    UpdateRemindersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
