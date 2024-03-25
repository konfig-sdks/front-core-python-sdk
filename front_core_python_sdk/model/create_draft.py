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


class CreateDraft(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "author_id",
            "body",
        }
        
        class properties:
            author_id = schemas.StrSchema
            body = schemas.StrSchema
            
            
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
            quote_body = schemas.StrSchema
            
            
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
            
            
            class mode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "private": "PRIVATE",
                        "shared": "SHARED",
                    }
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
                
                @schemas.classproperty
                def SHARED(cls):
                    return cls("shared")
            signature_id = schemas.StrSchema
            should_add_default_signature = schemas.BoolSchema
            __annotations__ = {
                "author_id": author_id,
                "body": body,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "subject": subject,
                "quote_body": quote_body,
                "attachments": attachments,
                "mode": mode,
                "signature_id": signature_id,
                "should_add_default_signature": should_add_default_signature,
            }

    
    author_id: MetaOapg.properties.author_id
    body: MetaOapg.properties.body
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cc"]) -> MetaOapg.properties.cc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcc"]) -> MetaOapg.properties.bcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quote_body"]) -> MetaOapg.properties.quote_body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature_id"]) -> MetaOapg.properties.signature_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["should_add_default_signature"]) -> MetaOapg.properties.should_add_default_signature: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["author_id", "body", "to", "cc", "bcc", "subject", "quote_body", "attachments", "mode", "signature_id", "should_add_default_signature", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cc"]) -> typing.Union[MetaOapg.properties.cc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcc"]) -> typing.Union[MetaOapg.properties.bcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quote_body"]) -> typing.Union[MetaOapg.properties.quote_body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature_id"]) -> typing.Union[MetaOapg.properties.signature_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["should_add_default_signature"]) -> typing.Union[MetaOapg.properties.should_add_default_signature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["author_id", "body", "to", "cc", "bcc", "subject", "quote_body", "attachments", "mode", "signature_id", "should_add_default_signature", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        author_id: typing.Union[MetaOapg.properties.author_id, str, ],
        body: typing.Union[MetaOapg.properties.body, str, ],
        to: typing.Union[MetaOapg.properties.to, list, tuple, schemas.Unset] = schemas.unset,
        cc: typing.Union[MetaOapg.properties.cc, list, tuple, schemas.Unset] = schemas.unset,
        bcc: typing.Union[MetaOapg.properties.bcc, list, tuple, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        quote_body: typing.Union[MetaOapg.properties.quote_body, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        mode: typing.Union[MetaOapg.properties.mode, str, schemas.Unset] = schemas.unset,
        signature_id: typing.Union[MetaOapg.properties.signature_id, str, schemas.Unset] = schemas.unset,
        should_add_default_signature: typing.Union[MetaOapg.properties.should_add_default_signature, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDraft':
        return super().__new__(
            cls,
            *args,
            author_id=author_id,
            body=body,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            quote_body=quote_body,
            attachments=attachments,
            mode=mode,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
            _configuration=_configuration,
            **kwargs,
        )
