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


class Attachment(BaseModel):
    # The unique identifier of the attachment.
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the attached file
    filename: typing.Optional[str] = Field(None, alias='filename')

    # URL to download the attached file
    url: typing.Optional[str] = Field(None, alias='url')

    # Content type of the attached file in [MIME format](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types). Note that some attachments types may not be supported.
    content_type: typing.Optional[str] = Field(None, alias='content_type')

    # Size (in byte) of the attached file
    size: typing.Optional[int] = Field(None, alias='size')

    # Attachment metadata
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
