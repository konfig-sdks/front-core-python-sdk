# coding: utf-8
"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

import typing
import inspect
from datetime import date, datetime
from front_core_python_sdk.client_custom import ClientCustom
from front_core_python_sdk.configuration import Configuration
from front_core_python_sdk.api_client import ApiClient
from front_core_python_sdk.type_util import copy_signature
from front_core_python_sdk.apis.tags.accounts_api import AccountsApi
from front_core_python_sdk.apis.tags.analytics_api import AnalyticsApi
from front_core_python_sdk.apis.tags.attachments_api import AttachmentsApi
from front_core_python_sdk.apis.tags.channels_api import ChannelsApi
from front_core_python_sdk.apis.tags.comments_api import CommentsApi
from front_core_python_sdk.apis.tags.contact_groups_api import ContactGroupsApi
from front_core_python_sdk.apis.tags.contact_handles_api import ContactHandlesApi
from front_core_python_sdk.apis.tags.contact_notes_api import ContactNotesApi
from front_core_python_sdk.apis.tags.contacts_api import ContactsApi
from front_core_python_sdk.apis.tags.conversations_api import ConversationsApi
from front_core_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from front_core_python_sdk.apis.tags.drafts_api import DraftsApi
from front_core_python_sdk.apis.tags.events_api import EventsApi
from front_core_python_sdk.apis.tags.inboxes_api import InboxesApi
from front_core_python_sdk.apis.tags.knowledge_bases_api import KnowledgeBasesApi
from front_core_python_sdk.apis.tags.links_api import LinksApi
from front_core_python_sdk.apis.tags.message_template_folders_api import MessageTemplateFoldersApi
from front_core_python_sdk.apis.tags.message_templates_api import MessageTemplatesApi
from front_core_python_sdk.apis.tags.messages_api import MessagesApi
from front_core_python_sdk.apis.tags.rules_api import RulesApi
from front_core_python_sdk.apis.tags.shifts_api import ShiftsApi
from front_core_python_sdk.apis.tags.signatures_api import SignaturesApi
from front_core_python_sdk.apis.tags.tags_api import TagsApi
from front_core_python_sdk.apis.tags.teammates_api import TeammatesApi
from front_core_python_sdk.apis.tags.teams_api import TeamsApi
from front_core_python_sdk.apis.tags.token_identity_api import TokenIdentityApi



class FrontCore(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.accounts: AccountsApi = AccountsApi(api_client)
        self.analytics: AnalyticsApi = AnalyticsApi(api_client)
        self.attachments: AttachmentsApi = AttachmentsApi(api_client)
        self.channels: ChannelsApi = ChannelsApi(api_client)
        self.comments: CommentsApi = CommentsApi(api_client)
        self.contact_groups: ContactGroupsApi = ContactGroupsApi(api_client)
        self.contact_handles: ContactHandlesApi = ContactHandlesApi(api_client)
        self.contact_notes: ContactNotesApi = ContactNotesApi(api_client)
        self.contacts: ContactsApi = ContactsApi(api_client)
        self.conversations: ConversationsApi = ConversationsApi(api_client)
        self.custom_fields: CustomFieldsApi = CustomFieldsApi(api_client)
        self.drafts: DraftsApi = DraftsApi(api_client)
        self.events: EventsApi = EventsApi(api_client)
        self.inboxes: InboxesApi = InboxesApi(api_client)
        self.knowledge_bases: KnowledgeBasesApi = KnowledgeBasesApi(api_client)
        self.links: LinksApi = LinksApi(api_client)
        self.message_template_folders: MessageTemplateFoldersApi = MessageTemplateFoldersApi(api_client)
        self.message_templates: MessageTemplatesApi = MessageTemplatesApi(api_client)
        self.messages: MessagesApi = MessagesApi(api_client)
        self.rules: RulesApi = RulesApi(api_client)
        self.shifts: ShiftsApi = ShiftsApi(api_client)
        self.signatures: SignaturesApi = SignaturesApi(api_client)
        self.tags: TagsApi = TagsApi(api_client)
        self.teammates: TeammatesApi = TeammatesApi(api_client)
        self.teams: TeamsApi = TeamsApi(api_client)
        self.token_identity: TokenIdentityApi = TokenIdentityApi(api_client)
