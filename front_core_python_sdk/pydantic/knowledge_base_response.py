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


class KnowledgeBaseResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the knowledge base
    id: typing.Optional[str] = Field(None, alias='id')

    # Knowledge base name
    name: typing.Optional[str] = Field(None, alias='name')

    # Status of the KB
    status: typing.Optional[Literal["published", "unpublished"]] = Field(None, alias='status')

    # Type of the KB
    type: typing.Optional[Literal["internal", "external"]] = Field(None, alias='type')

    # Locale of this requested KB
    locale: typing.Optional[Literal["fr", "en"]] = Field(None, alias='locale')

    # Timestamp when the knowledge base was created
    created_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='created_at')

    # Timestamp when the knowledge base was updated
    updated_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='updated_at')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
