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


class RequiredAttachment(TypedDict):
    pass

class OptionalAttachment(TypedDict, total=False):
    # The unique identifier of the attachment.
    id: str

    # Name of the attached file
    filename: str

    # URL to download the attached file
    url: str

    # Content type of the attached file in [MIME format](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types). Note that some attachments types may not be supported.
    content_type: str

    # Size (in byte) of the attached file
    size: int

    # Attachment metadata
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Attachment(RequiredAttachment, OptionalAttachment):
    pass
