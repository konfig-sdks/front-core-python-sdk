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


class UpdateTag(BaseModel):
    # Description of the tag
    description: typing.Optional[str] = Field(None, alias='description')

    # Name of the tag
    name: typing.Optional[str] = Field(None, alias='name')

    # Highlight color of the tag.
    highlight: typing.Optional[Literal["grey", "pink", "red", "orange", "yellow", "green", "light-blue", "blue", "purple"]] = Field(None, alias='highlight')

    # ID of the parent of this tag. Set to `null` to remove  the parent tag.
    parent_tag_id: typing.Optional[str] = Field(None, alias='parent_tag_id')

    # Whether the tag is visible in conversation lists.
    is_visible_in_conversation_lists: typing.Optional[bool] = Field(None, alias='is_visible_in_conversation_lists')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
