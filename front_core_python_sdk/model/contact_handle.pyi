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


class ContactHandle(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "handle",
            "source",
        }
        
        class properties:
            handle = schemas.StrSchema
            
            
            class source(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TWITTER(cls):
                    return cls("twitter")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("email")
                
                @schemas.classproperty
                def PHONE(cls):
                    return cls("phone")
                
                @schemas.classproperty
                def FACEBOOK(cls):
                    return cls("facebook")
                
                @schemas.classproperty
                def INTERCOM(cls):
                    return cls("intercom")
                
                @schemas.classproperty
                def FRONT_CHAT(cls):
                    return cls("front_chat")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
            __annotations__ = {
                "handle": handle,
                "source": source,
            }
    
    handle: MetaOapg.properties.handle
    source: MetaOapg.properties.source
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["handle", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["handle", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        handle: typing.Union[MetaOapg.properties.handle, str, ],
        source: typing.Union[MetaOapg.properties.source, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactHandle':
        return super().__new__(
            cls,
            *args,
            handle=handle,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )
