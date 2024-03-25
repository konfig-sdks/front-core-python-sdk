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

from front_core_python_sdk.pydantic.create_shared_message_template_attachments import CreateSharedMessageTemplateAttachments
from front_core_python_sdk.pydantic.create_shared_message_template_inbox_ids import CreateSharedMessageTemplateInboxIds

class CreateSharedMessageTemplate(BaseModel):
    # Name of the message template
    name: str = Field(alias='name')

    # Body of the message template
    body: str = Field(alias='body')

    # Subject of the message template. If not set, the name will be used to populate the subject.
    subject: typing.Optional[str] = Field(None, alias='subject')

    # ID of the message template folder to place this message template in
    folder_id: typing.Optional[str] = Field(None, alias='folder_id')

    inbox_ids: typing.Optional[CreateSharedMessageTemplateInboxIds] = Field(None, alias='inbox_ids')

    attachments: typing.Optional[CreateSharedMessageTemplateAttachments] = Field(None, alias='attachments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
