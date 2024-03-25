# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredCreateConversation(TypedDict):
    # Conversation type
    type: str

    # Subject of the conversation
    subject: str

    # Details for the starter comment
    comment: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalCreateConversation(TypedDict, total=False):
    # Inbox ID for the conversation. Either `inbox_id` OR `teammate_ids` must be provided (not both).
    inbox_id: str

    # Teammates to add to the conversation. Either `inbox_id` OR `teammate_ids` must be provided (not both).
    teammate_ids: typing.List[str]

class CreateConversation(RequiredCreateConversation, OptionalCreateConversation):
    pass
