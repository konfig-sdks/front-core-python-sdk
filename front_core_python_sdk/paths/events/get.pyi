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

from front_core_python_sdk.model.conversations_list_events_response import ConversationsListEventsResponse as ConversationsListEventsResponseSchema

from front_core_python_sdk.type.conversations_list_events_response import ConversationsListEventsResponse

from ...api_client import Dictionary
from front_core_python_sdk.pydantic.conversations_list_events_response import ConversationsListEventsResponse as ConversationsListEventsResponsePydantic

# Query params
QSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
PageTokenSchema = schemas.StrSchema
SortBySchema = schemas.StrSchema


class SortOrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'q': typing.Union[QSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'page_token': typing.Union[PageTokenSchema, str, ],
        'sort_by': typing.Union[SortBySchema, str, ],
        'sort_order': typing.Union[SortOrderSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_page_token = api_client.QueryParameter(
    name="page_token",
    style=api_client.ParameterStyle.FORM,
    schema=PageTokenSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sort_order",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ConversationsListEventsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConversationsListEventsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConversationsListEventsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_detailed_inbox_events_mapped_args(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if q is not None:
            _query_params["q"] = q
        if limit is not None:
            _query_params["limit"] = limit
        if page_token is not None:
            _query_params["page_token"] = page_token
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        if sort_order is not None:
            _query_params["sort_order"] = sort_order
        args.query = _query_params
        return args

    async def _alist_detailed_inbox_events_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List events
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_limit,
            request_query_page_token,
            request_query_sort_by,
            request_query_sort_order,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/events',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_detailed_inbox_events_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List events
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_limit,
            request_query_page_token,
            request_query_sort_by,
            request_query_sort_order,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/events',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListDetailedInboxEventsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_detailed_inbox_events(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_detailed_inbox_events_mapped_args(
            q=q,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return await self._alist_detailed_inbox_events_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_detailed_inbox_events(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_detailed_inbox_events_mapped_args(
            q=q,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return self._list_detailed_inbox_events_oapg(
            query_params=args.query,
        )

class ListDetailedInboxEvents(BaseApi):

    async def alist_detailed_inbox_events(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConversationsListEventsResponsePydantic:
        raw_response = await self.raw.alist_detailed_inbox_events(
            q=q,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            sort_order=sort_order,
            **kwargs,
        )
        if validate:
            return ConversationsListEventsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ConversationsListEventsResponsePydantic, raw_response.body)
    
    
    def list_detailed_inbox_events(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ConversationsListEventsResponsePydantic:
        raw_response = self.raw.list_detailed_inbox_events(
            q=q,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        if validate:
            return ConversationsListEventsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ConversationsListEventsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_detailed_inbox_events_mapped_args(
            q=q,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return await self._alist_detailed_inbox_events_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_detailed_inbox_events_mapped_args(
            q=q,
            limit=limit,
            page_token=page_token,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return self._list_detailed_inbox_events_oapg(
            query_params=args.query,
        )

