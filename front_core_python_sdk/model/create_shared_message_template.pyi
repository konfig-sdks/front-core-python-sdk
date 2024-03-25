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


class CreateSharedMessageTemplate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A message template that is used for pre-written responses
    """


    class MetaOapg:
        required = {
            "name",
            "body",
        }
        
        class properties:
            name = schemas.StrSchema
            body = schemas.StrSchema
            subject = schemas.StrSchema
            folder_id = schemas.StrSchema
        
            @staticmethod
            def inbox_ids() -> typing.Type['CreateSharedMessageTemplateInboxIds']:
                return CreateSharedMessageTemplateInboxIds
        
            @staticmethod
            def attachments() -> typing.Type['CreateSharedMessageTemplateAttachments']:
                return CreateSharedMessageTemplateAttachments
            __annotations__ = {
                "name": name,
                "body": body,
                "subject": subject,
                "folder_id": folder_id,
                "inbox_ids": inbox_ids,
                "attachments": attachments,
            }
    
    name: MetaOapg.properties.name
    body: MetaOapg.properties.body
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inbox_ids"]) -> 'CreateSharedMessageTemplateInboxIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> 'CreateSharedMessageTemplateAttachments': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "body", "subject", "folder_id", "inbox_ids", "attachments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_id"]) -> typing.Union[MetaOapg.properties.folder_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inbox_ids"]) -> typing.Union['CreateSharedMessageTemplateInboxIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union['CreateSharedMessageTemplateAttachments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "body", "subject", "folder_id", "inbox_ids", "attachments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        body: typing.Union[MetaOapg.properties.body, str, ],
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        folder_id: typing.Union[MetaOapg.properties.folder_id, str, schemas.Unset] = schemas.unset,
        inbox_ids: typing.Union['CreateSharedMessageTemplateInboxIds', schemas.Unset] = schemas.unset,
        attachments: typing.Union['CreateSharedMessageTemplateAttachments', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateSharedMessageTemplate':
        return super().__new__(
            cls,
            *args,
            name=name,
            body=body,
            subject=subject,
            folder_id=folder_id,
            inbox_ids=inbox_ids,
            attachments=attachments,
            _configuration=_configuration,
            **kwargs,
        )

from front_core_python_sdk.model.create_shared_message_template_attachments import CreateSharedMessageTemplateAttachments
from front_core_python_sdk.model.create_shared_message_template_inbox_ids import CreateSharedMessageTemplateInboxIds
