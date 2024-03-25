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

from front_core_python_sdk.type.attachment import Attachment
from front_core_python_sdk.type.recipient_response import RecipientResponse
from front_core_python_sdk.type.signature_response import SignatureResponse
from front_core_python_sdk.type.teammate_response import TeammateResponse

class RequiredMessageResponse(TypedDict):
    pass

class OptionalMessageResponse(TypedDict, total=False):
    # The current version of the message in Front
    version: str

    _links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the message
    id: str

    # Type of the message
    type: str

    # Whether or not the message has been received or sent
    is_inbound: bool

    # If the message is a draft, describes the draft mode. Can be 'private' (draft is visible to the author only) or 'shared' (draft is visible to all teammates with access to the conversation).
    draft_mode: typing.Optional[str]

    # Type of the error when the draft failed to be sent
    error_type: str

    # Date at which the message as been sent or received
    created_at: typing.Union[int, float]

    # Subject of the message
    subject: str

    # Preview of the message body
    blurb: str

    author: TeammateResponse

    recipients: typing.List[RecipientResponse]

    # Body of the message
    body: str

    # Text version of the body for email messages
    text: str

    # List of files attached to the message
    attachments: typing.List[Attachment]

    signature: SignatureResponse

    # Optional metadata about the message
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class MessageResponse(RequiredMessageResponse, OptionalMessageResponse):
    pass
