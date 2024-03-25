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

from front_core_python_sdk.pydantic.analytics_activities_exports_columns import AnalyticsActivitiesExportsColumns
from front_core_python_sdk.pydantic.analytics_filters import AnalyticsFilters
from front_core_python_sdk.pydantic.analytics_messages_export_columns import AnalyticsMessagesExportColumns

class AnalyticsExportRequest(BaseModel):
    # The type of export to create. The type you specify determines which columns are available for the export.
    type: typing.Optional[Literal["messages", "events"]] = Field(None, alias='type')

    # Start time of the data to include in the export (seconds since 1970-01-01T00:00:00+00). Will be rounded down to the start of the day.
    start: typing.Optional[typing.Union[int, float]] = Field(None, alias='start')

    # End time of the data to include in the export (seconds since 1970-01-01T00:00:00+00). Will be rounded up to the end of the day.
    end: typing.Optional[typing.Union[int, float]] = Field(None, alias='end')

    # [IANA name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the timezone to format the dates with. If omitted, the export will use Etc/UTC.
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    filters: typing.Optional[AnalyticsFilters] = Field(None, alias='filters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
AnalyticsExportRequest = typing.Union[AnalyticsMessagesExportColumns,AnalyticsActivitiesExportsColumns]
