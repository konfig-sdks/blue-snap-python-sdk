# coding: utf-8
"""
    API Settings

    At BlueSnap, we look at payments a little differently. Our Payment Orchestration Platform helps businesses accept payments globally and is designed to increase revenue and reduces costs. We provide a comprehensive back-end solutions that simplifies the complexity of payments, managing the full process from start to finish.  BlueSnap supports payments through multiple sales channels such as online and mobile sales, marketplaces, subscriptions, invoice payments and manual orders through a virtual terminal. And for businesses looking for embedded payments, we offer white-labeled payments for platforms with automated underwriting and onboarding that supports marketplaces and split payments.  And with one integration and contract, businesses can sell in over 200 geographies with access to local acquiring in 47 countries, 110+ currencies and 100+ global payment types, including popular eWallets, automated accounts receivable, world-class fraud protection and chargeback management, built-in solutions for regulation and tax compliance, and unified global reporting to help businesses grow.  With a US headquarters in Waltham, MA, and EU headquarters in Dublin, Ireland, BlueSnap is backed by world-class private equity investors including Great Hill Partners and Parthenon Capital Partners.   Learn more at BlueSnap.com

    The version of the OpenAPI document: 8976-Tools
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from blue_snap_python_sdk.client_custom import ClientCustom
from blue_snap_python_sdk.configuration import Configuration
from blue_snap_python_sdk.api_client import ApiClient
from blue_snap_python_sdk.type_util import copy_signature
from blue_snap_python_sdk.apis.tags.agreement_api import AgreementApi
from blue_snap_python_sdk.apis.tags.authorization_api import AuthorizationApi
from blue_snap_python_sdk.apis.tags.plan_api import PlanApi
from blue_snap_python_sdk.apis.tags.reversal_api import ReversalApi
from blue_snap_python_sdk.apis.tags.shopper_api import ShopperApi
from blue_snap_python_sdk.apis.tags.subscription_api import SubscriptionApi
from blue_snap_python_sdk.apis.tags.transaction_api import TransactionApi
from blue_snap_python_sdk.apis.tags.vendor_api import VendorApi



class BlueSnap(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.agreement: AgreementApi = AgreementApi(api_client)
        self.authorization: AuthorizationApi = AuthorizationApi(api_client)
        self.plan: PlanApi = PlanApi(api_client)
        self.reversal: ReversalApi = ReversalApi(api_client)
        self.shopper: ShopperApi = ShopperApi(api_client)
        self.subscription: SubscriptionApi = SubscriptionApi(api_client)
        self.transaction: TransactionApi = TransactionApi(api_client)
        self.vendor: VendorApi = VendorApi(api_client)
