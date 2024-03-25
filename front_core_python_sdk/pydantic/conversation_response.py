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

from front_core_python_sdk.pydantic.link_response import LinkResponse
from front_core_python_sdk.pydantic.recipient_response import RecipientResponse
from front_core_python_sdk.pydantic.reminder import Reminder
from front_core_python_sdk.pydantic.tag_response import TagResponse
from front_core_python_sdk.pydantic.teammate_response import TeammateResponse

class ConversationResponse(BaseModel):
    # List of the tags for this conversation
    tags: typing.Optional[typing.List[TagResponse]] = Field(None, alias='tags')

    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the conversation
    id: typing.Optional[str] = Field(None, alias='id')

    # Subject of the message for email message
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Status of the conversation
    status: typing.Optional[Literal["archived", "unassigned", "deleted", "assigned"]] = Field(None, alias='status')

    assignee: typing.Optional[TeammateResponse] = Field(None, alias='assignee')

    recipient: typing.Optional[RecipientResponse] = Field(None, alias='recipient')

    # List of the links for this conversation
    links: typing.Optional[typing.List[LinkResponse]] = Field(None, alias='links')

    # Custom field attributes for this conversation
    custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='custom_fields')

    # Timestamp at which the conversation have been created.
    created_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='created_at')

    # Timestamp of the oldest unreplied message.
    waiting_since: typing.Optional[typing.Union[int, float]] = Field(None, alias='waiting_since')

    # Whether or not the conversation is private
    is_private: typing.Optional[bool] = Field(None, alias='is_private')

    # List of scheduled (non-expired and non-canceled) reminders for this conversation
    scheduled_reminders: typing.Optional[typing.List[Reminder]] = Field(None, alias='scheduled_reminders')

    # Optional metadata about the conversation
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
