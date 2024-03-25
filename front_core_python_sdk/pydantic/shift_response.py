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

from front_core_python_sdk.pydantic.shift_intervals import ShiftIntervals
from front_core_python_sdk.pydantic.shift_response_links import ShiftResponseLinks

class ShiftResponse(BaseModel):
    _links: typing.Optional[ShiftResponseLinks] = Field(None, alias='_links')

    # Unique identifier of the shift
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the shift
    name: typing.Optional[str] = Field(None, alias='name')

    # Color of the shift
    color: typing.Optional[Literal["black", "grey", "pink", "purple", "blue", "teal", "green", "yellow", "orange", "red"]] = Field(None, alias='color')

    # A timezone name as defined in the IANA tz database
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    times: typing.Optional[ShiftIntervals] = Field(None, alias='times')

    # The timestamp when the shift was created.
    created_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='created_at')

    # The timestamp when the shift was updated.
    updated_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='updated_at')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
