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

from front_core_python_sdk.model.link_response import LinkResponse as LinkResponseSchema
from front_core_python_sdk.model.create_link import CreateLink as CreateLinkSchema

from front_core_python_sdk.type.create_link import CreateLink
from front_core_python_sdk.type.link_response import LinkResponse

from ...api_client import Dictionary
from front_core_python_sdk.pydantic.create_link import CreateLink as CreateLinkPydantic
from front_core_python_sdk.pydantic.link_response import LinkResponse as LinkResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateLinkSchema


request_body_create_link = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'http',
]
SchemaFor201ResponseBodyApplicationJson = LinkResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: LinkResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: LinkResponse


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

    def _create_link_mapped_args(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if external_url is not None:
            _body["external_url"] = external_url
        if pattern is not None:
            _body["pattern"] = pattern
        args.body = _body
        return args

    async def _acreate_link_oapg(
        self,
        body: typing.Any = None,
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
        Create link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/links',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_link.serialize(body, content_type)
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


    def _create_link_oapg(
        self,
        body: typing.Any = None,
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
        Create link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/links',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_link.serialize(body, content_type)
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


class CreateLinkRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_link(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_link_mapped_args(
            name=name,
            external_url=external_url,
            pattern=pattern,
        )
        return await self._acreate_link_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_link(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_link_mapped_args(
            name=name,
            external_url=external_url,
            pattern=pattern,
        )
        return self._create_link_oapg(
            body=args.body,
        )

class CreateLink(BaseApi):

    async def acreate_link(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LinkResponsePydantic:
        raw_response = await self.raw.acreate_link(
            name=name,
            external_url=external_url,
            pattern=pattern,
            **kwargs,
        )
        if validate:
            return LinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LinkResponsePydantic, raw_response.body)
    
    
    def create_link(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LinkResponsePydantic:
        raw_response = self.raw.create_link(
            name=name,
            external_url=external_url,
            pattern=pattern,
        )
        if validate:
            return LinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LinkResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_link_mapped_args(
            name=name,
            external_url=external_url,
            pattern=pattern,
        )
        return await self._acreate_link_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: typing.Optional[str] = None,
        external_url: typing.Optional[str] = None,
        pattern: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_link_mapped_args(
            name=name,
            external_url=external_url,
            pattern=pattern,
        )
        return self._create_link_oapg(
            body=args.body,
        )
