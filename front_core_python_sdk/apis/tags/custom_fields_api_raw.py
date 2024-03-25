# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.links_custom_fields.get import GetListRaw
from front_core_python_sdk.paths.accounts_custom_fields.get import ListAccountCustomFieldsRaw
from front_core_python_sdk.paths.custom_fields.get import ListContactCustomFieldsRaw
from front_core_python_sdk.paths.contacts_custom_fields.get import ListContactFieldsRaw
from front_core_python_sdk.paths.conversations_custom_fields.get import ListConversationCustomFieldsRaw
from front_core_python_sdk.paths.inboxes_custom_fields.get import ListInboxCustomFieldsRaw
from front_core_python_sdk.paths.teammates_custom_fields.get import ListTeammateCustomFieldsRaw


class CustomFieldsApiRaw(
    GetListRaw,
    ListAccountCustomFieldsRaw,
    ListContactCustomFieldsRaw,
    ListContactFieldsRaw,
    ListConversationCustomFieldsRaw,
    ListInboxCustomFieldsRaw,
    ListTeammateCustomFieldsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass