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


class RequiredUpdateTeammate(TypedDict):
    pass

class OptionalUpdateTeammate(TypedDict, total=False):
    # New username. It must be unique and can only contains lowercase letters, numbers and underscores.
    username: str

    # New first name
    first_name: str

    # New last name
    last_name: str

    # New availability status
    is_available: bool

    # Custom field attributes for this teammate. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.
    custom_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class UpdateTeammate(RequiredUpdateTeammate, OptionalUpdateTeammate):
    pass
