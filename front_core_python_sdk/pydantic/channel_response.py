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


class ChannelResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Unique identifier for the channel
    id: typing.Optional[str] = Field(None, alias='id')

    # The name of the channel
    name: typing.Optional[str] = Field(None, alias='name')

    # Address receiving the messages
    address: typing.Optional[str] = Field(None, alias='address')

    # Type of the channel
    types: typing.Optional[Literal["custom", "facebook", "gmail", "google_play", "imap", "intercom", "form", "office365", "layer_anon", "smooch", "smtp", "talkdesk", "truly", "twilio", "twilio_whatsapp", "twitter", "twitter_dm", "yalo_wha", "front_chat", "front_mail"]] = Field(None, alias='types')

    # Address which appears as the sender for messages sent from Front
    send_as: typing.Optional[str] = Field(None, alias='send_as')

    # Channel settings
    settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='settings')

    # Whether or not the channel is individual
    is_private: typing.Optional[bool] = Field(None, alias='is_private')

    # Whether or not the channel configuration is valid
    is_valid: typing.Optional[bool] = Field(None, alias='is_valid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
