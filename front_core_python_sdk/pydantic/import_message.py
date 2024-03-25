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


class ImportMessage(BaseModel):
    # Data of the sender
    sender: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='sender')

    # List of the recipient handles who will receive this message
    to: typing.List[str] = Field(alias='to')

    # Body of the message
    body: str = Field(alias='body')

    # External identifier of the message. Front won't import two messages with the same external ID.
    external_id: str = Field(alias='external_id')

    # Date at which the message as been sent or received.
    created_at: int = Field(alias='created_at')

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='metadata')

    # List of tag names to add to the conversation
    tags: typing.Optional[typing.List[str]] = Field(None, alias='tags')

    # List of the recipient handles who will receive a copy of this message
    cc: typing.Optional[typing.List[str]] = Field(None, alias='cc')

    # List of the recipient handles who will receive a blind copy of this message
    bcc: typing.Optional[typing.List[str]] = Field(None, alias='bcc')

    # Subject of the message
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Format of the message body. Can be `markdown` (default) or `html`, and can only be specified for `email` type.
    body_format: typing.Optional[Literal["html", "markdown"]] = Field(None, alias='body_format')

    # Type of the message to import. Default is `email`.
    type: typing.Optional[Literal["email", "sms", "intercom", "custom"]] = Field(None, alias='type')

    # ID of the teammate who will be assigned to the conversation.
    assignee_id: typing.Optional[str] = Field(None, alias='assignee_id')

    # If supplied, Front will thread this message into conversation with the given ID. Note that including this parameter nullifies the `thread_ref` parameter _completely_.
    conversation_id: typing.Optional[str] = Field(None, alias='conversation_id')

    # Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.
    attachments: typing.Optional[typing.List[typing.IO]] = Field(None, alias='attachments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
