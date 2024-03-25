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


class RequiredSignatureResponse(TypedDict):
    pass

class OptionalSignatureResponse(TypedDict, total=False):
    _links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the signature
    id: str

    # Name of the signature
    name: str

    # Body of the signature
    body: str

    # Sender info of the signature
    sender_info: str

    # Whether or not the signature is available in teammate channels.
    is_visible_for_all_teammate_channels: bool

    # Whether the signature is the default signature for the team or teammate.
    is_default: bool

    # Whether the signature is private to the teammate.
    is_private: bool

    channel_ids: typing.List[str]

class SignatureResponse(RequiredSignatureResponse, OptionalSignatureResponse):
    pass
