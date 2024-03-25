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

from front_core_python_sdk.model.analytics_metric_id import AnalyticsMetricId as AnalyticsMetricIdSchema
from front_core_python_sdk.model.analytics_filters import AnalyticsFilters as AnalyticsFiltersSchema
from front_core_python_sdk.model.analytics_report_request import AnalyticsReportRequest as AnalyticsReportRequestSchema

from front_core_python_sdk.type.analytics_filters import AnalyticsFilters
from front_core_python_sdk.type.analytics_report_request import AnalyticsReportRequest
from front_core_python_sdk.type.analytics_metric_id import AnalyticsMetricId

from ...api_client import Dictionary
from front_core_python_sdk.pydantic.analytics_filters import AnalyticsFilters as AnalyticsFiltersPydantic
from front_core_python_sdk.pydantic.analytics_report_request import AnalyticsReportRequest as AnalyticsReportRequestPydantic
from front_core_python_sdk.pydantic.analytics_metric_id import AnalyticsMetricId as AnalyticsMetricIdPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = AnalyticsReportRequestSchema


request_body_analytics_report_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'http',
]
SchemaFor201ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


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

    def _create_new_report_mapped_args(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if start is not None:
            _body["start"] = start
        if end is not None:
            _body["end"] = end
        if timezone is not None:
            _body["timezone"] = timezone
        if filters is not None:
            _body["filters"] = filters
        if metrics is not None:
            _body["metrics"] = metrics
        args.body = _body
        return args

    async def _acreate_new_report_oapg(
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
        Create a new analytics report.
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
            path_template='/analytics/reports',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_analytics_report_request.serialize(body, content_type)
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


    def _create_new_report_oapg(
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
        Create a new analytics report.
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
            path_template='/analytics/reports',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_analytics_report_request.serialize(body, content_type)
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


class CreateNewReportRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_report(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_report_mapped_args(
            body=body,
            start=start,
            end=end,
            metrics=metrics,
            timezone=timezone,
            filters=filters,
        )
        return await self._acreate_new_report_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_report(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_report_mapped_args(
            body=body,
            start=start,
            end=end,
            metrics=metrics,
            timezone=timezone,
            filters=filters,
        )
        return self._create_new_report_oapg(
            body=args.body,
        )

class CreateNewReport(BaseApi):

    async def acreate_new_report(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.acreate_new_report(
            body=body,
            start=start,
            end=end,
            metrics=metrics,
            timezone=timezone,
            filters=filters,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def create_new_report(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.create_new_report(
            body=body,
            start=start,
            end=end,
            metrics=metrics,
            timezone=timezone,
            filters=filters,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_report_mapped_args(
            body=body,
            start=start,
            end=end,
            metrics=metrics,
            timezone=timezone,
            filters=filters,
        )
        return await self._acreate_new_report_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        start: typing.Union[int, float],
        end: typing.Union[int, float],
        metrics: typing.List[AnalyticsMetricId],
        timezone: typing.Optional[str] = None,
        filters: typing.Optional[AnalyticsFilters] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_report_mapped_args(
            body=body,
            start=start,
            end=end,
            metrics=metrics,
            timezone=timezone,
            filters=filters,
        )
        return self._create_new_report_oapg(
            body=args.body,
        )

