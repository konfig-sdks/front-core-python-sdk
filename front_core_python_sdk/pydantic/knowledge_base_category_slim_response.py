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


class KnowledgeBaseCategorySlimResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the knowledge base category
    id: typing.Optional[str] = Field(None, alias='id')

    # Is the category hidden from navigation and breadcrumbs (topics are accessed as direct links)
    is_hidden: typing.Optional[bool] = Field(None, alias='is_hidden')

    # List of the locales the category supports
    locales: typing.Optional[typing.List[str]] = Field(None, alias='locales')

    # Timestamp when the category was created
    created_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='created_at')

    # Timestamp when the category was updated
    updated_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='updated_at')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
