operation_parameter_map = {
    '/agreements/debit/{region}/{type}-POST': {
        'parameters': [
            {
                'name': 'region'
            },
            {
                'name': 'type'
            },
            {
                'name': 'planid'
            },
            {
                'name': 'overriderecurringchargeamount'
            },
        ]
    },
    '/agreements/{agreementId}-GET': {
        'parameters': [
            {
                'name': 'agreementId'
            },
        ]
    },
    '/transactions-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'cardHolderInfo'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'creditCard'
            },
            {
                'name': 'cardTransactionType'
            },
        ]
    },
    '/recurring/plans-POST': {
        'parameters': [
            {
                'name': 'chargeFrequency'
            },
            {
                'name': 'gracePeriodDays'
            },
            {
                'name': 'trialPeriodDays'
            },
            {
                'name': 'initialChargeAmount'
            },
            {
                'name': 'name'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'maxNumberOfCharges'
            },
            {
                'name': 'recurringChargeAmount'
            },
            {
                'name': 'chargeOnPlanSwitch'
            },
        ]
    },
    '/recurring/plans?{parameters}-GET': {
        'parameters': [
            {
                'name': 'pagesize'
            },
            {
                'name': 'after'
            },
            {
                'name': 'gettotal'
            },
            {
                'name': 'fulldescription'
            },
        ]
    },
    '/recurring/plans/{planId}-GET': {
        'parameters': [
            {
                'name': 'planId'
            },
        ]
    },
    '/recurring/plans/{planId}-PUT': {
        'parameters': [
            {
                'name': 'planId'
            },
            {
                'name': 'chargeFrequency'
            },
            {
                'name': 'trialPeriodDays'
            },
            {
                'name': 'initialChargeAmount'
            },
            {
                'name': 'name'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'recurringChargeAmount'
            },
        ]
    },
    '/transactions-PUT': {
        'parameters': [
            {
                'name': 'cardTransactionType'
            },
            {
                'name': 'transactionId'
            },
        ]
    },
    '/vaulted-shoppers-POST': {
        'parameters': [
            {
                'name': 'paymentSources'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
        ]
    },
    '/vaulted-shoppers/{vaultedShopperId}-DELETE': {
        'parameters': [
            {
                'name': 'vaultedShopperId'
            },
        ]
    },
    '/vaulted-shoppers/{vaultedShopperId}-GET': {
        'parameters': [
            {
                'name': 'vaultedShopperId'
            },
        ]
    },
    '/vaulted-shoppers/{vaultedShopperId}-PUT': {
        'parameters': [
            {
                'name': 'vaultedShopperId'
            },
            {
                'name': 'paymentSources'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
        ]
    },
    '/recurring/ondemand/{subscriptionId}-POST': {
        'parameters': [
            {
                'name': 'subscriptionId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'merchantTransactionId'
            },
            {
                'name': 'taxReference'
            },
        ]
    },
    '/recurring/ondemand-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'payerInfo'
            },
            {
                'name': 'paymentSource'
            },
        ]
    },
    '/recurring/subscriptions-POST': {
        'parameters': [
            {
                'name': 'payerInfo'
            },
            {
                'name': 'paymentSource'
            },
            {
                'name': 'planId'
            },
        ]
    },
    '/recurring/subscriptions/{subscriptionId}-GET': {
        'parameters': [
            {
                'name': 'subscriptionId'
            },
        ]
    },
    '/recurring/subscriptions/:subscriptionId/switch-charge-amount-GET': {
        'parameters': [
            {
                'name': 'newplanid'
            },
            {
                'name': 'newquantity'
            },
        ]
    },
    '/recurring/subscriptions?{parameters}-GET': {
        'parameters': [
            {
                'name': 'pagesize'
            },
            {
                'name': 'after'
            },
            {
                'name': 'gettotal'
            },
            {
                'name': 'fulldescription'
            },
        ]
    },
    '/:subscriptionId/charges?{parameters}-GET': {
        'parameters': [
            {
                'name': 'pagesize'
            },
            {
                'name': 'after'
            },
            {
                'name': 'fulldescription'
            },
        ]
    },
    '/recurring/subscriptions/{subscriptionId}-PUT': {
        'parameters': [
            {
                'name': 'subscriptionId'
            },
            {
                'name': 'planId'
            },
        ]
    },
    '/transactions/approval-PUT': {
        'parameters': [
            {
                'name': 'transactionid'
            },
            {
                'name': 'approvetransaction'
            },
        ]
    },
    '/transactions/pending-refund/{transactionId}-DELETE': {
        'parameters': [
            {
                'name': 'transactionId'
            },
        ]
    },
    '/batch-transactions-POST': {
        'parameters': [
            {
                'name': 'batchTransaction'
            },
        ]
    },
    '/alt-transactions-POST': {
        'parameters': [
            {
                'name': 'ecpTransaction'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'payerInfo'
            },
            {
                'name': 'softDescriptor'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'authorizedByShopper'
            },
            {
                'name': 'becsDirectDebitTransaction'
            },
            {
                'name': 'idealTransaction'
            },
            {
                'name': 'localBankTransferTransaction'
            },
            {
                'name': 'paypalTransaction'
            },
            {
                'name': 'acssDirectDebitTransaction'
            },
            {
                'name': 'sepaDirectDebitTransaction'
            },
            {
                'name': 'sofortTransaction'
            },
        ]
    },
    '/batch-transactions/{batchId}-GET': {
        'parameters': [
            {
                'name': 'batchId'
            },
        ]
    },
    '/transactions/{transactionId}-GET': {
        'parameters': [
            {
                'name': 'transactionId'
            },
        ]
    },
    '/alt-transactions/resolve?orderId={orderId}-GET': {
        'parameters': [
            {
                'name': 'orderId'
            },
        ]
    },
    '/agreements/prenotification/{transactionId}-GET': {
        'parameters': [
            {
                'name': 'transactionId'
            },
        ]
    },
    '/alt-transactions/{transactionId}-GET': {
        'parameters': [
            {
                'name': 'transactionId'
            },
        ]
    },
    '/alt-transactions/resolve-GET': {
        'parameters': [
            {
                'name': 'orderId'
            },
        ]
    },
    '/transactions/refund/{transactionId}-POST': {
        'parameters': [
            {
                'name': 'transactionId'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'cancelSubscriptions'
            },
            {
                'name': 'transactionMetaData'
            },
        ]
    },
    '/alt-transactions-PUT': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'paypalTransaction'
            },
        ]
    },
    '/vendors-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'defaultPayoutCurrency'
            },
            {
                'name': 'ipnUrl'
            },
            {
                'name': 'vendorPrincipal'
            },
            {
                'name': 'vendorAgreement'
            },
            {
                'name': 'payoutInfo'
            },
        ]
    },
    '/vendors?{parameters}-GET': {
        'parameters': [
            {
                'name': 'gettotal'
            },
        ]
    },
    '/vendors/{vendorId}-GET': {
        'parameters': [
            {
                'name': 'vendorId'
            },
        ]
    },
    '/vendors/{vendorId}-PUT': {
        'parameters': [
            {
                'name': 'vendorId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'name'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'state'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'vendorUrl'
            },
            {
                'name': 'ipnUrl'
            },
            {
                'name': 'defaultPayoutCurrency'
            },
            {
                'name': 'vendorPrincipal'
            },
            {
                'name': 'payoutInfo'
            },
            {
                'name': 'vendorAgreement'
            },
        ]
    },
};