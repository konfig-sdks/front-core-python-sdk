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


class ConversationsRemoveFollowersRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "teammate_ids",
        }
        
        class properties:
        
            @staticmethod
            def teammate_ids() -> typing.Type['ConversationsRemoveFollowersRequestTeammateIds']:
                return ConversationsRemoveFollowersRequestTeammateIds
            __annotations__ = {
                "teammate_ids": teammate_ids,
            }
    
    teammate_ids: 'ConversationsRemoveFollowersRequestTeammateIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teammate_ids"]) -> 'ConversationsRemoveFollowersRequestTeammateIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["teammate_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teammate_ids"]) -> 'ConversationsRemoveFollowersRequestTeammateIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["teammate_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        teammate_ids: 'ConversationsRemoveFollowersRequestTeammateIds',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConversationsRemoveFollowersRequest':
        return super().__new__(
            cls,
            *args,
            teammate_ids=teammate_ids,
            _configuration=_configuration,
            **kwargs,
        )

from front_core_python_sdk.model.conversations_remove_followers_request_teammate_ids import ConversationsRemoveFollowersRequestTeammateIds