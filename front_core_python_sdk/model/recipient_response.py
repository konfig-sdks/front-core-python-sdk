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


class RecipientResponse(
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
                        
                        
                        class related(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    contact = schemas.StrSchema
                                    __annotations__ = {
                                        "contact": contact,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["contact"]) -> MetaOapg.properties.contact: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["contact", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> typing.Union[MetaOapg.properties.contact, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contact", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                contact: typing.Union[MetaOapg.properties.contact, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'related':
                                return super().__new__(
                                    cls,
                                    *args,
                                    contact=contact,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "related": related,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["related"]) -> MetaOapg.properties.related: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["related", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["related"]) -> typing.Union[MetaOapg.properties.related, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["related", ], str]):
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
            name = schemas.StrSchema
            handle = schemas.StrSchema
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "from": "FROM",
                        "to": "TO",
                        "cc": "CC",
                        "bcc": "BCC",
                    }
                
                @schemas.classproperty
                def FROM(cls):
                    return cls("from")
                
                @schemas.classproperty
                def TO(cls):
                    return cls("to")
                
                @schemas.classproperty
                def CC(cls):
                    return cls("cc")
                
                @schemas.classproperty
                def BCC(cls):
                    return cls("bcc")
            __annotations__ = {
                "_links": _links,
                "name": name,
                "handle": handle,
                "role": role,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "name", "handle", "role", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> typing.Union[MetaOapg.properties.handle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "name", "handle", "role", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        handle: typing.Union[MetaOapg.properties.handle, str, schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecipientResponse':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            name=name,
            handle=handle,
            role=role,
            _configuration=_configuration,
            **kwargs,
        )
