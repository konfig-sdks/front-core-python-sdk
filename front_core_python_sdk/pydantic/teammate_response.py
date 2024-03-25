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


class TeammateResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the teammate
    id: typing.Optional[str] = Field(None, alias='id')

    # Email address of the teammate
    email: typing.Optional[str] = Field(None, alias='email')

    # Username of the teammate (used for \"@\" mentions)
    username: typing.Optional[str] = Field(None, alias='username')

    # First name of the teammate
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # Last name of the teammate
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # Whether or not the teammate is an admin in your company
    is_admin: typing.Optional[bool] = Field(None, alias='is_admin')

    # Whether or not the teammate is available
    is_available: typing.Optional[bool] = Field(None, alias='is_available')

    # Whether or not the teammate account has been blocked
    is_blocked: typing.Optional[bool] = Field(None, alias='is_blocked')

    # Custom field attributes for this teammate
    custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='custom_fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
