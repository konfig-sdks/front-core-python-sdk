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


class RequiredUpdateMessageTemplateFolder(TypedDict):
    pass

class OptionalUpdateMessageTemplateFolder(TypedDict, total=False):
    # Name of the message template folder
    name: str

    # ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.
    parent_folder_id: str

class UpdateMessageTemplateFolder(RequiredUpdateMessageTemplateFolder, OptionalUpdateMessageTemplateFolder):
    pass
