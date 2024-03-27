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


class VendorUpdateVendorRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            email = schemas.StrSchema
            name = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            address = schemas.StrSchema
            city = schemas.StrSchema
            zip = schemas.StrSchema
            country = schemas.StrSchema
            phone = schemas.StrSchema
            state = schemas.StrSchema
            taxId = schemas.Int32Schema
            vendorUrl = schemas.StrSchema
            ipnUrl = schemas.StrSchema
            defaultPayoutCurrency = schemas.StrSchema
        
            @staticmethod
            def vendorPrincipal() -> typing.Type['VendorUpdateVendorRequestVendorPrincipal']:
                return VendorUpdateVendorRequestVendorPrincipal
        
            @staticmethod
            def payoutInfo() -> typing.Type['VendorUpdateVendorRequestPayoutInfo']:
                return VendorUpdateVendorRequestPayoutInfo
        
            @staticmethod
            def vendorAgreement() -> typing.Type['VendorUpdateVendorRequestVendorAgreement']:
                return VendorUpdateVendorRequestVendorAgreement
            __annotations__ = {
                "email": email,
                "name": name,
                "firstName": firstName,
                "lastName": lastName,
                "address": address,
                "city": city,
                "zip": zip,
                "country": country,
                "phone": phone,
                "state": state,
                "taxId": taxId,
                "vendorUrl": vendorUrl,
                "ipnUrl": ipnUrl,
                "defaultPayoutCurrency": defaultPayoutCurrency,
                "vendorPrincipal": vendorPrincipal,
                "payoutInfo": payoutInfo,
                "vendorAgreement": vendorAgreement,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendorUrl"]) -> MetaOapg.properties.vendorUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipnUrl"]) -> MetaOapg.properties.ipnUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultPayoutCurrency"]) -> MetaOapg.properties.defaultPayoutCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendorPrincipal"]) -> 'VendorUpdateVendorRequestVendorPrincipal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payoutInfo"]) -> 'VendorUpdateVendorRequestPayoutInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendorAgreement"]) -> 'VendorUpdateVendorRequestVendorAgreement': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "name", "firstName", "lastName", "address", "city", "zip", "country", "phone", "state", "taxId", "vendorUrl", "ipnUrl", "defaultPayoutCurrency", "vendorPrincipal", "payoutInfo", "vendorAgreement", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> typing.Union[MetaOapg.properties.zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> typing.Union[MetaOapg.properties.taxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendorUrl"]) -> typing.Union[MetaOapg.properties.vendorUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipnUrl"]) -> typing.Union[MetaOapg.properties.ipnUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultPayoutCurrency"]) -> typing.Union[MetaOapg.properties.defaultPayoutCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendorPrincipal"]) -> typing.Union['VendorUpdateVendorRequestVendorPrincipal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payoutInfo"]) -> typing.Union['VendorUpdateVendorRequestPayoutInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendorAgreement"]) -> typing.Union['VendorUpdateVendorRequestVendorAgreement', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "name", "firstName", "lastName", "address", "city", "zip", "country", "phone", "state", "taxId", "vendorUrl", "ipnUrl", "defaultPayoutCurrency", "vendorPrincipal", "payoutInfo", "vendorAgreement", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        taxId: typing.Union[MetaOapg.properties.taxId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        vendorUrl: typing.Union[MetaOapg.properties.vendorUrl, str, schemas.Unset] = schemas.unset,
        ipnUrl: typing.Union[MetaOapg.properties.ipnUrl, str, schemas.Unset] = schemas.unset,
        defaultPayoutCurrency: typing.Union[MetaOapg.properties.defaultPayoutCurrency, str, schemas.Unset] = schemas.unset,
        vendorPrincipal: typing.Union['VendorUpdateVendorRequestVendorPrincipal', schemas.Unset] = schemas.unset,
        payoutInfo: typing.Union['VendorUpdateVendorRequestPayoutInfo', schemas.Unset] = schemas.unset,
        vendorAgreement: typing.Union['VendorUpdateVendorRequestVendorAgreement', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VendorUpdateVendorRequest':
        return super().__new__(
            cls,
            *args,
            email=email,
            name=name,
            firstName=firstName,
            lastName=lastName,
            address=address,
            city=city,
            zip=zip,
            country=country,
            phone=phone,
            state=state,
            taxId=taxId,
            vendorUrl=vendorUrl,
            ipnUrl=ipnUrl,
            defaultPayoutCurrency=defaultPayoutCurrency,
            vendorPrincipal=vendorPrincipal,
            payoutInfo=payoutInfo,
            vendorAgreement=vendorAgreement,
            _configuration=_configuration,
            **kwargs,
        )

from blue_snap_python_sdk.model.vendor_update_vendor_request_payout_info import VendorUpdateVendorRequestPayoutInfo
from blue_snap_python_sdk.model.vendor_update_vendor_request_vendor_agreement import VendorUpdateVendorRequestVendorAgreement
from blue_snap_python_sdk.model.vendor_update_vendor_request_vendor_principal import VendorUpdateVendorRequestVendorPrincipal
