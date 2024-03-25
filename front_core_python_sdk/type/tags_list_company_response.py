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

from front_core_python_sdk.type.tag_response import TagResponse
from front_core_python_sdk.type.tags_list_company_response_links import TagsListCompanyResponseLinks

class RequiredTagsListCompanyResponse(TypedDict):
    pass

class OptionalTagsListCompanyResponse(TypedDict, total=False):
    _links: TagsListCompanyResponseLinks

    _results: typing.List[TagResponse]

class TagsListCompanyResponse(RequiredTagsListCompanyResponse, OptionalTagsListCompanyResponse):
    pass
