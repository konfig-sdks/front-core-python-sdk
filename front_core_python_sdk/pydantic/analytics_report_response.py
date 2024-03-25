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

from front_core_python_sdk.pydantic.analytics_scalar import AnalyticsScalar

class AnalyticsReportResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='_links')

    # Status of the report.
    status: typing.Optional[Literal["running", "done", "failed"]] = Field(None, alias='status')

    # Number ranging from 0 to 100 corresponding to the percentage of the analytics processed.
    progress: typing.Optional[int] = Field(None, alias='progress')

    # The metrics computed for the report.
    metrics: typing.Optional[typing.List[AnalyticsScalar]] = Field(None, alias='metrics')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
