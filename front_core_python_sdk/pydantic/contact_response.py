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

from front_core_python_sdk.pydantic.contact_group_responses import ContactGroupResponses
from front_core_python_sdk.pydantic.contact_handle import ContactHandle

class ContactResponse(BaseModel):
    # Contact description
    description: typing.Optional[str] = Field(None, alias='description')

    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier of the contact
    id: typing.Optional[str] = Field(None, alias='id')

    # Contact name
    name: typing.Optional[str] = Field(None, alias='name')

    # URL of the contact's avatar
    avatar_url: typing.Optional[str] = Field(None, alias='avatar_url')

    # Whether or not the contact is marked as a spammer
    is_spammer: typing.Optional[bool] = Field(None, alias='is_spammer')

    # List of all the links of the contact
    links: typing.Optional[typing.List[str]] = Field(None, alias='links')

    # List of the groups the contact belongs to.
    groups: typing.Optional[typing.List[ContactGroupResponses]] = Field(None, alias='groups')

    # List of the handles and sources with which the contact is reachable.
    handles: typing.Optional[typing.List[ContactHandle]] = Field(None, alias='handles')

    # Custom field attributes for this contact.
    custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='custom_fields')

    # Whether or not the contact is individual
    is_private: typing.Optional[bool] = Field(None, alias='is_private')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
