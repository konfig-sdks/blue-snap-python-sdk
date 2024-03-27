import typing_extensions

from blue_snap_python_sdk.paths import PathValues
from blue_snap_python_sdk.apis.paths.transactions import Transactions
from blue_snap_python_sdk.apis.paths.transactions_transaction_id import TransactionsTransactionId
from blue_snap_python_sdk.apis.paths.alt_transactions import AltTransactions
from blue_snap_python_sdk.apis.paths.alt_transactions_transaction_id import AltTransactionsTransactionId
from blue_snap_python_sdk.apis.paths.alt_transactions_resolve import AltTransactionsResolve
from blue_snap_python_sdk.apis.paths.agreements_debit_region_type import AgreementsDebitRegionType
from blue_snap_python_sdk.apis.paths.agreements_agreement_id import AgreementsAgreementId
from blue_snap_python_sdk.apis.paths.agreements_prenotification_transaction_id import AgreementsPrenotificationTransactionId
from blue_snap_python_sdk.apis.paths.alt_transactions_resolveorder_idorder_id import AltTransactionsResolveorderIdorderId
from blue_snap_python_sdk.apis.paths.batch_transactions import BatchTransactions
from blue_snap_python_sdk.apis.paths.batch_transactions_batch_id import BatchTransactionsBatchId
from blue_snap_python_sdk.apis.paths.transactions_refund_transaction_id import TransactionsRefundTransactionId
from blue_snap_python_sdk.apis.paths.transactions_pending_refund_transaction_id import TransactionsPendingRefundTransactionId
from blue_snap_python_sdk.apis.paths.vaulted_shoppers import VaultedShoppers
from blue_snap_python_sdk.apis.paths.vaulted_shoppers_vaulted_shopper_id import VaultedShoppersVaultedShopperId
from blue_snap_python_sdk.apis.paths.recurring_plans import RecurringPlans
from blue_snap_python_sdk.apis.paths.recurring_plans_plan_id import RecurringPlansPlanId
from blue_snap_python_sdk.apis.paths.recurring_plansparameters import RecurringPlansparameters
from blue_snap_python_sdk.apis.paths.recurring_subscriptions import RecurringSubscriptions
from blue_snap_python_sdk.apis.paths.recurring_subscriptions_subscription_id import RecurringSubscriptionsSubscriptionId
from blue_snap_python_sdk.apis.paths.recurring_ondemand import RecurringOndemand
from blue_snap_python_sdk.apis.paths.recurring_ondemand_subscription_id import RecurringOndemandSubscriptionId
from blue_snap_python_sdk.apis.paths.recurring_subscriptionsparameters import RecurringSubscriptionsparameters
from blue_snap_python_sdk.apis.paths.subscription_id_chargesparameters import SubscriptionIdChargesparameters
from blue_snap_python_sdk.apis.paths.recurring_subscriptions_subscription_id_switch_charge_amount import RecurringSubscriptionsSubscriptionIdSwitchChargeAmount
from blue_snap_python_sdk.apis.paths.transactions_approval import TransactionsApproval
from blue_snap_python_sdk.apis.paths.vendors import Vendors
from blue_snap_python_sdk.apis.paths.vendors_vendor_id import VendorsVendorId
from blue_snap_python_sdk.apis.paths.vendorsparameters import Vendorsparameters

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TRANSACTIONS: Transactions,
        PathValues.TRANSACTIONS_TRANSACTION_ID: TransactionsTransactionId,
        PathValues.ALTTRANSACTIONS: AltTransactions,
        PathValues.ALTTRANSACTIONS_TRANSACTION_ID: AltTransactionsTransactionId,
        PathValues.ALTTRANSACTIONS_RESOLVE: AltTransactionsResolve,
        PathValues.AGREEMENTS_DEBIT_REGION_TYPE: AgreementsDebitRegionType,
        PathValues.AGREEMENTS_AGREEMENT_ID: AgreementsAgreementId,
        PathValues.AGREEMENTS_PRENOTIFICATION_TRANSACTION_ID: AgreementsPrenotificationTransactionId,
        PathValues.ALTTRANSACTIONS_RESOLVEORDER_IDORDER_ID: AltTransactionsResolveorderIdorderId,
        PathValues.BATCHTRANSACTIONS: BatchTransactions,
        PathValues.BATCHTRANSACTIONS_BATCH_ID: BatchTransactionsBatchId,
        PathValues.TRANSACTIONS_REFUND_TRANSACTION_ID: TransactionsRefundTransactionId,
        PathValues.TRANSACTIONS_PENDINGREFUND_TRANSACTION_ID: TransactionsPendingRefundTransactionId,
        PathValues.VAULTEDSHOPPERS: VaultedShoppers,
        PathValues.VAULTEDSHOPPERS_VAULTED_SHOPPER_ID: VaultedShoppersVaultedShopperId,
        PathValues.RECURRING_PLANS: RecurringPlans,
        PathValues.RECURRING_PLANS_PLAN_ID: RecurringPlansPlanId,
        PathValues.RECURRING_PLANSPARAMETERS: RecurringPlansparameters,
        PathValues.RECURRING_SUBSCRIPTIONS: RecurringSubscriptions,
        PathValues.RECURRING_SUBSCRIPTIONS_SUBSCRIPTION_ID: RecurringSubscriptionsSubscriptionId,
        PathValues.RECURRING_ONDEMAND: RecurringOndemand,
        PathValues.RECURRING_ONDEMAND_SUBSCRIPTION_ID: RecurringOndemandSubscriptionId,
        PathValues.RECURRING_SUBSCRIPTIONSPARAMETERS: RecurringSubscriptionsparameters,
        PathValues.SUBSCRIPTION_ID_CHARGESPARAMETERS: SubscriptionIdChargesparameters,
        PathValues.RECURRING_SUBSCRIPTIONS_SUBSCRIPTION_ID_SWITCHCHARGEAMOUNT: RecurringSubscriptionsSubscriptionIdSwitchChargeAmount,
        PathValues.TRANSACTIONS_APPROVAL: TransactionsApproval,
        PathValues.VENDORS: Vendors,
        PathValues.VENDORS_VENDOR_ID: VendorsVendorId,
        PathValues.VENDORSPARAMETERS: Vendorsparameters,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TRANSACTIONS: Transactions,
        PathValues.TRANSACTIONS_TRANSACTION_ID: TransactionsTransactionId,
        PathValues.ALTTRANSACTIONS: AltTransactions,
        PathValues.ALTTRANSACTIONS_TRANSACTION_ID: AltTransactionsTransactionId,
        PathValues.ALTTRANSACTIONS_RESOLVE: AltTransactionsResolve,
        PathValues.AGREEMENTS_DEBIT_REGION_TYPE: AgreementsDebitRegionType,
        PathValues.AGREEMENTS_AGREEMENT_ID: AgreementsAgreementId,
        PathValues.AGREEMENTS_PRENOTIFICATION_TRANSACTION_ID: AgreementsPrenotificationTransactionId,
        PathValues.ALTTRANSACTIONS_RESOLVEORDER_IDORDER_ID: AltTransactionsResolveorderIdorderId,
        PathValues.BATCHTRANSACTIONS: BatchTransactions,
        PathValues.BATCHTRANSACTIONS_BATCH_ID: BatchTransactionsBatchId,
        PathValues.TRANSACTIONS_REFUND_TRANSACTION_ID: TransactionsRefundTransactionId,
        PathValues.TRANSACTIONS_PENDINGREFUND_TRANSACTION_ID: TransactionsPendingRefundTransactionId,
        PathValues.VAULTEDSHOPPERS: VaultedShoppers,
        PathValues.VAULTEDSHOPPERS_VAULTED_SHOPPER_ID: VaultedShoppersVaultedShopperId,
        PathValues.RECURRING_PLANS: RecurringPlans,
        PathValues.RECURRING_PLANS_PLAN_ID: RecurringPlansPlanId,
        PathValues.RECURRING_PLANSPARAMETERS: RecurringPlansparameters,
        PathValues.RECURRING_SUBSCRIPTIONS: RecurringSubscriptions,
        PathValues.RECURRING_SUBSCRIPTIONS_SUBSCRIPTION_ID: RecurringSubscriptionsSubscriptionId,
        PathValues.RECURRING_ONDEMAND: RecurringOndemand,
        PathValues.RECURRING_ONDEMAND_SUBSCRIPTION_ID: RecurringOndemandSubscriptionId,
        PathValues.RECURRING_SUBSCRIPTIONSPARAMETERS: RecurringSubscriptionsparameters,
        PathValues.SUBSCRIPTION_ID_CHARGESPARAMETERS: SubscriptionIdChargesparameters,
        PathValues.RECURRING_SUBSCRIPTIONS_SUBSCRIPTION_ID_SWITCHCHARGEAMOUNT: RecurringSubscriptionsSubscriptionIdSwitchChargeAmount,
        PathValues.TRANSACTIONS_APPROVAL: TransactionsApproval,
        PathValues.VENDORS: Vendors,
        PathValues.VENDORS_VENDOR_ID: VendorsVendorId,
        PathValues.VENDORSPARAMETERS: Vendorsparameters,
    }
)
