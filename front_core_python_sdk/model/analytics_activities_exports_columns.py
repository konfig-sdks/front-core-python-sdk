# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from front_core_python_sdk import schemas  # noqa: F401


class AnalyticsActivitiesExportsColumns(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "columns",
            "start",
            "end",
            "type",
        }
        
        class properties:
            
            
            class columns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AnalyticsActivitiesColumns']:
                        return AnalyticsActivitiesColumns
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AnalyticsActivitiesColumns'], typing.List['AnalyticsActivitiesColumns']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columns':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AnalyticsActivitiesColumns':
                    return super().__getitem__(i)
            __annotations__ = {
                "columns": columns,
            }
    
    columns: MetaOapg.properties.columns
    start: schemas.AnyTypeSchema
    end: schemas.AnyTypeSchema
    type: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["columns", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columns", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        columns: typing.Union[MetaOapg.properties.columns, list, tuple, ],
        start: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        end: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        type: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AnalyticsActivitiesExportsColumns':
        return super().__new__(
            cls,
            *args,
            columns=columns,
            start=start,
            end=end,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from front_core_python_sdk.model.analytics_activities_columns import AnalyticsActivitiesColumns
