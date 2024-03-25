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

from front_core_python_sdk.type.link_response import LinkResponse
from front_core_python_sdk.type.recipient_response import RecipientResponse
from front_core_python_sdk.type.reminder import Reminder
from front_core_python_sdk.type.tag_response import TagResponse
from front_core_python_sdk.type.teammate_response import TeammateResponse

class RequiredConversationResponse(TypedDict):
    pass

class OptionalConversationResponse(TypedDict, total=False):
    # List of the tags for this conversation
    tags: typing.List[TagResponse]

    _links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the conversation
    id: str

    # Subject of the message for email message
    subject: str

    # Status of the conversation
    status: str

    assignee: TeammateResponse

    recipient: RecipientResponse

    # List of the links for this conversation
    links: typing.List[LinkResponse]

    # Custom field attributes for this conversation
    custom_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Timestamp at which the conversation have been created.
    created_at: typing.Union[int, float]

    # Timestamp of the oldest unreplied message.
    waiting_since: typing.Union[int, float]

    # Whether or not the conversation is private
    is_private: bool

    # List of scheduled (non-expired and non-canceled) reminders for this conversation
    scheduled_reminders: typing.List[Reminder]

    # Optional metadata about the conversation
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class ConversationResponse(RequiredConversationResponse, OptionalConversationResponse):
    pass
