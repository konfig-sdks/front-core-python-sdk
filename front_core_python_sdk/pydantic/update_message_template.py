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


class UpdateMessageTemplate(BaseModel):
    # Name of the message template
    name: typing.Optional[str] = Field(None, alias='name')

    # Subject of the message template
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Body of the message template
    body: typing.Optional[str] = Field(None, alias='body')

    # ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.
    folder_id: typing.Optional[str] = Field(None, alias='folder_id')

    # The specific inboxes this template is available in. If null, then it will be available in all inboxes. Array should be non-empty. If unspecified, will retain previous value.
    inbox_ids: typing.Optional[typing.List[str]] = Field(None, alias='inbox_ids')

    # Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://dev.frontapp.com/docs/attachments-1). Max 25 MB. Specify an empty array to delete all attachments from a message template. If unspecified, it will retain previous value.
    attachments: typing.Optional[typing.List[typing.IO]] = Field(None, alias='attachments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
