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


class KnowledgeBaseCategoryResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            
            
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
                                    knowledge_base = schemas.StrSchema
                                    parent_category = schemas.StrSchema
                                    articles = schemas.StrSchema
                                    __annotations__ = {
                                        "knowledge_base": knowledge_base,
                                        "parent_category": parent_category,
                                        "articles": articles,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["knowledge_base"]) -> MetaOapg.properties.knowledge_base: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["parent_category"]) -> MetaOapg.properties.parent_category: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["articles"]) -> MetaOapg.properties.articles: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["knowledge_base", "parent_category", "articles", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["knowledge_base"]) -> typing.Union[MetaOapg.properties.knowledge_base, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["parent_category"]) -> typing.Union[MetaOapg.properties.parent_category, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["articles"]) -> typing.Union[MetaOapg.properties.articles, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["knowledge_base", "parent_category", "articles", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                knowledge_base: typing.Union[MetaOapg.properties.knowledge_base, str, schemas.Unset] = schemas.unset,
                                parent_category: typing.Union[MetaOapg.properties.parent_category, str, schemas.Unset] = schemas.unset,
                                articles: typing.Union[MetaOapg.properties.articles, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'related':
                                return super().__new__(
                                    cls,
                                    *args,
                                    knowledge_base=knowledge_base,
                                    parent_category=parent_category,
                                    articles=articles,
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
            is_hidden = schemas.BoolSchema
            
            
            class locale(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "fr": "FR",
                        "en": "EN",
                    }
                
                @schemas.classproperty
                def FR(cls):
                    return cls("fr")
                
                @schemas.classproperty
                def EN(cls):
                    return cls("en")
            created_at = schemas.NumberSchema
            updated_at = schemas.NumberSchema
            __annotations__ = {
                "description": description,
                "_links": _links,
                "id": id,
                "name": name,
                "is_hidden": is_hidden,
                "locale": locale,
                "created_at": created_at,
                "updated_at": updated_at,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_hidden"]) -> MetaOapg.properties.is_hidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "_links", "id", "name", "is_hidden", "locale", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_hidden"]) -> typing.Union[MetaOapg.properties.is_hidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> typing.Union[MetaOapg.properties.locale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "_links", "id", "name", "is_hidden", "locale", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        is_hidden: typing.Union[MetaOapg.properties.is_hidden, bool, schemas.Unset] = schemas.unset,
        locale: typing.Union[MetaOapg.properties.locale, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'KnowledgeBaseCategoryResponse':
        return super().__new__(
            cls,
            *args,
            description=description,
            _links=_links,
            id=id,
            name=name,
            is_hidden=is_hidden,
            locale=locale,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )