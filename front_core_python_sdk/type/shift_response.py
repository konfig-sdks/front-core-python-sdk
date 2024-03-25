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

from front_core_python_sdk.type.shift_intervals import ShiftIntervals
from front_core_python_sdk.type.shift_response_links import ShiftResponseLinks

class RequiredShiftResponse(TypedDict):
    pass

class OptionalShiftResponse(TypedDict, total=False):
    _links: ShiftResponseLinks

    # Unique identifier of the shift
    id: str

    # Name of the shift
    name: str

    # Color of the shift
    color: str

    # A timezone name as defined in the IANA tz database
    timezone: str

    times: ShiftIntervals

    # The timestamp when the shift was created.
    created_at: typing.Union[int, float]

    # The timestamp when the shift was updated.
    updated_at: typing.Union[int, float]

class ShiftResponse(RequiredShiftResponse, OptionalShiftResponse):
    pass