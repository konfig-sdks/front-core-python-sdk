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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from front_core_python_sdk.pydantic.comment_response import CommentResponse
from front_core_python_sdk.pydantic.conversation_response import ConversationResponse
from front_core_python_sdk.pydantic.inbox_response import InboxResponse
from front_core_python_sdk.pydantic.link_response import LinkResponse
from front_core_python_sdk.pydantic.message_response import MessageResponse
from front_core_python_sdk.pydantic.rule_response import RuleResponse
from front_core_python_sdk.pydantic.tag_response import TagResponse
from front_core_python_sdk.pydantic.teammate_response import TeammateResponse

class EventResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the event
    id: typing.Optional[str] = Field(None, alias='id')

    # Type of event
    type: typing.Optional[Literal["assign", "unassign", "archive", "reopen", "trash", "restore", "reminder", "comment", "mention", "inbound", "outbound", "outbound_reply", "move", "forward", "tag", "untag", "sending_error", "message_bounce_error", "conversations_merged", "link_added", "link_removed", "custom_field_updated"]] = Field(None, alias='type')

    # Date at which the event has been emitted
    emitted_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='emitted_at')

    # Event source
    source: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='source')

    # Partial representation (type & id) of the event's target
    target: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='target')

    conversation: typing.Optional[ConversationResponse] = Field(None, alias='conversation')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
