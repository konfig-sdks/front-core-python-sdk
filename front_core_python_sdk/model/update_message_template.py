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


class UpdateMessageTemplate(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            subject = schemas.StrSchema
            body = schemas.StrSchema
            folder_id = schemas.StrSchema
            
            
            class inbox_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'inbox_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
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
                "name": name,
                "subject": subject,
                "body": body,
                "folder_id": folder_id,
                "inbox_ids": inbox_ids,
                "attachments": attachments,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inbox_ids"]) -> MetaOapg.properties.inbox_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "subject", "body", "folder_id", "inbox_ids", "attachments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_id"]) -> typing.Union[MetaOapg.properties.folder_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inbox_ids"]) -> typing.Union[MetaOapg.properties.inbox_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "subject", "body", "folder_id", "inbox_ids", "attachments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        folder_id: typing.Union[MetaOapg.properties.folder_id, str, schemas.Unset] = schemas.unset,
        inbox_ids: typing.Union[MetaOapg.properties.inbox_ids, list, tuple, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateMessageTemplate':
        return super().__new__(
            cls,
            *args,
            name=name,
            subject=subject,
            body=body,
            folder_id=folder_id,
            inbox_ids=inbox_ids,
            attachments=attachments,
            _configuration=_configuration,
            **kwargs,
        )
