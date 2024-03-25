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

from front_core_python_sdk.type.messages_get_message_seen_status_response_links import MessagesGetMessageSeenStatusResponseLinks
from front_core_python_sdk.type.messages_get_message_seen_status_response_pagination import MessagesGetMessageSeenStatusResponsePagination
from front_core_python_sdk.type.seen_receipt_response import SeenReceiptResponse

class RequiredMessagesGetMessageSeenStatusResponse(TypedDict):
    pass

class OptionalMessagesGetMessageSeenStatusResponse(TypedDict, total=False):
    _pagination: MessagesGetMessageSeenStatusResponsePagination

    _links: MessagesGetMessageSeenStatusResponseLinks

    _results: typing.List[SeenReceiptResponse]

class MessagesGetMessageSeenStatusResponse(RequiredMessagesGetMessageSeenStatusResponse, OptionalMessagesGetMessageSeenStatusResponse):
    pass
