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

from front_core_python_sdk.model.create_tag import CreateTag as CreateTagSchema
from front_core_python_sdk.model.tag_response import TagResponse as TagResponseSchema

from front_core_python_sdk.type.create_tag import CreateTag
from front_core_python_sdk.type.tag_response import TagResponse

from ...api_client import Dictionary
from front_core_python_sdk.pydantic.create_tag import CreateTag as CreateTagPydantic
from front_core_python_sdk.pydantic.tag_response import TagResponse as TagResponsePydantic

from . import path

# Path params
TagIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'tag_id': typing.Union[TagIdSchema, str, ],
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


request_path_tag_id = api_client.PathParameter(
    name="tag_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TagIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CreateTagSchema


request_body_create_tag = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'http',
]
SchemaFor201ResponseBodyApplicationJson = TagResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: TagResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: TagResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_child_tag_mapped_args(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if highlight is not None:
            _body["highlight"] = highlight
        if is_visible_in_conversation_lists is not None:
            _body["is_visible_in_conversation_lists"] = is_visible_in_conversation_lists
        args.body = _body
        if tag_id is not None:
            _path_params["tag_id"] = tag_id
        args.path = _path_params
        return args

    async def _acreate_child_tag_oapg(
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
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create child tag
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_tag_id,
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
            path_template='/tags/{tag_id}/children',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_tag.serialize(body, content_type)
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


    def _create_child_tag_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create child tag
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_tag_id,
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
            path_template='/tags/{tag_id}/children',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_tag.serialize(body, content_type)
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


class CreateChildTagRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_child_tag(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_child_tag_mapped_args(
            name=name,
            tag_id=tag_id,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
        )
        return await self._acreate_child_tag_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_child_tag(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_child_tag_mapped_args(
            name=name,
            tag_id=tag_id,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
        )
        return self._create_child_tag_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateChildTag(BaseApi):

    async def acreate_child_tag(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> TagResponsePydantic:
        raw_response = await self.raw.acreate_child_tag(
            name=name,
            tag_id=tag_id,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
            **kwargs,
        )
        if validate:
            return TagResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TagResponsePydantic, raw_response.body)
    
    
    def create_child_tag(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> TagResponsePydantic:
        raw_response = self.raw.create_child_tag(
            name=name,
            tag_id=tag_id,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
        )
        if validate:
            return TagResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TagResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_child_tag_mapped_args(
            name=name,
            tag_id=tag_id,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
        )
        return await self._acreate_child_tag_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        tag_id: str,
        description: typing.Optional[str] = None,
        highlight: typing.Optional[str] = None,
        is_visible_in_conversation_lists: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_child_tag_mapped_args(
            name=name,
            tag_id=tag_id,
            description=description,
            highlight=highlight,
            is_visible_in_conversation_lists=is_visible_in_conversation_lists,
        )
        return self._create_child_tag_oapg(
            body=args.body,
            path_params=args.path,
        )

