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

from front_core_python_sdk.pydantic.inbox_response import InboxResponse
from front_core_python_sdk.pydantic.teammate_response import TeammateResponse

class TeamResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the team
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the team
    name: typing.Optional[str] = Field(None, alias='name')

    # List of the inboxes in the team
    inboxes: typing.Optional[typing.List[InboxResponse]] = Field(None, alias='inboxes')

    # List of the teammates that have access to the team
    members: typing.Optional[typing.List[TeammateResponse]] = Field(None, alias='members')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
