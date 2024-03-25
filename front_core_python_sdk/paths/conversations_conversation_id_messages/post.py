# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from front_core_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from front_core_python_sdk.api_response import AsyncGeneratorResponse
from front_core_python_sdk import api_client, exceptions
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

from front_core_python_sdk.model.outbound_reply_message import OutboundReplyMessage as OutboundReplyMessageSchema

from front_core_python_sdk.type.outbound_reply_message import OutboundReplyMessage

from ...api_client import Dictionary
from front_core_python_sdk.pydantic.outbound_reply_message import OutboundReplyMessage as OutboundReplyMessagePydantic

from . import path

# Path params
ConversationIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'conversation_id': typing.Union[ConversationIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_conversation_id = api_client.PathParameter(
    name="conversation_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConversationIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = OutboundReplyMessageSchema


request_body_outbound_reply_message = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'http',
]
SchemaFor202ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '202': _response_for_202,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_message_reply_mapped_args(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if to is not None:
            _body["to"] = to
        if cc is not None:
            _body["cc"] = cc
        if bcc is not None:
            _body["bcc"] = bcc
        if sender_name is not None:
            _body["sender_name"] = sender_name
        if subject is not None:
            _body["subject"] = subject
        if author_id is not None:
            _body["author_id"] = author_id
        if channel_id is not None:
            _body["channel_id"] = channel_id
        if body is not None:
            _body["body"] = body
        if text is not None:
            _body["text"] = text
        if quote_body is not None:
            _body["quote_body"] = quote_body
        if options is not None:
            _body["options"] = options
        if attachments is not None:
            _body["attachments"] = attachments
        if signature_id is not None:
            _body["signature_id"] = signature_id
        if should_add_default_signature is not None:
            _body["should_add_default_signature"] = should_add_default_signature
        args.body = _body
        if conversation_id is not None:
            _path_params["conversation_id"] = conversation_id
        args.path = _path_params
        return args

    async def _acreate_message_reply_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create message reply
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_conversation_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/conversations/{conversation_id}/messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_outbound_reply_message.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_message_reply_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create message reply
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_conversation_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/conversations/{conversation_id}/messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_outbound_reply_message.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateMessageReplyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_message_reply(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_message_reply_mapped_args(
            body=body,
            body=body,
            conversation_id=conversation_id,
            to=to,
            cc=cc,
            bcc=bcc,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            channel_id=channel_id,
            text=text,
            quote_body=quote_body,
            options=options,
            attachments=attachments,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
        )
        return await self._acreate_message_reply_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_message_reply(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_message_reply_mapped_args(
            body=body,
            body=body,
            conversation_id=conversation_id,
            to=to,
            cc=cc,
            bcc=bcc,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            channel_id=channel_id,
            text=text,
            quote_body=quote_body,
            options=options,
            attachments=attachments,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
        )
        return self._create_message_reply_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateMessageReply(BaseApi):

    async def acreate_message_reply(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.acreate_message_reply(
            body=body,
            body=body,
            conversation_id=conversation_id,
            to=to,
            cc=cc,
            bcc=bcc,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            channel_id=channel_id,
            text=text,
            quote_body=quote_body,
            options=options,
            attachments=attachments,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def create_message_reply(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.create_message_reply(
            body=body,
            body=body,
            conversation_id=conversation_id,
            to=to,
            cc=cc,
            bcc=bcc,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            channel_id=channel_id,
            text=text,
            quote_body=quote_body,
            options=options,
            attachments=attachments,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_message_reply_mapped_args(
            body=body,
            body=body,
            conversation_id=conversation_id,
            to=to,
            cc=cc,
            bcc=bcc,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            channel_id=channel_id,
            text=text,
            quote_body=quote_body,
            options=options,
            attachments=attachments,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
        )
        return await self._acreate_message_reply_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        body: str,
        conversation_id: str,
        to: typing.Optional[typing.List[str]] = None,
        cc: typing.Optional[typing.List[str]] = None,
        bcc: typing.Optional[typing.List[str]] = None,
        sender_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        author_id: typing.Optional[str] = None,
        channel_id: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        quote_body: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[typing.IO]] = None,
        signature_id: typing.Optional[str] = None,
        should_add_default_signature: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_message_reply_mapped_args(
            body=body,
            body=body,
            conversation_id=conversation_id,
            to=to,
            cc=cc,
            bcc=bcc,
            sender_name=sender_name,
            subject=subject,
            author_id=author_id,
            channel_id=channel_id,
            text=text,
            quote_body=quote_body,
            options=options,
            attachments=attachments,
            signature_id=signature_id,
            should_add_default_signature=should_add_default_signature,
        )
        return self._create_message_reply_oapg(
            body=args.body,
            path_params=args.path,
        )
