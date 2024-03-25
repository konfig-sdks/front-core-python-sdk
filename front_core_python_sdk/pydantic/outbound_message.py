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


class OutboundMessage(BaseModel):
    # List of the recipient handles who will receive this message
    to: typing.List[str] = Field(alias='to')

    # Body of the message
    body: str = Field(alias='body')

    # List of the recipient handles who will receive a copy of this message
    cc: typing.Optional[typing.List[str]] = Field(None, alias='cc')

    # List of the recipient handles who will receive a blind copy of this message
    bcc: typing.Optional[typing.List[str]] = Field(None, alias='bcc')

    # Name used for the sender info of the message
    sender_name: typing.Optional[str] = Field(None, alias='sender_name')

    # Subject of the message for email message
    subject: typing.Optional[str] = Field(None, alias='subject')

    # ID of the teammate on behalf of whom the answer is sent
    author_id: typing.Optional[str] = Field(None, alias='author_id')

    # Text version of the body for email messages
    text: typing.Optional[str] = Field(None, alias='text')

    options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='options')

    # Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1). Max 25 MB.
    attachments: typing.Optional[typing.List[typing.IO]] = Field(None, alias='attachments')

    # ID of the signature to attach to this draft. If null, no signature is attached.
    signature_id: typing.Optional[str] = Field(None, alias='signature_id')

    # Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;
    should_add_default_signature: typing.Optional[bool] = Field(None, alias='should_add_default_signature')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
