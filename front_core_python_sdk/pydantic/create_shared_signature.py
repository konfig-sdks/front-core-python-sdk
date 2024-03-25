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

from front_core_python_sdk.pydantic.create_shared_signature_channel_ids import CreateSharedSignatureChannelIds

class CreateSharedSignature(BaseModel):
    # Name of the signature
    name: str = Field(alias='name')

    # Body of the signature
    body: str = Field(alias='body')

    # Sender info of the signature that will appear in the From line of emails sent.
    sender_info: typing.Optional[str] = Field(None, alias='sender_info')

    # Whether or not the signature is visible in all individual channels for teammates in the given team.
    is_visible_for_all_teammate_channels: typing.Optional[bool] = Field(None, alias='is_visible_for_all_teammate_channels')

    # If true, the signature will be set as the default signature for the team.
    is_default: typing.Optional[bool] = Field(None, alias='is_default')

    channel_ids: typing.Optional[CreateSharedSignatureChannelIds] = Field(None, alias='channel_ids')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
