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

class MessageTemplateResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the message template
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the message template
    name: typing.Optional[str] = Field(None, alias='name')

    # Subject of the message template
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Body of the message template
    body: typing.Optional[str] = Field(None, alias='body')

    # List of files attached to the response
    attachments: typing.Optional[typing.List[Attachment]] = Field(None, alias='attachments')

    # Whether or not the template is available in all inboxes.
    is_available_for_all_inboxes: typing.Optional[bool] = Field(None, alias='is_available_for_all_inboxes')

    # List of inboxes the template is available in. Null if there are no restrictions.
    inbox_ids: typing.Optional[typing.List[str]] = Field(None, alias='inbox_ids')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
