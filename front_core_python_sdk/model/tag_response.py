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


class TagResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A tag is a label that can be used to classify conversations.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def _links() -> typing.Type['TagResponseLinks']:
                return TagResponseLinks
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class highlight(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "grey": "GREY",
                        "pink": "PINK",
                        "red": "RED",
                        "orange": "ORANGE",
                        "yellow": "YELLOW",
                        "green": "GREEN",
                        "light-blue": "LIGHTBLUE",
                        "blue": "BLUE",
                        "purple": "PURPLE",
                    }
                
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
            is_private = schemas.BoolSchema
            is_visible_in_conversation_lists = schemas.BoolSchema
            created_at = schemas.NumberSchema
            updated_at = schemas.NumberSchema
            __annotations__ = {
                "description": description,
                "_links": _links,
                "id": id,
                "name": name,
                "highlight": highlight,
                "is_private": is_private,
                "is_visible_in_conversation_lists": is_visible_in_conversation_lists,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'TagResponseLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["highlight"]) -> MetaOapg.properties.highlight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_private"]) -> MetaOapg.properties.is_private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_visible_in_conversation_lists"]) -> MetaOapg.properties.is_visible_in_conversation_lists: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "_links", "id", "name", "highlight", "is_private", "is_visible_in_conversation_lists", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['TagResponseLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["highlight"]) -> typing.Union[MetaOapg.properties.highlight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_private"]) -> typing.Union[MetaOapg.properties.is_private, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_visible_in_conversation_lists"]) -> typing.Union[MetaOapg.properties.is_visible_in_conversation_lists, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "_links", "id", "name", "highlight", "is_private", "is_visible_in_conversation_lists", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _links: typing.Union['TagResponseLinks', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        highlight: typing.Union[MetaOapg.properties.highlight, str, schemas.Unset] = schemas.unset,
        is_private: typing.Union[MetaOapg.properties.is_private, bool, schemas.Unset] = schemas.unset,
        is_visible_in_conversation_lists: typing.Union[MetaOapg.properties.is_visible_in_conversation_lists, bool, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TagResponse':
        return super().__new__(
            cls,
            *args,
            description=description,
            _links=_links,
            id=id,
            name=name,
            highlight=highlight,
            is_private=is_private,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from front_core_python_sdk.model.tag_response_links import TagResponseLinks
