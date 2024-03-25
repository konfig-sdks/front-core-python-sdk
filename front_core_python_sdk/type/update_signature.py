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

from front_core_python_sdk.type.update_signature_channel_ids import UpdateSignatureChannelIds

class RequiredUpdateSignature(TypedDict):
    pass

class OptionalUpdateSignature(TypedDict, total=False):
    # Name of the signature
    name: str

    # Sender info of the signature that will appear in the From line of emails sent.
    sender_info: str

    # Body of the signature
    body: str

    # Whether or not the signature is visible in all individual channels for teammates in the given team. Can only be set for shared signatures.
    is_visible_for_all_teammate_channels: bool

    # If true, the signature will be set as the default signature for the team or teammate.
    is_default: bool

    channel_ids: UpdateSignatureChannelIds

class UpdateSignature(RequiredUpdateSignature, OptionalUpdateSignature):
    pass
