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


class SignatureResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class _links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        _self = schemas.StrSchema
                        
                        
                        class related(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    owner = schemas.StrSchema
                                    __annotations__ = {
                                        "owner": owner,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["owner", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["owner", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'related':
                                return super().__new__(
                                    cls,
                                    *args,
                                    owner=owner,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "self": _self,
                            "related": related,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["related"]) -> MetaOapg.properties.related: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["self", "related", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["related"]) -> typing.Union[MetaOapg.properties.related, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["self", "related", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    related: typing.Union[MetaOapg.properties.related, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_links':
                    return super().__new__(
                        cls,
                        *args,
                        related=related,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            name = schemas.StrSchema
            body = schemas.StrSchema
            sender_info = schemas.StrSchema
            is_visible_for_all_teammate_channels = schemas.BoolSchema
            is_default = schemas.BoolSchema
            is_private = schemas.BoolSchema
            
            
            class channel_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'channel_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "_links": _links,
                "id": id,
                "name": name,
                "body": body,
                "sender_info": sender_info,
                "is_visible_for_all_teammate_channels": is_visible_for_all_teammate_channels,
                "is_default": is_default,
                "is_private": is_private,
                "channel_ids": channel_ids,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_info"]) -> MetaOapg.properties.sender_info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_visible_for_all_teammate_channels"]) -> MetaOapg.properties.is_visible_for_all_teammate_channels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_default"]) -> MetaOapg.properties.is_default: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_private"]) -> MetaOapg.properties.is_private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_ids"]) -> MetaOapg.properties.channel_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "id", "name", "body", "sender_info", "is_visible_for_all_teammate_channels", "is_default", "is_private", "channel_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_info"]) -> typing.Union[MetaOapg.properties.sender_info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_visible_for_all_teammate_channels"]) -> typing.Union[MetaOapg.properties.is_visible_for_all_teammate_channels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_default"]) -> typing.Union[MetaOapg.properties.is_default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_private"]) -> typing.Union[MetaOapg.properties.is_private, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_ids"]) -> typing.Union[MetaOapg.properties.channel_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "id", "name", "body", "sender_info", "is_visible_for_all_teammate_channels", "is_default", "is_private", "channel_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        sender_info: typing.Union[MetaOapg.properties.sender_info, str, schemas.Unset] = schemas.unset,
        is_visible_for_all_teammate_channels: typing.Union[MetaOapg.properties.is_visible_for_all_teammate_channels, bool, schemas.Unset] = schemas.unset,
        is_default: typing.Union[MetaOapg.properties.is_default, bool, schemas.Unset] = schemas.unset,
        is_private: typing.Union[MetaOapg.properties.is_private, bool, schemas.Unset] = schemas.unset,
        channel_ids: typing.Union[MetaOapg.properties.channel_ids, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SignatureResponse':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            id=id,
            name=name,
            body=body,
            sender_info=sender_info,
            is_visible_for_all_teammate_channels=is_visible_for_all_teammate_channels,
            is_default=is_default,
            is_private=is_private,
            channel_ids=channel_ids,
            _configuration=_configuration,
            **kwargs,
        )
