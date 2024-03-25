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

from front_core_python_sdk.type.link_response_links import LinkResponseLinks

class RequiredLinkResponse(TypedDict):
    pass

class OptionalLinkResponse(TypedDict, total=False):
    _links: LinkResponseLinks

    # Unique identifier of the link
    id: str

    # Display name of the link
    name: str

    # Type of the link. Typically associated with the underlying link provider (if known)
    type: str

    # Underlying identifying external URL of the link
    external_url: str

    # Custom field attributes for this link
    custom_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class LinkResponse(RequiredLinkResponse, OptionalLinkResponse):
    pass
