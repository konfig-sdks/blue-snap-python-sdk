# coding: utf-8

"""
    API Settings

    At BlueSnap, we look at payments a little differently. Our Payment Orchestration Platform helps businesses accept payments globally and is designed to increase revenue and reduces costs. We provide a comprehensive back-end solutions that simplifies the complexity of payments, managing the full process from start to finish.  BlueSnap supports payments through multiple sales channels such as online and mobile sales, marketplaces, subscriptions, invoice payments and manual orders through a virtual terminal. And for businesses looking for embedded payments, we offer white-labeled payments for platforms with automated underwriting and onboarding that supports marketplaces and split payments.  And with one integration and contract, businesses can sell in over 200 geographies with access to local acquiring in 47 countries, 110+ currencies and 100+ global payment types, including popular eWallets, automated accounts receivable, world-class fraud protection and chargeback management, built-in solutions for regulation and tax compliance, and unified global reporting to help businesses grow.  With a US headquarters in Waltham, MA, and EU headquarters in Dublin, Ireland, BlueSnap is backed by world-class private equity investors including Great Hill Partners and Parthenon Capital Partners.   Learn more at BlueSnap.com

    The version of the OpenAPI document: 8976-Tools
    Generated by: https://konfigthis.com
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

from blue_snap_python_sdk import schemas  # noqa: F401


class AuthorizationCreateTransactionRequestCreditCard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            expirationYear = schemas.Int32Schema
            securityCode = schemas.Int32Schema
            expirationMonth = schemas.StrSchema
            cardNumber = schemas.StrSchema
            __annotations__ = {
                "expirationYear": expirationYear,
                "securityCode": securityCode,
                "expirationMonth": expirationMonth,
                "cardNumber": cardNumber,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationYear"]) -> MetaOapg.properties.expirationYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securityCode"]) -> MetaOapg.properties.securityCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationMonth"]) -> MetaOapg.properties.expirationMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardNumber"]) -> MetaOapg.properties.cardNumber: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expirationYear", "securityCode", "expirationMonth", "cardNumber", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationYear"]) -> typing.Union[MetaOapg.properties.expirationYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securityCode"]) -> typing.Union[MetaOapg.properties.securityCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationMonth"]) -> typing.Union[MetaOapg.properties.expirationMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardNumber"]) -> typing.Union[MetaOapg.properties.cardNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expirationYear", "securityCode", "expirationMonth", "cardNumber", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        expirationYear: typing.Union[MetaOapg.properties.expirationYear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        securityCode: typing.Union[MetaOapg.properties.securityCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expirationMonth: typing.Union[MetaOapg.properties.expirationMonth, str, schemas.Unset] = schemas.unset,
        cardNumber: typing.Union[MetaOapg.properties.cardNumber, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthorizationCreateTransactionRequestCreditCard':
        return super().__new__(
            cls,
            *args,
            expirationYear=expirationYear,
            securityCode=securityCode,
            expirationMonth=expirationMonth,
            cardNumber=cardNumber,
            _configuration=_configuration,
            **kwargs,
        )
