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


class ImportMessage(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "metadata",
            "sender",
            "created_at",
            "external_id",
            "to",
            "body",
        }
        
        class properties:
            
            
            class sender(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "handle",
                    }
                    
                    class properties:
                        author_id = schemas.StrSchema
                        name = schemas.StrSchema
                        handle = schemas.StrSchema
                        __annotations__ = {
                            "author_id": author_id,
                            "name": name,
                            "handle": handle,
                        }
                
                handle: MetaOapg.properties.handle
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["author_id", "name", "handle", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["author_id"]) -> typing.Union[MetaOapg.properties.author_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["author_id", "name", "handle", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    handle: typing.Union[MetaOapg.properties.handle, str, ],
                    author_id: typing.Union[MetaOapg.properties.author_id, str, schemas.Unset] = schemas.unset,
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sender':
                    return super().__new__(
                        cls,
                        *args,
                        handle=handle,
                        author_id=author_id,
                        name=name,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class to(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'to':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            body = schemas.StrSchema
            external_id = schemas.StrSchema
            created_at = schemas.IntSchema
            
            
            class metadata(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "is_inbound",
                    }
                    
                    class properties:
                        thread_ref = schemas.StrSchema
                        is_inbound = schemas.BoolSchema
                        is_archived = schemas.BoolSchema
                        should_skip_rules = schemas.BoolSchema
                        __annotations__ = {
                            "thread_ref": thread_ref,
                            "is_inbound": is_inbound,
                            "is_archived": is_archived,
                            "should_skip_rules": should_skip_rules,
                        }
                
                is_inbound: MetaOapg.properties.is_inbound
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["thread_ref"]) -> MetaOapg.properties.thread_ref: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_inbound"]) -> MetaOapg.properties.is_inbound: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_archived"]) -> MetaOapg.properties.is_archived: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["should_skip_rules"]) -> MetaOapg.properties.should_skip_rules: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["thread_ref", "is_inbound", "is_archived", "should_skip_rules", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["thread_ref"]) -> typing.Union[MetaOapg.properties.thread_ref, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_inbound"]) -> MetaOapg.properties.is_inbound: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_archived"]) -> typing.Union[MetaOapg.properties.is_archived, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["should_skip_rules"]) -> typing.Union[MetaOapg.properties.should_skip_rules, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["thread_ref", "is_inbound", "is_archived", "should_skip_rules", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    is_inbound: typing.Union[MetaOapg.properties.is_inbound, bool, ],
                    thread_ref: typing.Union[MetaOapg.properties.thread_ref, str, schemas.Unset] = schemas.unset,
                    is_archived: typing.Union[MetaOapg.properties.is_archived, bool, schemas.Unset] = schemas.unset,
                    should_skip_rules: typing.Union[MetaOapg.properties.should_skip_rules, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'metadata':
                    return super().__new__(
                        cls,
                        *args,
                        is_inbound=is_inbound,
                        thread_ref=thread_ref,
                        is_archived=is_archived,
                        should_skip_rules=should_skip_rules,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class cc(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cc':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class bcc(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bcc':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            subject = schemas.StrSchema
            
            
            class body_format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def HTML(cls):
                    return cls("html")
                
                @schemas.classproperty
                def MARKDOWN(cls):
                    return cls("markdown")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("email")
                
                @schemas.classproperty
                def SMS(cls):
                    return cls("sms")
                
                @schemas.classproperty
                def INTERCOM(cls):
                    return cls("intercom")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
            assignee_id = schemas.StrSchema
            conversation_id = schemas.StrSchema
            
            
            class attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.BinarySchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "sender": sender,
                "to": to,
                "body": body,
                "external_id": external_id,
                "created_at": created_at,
                "metadata": metadata,
                "tags": tags,
                "cc": cc,
                "bcc": bcc,
                "subject": subject,
                "body_format": body_format,
                "type": type,
                "assignee_id": assignee_id,
                "conversation_id": conversation_id,
                "attachments": attachments,
            }

    
    metadata: MetaOapg.properties.metadata
    sender: MetaOapg.properties.sender
    created_at: MetaOapg.properties.created_at
    external_id: MetaOapg.properties.external_id
    to: MetaOapg.properties.to
    body: MetaOapg.properties.body
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender"]) -> MetaOapg.properties.sender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cc"]) -> MetaOapg.properties.cc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcc"]) -> MetaOapg.properties.bcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_format"]) -> MetaOapg.properties.body_format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee_id"]) -> MetaOapg.properties.assignee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_id"]) -> MetaOapg.properties.conversation_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sender", "to", "body", "external_id", "created_at", "metadata", "tags", "cc", "bcc", "subject", "body_format", "type", "assignee_id", "conversation_id", "attachments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender"]) -> MetaOapg.properties.sender: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cc"]) -> typing.Union[MetaOapg.properties.cc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcc"]) -> typing.Union[MetaOapg.properties.bcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_format"]) -> typing.Union[MetaOapg.properties.body_format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee_id"]) -> typing.Union[MetaOapg.properties.assignee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_id"]) -> typing.Union[MetaOapg.properties.conversation_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sender", "to", "body", "external_id", "created_at", "metadata", "tags", "cc", "bcc", "subject", "body_format", "type", "assignee_id", "conversation_id", "attachments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, ],
        sender: typing.Union[MetaOapg.properties.sender, dict, frozendict.frozendict, ],
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, ],
        external_id: typing.Union[MetaOapg.properties.external_id, str, ],
        to: typing.Union[MetaOapg.properties.to, list, tuple, ],
        body: typing.Union[MetaOapg.properties.body, str, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        cc: typing.Union[MetaOapg.properties.cc, list, tuple, schemas.Unset] = schemas.unset,
        bcc: typing.Union[MetaOapg.properties.bcc, list, tuple, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        body_format: typing.Union[MetaOapg.properties.body_format, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        assignee_id: typing.Union[MetaOapg.properties.assignee_id, str, schemas.Unset] = schemas.unset,
        conversation_id: typing.Union[MetaOapg.properties.conversation_id, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportMessage':
        return super().__new__(
            cls,
            *args,
            metadata=metadata,
            sender=sender,
            created_at=created_at,
            external_id=external_id,
            to=to,
            body=body,
            tags=tags,
            cc=cc,
            bcc=bcc,
            subject=subject,
            body_format=body_format,
            type=type,
            assignee_id=assignee_id,
            conversation_id=conversation_id,
            attachments=attachments,
            _configuration=_configuration,
            **kwargs,
        )
