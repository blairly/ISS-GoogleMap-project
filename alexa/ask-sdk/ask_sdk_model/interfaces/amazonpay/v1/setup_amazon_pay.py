# coding: utf-8

#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
    from datetime import datetime
    from ask_sdk_model.interfaces.amazonpay.model.v1.billing_agreement_attributes import BillingAgreementAttributes


class SetupAmazonPay(object):
    """
    Setup Amazon Pay Request Object  # noqa: E501

    NOTE: This class is auto generated.
    Do not edit the class manually.

    :param consent_token: Authorization token that contains the permissions consented to by the user.  # noqa: E501
    :type consent_token: (optional) str
    :param seller_id: The seller ID (also known as merchant ID). If you are an Ecommerce Provider (Solution Provider), please specify the ID of the merchant, not your provider ID.  # noqa: E501
    :type seller_id: (optional) str
    :param country_of_establishment: The country in which the merchant has registered, as an Amazon Payments legal entity.  # noqa: E501
    :type country_of_establishment: (optional) str
    :param ledger_currency: The currency of the merchant’s ledger account.  # noqa: E501
    :type ledger_currency: (optional) str
    :param checkout_language: The merchant&#39;s preferred language for checkout.  # noqa: E501
    :type checkout_language: (optional) str
    :type billing_agreement_attributes: (optional) ask_sdk_model.interfaces.amazonpay.model.v1.billing_agreement_attributes.BillingAgreementAttributes
    :param need_amazon_shipping_address: To receive the default user shipping address in the response, set this parameter to true. Not required if a user shipping address is not required.  # noqa: E501
    :type need_amazon_shipping_address: bool
    :param sandbox_mode: To test in Sandbox mode, set this parameter to true.  # noqa: E501
    :type sandbox_mode: bool
    :param sandbox_customer_email_id: Use this parameter to create a Sandbox payment object. In order to use this parameter, you first create a Sandbox user account in Seller Central. Then, pass the email address associated with that Sandbox user account.  # noqa: E501
    :type sandbox_customer_email_id: (optional) str
    """
    deserialized_types = {
        'consent_token': 'str',
        'seller_id': 'str',
        'country_of_establishment': 'str',
        'ledger_currency': 'str',
        'checkout_language': 'str',
        'billing_agreement_attributes': 'ask_sdk_model.interfaces.amazonpay.model.v1.billing_agreement_attributes.BillingAgreementAttributes',
        'need_amazon_shipping_address': 'bool',
        'sandbox_mode': 'bool',
        'sandbox_customer_email_id': 'str'
    }

    attribute_map = {
        'consent_token': 'consentToken',
        'seller_id': 'sellerId',
        'country_of_establishment': 'countryOfEstablishment',
        'ledger_currency': 'ledgerCurrency',
        'checkout_language': 'checkoutLanguage',
        'billing_agreement_attributes': 'billingAgreementAttributes',
        'need_amazon_shipping_address': 'needAmazonShippingAddress',
        'sandbox_mode': 'sandboxMode',
        'sandbox_customer_email_id': 'sandboxCustomerEmailId'
    }

    def __init__(self, consent_token=None, seller_id=None, country_of_establishment=None, ledger_currency=None, checkout_language=None, billing_agreement_attributes=None, need_amazon_shipping_address=False, sandbox_mode=False, sandbox_customer_email_id=None):  # noqa: E501
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[str], Optional[BillingAgreementAttributes], Optional[bool], Optional[bool], Optional[str]) -> None
        """Setup Amazon Pay Request Object  # noqa: E501

        :param consent_token: Authorization token that contains the permissions consented to by the user.  # noqa: E501
        :type consent_token: (optional) str
        :param seller_id: The seller ID (also known as merchant ID). If you are an Ecommerce Provider (Solution Provider), please specify the ID of the merchant, not your provider ID.  # noqa: E501
        :type seller_id: (optional) str
        :param country_of_establishment: The country in which the merchant has registered, as an Amazon Payments legal entity.  # noqa: E501
        :type country_of_establishment: (optional) str
        :param ledger_currency: The currency of the merchant’s ledger account.  # noqa: E501
        :type ledger_currency: (optional) str
        :param checkout_language: The merchant&#39;s preferred language for checkout.  # noqa: E501
        :type checkout_language: (optional) str
        :type billing_agreement_attributes: (optional) ask_sdk_model.interfaces.amazonpay.model.v1.billing_agreement_attributes.BillingAgreementAttributes
        :param need_amazon_shipping_address: To receive the default user shipping address in the response, set this parameter to true. Not required if a user shipping address is not required.  # noqa: E501
        :type need_amazon_shipping_address: bool
        :param sandbox_mode: To test in Sandbox mode, set this parameter to true.  # noqa: E501
        :type sandbox_mode: bool
        :param sandbox_customer_email_id: Use this parameter to create a Sandbox payment object. In order to use this parameter, you first create a Sandbox user account in Seller Central. Then, pass the email address associated with that Sandbox user account.  # noqa: E501
        :type sandbox_customer_email_id: (optional) str
        """
        self.__discriminator_value = None

        self.consent_token = consent_token
        self.seller_id = seller_id
        self.country_of_establishment = country_of_establishment
        self.ledger_currency = ledger_currency
        self.checkout_language = checkout_language
        self.billing_agreement_attributes = billing_agreement_attributes
        self.need_amazon_shipping_address = need_amazon_shipping_address
        self.sandbox_mode = sandbox_mode
        self.sandbox_customer_email_id = sandbox_customer_email_id

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, SetupAmazonPay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other