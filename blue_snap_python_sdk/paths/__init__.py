# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from blue_snap_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TRANSACTIONS = "/transactions"
    TRANSACTIONS_TRANSACTION_ID = "/transactions/{transactionId}"
    ALTTRANSACTIONS = "/alt-transactions"
    ALTTRANSACTIONS_TRANSACTION_ID = "/alt-transactions/{transactionId}"
    ALTTRANSACTIONS_RESOLVE = "/alt-transactions/resolve"
    AGREEMENTS_DEBIT_REGION_TYPE = "/agreements/debit/{region}/{type}"
    AGREEMENTS_AGREEMENT_ID = "/agreements/{agreementId}"
    AGREEMENTS_PRENOTIFICATION_TRANSACTION_ID = "/agreements/prenotification/{transactionId}"
    ALTTRANSACTIONS_RESOLVEORDER_IDORDER_ID = "/alt-transactions/resolve?orderId&#x3D;{orderId}"
    BATCHTRANSACTIONS = "/batch-transactions"
    BATCHTRANSACTIONS_BATCH_ID = "/batch-transactions/{batchId}"
    TRANSACTIONS_REFUND_TRANSACTION_ID = "/transactions/refund/{transactionId}"
    TRANSACTIONS_PENDINGREFUND_TRANSACTION_ID = "/transactions/pending-refund/{transactionId}"
    VAULTEDSHOPPERS = "/vaulted-shoppers"
    VAULTEDSHOPPERS_VAULTED_SHOPPER_ID = "/vaulted-shoppers/{vaultedShopperId}"
    RECURRING_PLANS = "/recurring/plans"
    RECURRING_PLANS_PLAN_ID = "/recurring/plans/{planId}"
    RECURRING_PLANSPARAMETERS = "/recurring/plans?{parameters}"
    RECURRING_SUBSCRIPTIONS = "/recurring/subscriptions"
    RECURRING_SUBSCRIPTIONS_SUBSCRIPTION_ID = "/recurring/subscriptions/{subscriptionId}"
    RECURRING_ONDEMAND = "/recurring/ondemand"
    RECURRING_ONDEMAND_SUBSCRIPTION_ID = "/recurring/ondemand/{subscriptionId}"
    RECURRING_SUBSCRIPTIONSPARAMETERS = "/recurring/subscriptions?{parameters}"
    SUBSCRIPTION_ID_CHARGESPARAMETERS = "/:subscriptionId/charges?{parameters}"
    RECURRING_SUBSCRIPTIONS_SUBSCRIPTION_ID_SWITCHCHARGEAMOUNT = "/recurring/subscriptions/:subscriptionId/switch-charge-amount"
    TRANSACTIONS_APPROVAL = "/transactions/approval"
    VENDORS = "/vendors"
    VENDORS_VENDOR_ID = "/vendors/{vendorId}"
    VENDORSPARAMETERS = "/vendors?{parameters}"
