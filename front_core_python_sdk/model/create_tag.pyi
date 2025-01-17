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


class CreateTag(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A tag is a label that can be used to classify conversations.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class highlight(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GREY(cls):
                    return cls("grey")
                
                @schemas.classproperty
                def PINK(cls):
                    return cls("pink")
                
                @schemas.classproperty
                def RED(cls):
                    return cls("red")
                
                @schemas.classproperty
                def ORANGE(cls):
                    return cls("orange")
                
                @schemas.classproperty
                def YELLOW(cls):
                    return cls("yellow")
                
                @schemas.classproperty
                def GREEN(cls):
                    return cls("green")
                
                @schemas.classproperty
                def LIGHTBLUE(cls):
                    return cls("light-blue")
                
                @schemas.classproperty
                def BLUE(cls):
                    return cls("blue")
                
                @schemas.classproperty
                def PURPLE(cls):
                    return cls("purple")
            is_visible_in_conversation_lists = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "description": description,
                "highlight": highlight,
                "is_visible_in_conversation_lists": is_visible_in_conversation_lists,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["highlight"]) -> MetaOapg.properties.highlight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_visible_in_conversation_lists"]) -> MetaOapg.properties.is_visible_in_conversation_lists: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "highlight", "is_visible_in_conversation_lists", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["highlight"]) -> typing.Union[MetaOapg.properties.highlight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_visible_in_conversation_lists"]) -> typing.Union[MetaOapg.properties.is_visible_in_conversation_lists, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "highlight", "is_visible_in_conversation_lists", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        highlight: typing.Union[MetaOapg.properties.highlight, str, schemas.Unset] = schemas.unset,
        is_visible_in_conversation_lists: typing.Union[MetaOapg.properties.is_visible_in_conversation_lists, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTag':
        return super().__new__(
            cls,
            *args,
            name=name,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
            _configuration=_configuration,
            **kwargs,
        )
