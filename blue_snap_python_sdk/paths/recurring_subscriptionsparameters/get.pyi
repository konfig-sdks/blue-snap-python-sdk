# coding: utf-8

"""
    API Settings

    At BlueSnap, we look at payments a little differently. Our Payment Orchestration Platform helps businesses accept payments globally and is designed to increase revenue and reduces costs. We provide a comprehensive back-end solutions that simplifies the complexity of payments, managing the full process from start to finish.  BlueSnap supports payments through multiple sales channels such as online and mobile sales, marketplaces, subscriptions, invoice payments and manual orders through a virtual terminal. And for businesses looking for embedded payments, we offer white-labeled payments for platforms with automated underwriting and onboarding that supports marketplaces and split payments.  And with one integration and contract, businesses can sell in over 200 geographies with access to local acquiring in 47 countries, 110+ currencies and 100+ global payment types, including popular eWallets, automated accounts receivable, world-class fraud protection and chargeback management, built-in solutions for regulation and tax compliance, and unified global reporting to help businesses grow.  With a US headquarters in Waltham, MA, and EU headquarters in Dublin, Ireland, BlueSnap is backed by world-class private equity investors including Great Hill Partners and Parthenon Capital Partners.   Learn more at BlueSnap.com

    The version of the OpenAPI document: 8976-Tools
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from blue_snap_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from blue_snap_python_sdk.api_response import AsyncGeneratorResponse
from blue_snap_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from blue_snap_python_sdk import schemas  # noqa: F401



from ...api_client import Dictionary

# Query params
PagesizeSchema = schemas.StrSchema
AfterSchema = schemas.StrSchema
GettotalSchema = schemas.BoolSchema
FulldescriptionSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'pagesize': typing.Union[PagesizeSchema, str, ],
        'after': typing.Union[AfterSchema, str, ],
        'gettotal': typing.Union[GettotalSchema, bool, ],
        'fulldescription': typing.Union[FulldescriptionSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_pagesize = api_client.QueryParameter(
    name="pagesize",
    style=api_client.ParameterStyle.FORM,
    schema=PagesizeSchema,
    explode=True,
)
request_query_after = api_client.QueryParameter(
    name="after",
    style=api_client.ParameterStyle.FORM,
    schema=AfterSchema,
    explode=True,
)
request_query_gettotal = api_client.QueryParameter(
    name="gettotal",
    style=api_client.ParameterStyle.FORM,
    schema=GettotalSchema,
    explode=True,
)
request_query_fulldescription = api_client.QueryParameter(
    name="fulldescription",
    style=api_client.ParameterStyle.FORM,
    schema=FulldescriptionSchema,
    explode=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


class BaseApi(api_client.Api):

    def _list_all_subscriptions_mapped_args(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if pagesize is not None:
            _query_params["pagesize"] = pagesize
        if after is not None:
            _query_params["after"] = after
        if gettotal is not None:
            _query_params["gettotal"] = gettotal
        if fulldescription is not None:
            _query_params["fulldescription"] = fulldescription
        args.query = _query_params
        return args

    async def _alist_all_subscriptions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve All Subscriptions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pagesize,
            request_query_after,
            request_query_gettotal,
            request_query_fulldescription,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/recurring/subscriptions?{parameters}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
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


    def _list_all_subscriptions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve All Subscriptions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_pagesize,
            request_query_after,
            request_query_gettotal,
            request_query_fulldescription,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/recurring/subscriptions?{parameters}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
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


class ListAllSubscriptionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_all_subscriptions(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_subscriptions_mapped_args(
            pagesize=pagesize,
            after=after,
            gettotal=gettotal,
            fulldescription=fulldescription,
        )
        return await self._alist_all_subscriptions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_all_subscriptions(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_subscriptions_mapped_args(
            pagesize=pagesize,
            after=after,
            gettotal=gettotal,
            fulldescription=fulldescription,
        )
        return self._list_all_subscriptions_oapg(
            query_params=args.query,
        )

class ListAllSubscriptions(BaseApi):

    async def alist_all_subscriptions(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.alist_all_subscriptions(
            pagesize=pagesize,
            after=after,
            gettotal=gettotal,
            fulldescription=fulldescription,
            **kwargs,
        )
    
    
    def list_all_subscriptions(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.list_all_subscriptions(
            pagesize=pagesize,
            after=after,
            gettotal=gettotal,
            fulldescription=fulldescription,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_subscriptions_mapped_args(
            pagesize=pagesize,
            after=after,
            gettotal=gettotal,
            fulldescription=fulldescription,
        )
        return await self._alist_all_subscriptions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        pagesize: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        gettotal: typing.Optional[bool] = None,
        fulldescription: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_subscriptions_mapped_args(
            pagesize=pagesize,
            after=after,
            gettotal=gettotal,
            fulldescription=fulldescription,
        )
        return self._list_all_subscriptions_oapg(
            query_params=args.query,
        )

