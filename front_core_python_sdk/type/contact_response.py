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

from front_core_python_sdk.type.contact_group_responses import ContactGroupResponses
from front_core_python_sdk.type.contact_handle import ContactHandle

class RequiredContactResponse(TypedDict):
    pass

class OptionalContactResponse(TypedDict, total=False):
    # Contact description
    description: str

    _links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the contact
    id: str

    # Contact name
    name: str

    # URL of the contact's avatar
    avatar_url: str

    # Whether or not the contact is marked as a spammer
    is_spammer: bool

    # List of all the links of the contact
    links: typing.List[str]

    # List of the groups the contact belongs to.
    groups: typing.List[ContactGroupResponses]

    # List of the handles and sources with which the contact is reachable.
    handles: typing.List[ContactHandle]

    # Custom field attributes for this contact.
    custom_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Whether or not the contact is individual
    is_private: bool

class ContactResponse(RequiredContactResponse, OptionalContactResponse):
    pass
