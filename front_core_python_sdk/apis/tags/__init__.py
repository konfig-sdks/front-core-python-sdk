# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from front_core_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    KNOWLEDGE_BASES = "Knowledge Bases"
    CONVERSATIONS = "Conversations"
    TAGS = "Tags"
    CONTACTS = "Contacts"
    MESSAGE_TEMPLATE_FOLDERS = "Message Template Folders"
    MESSAGE_TEMPLATES = "Message Templates"
    CONTACT_GROUPS = "Contact Groups"
    INBOXES = "Inboxes"
    SHIFTS = "Shifts"
    ACCOUNTS = "Accounts"
    CUSTOM_FIELDS = "Custom Fields"
    CHANNELS = "Channels"
    MESSAGES = "Messages"
    SIGNATURES = "Signatures"
    DRAFTS = "Drafts"
    RULES = "Rules"
    LINKS = "Links"
    TEAMMATES = "Teammates"
    ANALYTICS = "Analytics"
    COMMENTS = "Comments"
    TEAMS = "Teams"
    CONTACT_HANDLES = "Contact Handles"
    CONTACT_NOTES = "Contact Notes"
    EVENTS = "Events"
    ATTACHMENTS = "Attachments"
    TOKEN_IDENTITY = "Token Identity"
