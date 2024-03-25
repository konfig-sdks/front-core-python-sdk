import typing_extensions

from front_core_python_sdk.apis.tags import TagValues
from front_core_python_sdk.apis.tags.knowledge_bases_api import KnowledgeBasesApi
from front_core_python_sdk.apis.tags.conversations_api import ConversationsApi
from front_core_python_sdk.apis.tags.tags_api import TagsApi
from front_core_python_sdk.apis.tags.contacts_api import ContactsApi
from front_core_python_sdk.apis.tags.message_template_folders_api import MessageTemplateFoldersApi
from front_core_python_sdk.apis.tags.message_templates_api import MessageTemplatesApi
from front_core_python_sdk.apis.tags.contact_groups_api import ContactGroupsApi
from front_core_python_sdk.apis.tags.inboxes_api import InboxesApi
from front_core_python_sdk.apis.tags.shifts_api import ShiftsApi
from front_core_python_sdk.apis.tags.accounts_api import AccountsApi
from front_core_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from front_core_python_sdk.apis.tags.channels_api import ChannelsApi
from front_core_python_sdk.apis.tags.messages_api import MessagesApi
from front_core_python_sdk.apis.tags.signatures_api import SignaturesApi
from front_core_python_sdk.apis.tags.drafts_api import DraftsApi
from front_core_python_sdk.apis.tags.rules_api import RulesApi
from front_core_python_sdk.apis.tags.links_api import LinksApi
from front_core_python_sdk.apis.tags.teammates_api import TeammatesApi
from front_core_python_sdk.apis.tags.analytics_api import AnalyticsApi
from front_core_python_sdk.apis.tags.comments_api import CommentsApi
from front_core_python_sdk.apis.tags.teams_api import TeamsApi
from front_core_python_sdk.apis.tags.contact_handles_api import ContactHandlesApi
from front_core_python_sdk.apis.tags.contact_notes_api import ContactNotesApi
from front_core_python_sdk.apis.tags.events_api import EventsApi
from front_core_python_sdk.apis.tags.attachments_api import AttachmentsApi
from front_core_python_sdk.apis.tags.token_identity_api import TokenIdentityApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.KNOWLEDGE_BASES: KnowledgeBasesApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.TAGS: TagsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.MESSAGE_TEMPLATE_FOLDERS: MessageTemplateFoldersApi,
        TagValues.MESSAGE_TEMPLATES: MessageTemplatesApi,
        TagValues.CONTACT_GROUPS: ContactGroupsApi,
        TagValues.INBOXES: InboxesApi,
        TagValues.SHIFTS: ShiftsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.CHANNELS: ChannelsApi,
        TagValues.MESSAGES: MessagesApi,
        TagValues.SIGNATURES: SignaturesApi,
        TagValues.DRAFTS: DraftsApi,
        TagValues.RULES: RulesApi,
        TagValues.LINKS: LinksApi,
        TagValues.TEAMMATES: TeammatesApi,
        TagValues.ANALYTICS: AnalyticsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.CONTACT_HANDLES: ContactHandlesApi,
        TagValues.CONTACT_NOTES: ContactNotesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.TOKEN_IDENTITY: TokenIdentityApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.KNOWLEDGE_BASES: KnowledgeBasesApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.TAGS: TagsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.MESSAGE_TEMPLATE_FOLDERS: MessageTemplateFoldersApi,
        TagValues.MESSAGE_TEMPLATES: MessageTemplatesApi,
        TagValues.CONTACT_GROUPS: ContactGroupsApi,
        TagValues.INBOXES: InboxesApi,
        TagValues.SHIFTS: ShiftsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.CHANNELS: ChannelsApi,
        TagValues.MESSAGES: MessagesApi,
        TagValues.SIGNATURES: SignaturesApi,
        TagValues.DRAFTS: DraftsApi,
        TagValues.RULES: RulesApi,
        TagValues.LINKS: LinksApi,
        TagValues.TEAMMATES: TeammatesApi,
        TagValues.ANALYTICS: AnalyticsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.CONTACT_HANDLES: ContactHandlesApi,
        TagValues.CONTACT_NOTES: ContactNotesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.TOKEN_IDENTITY: TokenIdentityApi,
    }
)
