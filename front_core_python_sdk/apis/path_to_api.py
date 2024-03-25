import typing_extensions

from front_core_python_sdk.paths import PathValues
from front_core_python_sdk.apis.paths.accounts import Accounts
from front_core_python_sdk.apis.paths.accounts_custom_fields import AccountsCustomFields
from front_core_python_sdk.apis.paths.accounts_account_id import AccountsAccountId
from front_core_python_sdk.apis.paths.accounts_account_id_contacts import AccountsAccountIdContacts
from front_core_python_sdk.apis.paths.analytics_exports import AnalyticsExports
from front_core_python_sdk.apis.paths.analytics_exports_export_id import AnalyticsExportsExportId
from front_core_python_sdk.apis.paths.analytics_reports import AnalyticsReports
from front_core_python_sdk.apis.paths.analytics_reports_report_uid import AnalyticsReportsReportUid
from front_core_python_sdk.apis.paths.channels import Channels
from front_core_python_sdk.apis.paths.channels_channel_id import ChannelsChannelId
from front_core_python_sdk.apis.paths.channels_channel_id_drafts import ChannelsChannelIdDrafts
from front_core_python_sdk.apis.paths.channels_channel_id_incoming_messages import ChannelsChannelIdIncomingMessages
from front_core_python_sdk.apis.paths.channels_channel_id_messages import ChannelsChannelIdMessages
from front_core_python_sdk.apis.paths.channels_channel_id_validate import ChannelsChannelIdValidate
from front_core_python_sdk.apis.paths.comments_comment_id import CommentsCommentId
from front_core_python_sdk.apis.paths.comments_comment_id_mentions import CommentsCommentIdMentions
from front_core_python_sdk.apis.paths.company_rules import CompanyRules
from front_core_python_sdk.apis.paths.company_tags import CompanyTags
from front_core_python_sdk.apis.paths.contact_groups import ContactGroups
from front_core_python_sdk.apis.paths.contact_groups_contact_group_id import ContactGroupsContactGroupId
from front_core_python_sdk.apis.paths.contact_groups_contact_group_id_contacts import ContactGroupsContactGroupIdContacts
from front_core_python_sdk.apis.paths.contacts import Contacts
from front_core_python_sdk.apis.paths.contacts_custom_fields import ContactsCustomFields
from front_core_python_sdk.apis.paths.contacts_merge import ContactsMerge
from front_core_python_sdk.apis.paths.contacts_contact_id import ContactsContactId
from front_core_python_sdk.apis.paths.contacts_contact_id_conversations import ContactsContactIdConversations
from front_core_python_sdk.apis.paths.contacts_contact_id_handles import ContactsContactIdHandles
from front_core_python_sdk.apis.paths.contacts_contact_id_notes import ContactsContactIdNotes
from front_core_python_sdk.apis.paths.conversations import Conversations
from front_core_python_sdk.apis.paths.conversations_custom_fields import ConversationsCustomFields
from front_core_python_sdk.apis.paths.conversations_search_query import ConversationsSearchQuery
from front_core_python_sdk.apis.paths.conversations_conversation_id import ConversationsConversationId
from front_core_python_sdk.apis.paths.conversations_conversation_id_assignee import ConversationsConversationIdAssignee
from front_core_python_sdk.apis.paths.conversations_conversation_id_comments import ConversationsConversationIdComments
from front_core_python_sdk.apis.paths.conversations_conversation_id_drafts import ConversationsConversationIdDrafts
from front_core_python_sdk.apis.paths.conversations_conversation_id_events import ConversationsConversationIdEvents
from front_core_python_sdk.apis.paths.conversations_conversation_id_followers import ConversationsConversationIdFollowers
from front_core_python_sdk.apis.paths.conversations_conversation_id_inboxes import ConversationsConversationIdInboxes
from front_core_python_sdk.apis.paths.conversations_conversation_id_links import ConversationsConversationIdLinks
from front_core_python_sdk.apis.paths.conversations_conversation_id_messages import ConversationsConversationIdMessages
from front_core_python_sdk.apis.paths.conversations_conversation_id_reminders import ConversationsConversationIdReminders
from front_core_python_sdk.apis.paths.conversations_conversation_id_tags import ConversationsConversationIdTags
from front_core_python_sdk.apis.paths.custom_fields import CustomFields
from front_core_python_sdk.apis.paths.download_attachment_link_id import DownloadAttachmentLinkId
from front_core_python_sdk.apis.paths.drafts_draft_id import DraftsDraftId
from front_core_python_sdk.apis.paths.events import Events
from front_core_python_sdk.apis.paths.events_event_id import EventsEventId
from front_core_python_sdk.apis.paths.inboxes import Inboxes
from front_core_python_sdk.apis.paths.inboxes_custom_fields import InboxesCustomFields
from front_core_python_sdk.apis.paths.inboxes_inbox_id import InboxesInboxId
from front_core_python_sdk.apis.paths.inboxes_inbox_id_channels import InboxesInboxIdChannels
from front_core_python_sdk.apis.paths.inboxes_inbox_id_conversations import InboxesInboxIdConversations
from front_core_python_sdk.apis.paths.inboxes_inbox_id_imported_messages import InboxesInboxIdImportedMessages
from front_core_python_sdk.apis.paths.inboxes_inbox_id_teammates import InboxesInboxIdTeammates
from front_core_python_sdk.apis.paths.knowledge_base_articles_article_id import KnowledgeBaseArticlesArticleId
from front_core_python_sdk.apis.paths.knowledge_base_articles_article_id_content import KnowledgeBaseArticlesArticleIdContent
from front_core_python_sdk.apis.paths.knowledge_base_articles_article_id_download_attachment_id import KnowledgeBaseArticlesArticleIdDownloadAttachmentId
from front_core_python_sdk.apis.paths.knowledge_base_articles_article_id_locales_locale_content import KnowledgeBaseArticlesArticleIdLocalesLocaleContent
from front_core_python_sdk.apis.paths.knowledge_base_categories_category_id import KnowledgeBaseCategoriesCategoryId
from front_core_python_sdk.apis.paths.knowledge_base_categories_category_id_articles import KnowledgeBaseCategoriesCategoryIdArticles
from front_core_python_sdk.apis.paths.knowledge_base_categories_category_id_content import KnowledgeBaseCategoriesCategoryIdContent
from front_core_python_sdk.apis.paths.knowledge_base_categories_category_id_locales_locale_content import KnowledgeBaseCategoriesCategoryIdLocalesLocaleContent
from front_core_python_sdk.apis.paths.knowledge_bases import KnowledgeBases
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id import KnowledgeBasesKnowledgeBaseId
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id_articles import KnowledgeBasesKnowledgeBaseIdArticles
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id_categories import KnowledgeBasesKnowledgeBaseIdCategories
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id_content import KnowledgeBasesKnowledgeBaseIdContent
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id_locales_locale_articles import KnowledgeBasesKnowledgeBaseIdLocalesLocaleArticles
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id_locales_locale_categories import KnowledgeBasesKnowledgeBaseIdLocalesLocaleCategories
from front_core_python_sdk.apis.paths.knowledge_bases_knowledge_base_id_locales_locale_content import KnowledgeBasesKnowledgeBaseIdLocalesLocaleContent
from front_core_python_sdk.apis.paths.links import Links
from front_core_python_sdk.apis.paths.links_custom_fields import LinksCustomFields
from front_core_python_sdk.apis.paths.links_link_id import LinksLinkId
from front_core_python_sdk.apis.paths.links_link_id_conversations import LinksLinkIdConversations
from front_core_python_sdk.apis.paths.me import Me
from front_core_python_sdk.apis.paths.message_template_folders import MessageTemplateFolders
from front_core_python_sdk.apis.paths.message_template_folders_message_template_folder_id import MessageTemplateFoldersMessageTemplateFolderId
from front_core_python_sdk.apis.paths.message_template_folders_message_template_folder_id_message_template_folders import MessageTemplateFoldersMessageTemplateFolderIdMessageTemplateFolders
from front_core_python_sdk.apis.paths.message_template_folders_message_template_folder_id_message_templates import MessageTemplateFoldersMessageTemplateFolderIdMessageTemplates
from front_core_python_sdk.apis.paths.message_templates import MessageTemplates
from front_core_python_sdk.apis.paths.message_templates_message_template_id import MessageTemplatesMessageTemplateId
from front_core_python_sdk.apis.paths.messages_message_id import MessagesMessageId
from front_core_python_sdk.apis.paths.messages_message_id_seen import MessagesMessageIdSeen
from front_core_python_sdk.apis.paths.rules import Rules
from front_core_python_sdk.apis.paths.rules_rule_id import RulesRuleId
from front_core_python_sdk.apis.paths.shift_shift_id import ShiftShiftId
from front_core_python_sdk.apis.paths.shift_shift_id_teammates import ShiftShiftIdTeammates
from front_core_python_sdk.apis.paths.shifts import Shifts
from front_core_python_sdk.apis.paths.shifts_shift_id import ShiftsShiftId
from front_core_python_sdk.apis.paths.signatures_signature_id import SignaturesSignatureId
from front_core_python_sdk.apis.paths.tags import Tags
from front_core_python_sdk.apis.paths.tags_tag_id import TagsTagId
from front_core_python_sdk.apis.paths.tags_tag_id_children import TagsTagIdChildren
from front_core_python_sdk.apis.paths.tags_tag_id_conversations import TagsTagIdConversations
from front_core_python_sdk.apis.paths.teammates import Teammates
from front_core_python_sdk.apis.paths.teammates_custom_fields import TeammatesCustomFields
from front_core_python_sdk.apis.paths.teammates_teammate_id import TeammatesTeammateId
from front_core_python_sdk.apis.paths.teammates_teammate_id_channels import TeammatesTeammateIdChannels
from front_core_python_sdk.apis.paths.teammates_teammate_id_contact_groups import TeammatesTeammateIdContactGroups
from front_core_python_sdk.apis.paths.teammates_teammate_id_contacts import TeammatesTeammateIdContacts
from front_core_python_sdk.apis.paths.teammates_teammate_id_conversations import TeammatesTeammateIdConversations
from front_core_python_sdk.apis.paths.teammates_teammate_id_inboxes import TeammatesTeammateIdInboxes
from front_core_python_sdk.apis.paths.teammates_teammate_id_message_template_folders import TeammatesTeammateIdMessageTemplateFolders
from front_core_python_sdk.apis.paths.teammates_teammate_id_message_templates import TeammatesTeammateIdMessageTemplates
from front_core_python_sdk.apis.paths.teammates_teammate_id_rules import TeammatesTeammateIdRules
from front_core_python_sdk.apis.paths.teammates_teammate_id_shifts import TeammatesTeammateIdShifts
from front_core_python_sdk.apis.paths.teammates_teammate_id_signatures import TeammatesTeammateIdSignatures
from front_core_python_sdk.apis.paths.teammates_teammate_id_tags import TeammatesTeammateIdTags
from front_core_python_sdk.apis.paths.teams import Teams
from front_core_python_sdk.apis.paths.teams_team_id import TeamsTeamId
from front_core_python_sdk.apis.paths.teams_team_id_channels import TeamsTeamIdChannels
from front_core_python_sdk.apis.paths.teams_team_id_contact_groups import TeamsTeamIdContactGroups
from front_core_python_sdk.apis.paths.teams_team_id_contacts import TeamsTeamIdContacts
from front_core_python_sdk.apis.paths.teams_team_id_inboxes import TeamsTeamIdInboxes
from front_core_python_sdk.apis.paths.teams_team_id_message_template_folders import TeamsTeamIdMessageTemplateFolders
from front_core_python_sdk.apis.paths.teams_team_id_message_templates import TeamsTeamIdMessageTemplates
from front_core_python_sdk.apis.paths.teams_team_id_rules import TeamsTeamIdRules
from front_core_python_sdk.apis.paths.teams_team_id_shifts import TeamsTeamIdShifts
from front_core_python_sdk.apis.paths.teams_team_id_signatures import TeamsTeamIdSignatures
from front_core_python_sdk.apis.paths.teams_team_id_tags import TeamsTeamIdTags
from front_core_python_sdk.apis.paths.teams_team_id_teammates import TeamsTeamIdTeammates
from front_core_python_sdk.apis.paths.drafts_message_id import DraftsMessageId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_CUSTOM_FIELDS: AccountsCustomFields,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_CONTACTS: AccountsAccountIdContacts,
        PathValues.ANALYTICS_EXPORTS: AnalyticsExports,
        PathValues.ANALYTICS_EXPORTS_EXPORT_ID: AnalyticsExportsExportId,
        PathValues.ANALYTICS_REPORTS: AnalyticsReports,
        PathValues.ANALYTICS_REPORTS_REPORT_UID: AnalyticsReportsReportUid,
        PathValues.CHANNELS: Channels,
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_DRAFTS: ChannelsChannelIdDrafts,
        PathValues.CHANNELS_CHANNEL_ID_INCOMING_MESSAGES: ChannelsChannelIdIncomingMessages,
        PathValues.CHANNELS_CHANNEL_ID_MESSAGES: ChannelsChannelIdMessages,
        PathValues.CHANNELS_CHANNEL_ID_VALIDATE: ChannelsChannelIdValidate,
        PathValues.COMMENTS_COMMENT_ID: CommentsCommentId,
        PathValues.COMMENTS_COMMENT_ID_MENTIONS: CommentsCommentIdMentions,
        PathValues.COMPANY_RULES: CompanyRules,
        PathValues.COMPANY_TAGS: CompanyTags,
        PathValues.CONTACT_GROUPS: ContactGroups,
        PathValues.CONTACT_GROUPS_CONTACT_GROUP_ID: ContactGroupsContactGroupId,
        PathValues.CONTACT_GROUPS_CONTACT_GROUP_ID_CONTACTS: ContactGroupsContactGroupIdContacts,
        PathValues.CONTACTS: Contacts,
        PathValues.CONTACTS_CUSTOM_FIELDS: ContactsCustomFields,
        PathValues.CONTACTS_MERGE: ContactsMerge,
        PathValues.CONTACTS_CONTACT_ID: ContactsContactId,
        PathValues.CONTACTS_CONTACT_ID_CONVERSATIONS: ContactsContactIdConversations,
        PathValues.CONTACTS_CONTACT_ID_HANDLES: ContactsContactIdHandles,
        PathValues.CONTACTS_CONTACT_ID_NOTES: ContactsContactIdNotes,
        PathValues.CONVERSATIONS: Conversations,
        PathValues.CONVERSATIONS_CUSTOM_FIELDS: ConversationsCustomFields,
        PathValues.CONVERSATIONS_SEARCH_QUERY: ConversationsSearchQuery,
        PathValues.CONVERSATIONS_CONVERSATION_ID: ConversationsConversationId,
        PathValues.CONVERSATIONS_CONVERSATION_ID_ASSIGNEE: ConversationsConversationIdAssignee,
        PathValues.CONVERSATIONS_CONVERSATION_ID_COMMENTS: ConversationsConversationIdComments,
        PathValues.CONVERSATIONS_CONVERSATION_ID_DRAFTS: ConversationsConversationIdDrafts,
        PathValues.CONVERSATIONS_CONVERSATION_ID_EVENTS: ConversationsConversationIdEvents,
        PathValues.CONVERSATIONS_CONVERSATION_ID_FOLLOWERS: ConversationsConversationIdFollowers,
        PathValues.CONVERSATIONS_CONVERSATION_ID_INBOXES: ConversationsConversationIdInboxes,
        PathValues.CONVERSATIONS_CONVERSATION_ID_LINKS: ConversationsConversationIdLinks,
        PathValues.CONVERSATIONS_CONVERSATION_ID_MESSAGES: ConversationsConversationIdMessages,
        PathValues.CONVERSATIONS_CONVERSATION_ID_REMINDERS: ConversationsConversationIdReminders,
        PathValues.CONVERSATIONS_CONVERSATION_ID_TAGS: ConversationsConversationIdTags,
        PathValues.CUSTOM_FIELDS: CustomFields,
        PathValues.DOWNLOAD_ATTACHMENT_LINK_ID: DownloadAttachmentLinkId,
        PathValues.DRAFTS_DRAFT_ID: DraftsDraftId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_EVENT_ID: EventsEventId,
        PathValues.INBOXES: Inboxes,
        PathValues.INBOXES_CUSTOM_FIELDS: InboxesCustomFields,
        PathValues.INBOXES_INBOX_ID: InboxesInboxId,
        PathValues.INBOXES_INBOX_ID_CHANNELS: InboxesInboxIdChannels,
        PathValues.INBOXES_INBOX_ID_CONVERSATIONS: InboxesInboxIdConversations,
        PathValues.INBOXES_INBOX_ID_IMPORTED_MESSAGES: InboxesInboxIdImportedMessages,
        PathValues.INBOXES_INBOX_ID_TEAMMATES: InboxesInboxIdTeammates,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID: KnowledgeBaseArticlesArticleId,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID_CONTENT: KnowledgeBaseArticlesArticleIdContent,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID_DOWNLOAD_ATTACHMENT_ID: KnowledgeBaseArticlesArticleIdDownloadAttachmentId,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID_LOCALES_LOCALE_CONTENT: KnowledgeBaseArticlesArticleIdLocalesLocaleContent,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID: KnowledgeBaseCategoriesCategoryId,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID_ARTICLES: KnowledgeBaseCategoriesCategoryIdArticles,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID_CONTENT: KnowledgeBaseCategoriesCategoryIdContent,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID_LOCALES_LOCALE_CONTENT: KnowledgeBaseCategoriesCategoryIdLocalesLocaleContent,
        PathValues.KNOWLEDGE_BASES: KnowledgeBases,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID: KnowledgeBasesKnowledgeBaseId,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_ARTICLES: KnowledgeBasesKnowledgeBaseIdArticles,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_CATEGORIES: KnowledgeBasesKnowledgeBaseIdCategories,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_CONTENT: KnowledgeBasesKnowledgeBaseIdContent,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_LOCALES_LOCALE_ARTICLES: KnowledgeBasesKnowledgeBaseIdLocalesLocaleArticles,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_LOCALES_LOCALE_CATEGORIES: KnowledgeBasesKnowledgeBaseIdLocalesLocaleCategories,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_LOCALES_LOCALE_CONTENT: KnowledgeBasesKnowledgeBaseIdLocalesLocaleContent,
        PathValues.LINKS: Links,
        PathValues.LINKS_CUSTOM_FIELDS: LinksCustomFields,
        PathValues.LINKS_LINK_ID: LinksLinkId,
        PathValues.LINKS_LINK_ID_CONVERSATIONS: LinksLinkIdConversations,
        PathValues.ME: Me,
        PathValues.MESSAGE_TEMPLATE_FOLDERS: MessageTemplateFolders,
        PathValues.MESSAGE_TEMPLATE_FOLDERS_MESSAGE_TEMPLATE_FOLDER_ID: MessageTemplateFoldersMessageTemplateFolderId,
        PathValues.MESSAGE_TEMPLATE_FOLDERS_MESSAGE_TEMPLATE_FOLDER_ID_MESSAGE_TEMPLATE_FOLDERS: MessageTemplateFoldersMessageTemplateFolderIdMessageTemplateFolders,
        PathValues.MESSAGE_TEMPLATE_FOLDERS_MESSAGE_TEMPLATE_FOLDER_ID_MESSAGE_TEMPLATES: MessageTemplateFoldersMessageTemplateFolderIdMessageTemplates,
        PathValues.MESSAGE_TEMPLATES: MessageTemplates,
        PathValues.MESSAGE_TEMPLATES_MESSAGE_TEMPLATE_ID: MessageTemplatesMessageTemplateId,
        PathValues.MESSAGES_MESSAGE_ID: MessagesMessageId,
        PathValues.MESSAGES_MESSAGE_ID_SEEN: MessagesMessageIdSeen,
        PathValues.RULES: Rules,
        PathValues.RULES_RULE_ID: RulesRuleId,
        PathValues.SHIFT_SHIFT_ID: ShiftShiftId,
        PathValues.SHIFT_SHIFT_ID_TEAMMATES: ShiftShiftIdTeammates,
        PathValues.SHIFTS: Shifts,
        PathValues.SHIFTS_SHIFT_ID: ShiftsShiftId,
        PathValues.SIGNATURES_SIGNATURE_ID: SignaturesSignatureId,
        PathValues.TAGS: Tags,
        PathValues.TAGS_TAG_ID: TagsTagId,
        PathValues.TAGS_TAG_ID_CHILDREN: TagsTagIdChildren,
        PathValues.TAGS_TAG_ID_CONVERSATIONS: TagsTagIdConversations,
        PathValues.TEAMMATES: Teammates,
        PathValues.TEAMMATES_CUSTOM_FIELDS: TeammatesCustomFields,
        PathValues.TEAMMATES_TEAMMATE_ID: TeammatesTeammateId,
        PathValues.TEAMMATES_TEAMMATE_ID_CHANNELS: TeammatesTeammateIdChannels,
        PathValues.TEAMMATES_TEAMMATE_ID_CONTACT_GROUPS: TeammatesTeammateIdContactGroups,
        PathValues.TEAMMATES_TEAMMATE_ID_CONTACTS: TeammatesTeammateIdContacts,
        PathValues.TEAMMATES_TEAMMATE_ID_CONVERSATIONS: TeammatesTeammateIdConversations,
        PathValues.TEAMMATES_TEAMMATE_ID_INBOXES: TeammatesTeammateIdInboxes,
        PathValues.TEAMMATES_TEAMMATE_ID_MESSAGE_TEMPLATE_FOLDERS: TeammatesTeammateIdMessageTemplateFolders,
        PathValues.TEAMMATES_TEAMMATE_ID_MESSAGE_TEMPLATES: TeammatesTeammateIdMessageTemplates,
        PathValues.TEAMMATES_TEAMMATE_ID_RULES: TeammatesTeammateIdRules,
        PathValues.TEAMMATES_TEAMMATE_ID_SHIFTS: TeammatesTeammateIdShifts,
        PathValues.TEAMMATES_TEAMMATE_ID_SIGNATURES: TeammatesTeammateIdSignatures,
        PathValues.TEAMMATES_TEAMMATE_ID_TAGS: TeammatesTeammateIdTags,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_ID: TeamsTeamId,
        PathValues.TEAMS_TEAM_ID_CHANNELS: TeamsTeamIdChannels,
        PathValues.TEAMS_TEAM_ID_CONTACT_GROUPS: TeamsTeamIdContactGroups,
        PathValues.TEAMS_TEAM_ID_CONTACTS: TeamsTeamIdContacts,
        PathValues.TEAMS_TEAM_ID_INBOXES: TeamsTeamIdInboxes,
        PathValues.TEAMS_TEAM_ID_MESSAGE_TEMPLATE_FOLDERS: TeamsTeamIdMessageTemplateFolders,
        PathValues.TEAMS_TEAM_ID_MESSAGE_TEMPLATES: TeamsTeamIdMessageTemplates,
        PathValues.TEAMS_TEAM_ID_RULES: TeamsTeamIdRules,
        PathValues.TEAMS_TEAM_ID_SHIFTS: TeamsTeamIdShifts,
        PathValues.TEAMS_TEAM_ID_SIGNATURES: TeamsTeamIdSignatures,
        PathValues.TEAMS_TEAM_ID_TAGS: TeamsTeamIdTags,
        PathValues.TEAMS_TEAM_ID_TEAMMATES: TeamsTeamIdTeammates,
        PathValues.DRAFTS_MESSAGE_ID: DraftsMessageId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_CUSTOM_FIELDS: AccountsCustomFields,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_CONTACTS: AccountsAccountIdContacts,
        PathValues.ANALYTICS_EXPORTS: AnalyticsExports,
        PathValues.ANALYTICS_EXPORTS_EXPORT_ID: AnalyticsExportsExportId,
        PathValues.ANALYTICS_REPORTS: AnalyticsReports,
        PathValues.ANALYTICS_REPORTS_REPORT_UID: AnalyticsReportsReportUid,
        PathValues.CHANNELS: Channels,
        PathValues.CHANNELS_CHANNEL_ID: ChannelsChannelId,
        PathValues.CHANNELS_CHANNEL_ID_DRAFTS: ChannelsChannelIdDrafts,
        PathValues.CHANNELS_CHANNEL_ID_INCOMING_MESSAGES: ChannelsChannelIdIncomingMessages,
        PathValues.CHANNELS_CHANNEL_ID_MESSAGES: ChannelsChannelIdMessages,
        PathValues.CHANNELS_CHANNEL_ID_VALIDATE: ChannelsChannelIdValidate,
        PathValues.COMMENTS_COMMENT_ID: CommentsCommentId,
        PathValues.COMMENTS_COMMENT_ID_MENTIONS: CommentsCommentIdMentions,
        PathValues.COMPANY_RULES: CompanyRules,
        PathValues.COMPANY_TAGS: CompanyTags,
        PathValues.CONTACT_GROUPS: ContactGroups,
        PathValues.CONTACT_GROUPS_CONTACT_GROUP_ID: ContactGroupsContactGroupId,
        PathValues.CONTACT_GROUPS_CONTACT_GROUP_ID_CONTACTS: ContactGroupsContactGroupIdContacts,
        PathValues.CONTACTS: Contacts,
        PathValues.CONTACTS_CUSTOM_FIELDS: ContactsCustomFields,
        PathValues.CONTACTS_MERGE: ContactsMerge,
        PathValues.CONTACTS_CONTACT_ID: ContactsContactId,
        PathValues.CONTACTS_CONTACT_ID_CONVERSATIONS: ContactsContactIdConversations,
        PathValues.CONTACTS_CONTACT_ID_HANDLES: ContactsContactIdHandles,
        PathValues.CONTACTS_CONTACT_ID_NOTES: ContactsContactIdNotes,
        PathValues.CONVERSATIONS: Conversations,
        PathValues.CONVERSATIONS_CUSTOM_FIELDS: ConversationsCustomFields,
        PathValues.CONVERSATIONS_SEARCH_QUERY: ConversationsSearchQuery,
        PathValues.CONVERSATIONS_CONVERSATION_ID: ConversationsConversationId,
        PathValues.CONVERSATIONS_CONVERSATION_ID_ASSIGNEE: ConversationsConversationIdAssignee,
        PathValues.CONVERSATIONS_CONVERSATION_ID_COMMENTS: ConversationsConversationIdComments,
        PathValues.CONVERSATIONS_CONVERSATION_ID_DRAFTS: ConversationsConversationIdDrafts,
        PathValues.CONVERSATIONS_CONVERSATION_ID_EVENTS: ConversationsConversationIdEvents,
        PathValues.CONVERSATIONS_CONVERSATION_ID_FOLLOWERS: ConversationsConversationIdFollowers,
        PathValues.CONVERSATIONS_CONVERSATION_ID_INBOXES: ConversationsConversationIdInboxes,
        PathValues.CONVERSATIONS_CONVERSATION_ID_LINKS: ConversationsConversationIdLinks,
        PathValues.CONVERSATIONS_CONVERSATION_ID_MESSAGES: ConversationsConversationIdMessages,
        PathValues.CONVERSATIONS_CONVERSATION_ID_REMINDERS: ConversationsConversationIdReminders,
        PathValues.CONVERSATIONS_CONVERSATION_ID_TAGS: ConversationsConversationIdTags,
        PathValues.CUSTOM_FIELDS: CustomFields,
        PathValues.DOWNLOAD_ATTACHMENT_LINK_ID: DownloadAttachmentLinkId,
        PathValues.DRAFTS_DRAFT_ID: DraftsDraftId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_EVENT_ID: EventsEventId,
        PathValues.INBOXES: Inboxes,
        PathValues.INBOXES_CUSTOM_FIELDS: InboxesCustomFields,
        PathValues.INBOXES_INBOX_ID: InboxesInboxId,
        PathValues.INBOXES_INBOX_ID_CHANNELS: InboxesInboxIdChannels,
        PathValues.INBOXES_INBOX_ID_CONVERSATIONS: InboxesInboxIdConversations,
        PathValues.INBOXES_INBOX_ID_IMPORTED_MESSAGES: InboxesInboxIdImportedMessages,
        PathValues.INBOXES_INBOX_ID_TEAMMATES: InboxesInboxIdTeammates,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID: KnowledgeBaseArticlesArticleId,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID_CONTENT: KnowledgeBaseArticlesArticleIdContent,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID_DOWNLOAD_ATTACHMENT_ID: KnowledgeBaseArticlesArticleIdDownloadAttachmentId,
        PathValues.KNOWLEDGE_BASE_ARTICLES_ARTICLE_ID_LOCALES_LOCALE_CONTENT: KnowledgeBaseArticlesArticleIdLocalesLocaleContent,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID: KnowledgeBaseCategoriesCategoryId,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID_ARTICLES: KnowledgeBaseCategoriesCategoryIdArticles,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID_CONTENT: KnowledgeBaseCategoriesCategoryIdContent,
        PathValues.KNOWLEDGE_BASE_CATEGORIES_CATEGORY_ID_LOCALES_LOCALE_CONTENT: KnowledgeBaseCategoriesCategoryIdLocalesLocaleContent,
        PathValues.KNOWLEDGE_BASES: KnowledgeBases,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID: KnowledgeBasesKnowledgeBaseId,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_ARTICLES: KnowledgeBasesKnowledgeBaseIdArticles,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_CATEGORIES: KnowledgeBasesKnowledgeBaseIdCategories,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_CONTENT: KnowledgeBasesKnowledgeBaseIdContent,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_LOCALES_LOCALE_ARTICLES: KnowledgeBasesKnowledgeBaseIdLocalesLocaleArticles,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_LOCALES_LOCALE_CATEGORIES: KnowledgeBasesKnowledgeBaseIdLocalesLocaleCategories,
        PathValues.KNOWLEDGE_BASES_KNOWLEDGE_BASE_ID_LOCALES_LOCALE_CONTENT: KnowledgeBasesKnowledgeBaseIdLocalesLocaleContent,
        PathValues.LINKS: Links,
        PathValues.LINKS_CUSTOM_FIELDS: LinksCustomFields,
        PathValues.LINKS_LINK_ID: LinksLinkId,
        PathValues.LINKS_LINK_ID_CONVERSATIONS: LinksLinkIdConversations,
        PathValues.ME: Me,
        PathValues.MESSAGE_TEMPLATE_FOLDERS: MessageTemplateFolders,
        PathValues.MESSAGE_TEMPLATE_FOLDERS_MESSAGE_TEMPLATE_FOLDER_ID: MessageTemplateFoldersMessageTemplateFolderId,
        PathValues.MESSAGE_TEMPLATE_FOLDERS_MESSAGE_TEMPLATE_FOLDER_ID_MESSAGE_TEMPLATE_FOLDERS: MessageTemplateFoldersMessageTemplateFolderIdMessageTemplateFolders,
        PathValues.MESSAGE_TEMPLATE_FOLDERS_MESSAGE_TEMPLATE_FOLDER_ID_MESSAGE_TEMPLATES: MessageTemplateFoldersMessageTemplateFolderIdMessageTemplates,
        PathValues.MESSAGE_TEMPLATES: MessageTemplates,
        PathValues.MESSAGE_TEMPLATES_MESSAGE_TEMPLATE_ID: MessageTemplatesMessageTemplateId,
        PathValues.MESSAGES_MESSAGE_ID: MessagesMessageId,
        PathValues.MESSAGES_MESSAGE_ID_SEEN: MessagesMessageIdSeen,
        PathValues.RULES: Rules,
        PathValues.RULES_RULE_ID: RulesRuleId,
        PathValues.SHIFT_SHIFT_ID: ShiftShiftId,
        PathValues.SHIFT_SHIFT_ID_TEAMMATES: ShiftShiftIdTeammates,
        PathValues.SHIFTS: Shifts,
        PathValues.SHIFTS_SHIFT_ID: ShiftsShiftId,
        PathValues.SIGNATURES_SIGNATURE_ID: SignaturesSignatureId,
        PathValues.TAGS: Tags,
        PathValues.TAGS_TAG_ID: TagsTagId,
        PathValues.TAGS_TAG_ID_CHILDREN: TagsTagIdChildren,
        PathValues.TAGS_TAG_ID_CONVERSATIONS: TagsTagIdConversations,
        PathValues.TEAMMATES: Teammates,
        PathValues.TEAMMATES_CUSTOM_FIELDS: TeammatesCustomFields,
        PathValues.TEAMMATES_TEAMMATE_ID: TeammatesTeammateId,
        PathValues.TEAMMATES_TEAMMATE_ID_CHANNELS: TeammatesTeammateIdChannels,
        PathValues.TEAMMATES_TEAMMATE_ID_CONTACT_GROUPS: TeammatesTeammateIdContactGroups,
        PathValues.TEAMMATES_TEAMMATE_ID_CONTACTS: TeammatesTeammateIdContacts,
        PathValues.TEAMMATES_TEAMMATE_ID_CONVERSATIONS: TeammatesTeammateIdConversations,
        PathValues.TEAMMATES_TEAMMATE_ID_INBOXES: TeammatesTeammateIdInboxes,
        PathValues.TEAMMATES_TEAMMATE_ID_MESSAGE_TEMPLATE_FOLDERS: TeammatesTeammateIdMessageTemplateFolders,
        PathValues.TEAMMATES_TEAMMATE_ID_MESSAGE_TEMPLATES: TeammatesTeammateIdMessageTemplates,
        PathValues.TEAMMATES_TEAMMATE_ID_RULES: TeammatesTeammateIdRules,
        PathValues.TEAMMATES_TEAMMATE_ID_SHIFTS: TeammatesTeammateIdShifts,
        PathValues.TEAMMATES_TEAMMATE_ID_SIGNATURES: TeammatesTeammateIdSignatures,
        PathValues.TEAMMATES_TEAMMATE_ID_TAGS: TeammatesTeammateIdTags,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_ID: TeamsTeamId,
        PathValues.TEAMS_TEAM_ID_CHANNELS: TeamsTeamIdChannels,
        PathValues.TEAMS_TEAM_ID_CONTACT_GROUPS: TeamsTeamIdContactGroups,
        PathValues.TEAMS_TEAM_ID_CONTACTS: TeamsTeamIdContacts,
        PathValues.TEAMS_TEAM_ID_INBOXES: TeamsTeamIdInboxes,
        PathValues.TEAMS_TEAM_ID_MESSAGE_TEMPLATE_FOLDERS: TeamsTeamIdMessageTemplateFolders,
        PathValues.TEAMS_TEAM_ID_MESSAGE_TEMPLATES: TeamsTeamIdMessageTemplates,
        PathValues.TEAMS_TEAM_ID_RULES: TeamsTeamIdRules,
        PathValues.TEAMS_TEAM_ID_SHIFTS: TeamsTeamIdShifts,
        PathValues.TEAMS_TEAM_ID_SIGNATURES: TeamsTeamIdSignatures,
        PathValues.TEAMS_TEAM_ID_TAGS: TeamsTeamIdTags,
        PathValues.TEAMS_TEAM_ID_TEAMMATES: TeamsTeamIdTeammates,
        PathValues.DRAFTS_MESSAGE_ID: DraftsMessageId,
    }
)
