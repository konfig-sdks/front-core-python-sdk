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

from front_core_python_sdk.pydantic.attachment import Attachment
from front_core_python_sdk.pydantic.recipient_response import RecipientResponse
from front_core_python_sdk.pydantic.signature_response import SignatureResponse
from front_core_python_sdk.pydantic.teammate_response import TeammateResponse

class MessageResponse(BaseModel):
    # The current version of the message in Front
    version: typing.Optional[str] = Field(None, alias='version')

    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the message
    id: typing.Optional[str] = Field(None, alias='id')

    # Type of the message
    type: typing.Optional[Literal["call", "custom", "email", "facebook", "front_chat", "googleplay", "intercom", "internal", "phone-call", "sms", "smooch", "tweet", "tweet_dm", "whatsapp", "yalo_wha"]] = Field(None, alias='type')

    # Whether or not the message has been received or sent
    is_inbound: typing.Optional[bool] = Field(None, alias='is_inbound')

    # If the message is a draft, describes the draft mode. Can be 'private' (draft is visible to the author only) or 'shared' (draft is visible to all teammates with access to the conversation).
    draft_mode: typing.Optional[Literal["shared", "private"]] = Field(None, alias='draft_mode')

    # Type of the error when the draft failed to be sent
    error_type: typing.Optional[str] = Field(None, alias='error_type')

    # Date at which the message as been sent or received
    created_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='created_at')

    # Subject of the message
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Preview of the message body
    blurb: typing.Optional[str] = Field(None, alias='blurb')

    author: typing.Optional[TeammateResponse] = Field(None, alias='author')

    recipients: typing.Optional[typing.List[RecipientResponse]] = Field(None, alias='recipients')

    # Body of the message
    body: typing.Optional[str] = Field(None, alias='body')

    # Text version of the body for email messages
    text: typing.Optional[str] = Field(None, alias='text')

    # List of files attached to the message
    attachments: typing.Optional[typing.List[Attachment]] = Field(None, alias='attachments')

    signature: typing.Optional[SignatureResponse] = Field(None, alias='signature')

    # Optional metadata about the message
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
