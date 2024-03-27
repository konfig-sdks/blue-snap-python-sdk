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

from blue_snap_python_sdk.model.authorization_create_transaction_request_credit_card import AuthorizationCreateTransactionRequestCreditCard as AuthorizationCreateTransactionRequestCreditCardSchema
from blue_snap_python_sdk.model.authorization_create_transaction_request_card_holder_info import AuthorizationCreateTransactionRequestCardHolderInfo as AuthorizationCreateTransactionRequestCardHolderInfoSchema
from blue_snap_python_sdk.model.authorization_create_transaction_request import AuthorizationCreateTransactionRequest as AuthorizationCreateTransactionRequestSchema

from blue_snap_python_sdk.type.authorization_create_transaction_request import AuthorizationCreateTransactionRequest
from blue_snap_python_sdk.type.authorization_create_transaction_request_card_holder_info import AuthorizationCreateTransactionRequestCardHolderInfo
from blue_snap_python_sdk.type.authorization_create_transaction_request_credit_card import AuthorizationCreateTransactionRequestCreditCard

from ...api_client import Dictionary
from blue_snap_python_sdk.pydantic.authorization_create_transaction_request_credit_card import AuthorizationCreateTransactionRequestCreditCard as AuthorizationCreateTransactionRequestCreditCardPydantic
from blue_snap_python_sdk.pydantic.authorization_create_transaction_request_card_holder_info import AuthorizationCreateTransactionRequestCardHolderInfo as AuthorizationCreateTransactionRequestCardHolderInfoPydantic
from blue_snap_python_sdk.pydantic.authorization_create_transaction_request import AuthorizationCreateTransactionRequest as AuthorizationCreateTransactionRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = AuthorizationCreateTransactionRequestSchema


request_body_authorization_create_transaction_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
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

    def _create_transaction_mapped_args(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if amount is not None:
            _body["amount"] = amount
        if soft_descriptor is not None:
            _body["softDescriptor"] = soft_descriptor
        if card_holder_info is not None:
            _body["cardHolderInfo"] = card_holder_info
        if currency is not None:
            _body["currency"] = currency
        if credit_card is not None:
            _body["creditCard"] = credit_card
        if card_transaction_type is not None:
            _body["cardTransactionType"] = card_transaction_type
        args.body = _body
        return args

    async def _acreate_transaction_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Auth Only
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transactions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_authorization_create_transaction_request.serialize(body, content_type)
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


    def _create_transaction_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Auth Only
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transactions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_authorization_create_transaction_request.serialize(body, content_type)
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


class CreateTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_transaction(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_transaction_mapped_args(
            amount=amount,
            soft_descriptor=soft_descriptor,
            card_holder_info=card_holder_info,
            currency=currency,
            credit_card=credit_card,
            card_transaction_type=card_transaction_type,
        )
        return await self._acreate_transaction_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_transaction(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_transaction_mapped_args(
            amount=amount,
            soft_descriptor=soft_descriptor,
            card_holder_info=card_holder_info,
            currency=currency,
            credit_card=credit_card,
            card_transaction_type=card_transaction_type,
        )
        return self._create_transaction_oapg(
            body=args.body,
        )

class CreateTransaction(BaseApi):

    async def acreate_transaction(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_transaction(
            amount=amount,
            soft_descriptor=soft_descriptor,
            card_holder_info=card_holder_info,
            currency=currency,
            credit_card=credit_card,
            card_transaction_type=card_transaction_type,
            **kwargs,
        )
    
    
    def create_transaction(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_transaction(
            amount=amount,
            soft_descriptor=soft_descriptor,
            card_holder_info=card_holder_info,
            currency=currency,
            credit_card=credit_card,
            card_transaction_type=card_transaction_type,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_transaction_mapped_args(
            amount=amount,
            soft_descriptor=soft_descriptor,
            card_holder_info=card_holder_info,
            currency=currency,
            credit_card=credit_card,
            card_transaction_type=card_transaction_type,
        )
        return await self._acreate_transaction_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        amount: typing.Optional[typing.Union[int, float]] = None,
        soft_descriptor: typing.Optional[str] = None,
        card_holder_info: typing.Optional[AuthorizationCreateTransactionRequestCardHolderInfo] = None,
        currency: typing.Optional[str] = None,
        credit_card: typing.Optional[AuthorizationCreateTransactionRequestCreditCard] = None,
        card_transaction_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_transaction_mapped_args(
            amount=amount,
            soft_descriptor=soft_descriptor,
            card_holder_info=card_holder_info,
            currency=currency,
            credit_card=credit_card,
            card_transaction_type=card_transaction_type,
        )
        return self._create_transaction_oapg(
            body=args.body,
        )

