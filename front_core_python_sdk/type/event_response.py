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

from front_core_python_sdk.type.comment_response import CommentResponse
from front_core_python_sdk.type.conversation_response import ConversationResponse
from front_core_python_sdk.type.inbox_response import InboxResponse
from front_core_python_sdk.type.link_response import LinkResponse
from front_core_python_sdk.type.message_response import MessageResponse
from front_core_python_sdk.type.rule_response import RuleResponse
from front_core_python_sdk.type.tag_response import TagResponse
from front_core_python_sdk.type.teammate_response import TeammateResponse

class RequiredEventResponse(TypedDict):
    pass

class OptionalEventResponse(TypedDict, total=False):
    _links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the event
    id: str

    # Type of event
    type: str

    # Date at which the event has been emitted
    emitted_at: typing.Union[int, float]

    # Event source
    source: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Partial representation (type & id) of the event's target
    target: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    conversation: ConversationResponse

class EventResponse(RequiredEventResponse, OptionalEventResponse):
    pass
