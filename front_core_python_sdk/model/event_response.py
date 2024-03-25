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


class EventResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An event is created everytime something interesting is happening in Front.
    """


    class MetaOapg:
        
        class properties:
            
            
            class _links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        _self = schemas.StrSchema
                        __annotations__ = {
                            "self": _self,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["self", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["self", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_links':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "assign": "ASSIGN",
                        "unassign": "UNASSIGN",
                        "archive": "ARCHIVE",
                        "reopen": "REOPEN",
                        "trash": "TRASH",
                        "restore": "RESTORE",
                        "reminder": "REMINDER",
                        "comment": "COMMENT",
                        "mention": "MENTION",
                        "inbound": "INBOUND",
                        "outbound": "OUTBOUND",
                        "outbound_reply": "OUTBOUND_REPLY",
                        "move": "MOVE",
                        "forward": "FORWARD",
                        "tag": "TAG",
                        "untag": "UNTAG",
                        "sending_error": "SENDING_ERROR",
                        "message_bounce_error": "MESSAGE_BOUNCE_ERROR",
                        "conversations_merged": "CONVERSATIONS_MERGED",
                        "link_added": "LINK_ADDED",
                        "link_removed": "LINK_REMOVED",
                        "custom_field_updated": "CUSTOM_FIELD_UPDATED",
                    }
                
                @schemas.classproperty
                def ASSIGN(cls):
                    return cls("assign")
                
                @schemas.classproperty
                def UNASSIGN(cls):
                    return cls("unassign")
                
                @schemas.classproperty
                def ARCHIVE(cls):
                    return cls("archive")
                
                @schemas.classproperty
                def REOPEN(cls):
                    return cls("reopen")
                
                @schemas.classproperty
                def TRASH(cls):
                    return cls("trash")
                
                @schemas.classproperty
                def RESTORE(cls):
                    return cls("restore")
                
                @schemas.classproperty
                def REMINDER(cls):
                    return cls("reminder")
                
                @schemas.classproperty
                def COMMENT(cls):
                    return cls("comment")
                
                @schemas.classproperty
                def MENTION(cls):
                    return cls("mention")
                
                @schemas.classproperty
                def INBOUND(cls):
                    return cls("inbound")
                
                @schemas.classproperty
                def OUTBOUND(cls):
                    return cls("outbound")
                
                @schemas.classproperty
                def OUTBOUND_REPLY(cls):
                    return cls("outbound_reply")
                
                @schemas.classproperty
                def MOVE(cls):
                    return cls("move")
                
                @schemas.classproperty
                def FORWARD(cls):
                    return cls("forward")
                
                @schemas.classproperty
                def TAG(cls):
                    return cls("tag")
                
                @schemas.classproperty
                def UNTAG(cls):
                    return cls("untag")
                
                @schemas.classproperty
                def SENDING_ERROR(cls):
                    return cls("sending_error")
                
                @schemas.classproperty
                def MESSAGE_BOUNCE_ERROR(cls):
                    return cls("message_bounce_error")
                
                @schemas.classproperty
                def CONVERSATIONS_MERGED(cls):
                    return cls("conversations_merged")
                
                @schemas.classproperty
                def LINK_ADDED(cls):
                    return cls("link_added")
                
                @schemas.classproperty
                def LINK_REMOVED(cls):
                    return cls("link_removed")
                
                @schemas.classproperty
                def CUSTOM_FIELD_UPDATED(cls):
                    return cls("custom_field_updated")
            emitted_at = schemas.NumberSchema
            
            
            class source(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class _meta(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class type(
                                        schemas.EnumBase,
                                        schemas.StrSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            enum_value_to_name = {
                                                "api": "API",
                                                "oauth_client": "OAUTH_CLIENT",
                                                "rule": "RULE",
                                                "teammate": "TEAMMATE",
                                                "imap": "IMAP",
                                                "gmail": "GMAIL",
                                                "reminder": "REMINDER",
                                                "inboxes": "INBOXES",
                                                "recipient": "RECIPIENT",
                                            }
                                        
                                        @schemas.classproperty
                                        def API(cls):
                                            return cls("api")
                                        
                                        @schemas.classproperty
                                        def OAUTH_CLIENT(cls):
                                            return cls("oauth_client")
                                        
                                        @schemas.classproperty
                                        def RULE(cls):
                                            return cls("rule")
                                        
                                        @schemas.classproperty
                                        def TEAMMATE(cls):
                                            return cls("teammate")
                                        
                                        @schemas.classproperty
                                        def IMAP(cls):
                                            return cls("imap")
                                        
                                        @schemas.classproperty
                                        def GMAIL(cls):
                                            return cls("gmail")
                                        
                                        @schemas.classproperty
                                        def REMINDER(cls):
                                            return cls("reminder")
                                        
                                        @schemas.classproperty
                                        def INBOXES(cls):
                                            return cls("inboxes")
                                        
                                        @schemas.classproperty
                                        def RECIPIENT(cls):
                                            return cls("recipient")
                                    __annotations__ = {
                                        "type": type,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> '_meta':
                                return super().__new__(
                                    cls,
                                    *args,
                                    type=type,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class data(
                            schemas.ComposedSchema,
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class one_of_2(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['InboxResponse']:
                                            return InboxResponse
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple['InboxResponse'], typing.List['InboxResponse']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'one_of_2':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'InboxResponse':
                                        return super().__getitem__(i)
                                
                                @classmethod
                                @functools.lru_cache()
                                def one_of(cls):
                                    # we need this here to make our import statements work
                                    # we must store _composed_schemas in here so the code is only run
                                    # when we invoke this method. If we kept this at the class
                                    # level we would get an error because the class level
                                    # code would be run when this module is imported, and these composed
                                    # classes don't exist yet because their module has not finished
                                    # loading
                                    return [
                                        RuleResponse,
                                        TeammateResponse,
                                        cls.one_of_2,
                                    ]
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'data':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "_meta": _meta,
                            "data": data,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["_meta"]) -> MetaOapg.properties._meta: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["_meta", "data", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["_meta"]) -> typing.Union[MetaOapg.properties._meta, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_meta", "data", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _meta: typing.Union[MetaOapg.properties._meta, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'source':
                    return super().__new__(
                        cls,
                        *args,
                        _meta=_meta,
                        data=data,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class target(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class _meta(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class type(
                                        schemas.EnumBase,
                                        schemas.StrSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            enum_value_to_name = {
                                                "teammate": "TEAMMATE",
                                                "inboxes": "INBOXES",
                                                "message": "MESSAGE",
                                                "comment": "COMMENT",
                                                "tag": "TAG",
                                                "deleted_conversation_ids": "DELETED_CONVERSATION_IDS",
                                                "link": "LINK",
                                                "custom_field": "CUSTOM_FIELD",
                                            }
                                        
                                        @schemas.classproperty
                                        def TEAMMATE(cls):
                                            return cls("teammate")
                                        
                                        @schemas.classproperty
                                        def INBOXES(cls):
                                            return cls("inboxes")
                                        
                                        @schemas.classproperty
                                        def MESSAGE(cls):
                                            return cls("message")
                                        
                                        @schemas.classproperty
                                        def COMMENT(cls):
                                            return cls("comment")
                                        
                                        @schemas.classproperty
                                        def TAG(cls):
                                            return cls("tag")
                                        
                                        @schemas.classproperty
                                        def DELETED_CONVERSATION_IDS(cls):
                                            return cls("deleted_conversation_ids")
                                        
                                        @schemas.classproperty
                                        def LINK(cls):
                                            return cls("link")
                                        
                                        @schemas.classproperty
                                        def CUSTOM_FIELD(cls):
                                            return cls("custom_field")
                                    __annotations__ = {
                                        "type": type,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> '_meta':
                                return super().__new__(
                                    cls,
                                    *args,
                                    type=type,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class data(
                            schemas.ComposedSchema,
                        ):
                        
                        
                            class MetaOapg:
                                
                                @classmethod
                                @functools.lru_cache()
                                def one_of(cls):
                                    # we need this here to make our import statements work
                                    # we must store _composed_schemas in here so the code is only run
                                    # when we invoke this method. If we kept this at the class
                                    # level we would get an error because the class level
                                    # code would be run when this module is imported, and these composed
                                    # classes don't exist yet because their module has not finished
                                    # loading
                                    return [
                                        TeammateResponse,
                                        InboxResponse,
                                        TagResponse,
                                        CommentResponse,
                                        MessageResponse,
                                        LinkResponse,
                                    ]
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'data':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "_meta": _meta,
                            "data": data,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["_meta"]) -> MetaOapg.properties._meta: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["_meta", "data", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["_meta"]) -> typing.Union[MetaOapg.properties._meta, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_meta", "data", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _meta: typing.Union[MetaOapg.properties._meta, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'target':
                    return super().__new__(
                        cls,
                        *args,
                        _meta=_meta,
                        data=data,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def conversation() -> typing.Type['ConversationResponse']:
                return ConversationResponse
            __annotations__ = {
                "_links": _links,
                "id": id,
                "type": type,
                "emitted_at": emitted_at,
                "source": source,
                "target": target,
                "conversation": conversation,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emitted_at"]) -> MetaOapg.properties.emitted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation"]) -> 'ConversationResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "id", "type", "emitted_at", "source", "target", "conversation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emitted_at"]) -> typing.Union[MetaOapg.properties.emitted_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> typing.Union[MetaOapg.properties.target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation"]) -> typing.Union['ConversationResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "id", "type", "emitted_at", "source", "target", "conversation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        emitted_at: typing.Union[MetaOapg.properties.emitted_at, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        target: typing.Union[MetaOapg.properties.target, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        conversation: typing.Union['ConversationResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventResponse':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            id=id,
            type=type,
            emitted_at=emitted_at,
            source=source,
            target=target,
            conversation=conversation,
            _configuration=_configuration,
            **kwargs,
        )

from front_core_python_sdk.model.comment_response import CommentResponse
from front_core_python_sdk.model.conversation_response import ConversationResponse
from front_core_python_sdk.model.inbox_response import InboxResponse
from front_core_python_sdk.model.link_response import LinkResponse
from front_core_python_sdk.model.message_response import MessageResponse
from front_core_python_sdk.model.rule_response import RuleResponse
from front_core_python_sdk.model.tag_response import TagResponse
from front_core_python_sdk.model.teammate_response import TeammateResponse