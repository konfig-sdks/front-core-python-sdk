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


class RequiredAccountResponse(TypedDict):
    pass

class OptionalAccountResponse(TypedDict, total=False):
    # Account Description
    description: str

    _links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the account
    id: str

    # Account name
    name: str

    # URL of the Account's logo
    logo_url: str

    # List of domains associated to the Account
    domains: typing.List[str]

    # ID of the Account in an External system, such as your backoffice system or CRM
    external_id: str

    # Custom Attributes for this account
    custom_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Timestamp when the account was created
    created_at: typing.Union[int, float]

    # Timestamp when the account was updated
    updated_at: typing.Union[int, float]

class AccountResponse(RequiredAccountResponse, OptionalAccountResponse):
    pass
