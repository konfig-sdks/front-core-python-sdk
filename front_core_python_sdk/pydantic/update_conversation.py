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


class UpdateConversation(BaseModel):
    # ID of the teammate to assign the conversation to. Set it to null to unassign.
    assignee_id: typing.Optional[str] = Field(None, alias='assignee_id')

    # ID of the inbox to move the conversation to.
    inbox_id: typing.Optional[str] = Field(None, alias='inbox_id')

    # New status of the conversation
    status: typing.Optional[Literal["archived", "open", "deleted", "spam"]] = Field(None, alias='status')

    # List of all the tag IDs replacing the old conversation tags
    tag_ids: typing.Optional[typing.List[str]] = Field(None, alias='tag_ids')

    # Custom field attributes for this conversation. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.
    custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='custom_fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
