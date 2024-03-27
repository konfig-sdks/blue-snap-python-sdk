<div align="left">

[![Visit Bluesnap](./header.png)](https://www.bluesnap.com&#x2F;)

# Bluesnap<a id="bluesnap"></a>

At BlueSnap, we look at payments a little differently. Our Payment Orchestration Platform helps businesses accept payments globally and is designed to increase revenue and reduces costs. We provide a comprehensive back-end solutions that simplifies the complexity of payments, managing the full process from start to finish.

BlueSnap supports payments through multiple sales channels such as online and mobile sales, marketplaces, subscriptions, invoice payments and manual orders through a virtual terminal. And for businesses looking for embedded payments, we offer white-labeled payments for platforms with automated underwriting and onboarding that supports marketplaces and split payments.

And with one integration and contract, businesses can sell in over 200 geographies with access to local acquiring in 47 countries, 110+ currencies and 100+ global payment types, including popular eWallets, automated accounts receivable, world-class fraud protection and chargeback management, built-in solutions for regulation and tax compliance, and unified global reporting to help businesses grow.

With a US headquarters in Waltham, MA, and EU headquarters in Dublin, Ireland, BlueSnap is backed by world-class private equity investors including Great Hill Partners and Parthenon Capital Partners. 

Learn more at BlueSnap.com


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`bluesnap.agreement.create_debit_for_aus_can`](#bluesnapagreementcreate_debit_for_aus_can)
  * [`bluesnap.agreement.get_debit`](#bluesnapagreementget_debit)
  * [`bluesnap.authorization.create_transaction`](#bluesnapauthorizationcreate_transaction)
  * [`bluesnap.plan.create_recurring_plan`](#bluesnapplancreate_recurring_plan)
  * [`bluesnap.plan.get_all`](#bluesnapplanget_all)
  * [`bluesnap.plan.get_specific`](#bluesnapplanget_specific)
  * [`bluesnap.plan.update_recurring_plan`](#bluesnapplanupdate_recurring_plan)
  * [`bluesnap.reversal.auth_transaction`](#bluesnapreversalauth_transaction)
  * [`bluesnap.shopper.create_vaulted_shopper`](#bluesnapshoppercreate_vaulted_shopper)
  * [`bluesnap.shopper.delete_vaulted_shopper`](#bluesnapshopperdelete_vaulted_shopper)
  * [`bluesnap.shopper.get`](#bluesnapshopperget)
  * [`bluesnap.shopper.update_vaulted_shopper`](#bluesnapshopperupdate_vaulted_shopper)
  * [`bluesnap.subscription.create_merchant_managed_charge`](#bluesnapsubscriptioncreate_merchant_managed_charge)
  * [`bluesnap.subscription.create_merchant_managed_subscription`](#bluesnapsubscriptioncreate_merchant_managed_subscription)
  * [`bluesnap.subscription.create_new`](#bluesnapsubscriptioncreate_new)
  * [`bluesnap.subscription.get_specific`](#bluesnapsubscriptionget_specific)
  * [`bluesnap.subscription.get_switch_charge_amount`](#bluesnapsubscriptionget_switch_charge_amount)
  * [`bluesnap.subscription.list_all_subscriptions`](#bluesnapsubscriptionlist_all_subscriptions)
  * [`bluesnap.subscription.list_charges`](#bluesnapsubscriptionlist_charges)
  * [`bluesnap.subscription.update_subscription`](#bluesnapsubscriptionupdate_subscription)
  * [`bluesnap.transaction.approve_merchant_transaction`](#bluesnaptransactionapprove_merchant_transaction)
  * [`bluesnap.transaction.cancel_pending_refund`](#bluesnaptransactioncancel_pending_refund)
  * [`bluesnap.transaction.create_batch_transaction`](#bluesnaptransactioncreate_batch_transaction)
  * [`bluesnap.transaction.create_sofort_transaction`](#bluesnaptransactioncreate_sofort_transaction)
  * [`bluesnap.transaction.get_batch_transaction`](#bluesnaptransactionget_batch_transaction)
  * [`bluesnap.transaction.get_by_id`](#bluesnaptransactionget_by_id)
  * [`bluesnap.transaction.get_paypal_transaction`](#bluesnaptransactionget_paypal_transaction)
  * [`bluesnap.transaction.get_pre_notification_debit_agreement`](#bluesnaptransactionget_pre_notification_debit_agreement)
  * [`bluesnap.transaction.get_sepa_dd`](#bluesnaptransactionget_sepa_dd)
  * [`bluesnap.transaction.get_sofort_transaction`](#bluesnaptransactionget_sofort_transaction)
  * [`bluesnap.transaction.initiate_refund`](#bluesnaptransactioninitiate_refund)
  * [`bluesnap.transaction.update_paypal_transaction`](#bluesnaptransactionupdate_paypal_transaction)
  * [`bluesnap.vendor.create`](#bluesnapvendorcreate)
  * [`bluesnap.vendor.get_all_vendors`](#bluesnapvendorget_all_vendors)
  * [`bluesnap.vendor.get_vendor`](#bluesnapvendorget_vendor)
  * [`bluesnap.vendor.update_vendor`](#bluesnapvendorupdate_vendor)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=BlueSnap&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from blue_snap_python_sdk import BlueSnap, ApiException

bluesnap = BlueSnap(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    sec1="YOUR_API_KEY",
)

try:
    # Create Debit Agreement
    bluesnap.agreement.create_debit_for_aus_can(
        region="ca",
        type="onetime",
        planid="string_example",
        overriderecurringchargeamount="string_example",
    )
except ApiException as e:
    print("Exception when calling AgreementApi.create_debit_for_aus_can: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from blue_snap_python_sdk import BlueSnap, ApiException

bluesnap = BlueSnap(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    sec1="YOUR_API_KEY",
)


async def main():
    try:
        # Create Debit Agreement
        await bluesnap.agreement.acreate_debit_for_aus_can(
            region="ca",
            type="onetime",
            planid="string_example",
            overriderecurringchargeamount="string_example",
        )
    except ApiException as e:
        print("Exception when calling AgreementApi.create_debit_for_aus_can: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from blue_snap_python_sdk import BlueSnap, ApiException

bluesnap = BlueSnap(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    sec1="YOUR_API_KEY",
)

try:
    # Create Debit Agreement
    create_debit_for_aus_can_response = bluesnap.agreement.raw.create_debit_for_aus_can(
        region="ca",
        type="onetime",
        planid="string_example",
        overriderecurringchargeamount="string_example",
    )
    pprint(create_debit_for_aus_can_response.headers)
    pprint(create_debit_for_aus_can_response.status)
    pprint(create_debit_for_aus_can_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AgreementApi.create_debit_for_aus_can: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `bluesnap.agreement.create_debit_for_aus_can`<a id="bluesnapagreementcreate_debit_for_aus_can"></a>

for Australia and Canada

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.agreement.create_debit_for_aus_can(
    region="ca",
    type="onetime",
    planid="string_example",
    overriderecurringchargeamount="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### region: `str`<a id="region-str"></a>

Represents the country. Possible Values: `au`, `ca`

##### type: `str`<a id="type-str"></a>

Represents the mandate type. Possible Values: `onetime`,`recurring`, `ondemand`

##### planid: `str`<a id="planid-str"></a>

SKU number

##### overriderecurringchargeamount: `str`<a id="overriderecurringchargeamount-str"></a>

the amount which overrides recurring charge

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/agreements/debit/{region}/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.agreement.get_debit`<a id="bluesnapagreementget_debit"></a>

for Australia and Canada

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.agreement.get_debit(
    agreement_id="1065",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### agreement_id: `str`<a id="agreement_id-str"></a>

Argument included in the response for the Create Debit Agreement request

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/agreements/{agreementId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.authorization.create_transaction`<a id="bluesnapauthorizationcreate_transaction"></a>

Auth Only

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.authorization.create_transaction(
    amount=11,
    soft_descriptor="DescTest",
    card_holder_info={
        "first_name": "test first name",
        "last_name": "test last name",
        "zip": "02453",
    },
    currency="USD",
    credit_card={
        "expiration_year": 2026,
        "security_code": 837,
        "expiration_month": "02",
        "card_number": "4263982640269299",
    },
    card_transaction_type="AUTH_ONLY",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### soft_descriptor: `str`<a id="soft_descriptor-str"></a>

##### card_holder_info: [`AuthorizationCreateTransactionRequestCardHolderInfo`](./blue_snap_python_sdk/type/authorization_create_transaction_request_card_holder_info.py)<a id="card_holder_info-authorizationcreatetransactionrequestcardholderinfoblue_snap_python_sdktypeauthorization_create_transaction_request_card_holder_infopy"></a>


##### currency: `str`<a id="currency-str"></a>

##### credit_card: [`AuthorizationCreateTransactionRequestCreditCard`](./blue_snap_python_sdk/type/authorization_create_transaction_request_credit_card.py)<a id="credit_card-authorizationcreatetransactionrequestcreditcardblue_snap_python_sdktypeauthorization_create_transaction_request_credit_cardpy"></a>


##### card_transaction_type: `str`<a id="card_transaction_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizationCreateTransactionRequest`](./blue_snap_python_sdk/type/authorization_create_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.plan.create_recurring_plan`<a id="bluesnapplancreate_recurring_plan"></a>

Create Plan

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.plan.create_recurring_plan(
    charge_frequency="MONTHLY",
    grace_period_days=10,
    trial_period_days=14,
    initial_charge_amount=100,
    name="Gold Plan",
    currency="USD",
    max_number_of_charges=12,
    recurring_charge_amount=29.99,
    charge_on_plan_switch=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### charge_frequency: `str`<a id="charge_frequency-str"></a>

##### grace_period_days: `int`<a id="grace_period_days-int"></a>

##### trial_period_days: `int`<a id="trial_period_days-int"></a>

##### initial_charge_amount: `int`<a id="initial_charge_amount-int"></a>

##### name: `str`<a id="name-str"></a>

##### currency: `str`<a id="currency-str"></a>

##### max_number_of_charges: `int`<a id="max_number_of_charges-int"></a>

##### recurring_charge_amount: `Union[int, float]`<a id="recurring_charge_amount-unionint-float"></a>

##### charge_on_plan_switch: `bool`<a id="charge_on_plan_switch-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlanCreateRecurringPlanRequest`](./blue_snap_python_sdk/type/plan_create_recurring_plan_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/plans` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.plan.get_all`<a id="bluesnapplanget_all"></a>

Retrieve All Plans

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.plan.get_all(
    pagesize="5",
    after="2185254",
    gettotal=True,
    fulldescription=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `str`<a id="pagesize-str"></a>

##### after: `str`<a id="after-str"></a>

##### gettotal: `bool`<a id="gettotal-bool"></a>

##### fulldescription: `bool`<a id="fulldescription-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/plans?{parameters}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.plan.get_specific`<a id="bluesnapplanget_specific"></a>

Retrieve Specific Plan

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.plan.get_specific(
    plan_id=2283845,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plan_id: `int`<a id="plan_id-int"></a>

BlueSnap identifier for the plan.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/plans/{planId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.plan.update_recurring_plan`<a id="bluesnapplanupdate_recurring_plan"></a>

Update Plan

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.plan.update_recurring_plan(
    plan_id=2111111,
    charge_frequency="MONTHLY",
    trial_period_days="7",
    initial_charge_amount="30",
    name="Gold Plan",
    currency="USD",
    recurring_charge_amount="19",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plan_id: `int`<a id="plan_id-int"></a>

BlueSnap identifier for the plan.

##### charge_frequency: `str`<a id="charge_frequency-str"></a>

##### trial_period_days: `str`<a id="trial_period_days-str"></a>

##### initial_charge_amount: `str`<a id="initial_charge_amount-str"></a>

##### name: `str`<a id="name-str"></a>

##### currency: `str`<a id="currency-str"></a>

##### recurring_charge_amount: `str`<a id="recurring_charge_amount-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlanUpdateRecurringPlanRequest`](./blue_snap_python_sdk/type/plan_update_recurring_plan_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/plans/{planId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.reversal.auth_transaction`<a id="bluesnapreversalauth_transaction"></a>

Auth Reversal

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.reversal.auth_transaction(
    card_transaction_type="AUTH_REVERSAL",
    transaction_id=1011671987,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_transaction_type: `str`<a id="card_transaction_type-str"></a>

##### transaction_id: `int`<a id="transaction_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReversalAuthTransactionRequest`](./blue_snap_python_sdk/type/reversal_auth_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.shopper.create_vaulted_shopper`<a id="bluesnapshoppercreate_vaulted_shopper"></a>

Create Vaulted Shopper

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.shopper.create_vaulted_shopper(
    payment_sources={},
    first_name="FirstName",
    last_name="LastName",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_sources: [`ShopperCreateVaultedShopperRequestPaymentSources`](./blue_snap_python_sdk/type/shopper_create_vaulted_shopper_request_payment_sources.py)<a id="payment_sources-shoppercreatevaultedshopperrequestpaymentsourcesblue_snap_python_sdktypeshopper_create_vaulted_shopper_request_payment_sourcespy"></a>


##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShopperCreateVaultedShopperRequest`](./blue_snap_python_sdk/type/shopper_create_vaulted_shopper_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vaulted-shoppers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.shopper.delete_vaulted_shopper`<a id="bluesnapshopperdelete_vaulted_shopper"></a>

Delete Vaulted Shopper

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.shopper.delete_vaulted_shopper(
    vaulted_shopper_id="20769005",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vaulted_shopper_id: `str`<a id="vaulted_shopper_id-str"></a>

vaultedShopperId received from BlueSnap

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vaulted-shoppers/{vaultedShopperId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.shopper.get`<a id="bluesnapshopperget"></a>

Retrieve Vaulted Shopper

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.shopper.get(
    vaulted_shopper_id="20769005",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vaulted_shopper_id: `str`<a id="vaulted_shopper_id-str"></a>

vaultedShopperId received from BlueSnap

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vaulted-shoppers/{vaultedShopperId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.shopper.update_vaulted_shopper`<a id="bluesnapshopperupdate_vaulted_shopper"></a>

Update Vaulted Shopper

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.shopper.update_vaulted_shopper(
    vaulted_shopper_id="40444721",
    payment_sources={},
    first_name="FirstName",
    last_name="LastName",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vaulted_shopper_id: `str`<a id="vaulted_shopper_id-str"></a>

vaultedShopperId received from BlueSnap

##### payment_sources: [`ShopperUpdateVaultedShopperRequestPaymentSources`](./blue_snap_python_sdk/type/shopper_update_vaulted_shopper_request_payment_sources.py)<a id="payment_sources-shopperupdatevaultedshopperrequestpaymentsourcesblue_snap_python_sdktypeshopper_update_vaulted_shopper_request_payment_sourcespy"></a>


##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShopperUpdateVaultedShopperRequest`](./blue_snap_python_sdk/type/shopper_update_vaulted_shopper_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vaulted-shoppers/{vaultedShopperId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.create_merchant_managed_charge`<a id="bluesnapsubscriptioncreate_merchant_managed_charge"></a>

Create Merchant-Managed Subscription Charge

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.create_merchant_managed_charge(
    subscription_id=10543419,
    amount=45,
    currency="USD",
    merchant_transaction_id="MyUniqueOnDemandSubscription",
    tax_reference="048deff0-a285-47e1-bc39-42f79bf0095b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `int`<a id="subscription_id-int"></a>

BlueSnap identifier for the subscription.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### currency: `str`<a id="currency-str"></a>

##### merchant_transaction_id: `str`<a id="merchant_transaction_id-str"></a>

##### tax_reference: `str`<a id="tax_reference-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriptionCreateMerchantManagedChargeRequest`](./blue_snap_python_sdk/type/subscription_create_merchant_managed_charge_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/ondemand/{subscriptionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.create_merchant_managed_subscription`<a id="bluesnapsubscriptioncreate_merchant_managed_subscription"></a>

Create Merchant-Managed Subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.create_merchant_managed_subscription(
    amount=45,
    currency="USD",
    payer_info={
        "first_name": "John",
        "last_name": "Doe",
        "zip": "02453",
        "country": "us",
    },
    payment_source={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### currency: `str`<a id="currency-str"></a>

##### payer_info: [`SubscriptionCreateMerchantManagedSubscriptionRequestPayerInfo`](./blue_snap_python_sdk/type/subscription_create_merchant_managed_subscription_request_payer_info.py)<a id="payer_info-subscriptioncreatemerchantmanagedsubscriptionrequestpayerinfoblue_snap_python_sdktypesubscription_create_merchant_managed_subscription_request_payer_infopy"></a>


##### payment_source: [`SubscriptionCreateMerchantManagedSubscriptionRequestPaymentSource`](./blue_snap_python_sdk/type/subscription_create_merchant_managed_subscription_request_payment_source.py)<a id="payment_source-subscriptioncreatemerchantmanagedsubscriptionrequestpaymentsourceblue_snap_python_sdktypesubscription_create_merchant_managed_subscription_request_payment_sourcepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriptionCreateMerchantManagedSubscriptionRequest`](./blue_snap_python_sdk/type/subscription_create_merchant_managed_subscription_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/ondemand` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.create_new`<a id="bluesnapsubscriptioncreate_new"></a>

Create Subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.create_new(
    payer_info={
        "zip": "02453",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "1234567890",
    },
    payment_source={},
    plan_id=2283845,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payer_info: [`SubscriptionCreateNewRequestPayerInfo`](./blue_snap_python_sdk/type/subscription_create_new_request_payer_info.py)<a id="payer_info-subscriptioncreatenewrequestpayerinfoblue_snap_python_sdktypesubscription_create_new_request_payer_infopy"></a>


##### payment_source: [`SubscriptionCreateNewRequestPaymentSource`](./blue_snap_python_sdk/type/subscription_create_new_request_payment_source.py)<a id="payment_source-subscriptioncreatenewrequestpaymentsourceblue_snap_python_sdktypesubscription_create_new_request_payment_sourcepy"></a>


##### plan_id: `int`<a id="plan_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriptionCreateNewRequest`](./blue_snap_python_sdk/type/subscription_create_new_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/subscriptions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.get_specific`<a id="bluesnapsubscriptionget_specific"></a>

Retrieve Specific Subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.get_specific(
    subscription_id=8491535,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `int`<a id="subscription_id-int"></a>

BlueSnap identifier for the subscription.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/subscriptions/{subscriptionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.get_switch_charge_amount`<a id="bluesnapsubscriptionget_switch_charge_amount"></a>

Retrieve Subscription Switch Charge Amount

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.get_switch_charge_amount(
    newplanid="111111",
    newquantity="2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### newplanid: `str`<a id="newplanid-str"></a>

##### newquantity: `str`<a id="newquantity-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/subscriptions/:subscriptionId/switch-charge-amount` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.list_all_subscriptions`<a id="bluesnapsubscriptionlist_all_subscriptions"></a>

Retrieve All Subscriptions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.list_all_subscriptions(
    pagesize="5",
    after="34567",
    gettotal=True,
    fulldescription=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `str`<a id="pagesize-str"></a>

##### after: `str`<a id="after-str"></a>

##### gettotal: `bool`<a id="gettotal-bool"></a>

##### fulldescription: `bool`<a id="fulldescription-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/subscriptions?{parameters}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.list_charges`<a id="bluesnapsubscriptionlist_charges"></a>

Retrieve All Charges for a Subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.list_charges(
    pagesize="3",
    after="163193",
    fulldescription=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pagesize: `str`<a id="pagesize-str"></a>

##### after: `str`<a id="after-str"></a>

##### fulldescription: `bool`<a id="fulldescription-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/:subscriptionId/charges?{parameters}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.subscription.update_subscription`<a id="bluesnapsubscriptionupdate_subscription"></a>

Update Subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.subscription.update_subscription(
    subscription_id=8491543,
    plan_id="2283849",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `int`<a id="subscription_id-int"></a>

BlueSnap identifier for the subscription.

##### plan_id: `str`<a id="plan_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriptionUpdateSubscriptionRequest`](./blue_snap_python_sdk/type/subscription_update_subscription_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recurring/subscriptions/{subscriptionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.approve_merchant_transaction`<a id="bluesnaptransactionapprove_merchant_transaction"></a>

Merchant Approve Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.approve_merchant_transaction(
    transactionid="38612140",
    approvetransaction=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transactionid: `str`<a id="transactionid-str"></a>

either `transactionid` or `merchanttransactionid` <b>is required</b> <br />ID of the transaction to be approved/declined

##### approvetransaction: `bool`<a id="approvetransaction-bool"></a>

Set to `true` to approve the transaction or to `false` to decline the transaction. Default value is `true`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions/approval` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.cancel_pending_refund`<a id="bluesnaptransactioncancel_pending_refund"></a>

Cancel Pending Refund

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.cancel_pending_refund(
    transaction_id="1109144995",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

transactionId received from BlueSnap

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions/pending-refund/{transactionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.create_batch_transaction`<a id="bluesnaptransactioncreate_batch_transaction"></a>

Create Batch Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.create_batch_transaction(
    batch_transaction={
        "batch_id": "567890",
        "callback_url": "http://example.com/batch_callback",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_transaction: [`TransactionCreateBatchTransactionRequestBatchTransaction`](./blue_snap_python_sdk/type/transaction_create_batch_transaction_request_batch_transaction.py)<a id="batch_transaction-transactioncreatebatchtransactionrequestbatchtransactionblue_snap_python_sdktypetransaction_create_batch_transaction_request_batch_transactionpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionCreateBatchTransactionRequest`](./blue_snap_python_sdk/type/transaction_create_batch_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/batch-transactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.create_sofort_transaction`<a id="bluesnaptransactioncreate_sofort_transaction"></a>

Create Sofort Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.create_sofort_transaction(
    ecp_transaction={
        "routing_number": "011075150",
        "account_type": "CONSUMER_CHECKING",
        "account_number": 4099999992,
    },
    amount=42,
    payer_info={
        "zip": "12345",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "1234567890",
        "country": "uk",
    },
    soft_descriptor="ABC COMPANY",
    currency="GBP",
    authorized_by_shopper=True,
    becs_direct_debit_transaction={
        "bsb_number": "980201",
        "account_number": "9990000001",
        "account_name": "Boris Britva",
        "financial_institution": "financialInstitution",
        "branch_name": "branchName",
        "agreement_id": 81,
    },
    ideal_transaction={
        "return_url": "http://www.returnURL.com",
    },
    local_bank_transfer_transaction={},
    paypal_transaction={
        "cancel_url": "http://www.cancelURL.com",
        "return_url": "http://www.returnURL.com",
        "transaction_type": "SET_ORDER",
    },
    acss_direct_debit_transaction={
        "routing_number": "001004820",
        "account_number": "9990000001",
        "account_type": "PERSONAL",
        "agreement_id": 87,
    },
    sepa_direct_debit_transaction={
        "iban": "DE09100100101234567893",
    },
    sofort_transaction={
        "return_url": "http://www.returnURL.com",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ecp_transaction: [`TransactionCreateSofortTransactionRequestEcpTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_ecp_transaction.py)<a id="ecp_transaction-transactioncreatesoforttransactionrequestecptransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_ecp_transactionpy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### payer_info: [`TransactionCreateSofortTransactionRequestPayerInfo`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_payer_info.py)<a id="payer_info-transactioncreatesoforttransactionrequestpayerinfoblue_snap_python_sdktypetransaction_create_sofort_transaction_request_payer_infopy"></a>


##### soft_descriptor: `str`<a id="soft_descriptor-str"></a>

##### currency: `str`<a id="currency-str"></a>

##### authorized_by_shopper: `bool`<a id="authorized_by_shopper-bool"></a>

##### becs_direct_debit_transaction: [`TransactionCreateSofortTransactionRequestBecsDirectDebitTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_becs_direct_debit_transaction.py)<a id="becs_direct_debit_transaction-transactioncreatesoforttransactionrequestbecsdirectdebittransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_becs_direct_debit_transactionpy"></a>


##### ideal_transaction: [`TransactionCreateSofortTransactionRequestIdealTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_ideal_transaction.py)<a id="ideal_transaction-transactioncreatesoforttransactionrequestidealtransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_ideal_transactionpy"></a>


##### local_bank_transfer_transaction: [`TransactionCreateSofortTransactionRequestLocalBankTransferTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_local_bank_transfer_transaction.py)<a id="local_bank_transfer_transaction-transactioncreatesoforttransactionrequestlocalbanktransfertransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_local_bank_transfer_transactionpy"></a>


##### paypal_transaction: [`TransactionCreateSofortTransactionRequestPaypalTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_paypal_transaction.py)<a id="paypal_transaction-transactioncreatesoforttransactionrequestpaypaltransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_paypal_transactionpy"></a>


##### acss_direct_debit_transaction: [`TransactionCreateSofortTransactionRequestAcssDirectDebitTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_acss_direct_debit_transaction.py)<a id="acss_direct_debit_transaction-transactioncreatesoforttransactionrequestacssdirectdebittransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_acss_direct_debit_transactionpy"></a>


##### sepa_direct_debit_transaction: [`TransactionCreateSofortTransactionRequestSepaDirectDebitTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_sepa_direct_debit_transaction.py)<a id="sepa_direct_debit_transaction-transactioncreatesoforttransactionrequestsepadirectdebittransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_sepa_direct_debit_transactionpy"></a>


##### sofort_transaction: [`TransactionCreateSofortTransactionRequestSofortTransaction`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request_sofort_transaction.py)<a id="sofort_transaction-transactioncreatesoforttransactionrequestsoforttransactionblue_snap_python_sdktypetransaction_create_sofort_transaction_request_sofort_transactionpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionCreateSofortTransactionRequest`](./blue_snap_python_sdk/type/transaction_create_sofort_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alt-transactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.get_batch_transaction`<a id="bluesnaptransactionget_batch_transaction"></a>

Retrieve Batch Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.get_batch_transaction(
    batch_id="567890",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: `str`<a id="batch_id-str"></a>

batch ID sent in the Create Batch Transaction request

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/batch-transactions/{batchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.get_by_id`<a id="bluesnaptransactionget_by_id"></a>

Retrieve

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.get_by_id(
    transaction_id="1011582369",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

transaction ID received in the response from BlueSnap

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions/{transactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.get_paypal_transaction`<a id="bluesnaptransactionget_paypal_transaction"></a>

Retrieve PayPal Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.get_paypal_transaction(
    order_id="5666625",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `str`<a id="order_id-str"></a>

order ID received in the response

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alt-transactions/resolve?orderId&#x3D;{orderId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.get_pre_notification_debit_agreement`<a id="bluesnaptransactionget_pre_notification_debit_agreement"></a>

for Australia and Canada

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.get_pre_notification_debit_agreement(
    transaction_id="38943468",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

Argument included in the response for the Create Debit Agreement request

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/agreements/prenotification/{transactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.get_sepa_dd`<a id="bluesnaptransactionget_sepa_dd"></a>

Retrieve SEPA DD Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.get_sepa_dd(
    transaction_id="1014672453",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

transaction ID received in the response from BlueSnap

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alt-transactions/{transactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.get_sofort_transaction`<a id="bluesnaptransactionget_sofort_transaction"></a>

Retrieve Sofort Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.get_sofort_transaction(
    order_id=20922493,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `int`<a id="order_id-int"></a>

Order ID received in the Create Sofort Transaction response from BlueSnap

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alt-transactions/resolve` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.initiate_refund`<a id="bluesnaptransactioninitiate_refund"></a>

Refund

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.initiate_refund(
    transaction_id="1095710747",
    reason="Refund for order #1992",
    cancel_subscriptions=False,
    transaction_meta_data={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

ID of the transaction to be refunded <br> Required if not using `merchantTransactionId`

##### reason: `str`<a id="reason-str"></a>

##### cancel_subscriptions: `bool`<a id="cancel_subscriptions-bool"></a>

##### transaction_meta_data: [`TransactionInitiateRefundRequestTransactionMetaData`](./blue_snap_python_sdk/type/transaction_initiate_refund_request_transaction_meta_data.py)<a id="transaction_meta_data-transactioninitiaterefundrequesttransactionmetadatablue_snap_python_sdktypetransaction_initiate_refund_request_transaction_meta_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionInitiateRefundRequest`](./blue_snap_python_sdk/type/transaction_initiate_refund_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions/refund/{transactionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.transaction.update_paypal_transaction`<a id="bluesnaptransactionupdate_paypal_transaction"></a>

Update PayPal Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.transaction.update_paypal_transaction(
    amount=105,
    currency="USD",
    paypal_transaction={
        "order_id": "7078033",
        "transaction_type": "DO_ORDER",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

##### currency: `str`<a id="currency-str"></a>

##### paypal_transaction: [`TransactionUpdatePaypalTransactionRequestPaypalTransaction`](./blue_snap_python_sdk/type/transaction_update_paypal_transaction_request_paypal_transaction.py)<a id="paypal_transaction-transactionupdatepaypaltransactionrequestpaypaltransactionblue_snap_python_sdktypetransaction_update_paypal_transaction_request_paypal_transactionpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionUpdatePaypalTransactionRequest`](./blue_snap_python_sdk/type/transaction_update_paypal_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/alt-transactions` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.vendor.create`<a id="bluesnapvendorcreate"></a>

Create Vendor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.vendor.create(
    email="vendor@example.com",
    first_name="Joe",
    last_name="Smith",
    phone="1-123-456-7890",
    address="123 Main Street",
    city="Boston",
    country="US",
    state="MA",
    zip="02453",
    default_payout_currency="USD",
    ipn_url="https://ipnaddress.com",
    vendor_principal={
        "first_name": "Joe",
        "last_name": "Smith",
        "address": "123 Main Street",
        "city": "Boston",
        "country": "US",
        "zip": "02453",
        "dob": "28-09-9999",
        "personal_identification_number": "1234",
        "driver_license_number": "561196411",
        "email": "individual.vendor@bluesnap.com",
    },
    vendor_agreement={
        "commission_percent": 30,
    },
    payout_info={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### address: `str`<a id="address-str"></a>

##### city: `str`<a id="city-str"></a>

##### country: `str`<a id="country-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### default_payout_currency: `str`<a id="default_payout_currency-str"></a>

##### ipn_url: `str`<a id="ipn_url-str"></a>

##### vendor_principal: [`VendorCreateRequestVendorPrincipal`](./blue_snap_python_sdk/type/vendor_create_request_vendor_principal.py)<a id="vendor_principal-vendorcreaterequestvendorprincipalblue_snap_python_sdktypevendor_create_request_vendor_principalpy"></a>


##### vendor_agreement: [`VendorCreateRequestVendorAgreement`](./blue_snap_python_sdk/type/vendor_create_request_vendor_agreement.py)<a id="vendor_agreement-vendorcreaterequestvendoragreementblue_snap_python_sdktypevendor_create_request_vendor_agreementpy"></a>


##### payout_info: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="payout_info-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VendorCreateRequest`](./blue_snap_python_sdk/type/vendor_create_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vendors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.vendor.get_all_vendors`<a id="bluesnapvendorget_all_vendors"></a>

Retrieve All Vendors

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.vendor.get_all_vendors(
    gettotal=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### gettotal: `bool`<a id="gettotal-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vendors?{parameters}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.vendor.get_vendor`<a id="bluesnapvendorget_vendor"></a>

Retrieve Vendor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.vendor.get_vendor(
    vendor_id=837389,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vendor_id: `int`<a id="vendor_id-int"></a>

BlueSnap identifier for the vendor

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vendors/{vendorId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluesnap.vendor.update_vendor`<a id="bluesnapvendorupdate_vendor"></a>

Update Vendor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluesnap.vendor.update_vendor(
    vendor_id=1,
    email="vendor@bluesnap.com",
    name="Important Vendor",
    first_name="Joe",
    last_name="Smith",
    address="123 Main Street",
    city="testing city",
    zip="02453",
    country="US",
    phone="1-054-976-6778",
    state="MA",
    tax_id=123456789,
    vendor_url="http://mycompany.com",
    ipn_url="https://ipnaddress.com",
    default_payout_currency="USD",
    vendor_principal={
        "first_name": "Joe",
        "last_name": "Smith",
        "address": "123 Main Street",
        "city": "Juneau",
        "zip": "02453",
        "country": "US",
        "dob": "28-09-9999",
        "personal_identification_number": 1234,
        "driver_license_number": "561196411",
        "email": "principal.name@vendor.com",
    },
    payout_info=[
        {
            "payout_type": "ACH",
            "base_currency": "USD",
            "name_on_account": "vendor",
            "bank_account_class": "PERSONAL",
            "bank_account_type": "CHECKING",
            "bank_name": "Leumi",
            "bank_id": "123456789",
            "country": "US",
            "city": "Portland",
            "address": "1 bank address",
            "state": "MA",
            "zip": "02453",
            "bank_account_id": "123456789",
            "minimal_payout_amount": 50,
            "payment_reference": "Payment for vendor 1234",
            "refund_reserve": 200,
        }
    ],
    vendor_agreement={
        "commission_percent": 20,
        "account_status": "ACTIVE",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vendor_id: `int`<a id="vendor_id-int"></a>

BlueSnap identifier for the vendor

##### email: `str`<a id="email-str"></a>

##### name: `str`<a id="name-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### address: `str`<a id="address-str"></a>

##### city: `str`<a id="city-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### country: `str`<a id="country-str"></a>

##### phone: `str`<a id="phone-str"></a>

##### state: `str`<a id="state-str"></a>

##### tax_id: `int`<a id="tax_id-int"></a>

##### vendor_url: `str`<a id="vendor_url-str"></a>

##### ipn_url: `str`<a id="ipn_url-str"></a>

##### default_payout_currency: `str`<a id="default_payout_currency-str"></a>

##### vendor_principal: [`VendorUpdateVendorRequestVendorPrincipal`](./blue_snap_python_sdk/type/vendor_update_vendor_request_vendor_principal.py)<a id="vendor_principal-vendorupdatevendorrequestvendorprincipalblue_snap_python_sdktypevendor_update_vendor_request_vendor_principalpy"></a>


##### payout_info: [`VendorUpdateVendorRequestPayoutInfo`](./blue_snap_python_sdk/type/vendor_update_vendor_request_payout_info.py)<a id="payout_info-vendorupdatevendorrequestpayoutinfoblue_snap_python_sdktypevendor_update_vendor_request_payout_infopy"></a>

##### vendor_agreement: [`VendorUpdateVendorRequestVendorAgreement`](./blue_snap_python_sdk/type/vendor_update_vendor_request_vendor_agreement.py)<a id="vendor_agreement-vendorupdatevendorrequestvendoragreementblue_snap_python_sdktypevendor_update_vendor_request_vendor_agreementpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VendorUpdateVendorRequest`](./blue_snap_python_sdk/type/vendor_update_vendor_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vendors/{vendorId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
