import typing_extensions

from blue_snap_python_sdk.apis.tags import TagValues
from blue_snap_python_sdk.apis.tags.transaction_api import TransactionApi
from blue_snap_python_sdk.apis.tags.subscription_api import SubscriptionApi
from blue_snap_python_sdk.apis.tags.plan_api import PlanApi
from blue_snap_python_sdk.apis.tags.shopper_api import ShopperApi
from blue_snap_python_sdk.apis.tags.vendor_api import VendorApi
from blue_snap_python_sdk.apis.tags.agreement_api import AgreementApi
from blue_snap_python_sdk.apis.tags.reversal_api import ReversalApi
from blue_snap_python_sdk.apis.tags.authorization_api import AuthorizationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TRANSACTION: TransactionApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.PLAN: PlanApi,
        TagValues.SHOPPER: ShopperApi,
        TagValues.VENDOR: VendorApi,
        TagValues.AGREEMENT: AgreementApi,
        TagValues.REVERSAL: ReversalApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TRANSACTION: TransactionApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.PLAN: PlanApi,
        TagValues.SHOPPER: ShopperApi,
        TagValues.VENDOR: VendorApi,
        TagValues.AGREEMENT: AgreementApi,
        TagValues.REVERSAL: ReversalApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
    }
)
