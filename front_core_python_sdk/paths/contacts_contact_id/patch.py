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

from front_core_python_sdk.model.contact import Contact as ContactSchema

from front_core_python_sdk.type.contact import Contact

from ...api_client import Dictionary
from front_core_python_sdk.pydantic.contact import Contact as ContactPydantic

from . import path

# Path params
ContactIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'contact_id': typing.Union[ContactIdSchema, str, ],
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


request_path_contact_id = api_client.PathParameter(
    name="contact_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContactIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ContactSchema


request_body_contact = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'http',
]


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
)
_status_code_to_response = {
    '204': _response_for_204,
}


class BaseApi(api_client.Api):

    def _update_contact_mapped_args(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if avatar is not None:
            _body["avatar"] = avatar
        if is_spammer is not None:
            _body["is_spammer"] = is_spammer
        if links is not None:
            _body["links"] = links
        if group_names is not None:
            _body["group_names"] = group_names
        if custom_fields is not None:
            _body["custom_fields"] = custom_fields
        args.body = _body
        if contact_id is not None:
            _path_params["contact_id"] = contact_id
        args.path = _path_params
        return args

    async def _aupdate_contact_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update a contact
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_contact_id,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contacts/{contact_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_contact.serialize(body, content_type)
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


    def _update_contact_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update a contact
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_contact_id,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/contacts/{contact_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_contact.serialize(body, content_type)
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


class UpdateContactRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_contact(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_contact_mapped_args(
            body=body,
            contact_id=contact_id,
            description=description,
            name=name,
            avatar=avatar,
            is_spammer=is_spammer,
            links=links,
            group_names=group_names,
            custom_fields=custom_fields,
        )
        return await self._aupdate_contact_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_contact(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_contact_mapped_args(
            body=body,
            contact_id=contact_id,
            description=description,
            name=name,
            avatar=avatar,
            is_spammer=is_spammer,
            links=links,
            group_names=group_names,
            custom_fields=custom_fields,
        )
        return self._update_contact_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateContact(BaseApi):

    async def aupdate_contact(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_contact(
            body=body,
            contact_id=contact_id,
            description=description,
            name=name,
            avatar=avatar,
            is_spammer=is_spammer,
            links=links,
            group_names=group_names,
            custom_fields=custom_fields,
            **kwargs,
        )
    
    
    def update_contact(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_contact(
            body=body,
            contact_id=contact_id,
            description=description,
            name=name,
            avatar=avatar,
            is_spammer=is_spammer,
            links=links,
            group_names=group_names,
            custom_fields=custom_fields,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_contact_mapped_args(
            body=body,
            contact_id=contact_id,
            description=description,
            name=name,
            avatar=avatar,
            is_spammer=is_spammer,
            links=links,
            group_names=group_names,
            custom_fields=custom_fields,
        )
        return await self._aupdate_contact_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        contact_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        avatar: typing.Optional[typing.IO] = None,
        is_spammer: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[str]] = None,
        group_names: typing.Optional[typing.List[str]] = None,
        custom_fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_contact_mapped_args(
            body=body,
            contact_id=contact_id,
            description=description,
            name=name,
            avatar=avatar,
            is_spammer=is_spammer,
            links=links,
            group_names=group_names,
            custom_fields=custom_fields,
        )
        return self._update_contact_oapg(
            body=args.body,
            path_params=args.path,
        )
