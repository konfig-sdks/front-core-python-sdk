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


class RequiredOutboundReplyMessage(TypedDict):
    # Body of the message
    body: str

class OptionalOutboundReplyMessage(TypedDict, total=False):
    # List of the recipient handles who will receive this message
    to: typing.List[str]

    # List of the recipient handles who will receive a copy of this message
    cc: typing.List[str]

    # List of the recipient handles who will receive a copy of this message
    bcc: typing.List[str]

    # Name used for the sender info of the message
    sender_name: str

    # Subject of the message for email message
    subject: str

    # ID of the teammate on behalf of whom the answer is sent
    author_id: str

    # Channel ID the message is sent from
    channel_id: str

    # Text version of the body for email messages
    text: str

    # Body for the quote that the message is referencing. Only available on email channels.
    quote_body: str

    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.
    attachments: typing.List[typing.IO]

    # ID of the signature to attach to this draft. If null, no signature is attached.
    signature_id: str

    # Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;
    should_add_default_signature: bool

class OutboundReplyMessage(RequiredOutboundReplyMessage, OptionalOutboundReplyMessage):
    pass
