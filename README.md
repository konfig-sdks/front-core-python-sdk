<div align="left">

[![Visit Front](./header.png)](https://front.com)

# Front<a id="front"></a>

Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.

With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`frontcore.accounts.add_contacts_to_account`](#frontcoreaccountsadd_contacts_to_account)
  * [`frontcore.accounts.create_new_account`](#frontcoreaccountscreate_new_account)
  * [`frontcore.accounts.delete_account`](#frontcoreaccountsdelete_account)
  * [`frontcore.accounts.get_account`](#frontcoreaccountsget_account)
  * [`frontcore.accounts.list_account_contacts`](#frontcoreaccountslist_account_contacts)
  * [`frontcore.accounts.list_company_accounts`](#frontcoreaccountslist_company_accounts)
  * [`frontcore.accounts.remove_contact_from`](#frontcoreaccountsremove_contact_from)
  * [`frontcore.accounts.update_account`](#frontcoreaccountsupdate_account)
  * [`frontcore.analytics.create_new_export`](#frontcoreanalyticscreate_new_export)
  * [`frontcore.analytics.create_new_report`](#frontcoreanalyticscreate_new_report)
  * [`frontcore.analytics.get_export`](#frontcoreanalyticsget_export)
  * [`frontcore.analytics.get_report`](#frontcoreanalyticsget_report)
  * [`frontcore.attachments.download_attachment_file`](#frontcoreattachmentsdownload_attachment_file)
  * [`frontcore.channels.create_inbox_channel`](#frontcorechannelscreate_inbox_channel)
  * [`frontcore.channels.get_channel`](#frontcorechannelsget_channel)
  * [`frontcore.channels.list`](#frontcorechannelslist)
  * [`frontcore.channels.list_team`](#frontcorechannelslist_team)
  * [`frontcore.channels.list_teammate`](#frontcorechannelslist_teammate)
  * [`frontcore.channels.update_channel`](#frontcorechannelsupdate_channel)
  * [`frontcore.channels.validate_smtp_settings`](#frontcorechannelsvalidate_smtp_settings)
  * [`frontcore.comments.add_new_comment`](#frontcorecommentsadd_new_comment)
  * [`frontcore.comments.get_comment`](#frontcorecommentsget_comment)
  * [`frontcore.comments.list_conversation_comments`](#frontcorecommentslist_conversation_comments)
  * [`frontcore.comments.list_mentioned_teammates`](#frontcorecommentslist_mentioned_teammates)
  * [`frontcore.contact_groups.add_contacts_to_group`](#frontcorecontact_groupsadd_contacts_to_group)
  * [`frontcore.contact_groups.create_new_group`](#frontcorecontact_groupscreate_new_group)
  * [`frontcore.contact_groups.create_new_group_0`](#frontcorecontact_groupscreate_new_group_0)
  * [`frontcore.contact_groups.create_teammate_group`](#frontcorecontact_groupscreate_teammate_group)
  * [`frontcore.contact_groups.delete_group`](#frontcorecontact_groupsdelete_group)
  * [`frontcore.contact_groups.list_group_contacts`](#frontcorecontact_groupslist_group_contacts)
  * [`frontcore.contact_groups.list_groups`](#frontcorecontact_groupslist_groups)
  * [`frontcore.contact_groups.list_team_groups`](#frontcorecontact_groupslist_team_groups)
  * [`frontcore.contact_groups.list_teammate_groups`](#frontcorecontact_groupslist_teammate_groups)
  * [`frontcore.contact_groups.remove_contacts`](#frontcorecontact_groupsremove_contacts)
  * [`frontcore.contact_handles.add_new_handle`](#frontcorecontact_handlesadd_new_handle)
  * [`frontcore.contact_handles.remove_handle`](#frontcorecontact_handlesremove_handle)
  * [`frontcore.contact_notes.create_new_note`](#frontcorecontact_notescreate_new_note)
  * [`frontcore.contact_notes.list`](#frontcorecontact_noteslist)
  * [`frontcore.contacts.create_new_contact`](#frontcorecontactscreate_new_contact)
  * [`frontcore.contacts.create_team_contact`](#frontcorecontactscreate_team_contact)
  * [`frontcore.contacts.create_teammate_contact`](#frontcorecontactscreate_teammate_contact)
  * [`frontcore.contacts.delete_contact`](#frontcorecontactsdelete_contact)
  * [`frontcore.contacts.get_one_contact`](#frontcorecontactsget_one_contact)
  * [`frontcore.contacts.list_company_contacts`](#frontcorecontactslist_company_contacts)
  * [`frontcore.contacts.list_conversations_reverse_chronological_order`](#frontcorecontactslist_conversations_reverse_chronological_order)
  * [`frontcore.contacts.list_team_contacts`](#frontcorecontactslist_team_contacts)
  * [`frontcore.contacts.list_teammate_contacts`](#frontcorecontactslist_teammate_contacts)
  * [`frontcore.contacts.merge_contacts`](#frontcorecontactsmerge_contacts)
  * [`frontcore.contacts.update_contact`](#frontcorecontactsupdate_contact)
  * [`frontcore.conversations.add_followers`](#frontcoreconversationsadd_followers)
  * [`frontcore.conversations.add_link`](#frontcoreconversationsadd_link)
  * [`frontcore.conversations.add_tags_to_conversation`](#frontcoreconversationsadd_tags_to_conversation)
  * [`frontcore.conversations.create_discussion`](#frontcoreconversationscreate_discussion)
  * [`frontcore.conversations.get_by_id`](#frontcoreconversationsget_by_id)
  * [`frontcore.conversations.list_events`](#frontcoreconversationslist_events)
  * [`frontcore.conversations.list_followers`](#frontcoreconversationslist_followers)
  * [`frontcore.conversations.list_in_reverse_chronological_order`](#frontcoreconversationslist_in_reverse_chronological_order)
  * [`frontcore.conversations.list_inboxes`](#frontcoreconversationslist_inboxes)
  * [`frontcore.conversations.list_messages_in_reverse_chronological_order`](#frontcoreconversationslist_messages_in_reverse_chronological_order)
  * [`frontcore.conversations.remove_followers`](#frontcoreconversationsremove_followers)
  * [`frontcore.conversations.remove_links`](#frontcoreconversationsremove_links)
  * [`frontcore.conversations.remove_tag`](#frontcoreconversationsremove_tag)
  * [`frontcore.conversations.search_by_query`](#frontcoreconversationssearch_by_query)
  * [`frontcore.conversations.update_assignee`](#frontcoreconversationsupdate_assignee)
  * [`frontcore.conversations.update_conversation_by_id`](#frontcoreconversationsupdate_conversation_by_id)
  * [`frontcore.conversations.update_reminders`](#frontcoreconversationsupdate_reminders)
  * [`frontcore.custom_fields.get_list`](#frontcorecustom_fieldsget_list)
  * [`frontcore.custom_fields.list_account_custom_fields`](#frontcorecustom_fieldslist_account_custom_fields)
  * [`frontcore.custom_fields.list_contact_custom_fields`](#frontcorecustom_fieldslist_contact_custom_fields)
  * [`frontcore.custom_fields.list_contact_fields`](#frontcorecustom_fieldslist_contact_fields)
  * [`frontcore.custom_fields.list_conversation_custom_fields`](#frontcorecustom_fieldslist_conversation_custom_fields)
  * [`frontcore.custom_fields.list_inbox_custom_fields`](#frontcorecustom_fieldslist_inbox_custom_fields)
  * [`frontcore.custom_fields.list_teammate_custom_fields`](#frontcorecustom_fieldslist_teammate_custom_fields)
  * [`frontcore.drafts.create_draft_reply`](#frontcoredraftscreate_draft_reply)
  * [`frontcore.drafts.create_new_draft_message`](#frontcoredraftscreate_new_draft_message)
  * [`frontcore.drafts.delete_draft_message`](#frontcoredraftsdelete_draft_message)
  * [`frontcore.drafts.edit_message`](#frontcoredraftsedit_message)
  * [`frontcore.drafts.list_conversation_drafts`](#frontcoredraftslist_conversation_drafts)
  * [`frontcore.events.get_event`](#frontcoreeventsget_event)
  * [`frontcore.events.list_detailed_inbox_events`](#frontcoreeventslist_detailed_inbox_events)
  * [`frontcore.inboxes.add_teammate_access`](#frontcoreinboxesadd_teammate_access)
  * [`frontcore.inboxes.create_default_team_inbox`](#frontcoreinboxescreate_default_team_inbox)
  * [`frontcore.inboxes.create_team_inbox`](#frontcoreinboxescreate_team_inbox)
  * [`frontcore.inboxes.get_inbox`](#frontcoreinboxesget_inbox)
  * [`frontcore.inboxes.list_channels`](#frontcoreinboxeslist_channels)
  * [`frontcore.inboxes.list_conversations_inbox`](#frontcoreinboxeslist_conversations_inbox)
  * [`frontcore.inboxes.list_inboxes`](#frontcoreinboxeslist_inboxes)
  * [`frontcore.inboxes.list_team_inboxes`](#frontcoreinboxeslist_team_inboxes)
  * [`frontcore.inboxes.list_teammates_access`](#frontcoreinboxeslist_teammates_access)
  * [`frontcore.inboxes.remove_access`](#frontcoreinboxesremove_access)
  * [`frontcore.knowledge_bases.create_article_default_locale`](#frontcoreknowledge_basescreate_article_default_locale)
  * [`frontcore.knowledge_bases.create_article_locale`](#frontcoreknowledge_basescreate_article_locale)
  * [`frontcore.knowledge_bases.create_category_default_locale`](#frontcoreknowledge_basescreate_category_default_locale)
  * [`frontcore.knowledge_bases.create_category_in_locale`](#frontcoreknowledge_basescreate_category_in_locale)
  * [`frontcore.knowledge_bases.create_new_knowledge_base`](#frontcoreknowledge_basescreate_new_knowledge_base)
  * [`frontcore.knowledge_bases.delete_article`](#frontcoreknowledge_basesdelete_article)
  * [`frontcore.knowledge_bases.delete_category`](#frontcoreknowledge_basesdelete_category)
  * [`frontcore.knowledge_bases.download_attachment_article`](#frontcoreknowledge_basesdownload_attachment_article)
  * [`frontcore.knowledge_bases.get_article_by_id`](#frontcoreknowledge_basesget_article_by_id)
  * [`frontcore.knowledge_bases.get_article_content`](#frontcoreknowledge_basesget_article_content)
  * [`frontcore.knowledge_bases.get_category`](#frontcoreknowledge_basesget_category)
  * [`frontcore.knowledge_bases.get_category_content_default_locale`](#frontcoreknowledge_basesget_category_content_default_locale)
  * [`frontcore.knowledge_bases.get_category_content_locale`](#frontcoreknowledge_basesget_category_content_locale)
  * [`frontcore.knowledge_bases.get_content_default_locale`](#frontcoreknowledge_basesget_content_default_locale)
  * [`frontcore.knowledge_bases.get_content_default_locale_0`](#frontcoreknowledge_basesget_content_default_locale_0)
  * [`frontcore.knowledge_bases.get_knowledge_base`](#frontcoreknowledge_basesget_knowledge_base)
  * [`frontcore.knowledge_bases.get_knowledge_base_content_in_locale`](#frontcoreknowledge_basesget_knowledge_base_content_in_locale)
  * [`frontcore.knowledge_bases.list_articles_in_base`](#frontcoreknowledge_baseslist_articles_in_base)
  * [`frontcore.knowledge_bases.list_articles_in_category`](#frontcoreknowledge_baseslist_articles_in_category)
  * [`frontcore.knowledge_bases.list_categories_in_base`](#frontcoreknowledge_baseslist_categories_in_base)
  * [`frontcore.knowledge_bases.list_knowledge_bases`](#frontcoreknowledge_baseslist_knowledge_bases)
  * [`frontcore.knowledge_bases.update_article_content_default_locale`](#frontcoreknowledge_basesupdate_article_content_default_locale)
  * [`frontcore.knowledge_bases.update_article_content_locale`](#frontcoreknowledge_basesupdate_article_content_locale)
  * [`frontcore.knowledge_bases.update_category_content_locale`](#frontcoreknowledge_basesupdate_category_content_locale)
  * [`frontcore.knowledge_bases.update_category_default_locale`](#frontcoreknowledge_basesupdate_category_default_locale)
  * [`frontcore.knowledge_bases.update_default_knowledge_base`](#frontcoreknowledge_basesupdate_default_knowledge_base)
  * [`frontcore.knowledge_bases.update_knowledge_base_locale`](#frontcoreknowledge_basesupdate_knowledge_base_locale)
  * [`frontcore.links.create_link`](#frontcorelinkscreate_link)
  * [`frontcore.links.get_link`](#frontcorelinksget_link)
  * [`frontcore.links.list_by_id_and_type`](#frontcorelinkslist_by_id_and_type)
  * [`frontcore.links.list_conversations`](#frontcorelinkslist_conversations)
  * [`frontcore.links.update_link`](#frontcorelinksupdate_link)
  * [`frontcore.message_template_folders.create_child_folder`](#frontcoremessage_template_folderscreate_child_folder)
  * [`frontcore.message_template_folders.create_new_folder`](#frontcoremessage_template_folderscreate_new_folder)
  * [`frontcore.message_template_folders.create_new_folder_0`](#frontcoremessage_template_folderscreate_new_folder_0)
  * [`frontcore.message_template_folders.create_new_folder_1`](#frontcoremessage_template_folderscreate_new_folder_1)
  * [`frontcore.message_template_folders.delete_folder`](#frontcoremessage_template_foldersdelete_folder)
  * [`frontcore.message_template_folders.get_child_folders`](#frontcoremessage_template_foldersget_child_folders)
  * [`frontcore.message_template_folders.get_folder`](#frontcoremessage_template_foldersget_folder)
  * [`frontcore.message_template_folders.list_folders`](#frontcoremessage_template_folderslist_folders)
  * [`frontcore.message_template_folders.list_team_folders`](#frontcoremessage_template_folderslist_team_folders)
  * [`frontcore.message_template_folders.list_teammate_folders`](#frontcoremessage_template_folderslist_teammate_folders)
  * [`frontcore.message_template_folders.update_folder`](#frontcoremessage_template_foldersupdate_folder)
  * [`frontcore.message_templates.add_new_teammate_template`](#frontcoremessage_templatesadd_new_teammate_template)
  * [`frontcore.message_templates.create_child_template`](#frontcoremessage_templatescreate_child_template)
  * [`frontcore.message_templates.create_new_template`](#frontcoremessage_templatescreate_new_template)
  * [`frontcore.message_templates.create_team_template`](#frontcoremessage_templatescreate_team_template)
  * [`frontcore.message_templates.delete_template`](#frontcoremessage_templatesdelete_template)
  * [`frontcore.message_templates.get_child_templates`](#frontcoremessage_templatesget_child_templates)
  * [`frontcore.message_templates.get_template_by_id`](#frontcoremessage_templatesget_template_by_id)
  * [`frontcore.message_templates.list`](#frontcoremessage_templateslist)
  * [`frontcore.message_templates.list_team_templates`](#frontcoremessage_templateslist_team_templates)
  * [`frontcore.message_templates.list_teammate_templates`](#frontcoremessage_templateslist_teammate_templates)
  * [`frontcore.message_templates.update_template_by_id`](#frontcoremessage_templatesupdate_template_by_id)
  * [`frontcore.messages.create_message_reply`](#frontcoremessagescreate_message_reply)
  * [`frontcore.messages.create_new_message`](#frontcoremessagescreate_new_message)
  * [`frontcore.messages.get_message_by_id`](#frontcoremessagesget_message_by_id)
  * [`frontcore.messages.get_message_seen_status`](#frontcoremessagesget_message_seen_status)
  * [`frontcore.messages.import_new_inbox_message`](#frontcoremessagesimport_new_inbox_message)
  * [`frontcore.messages.mark_message_seen`](#frontcoremessagesmark_message_seen)
  * [`frontcore.messages.receive_custom_message`](#frontcoremessagesreceive_custom_message)
  * [`frontcore.rules.get_rule`](#frontcorerulesget_rule)
  * [`frontcore.rules.list_all_company_rules`](#frontcoreruleslist_all_company_rules)
  * [`frontcore.rules.list_company_rules`](#frontcoreruleslist_company_rules)
  * [`frontcore.rules.list_team_rules`](#frontcoreruleslist_team_rules)
  * [`frontcore.rules.list_teammate_rules`](#frontcoreruleslist_teammate_rules)
  * [`frontcore.shifts.add_teammates_to_shift`](#frontcoreshiftsadd_teammates_to_shift)
  * [`frontcore.shifts.create_shift`](#frontcoreshiftscreate_shift)
  * [`frontcore.shifts.create_team_shift`](#frontcoreshiftscreate_team_shift)
  * [`frontcore.shifts.get_shift`](#frontcoreshiftsget_shift)
  * [`frontcore.shifts.list_shift_teammates`](#frontcoreshiftslist_shift_teammates)
  * [`frontcore.shifts.list_shifts`](#frontcoreshiftslist_shifts)
  * [`frontcore.shifts.list_team_shifts`](#frontcoreshiftslist_team_shifts)
  * [`frontcore.shifts.remove_teammates_from_shift`](#frontcoreshiftsremove_teammates_from_shift)
  * [`frontcore.shifts.teammate_shifts_list`](#frontcoreshiftsteammate_shifts_list)
  * [`frontcore.shifts.update_shift`](#frontcoreshiftsupdate_shift)
  * [`frontcore.signatures.create_team_signature`](#frontcoresignaturescreate_team_signature)
  * [`frontcore.signatures.create_teammate_signature`](#frontcoresignaturescreate_teammate_signature)
  * [`frontcore.signatures.delete_signature`](#frontcoresignaturesdelete_signature)
  * [`frontcore.signatures.get_signature`](#frontcoresignaturesget_signature)
  * [`frontcore.signatures.list_team`](#frontcoresignatureslist_team)
  * [`frontcore.signatures.list_teammate`](#frontcoresignatureslist_teammate)
  * [`frontcore.signatures.update_signature`](#frontcoresignaturesupdate_signature)
  * [`frontcore.tags.create_child_tag`](#frontcoretagscreate_child_tag)
  * [`frontcore.tags.create_company_tag`](#frontcoretagscreate_company_tag)
  * [`frontcore.tags.create_tag_oldest_team`](#frontcoretagscreate_tag_oldest_team)
  * [`frontcore.tags.create_team_tag`](#frontcoretagscreate_team_tag)
  * [`frontcore.tags.create_teammate_tag`](#frontcoretagscreate_teammate_tag)
  * [`frontcore.tags.delete_tag`](#frontcoretagsdelete_tag)
  * [`frontcore.tags.get_tag`](#frontcoretagsget_tag)
  * [`frontcore.tags.list_all`](#frontcoretagslist_all)
  * [`frontcore.tags.list_children`](#frontcoretagslist_children)
  * [`frontcore.tags.list_company`](#frontcoretagslist_company)
  * [`frontcore.tags.list_tagged_conversations`](#frontcoretagslist_tagged_conversations)
  * [`frontcore.tags.list_team_tags`](#frontcoretagslist_team_tags)
  * [`frontcore.tags.list_teammate_tags`](#frontcoretagslist_teammate_tags)
  * [`frontcore.tags.update_tag`](#frontcoretagsupdate_tag)
  * [`frontcore.teammates.get_inbox_list`](#frontcoreteammatesget_inbox_list)
  * [`frontcore.teammates.get_teammate_by_id`](#frontcoreteammatesget_teammate_by_id)
  * [`frontcore.teammates.list_assigned_conversations`](#frontcoreteammateslist_assigned_conversations)
  * [`frontcore.teammates.list_company_members`](#frontcoreteammateslist_company_members)
  * [`frontcore.teammates.update_teammate`](#frontcoreteammatesupdate_teammate)
  * [`frontcore.teams.add_teammates`](#frontcoreteamsadd_teammates)
  * [`frontcore.teams.get_workspace`](#frontcoreteamsget_workspace)
  * [`frontcore.teams.list_teams`](#frontcoreteamslist_teams)
  * [`frontcore.teams.remove_teammates`](#frontcoreteamsremove_teammates)
  * [`frontcore.token_identity.get_details`](#frontcoretoken_identityget_details)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Front&serviceName=Core&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from front_core_python_sdk import FrontCore, ApiException

frontcore = FrontCore(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Add contact to Account
    frontcore.accounts.add_contacts_to_account(
        contact_ids=[
        "string_example"
    ],
        account_id="acc_123",
    )
except ApiException as e:
    print("Exception when calling AccountsApi.add_contacts_to_account: %s\n" % e)
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
from front_core_python_sdk import FrontCore, ApiException

frontcore = FrontCore(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Add contact to Account
        await frontcore.accounts.aadd_contacts_to_account(
            contact_ids=[
        "string_example"
    ],
            account_id="acc_123",
        )
    except ApiException as e:
        print("Exception when calling AccountsApi.add_contacts_to_account: %s\n" % e)
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
from front_core_python_sdk import FrontCore, ApiException

frontcore = FrontCore(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Add contact to Account
    add_contacts_to_account_response = frontcore.accounts.raw.add_contacts_to_account(
        contact_ids=[
        "string_example"
    ],
        account_id="acc_123",
    )
    pprint(add_contacts_to_account_response.headers)
    pprint(add_contacts_to_account_response.status)
    pprint(add_contacts_to_account_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountsApi.add_contacts_to_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `frontcore.accounts.add_contacts_to_account`<a id="frontcoreaccountsadd_contacts_to_account"></a>

Adds a list of contacts to an Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.accounts.add_contacts_to_account(
    contact_ids=[
        "string_example"
    ],
    account_id="acc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_ids: List[`str`]<a id="contact_ids-liststr"></a>

The contact IDs to include. Alternatively, you can supply the contact source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### account_id: `str`<a id="account_id-str"></a>

The Account ID. Alternatively, you can supply the account domain or external ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContactIds`](./front_core_python_sdk/type/contact_ids.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.create_new_account`<a id="frontcoreaccountscreate_new_account"></a>

Create a new account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_account_response = frontcore.accounts.create_new_account(
    description="string_example",
    name="string_example",
    domains=[
        "string_example"
    ],
    external_id="string_example",
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Account description

##### name: `str`<a id="name-str"></a>

Name of the Account

##### domains: [`AccountDomains`](./front_core_python_sdk/type/account_domains.py)<a id="domains-accountdomainsfront_core_python_sdktypeaccount_domainspy"></a>

##### external_id: `str`<a id="external_id-str"></a>

ID of the Account in an external system

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Account`](./front_core_python_sdk/type/account.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.delete_account`<a id="frontcoreaccountsdelete_account"></a>

Deletes an account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.accounts.delete_account(
    account_id="acc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

The Account ID. Alternatively, you can supply the account domain or external ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.get_account`<a id="frontcoreaccountsget_account"></a>

Fetches an account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_response = frontcore.accounts.get_account(
    account_id="acc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

The Account ID. Alternatively, you can supply the account domain or external ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.list_account_contacts`<a id="frontcoreaccountslist_account_contacts"></a>

Lists the contacts associated with an Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_account_contacts_response = frontcore.accounts.list_account_contacts(
    account_id="acc_123",
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    limit=25,
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

The Account ID. Alternatively, you can supply the account domain or external ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the contacts. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListAccountContactsResponse`](./front_core_python_sdk/pydantic/accounts_list_account_contacts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.list_company_accounts`<a id="frontcoreaccountslist_company_accounts"></a>

List the accounts of the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_accounts_response = frontcore.accounts.list_company_accounts(
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the accounts. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListCompanyAccountsResponse`](./front_core_python_sdk/pydantic/accounts_list_company_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.remove_contact_from`<a id="frontcoreaccountsremove_contact_from"></a>

Removes a list of contacts from an Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.accounts.remove_contact_from(
    contact_ids=[
        "string_example"
    ],
    account_id="acc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_ids: List[`str`]<a id="contact_ids-liststr"></a>

The contact IDs to include. Alternatively, you can supply the contact source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### account_id: `str`<a id="account_id-str"></a>

The Account ID. Alternatively, you can supply the account domain or external ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContactIds`](./front_core_python_sdk/type/contact_ids.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}/contacts` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.accounts.update_account`<a id="frontcoreaccountsupdate_account"></a>

Updates an account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_account_response = frontcore.accounts.update_account(
    account_id="acc_123",
    description="string_example",
    name="string_example",
    domains=[
        "string_example"
    ],
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

The Account ID. Alternatively, you can supply the account domain or external ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### description: `str`<a id="description-str"></a>

Account description

##### name: `str`<a id="name-str"></a>

Name of the Account

##### domains: [`AccountPatchDomains`](./front_core_python_sdk/type/account_patch_domains.py)<a id="domains-accountpatchdomainsfront_core_python_sdktypeaccount_patch_domainspy"></a>

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this account. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountPatch`](./front_core_python_sdk/type/account_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.analytics.create_new_export`<a id="frontcoreanalyticscreate_new_export"></a>

Create a new analytics export of messages or events (activities) over a specific time span.
The export will be executed asynchronously. The response will include a link that can be used to retrieve the export status & result. Refer to the [Analytics](https://dev.frontapp.com/reference/analytics) topic for details about specific metrics.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_export_response = frontcore.analytics.create_new_export(
    body={},
    columns=["Activity ID", "Type", "Source", "Message ID", "Conversation ID", "Segment", "Segment start", "Segment end", "Direction", "Status", "Status at activity time", "Inbox", "Inbox API ID", "Inbox at activity time", "Inbox API IDs at activity time", "Previous inbox IDs", "Message date", "Autoreply", "Reaction time", "Total reply time", "Handle time", "Response time", "Stage resolution time", "Replies to resolution", "Attributed to", "Assignee", "Author", "Contact name", "Contact handle", "Account names", "To", "Cc", "Bcc", "Extract", "Tags", "Tag API IDs", "Tags at activity time", "Tag API IDs at activity time", "Tag application duration", "Activity API ID", "Message API ID", "Comment API ID", "Conversation API ID", "Message original ID", "New Conversation", "First response", "Business hours", "Subject", "Account name", "Survey rating", "Survey comment", "Segment closed", "Segment contains messages", "Last segment activity"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### columns: List[[`AnalyticsActivitiesColumns`](./front_core_python_sdk/type/analytics_activities_columns.py)]<a id="columns-listanalyticsactivitiescolumnsfront_core_python_sdktypeanalytics_activities_columnspy"></a>

List of the columns to include in the export. ❗️Columns \\\"Resolution time\\\" and \\\"Final resolution\\\" are deprecated and not supported anymore through the \\\"columns\\\" field. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AnalyticsExportRequest`](./front_core_python_sdk/type/analytics_export_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/exports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.analytics.create_new_report`<a id="frontcoreanalyticscreate_new_report"></a>

Create a new analytics report for a set of metrics over a specific time span. Different filters (e.g. Inbox v Tag v Teammates) will be joined with AND logic, but the IDs within a filter will be joined with OR logic (e.g. Inbox A or Inbox B, Tag A or Tag B).
The report will be executed asynchronously. The response will include a link that can be used to retrieve the
report status & result. Refer to the [Analytics](https://dev.frontapp.com/reference/analytics) topic for details about specific metrics.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_report_response = frontcore.analytics.create_new_report(
    body=None,
    start=3.14,
    end=3.14,
    metrics=[
        "string_example"
    ],
    timezone="string_example",
    filters={
        "tag_ids": [
            "tag_ids_example"
        ],
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start: `Union[int, float]`<a id="start-unionint-float"></a>

Start time of the data to include in the export (seconds since 1970-01-01T00:00:00+00). Will be rounded down to the start of the day.

##### end: `Union[int, float]`<a id="end-unionint-float"></a>

End time of the data to include in the export (seconds since 1970-01-01T00:00:00+00). Will be rounded up to the end of the day.

##### metrics: List[[`AnalyticsMetricId`](./front_core_python_sdk/type/analytics_metric_id.py)]<a id="metrics-listanalyticsmetricidfront_core_python_sdktypeanalytics_metric_idpy"></a>

List of the metrics required.

##### timezone: `str`<a id="timezone-str"></a>

[IANA name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the timezone to format the dates with. If omitted, the export will use Etc/UTC.

##### filters: `AnalyticsFilters`<a id="filters-analyticsfilters"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AnalyticsReportRequest`](./front_core_python_sdk/type/analytics_report_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/reports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.analytics.get_export`<a id="frontcoreanalyticsget_export"></a>

Fetch an analytics exports. Refer to the [Analytics](https://dev.frontapp.com/reference/analytics) topic for details about specific metrics.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_export_response = frontcore.analytics.get_export(
    export_id="exp_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### export_id: `str`<a id="export_id-str"></a>

The export ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/exports/{export_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.analytics.get_report`<a id="frontcoreanalyticsget_report"></a>

Fetch an analytics report. Refer to the [Analytics](https://dev.frontapp.com/reference/analytics) topic for details about specific metrics.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_response = frontcore.analytics.get_report(
    report_uid="723ec32796f12c6f05f6b124d8ef76191a38cec990e0f65d549206c51373f1a0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_uid: `str`<a id="report_uid-str"></a>

The report UID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/reports/{report_uid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.attachments.download_attachment_file`<a id="frontcoreattachmentsdownload_attachment_file"></a>

Download an attachment file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_attachment_file_response = frontcore.attachments.download_attachment_file(
    attachment_link_id="fil_55c8c149",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attachment_link_id: `str`<a id="attachment_link_id-str"></a>

The Attachment ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/download/{attachment_link_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.create_inbox_channel`<a id="frontcorechannelscreate_inbox_channel"></a>

Create a channel in an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.channels.create_inbox_channel(
    body=None,
    type="custom",
    inbox_id="inb_123",
    name="string_example",
    settings={
        "undo_send_time": 0,
    },
    send_as="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of the channel

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

##### name: `str`<a id="name-str"></a>

Name of the channel

##### settings: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="settings-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Settings of the channel

##### send_as: `str`<a id="send_as-str"></a>

Sending address of your channel. Required for SMTP channels.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateChannel`](./front_core_python_sdk/type/create_channel.py)
Channel to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/channels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.get_channel`<a id="frontcorechannelsget_channel"></a>

Fetch a channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_channel_response = frontcore.channels.get_channel(
    channel_id="cha_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The Channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.list`<a id="frontcorechannelslist"></a>

List the channels of the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = frontcore.channels.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ChannelsListResponse`](./front_core_python_sdk/pydantic/channels_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.list_team`<a id="frontcorechannelslist_team"></a>

List the channels of a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_response = frontcore.channels.list_team(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### 🔄 Return<a id="🔄-return"></a>

[`ChannelsListResponse`](./front_core_python_sdk/pydantic/channels_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/channels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.list_teammate`<a id="frontcorechannelslist_teammate"></a>

List the channels of a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_response = frontcore.channels.list_teammate(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`ChannelsListResponse`](./front_core_python_sdk/pydantic/channels_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/channels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.update_channel`<a id="frontcorechannelsupdate_channel"></a>

Update a channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.channels.update_channel(
    body=None,
    channel_id="cha_123",
    name="Your channel name",
    inbox_id="string_example",
    settings={
        "undo_send_time": 0,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The Channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### name: `str`<a id="name-str"></a>

Name of the channel

##### inbox_id: `str`<a id="inbox_id-str"></a>

ID of the inbox to move this channel to. Will also move corresponding conversations.

##### settings: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="settings-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Settings to replace. For custom channels, all settings may be replaced. For all other channels, only `undo_send_time` and `all_teammates_can_reply` may be replaced. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateChannel`](./front_core_python_sdk/type/update_channel.py)
Channel details

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.channels.validate_smtp_settings`<a id="frontcorechannelsvalidate_smtp_settings"></a>

Asynchronously validate an SMTP channel (this endpoint is irrelevant to other channel types). When you create an SMTP channel via the API, [create a channel](https://dev.frontapp.com/reference/post_inboxes-inbox-id-channels) with type smtp and the send_as set to the needed email address. You then [configure the email provider](https://help.front.com/en/articles/2081), after which you use this endpoint to asynchronously validate the SMTP settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_smtp_settings_response = frontcore.channels.validate_smtp_settings(
    channel_id="cha_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The Channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`ChannelsValidateSmtpSettingsResponse`](./front_core_python_sdk/pydantic/channels_validate_smtp_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.comments.add_new_comment`<a id="frontcorecommentsadd_new_comment"></a>

Add a comment to a [conversation](https://dev.frontapp.com/reference/conversations). If you want to create a new comment-only conversation, use the [Create discussion conversation](https://dev.frontapp.com/reference/create-conversation) endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_comment_response = frontcore.comments.add_new_comment(
    body=None,
    body="string_example",
    conversation_id="cnv_123",
    author_id="string_example",
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### body: `str`<a id="body-str"></a>

Content of the comment. Can include markdown formatting.

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate creating the comment. Alternatively, you can supply the author as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1). If omitted, will post as the API Token or OAuth client of the requester.

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateComment`](./front_core_python_sdk/type/create_comment.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.comments.get_comment`<a id="frontcorecommentsget_comment"></a>

Fetches a comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comment_response = frontcore.comments.get_comment(
    comment_id="com_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

The Comment ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{comment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.comments.list_conversation_comments`<a id="frontcorecommentslist_conversation_comments"></a>

List the comments in a conversation in reverse chronological order (newest first).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_conversation_comments_response = frontcore.comments.list_conversation_comments(
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsListConversationCommentsResponse`](./front_core_python_sdk/pydantic/comments_list_conversation_comments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.comments.list_mentioned_teammates`<a id="frontcorecommentslist_mentioned_teammates"></a>

List the teammates mentioned in a comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_mentioned_teammates_response = frontcore.comments.list_mentioned_teammates(
    comment_id="com_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

The Comment ID

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsListMentionedTeammatesResponse`](./front_core_python_sdk/pydantic/comments_list_mentioned_teammates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{comment_id}/mentions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.add_contacts_to_group`<a id="frontcorecontact_groupsadd_contacts_to_group"></a>

Add contacts to the requested group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_groups.add_contacts_to_group(
    body=None,
    contact_ids=[
        "string_example"
    ],
    contact_group_id="grp_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_ids: List[`str`]<a id="contact_ids-liststr"></a>

List of IDs of the contacts to add in the requested group. Alternatively, you can supply the contact source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### contact_group_id: `str`<a id="contact_group_id-str"></a>

The contact group ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddContactsToGroup`](./front_core_python_sdk/type/add_contacts_to_group.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact_groups/{contact_group_id}/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.create_new_group`<a id="frontcorecontact_groupscreate_new_group"></a>

Create a new contact group in the default team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_groups.create_new_group(
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the group

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContactGroup`](./front_core_python_sdk/type/create_contact_group.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact_groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.create_new_group_0`<a id="frontcorecontact_groupscreate_new_group_0"></a>

Create a new contact group for the requested team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_groups.create_new_group_0(
    name="string_example",
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the group

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContactGroup`](./front_core_python_sdk/type/create_contact_group.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/contact_groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.create_teammate_group`<a id="frontcorecontact_groupscreate_teammate_group"></a>

Create a new contact group for the requested teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_groups.create_teammate_group(
    name="string_example",
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the group

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContactGroup`](./front_core_python_sdk/type/create_contact_group.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/contact_groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.delete_group`<a id="frontcorecontact_groupsdelete_group"></a>

Delete a contact group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_groups.delete_group(
    contact_group_id="grp_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_group_id: `str`<a id="contact_group_id-str"></a>

The contact group ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact_groups/{contact_group_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.list_group_contacts`<a id="frontcorecontact_groupslist_group_contacts"></a>

List the contacts belonging to the requested group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_group_contacts_response = frontcore.contact_groups.list_group_contacts(
    contact_group_id="grp_123",
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    limit=25,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_group_id: `str`<a id="contact_group_id-str"></a>

The contact group ID

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListAccountContactsResponse`](./front_core_python_sdk/pydantic/accounts_list_account_contacts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact_groups/{contact_group_id}/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.list_groups`<a id="frontcorecontact_groupslist_groups"></a>

List the contact groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_groups_response = frontcore.contact_groups.list_groups()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContactGroupsListGroupsResponse`](./front_core_python_sdk/pydantic/contact_groups_list_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact_groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.list_team_groups`<a id="frontcorecontact_groupslist_team_groups"></a>

List contact groups belonging to the requested team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_groups_response = frontcore.contact_groups.list_team_groups(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### 🔄 Return<a id="🔄-return"></a>

[`ContactGroupsListGroupsResponse`](./front_core_python_sdk/pydantic/contact_groups_list_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/contact_groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.list_teammate_groups`<a id="frontcorecontact_groupslist_teammate_groups"></a>

List the contact groups belonging to the requested teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_groups_response = frontcore.contact_groups.list_teammate_groups(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`ContactGroupsListGroupsResponse`](./front_core_python_sdk/pydantic/contact_groups_list_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/contact_groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_groups.remove_contacts`<a id="frontcorecontact_groupsremove_contacts"></a>

Remove contacts from the requested group.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_groups.remove_contacts(
    body=None,
    contact_ids=[
        "string_example"
    ],
    contact_group_id="grp_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_ids: List[`str`]<a id="contact_ids-liststr"></a>

List of IDs of the contacts to remove from the requested group. Alternatively, you can supply the contact source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### contact_group_id: `str`<a id="contact_group_id-str"></a>

The contact group ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RemoveContactsFromGroup`](./front_core_python_sdk/type/remove_contacts_from_group.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact_groups/{contact_group_id}/contacts` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_handles.add_new_handle`<a id="frontcorecontact_handlesadd_new_handle"></a>

Adds a new handle to a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_handles.add_new_handle(
    handle="dwight@limitlesspaper.com",
    source="email",
    contact_id="crd_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### handle: `str`<a id="handle-str"></a>

Handle used to reach the contact.

##### source: `str`<a id="source-str"></a>

Source of the handle. Can be `email`, `phone`, `twitter`, `facebook`, `intercom`, `front_chat`, or `custom`.

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContactHandle`](./front_core_python_sdk/type/contact_handle.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}/handles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_handles.remove_handle`<a id="frontcorecontact_handlesremove_handle"></a>

Remove a handle from a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contact_handles.remove_handle(
    body=None,
    contact_id="crd_123",
    handle="dwight@limitlesspaper.com",
    source="email",
    force=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### handle: `str`<a id="handle-str"></a>

Handle used to reach the contact.

##### source: `str`<a id="source-str"></a>

Source of the handle. Can be `email`, `phone`, `twitter`, `facebook`, `intercom`, `front_chat`, or `custom`.

##### force: `bool`<a id="force-bool"></a>

Force the deletetion of the contact if the handle is the last one

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteContactHandle`](./front_core_python_sdk/type/delete_contact_handle.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}/handles` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_notes.create_new_note`<a id="frontcorecontact_notescreate_new_note"></a>

Create a new note on a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_note_response = frontcore.contact_notes.create_new_note(
    author_id="string_example",
    body="string_example",
    contact_id="crd_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### author_id: `str`<a id="author_id-str"></a>

ID of teammate creating the note

##### body: `str`<a id="body-str"></a>

Content of the note

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContactNote`](./front_core_python_sdk/type/create_contact_note.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContactNoteResponses`](./front_core_python_sdk/pydantic/contact_note_responses.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}/notes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contact_notes.list`<a id="frontcorecontact_noteslist"></a>

List the notes added to a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = frontcore.contact_notes.list(
    contact_id="crd_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`ContactNotesListResponse`](./front_core_python_sdk/pydantic/contact_notes_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}/notes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.create_new_contact`<a id="frontcorecontactscreate_new_contact"></a>

Create a new contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_contact_response = frontcore.contacts.create_new_contact(
    body=None,
    handles=[
        {
            "handle": "dwight@limitlesspaper.com",
            "source": "email",
        }
    ],
    description="string_example",
    name="string_example",
    avatar=open('/path/to/file', 'rb'),
    is_spammer=True,
    links=[
        "string_example"
    ],
    group_names=[
        "string_example"
    ],
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### handles: List[`ContactHandle`]<a id="handles-listcontacthandle"></a>

List of the handles for this contact. Each handle object should include `handle` and `source` fields.

##### description: `str`<a id="description-str"></a>

Contact description

##### name: `str`<a id="name-str"></a>

Contact name

##### avatar: `IO`<a id="avatar-io"></a>

Binary data of avatar. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

##### is_spammer: `bool`<a id="is_spammer-bool"></a>

Whether or not the contact is marked as a spammer

##### links: List[`str`]<a id="links-liststr"></a>

List of all the links of the contact

##### group_names: List[`str`]<a id="group_names-liststr"></a>

List of all the group names the contact belongs to. It will automatically create missing groups

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this contact. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContact`](./front_core_python_sdk/type/create_contact.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.create_team_contact`<a id="frontcorecontactscreate_team_contact"></a>

Create a contact for a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_contact_response = frontcore.contacts.create_team_contact(
    body=None,
    handles=[
        {
            "handle": "dwight@limitlesspaper.com",
            "source": "email",
        }
    ],
    team_id="tim_123",
    description="string_example",
    name="string_example",
    avatar=open('/path/to/file', 'rb'),
    is_spammer=True,
    links=[
        "string_example"
    ],
    group_names=[
        "string_example"
    ],
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### handles: List[`ContactHandle`]<a id="handles-listcontacthandle"></a>

List of the handles for this contact. Each handle object should include `handle` and `source` fields.

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### description: `str`<a id="description-str"></a>

Contact description

##### name: `str`<a id="name-str"></a>

Contact name

##### avatar: `IO`<a id="avatar-io"></a>

Binary data of avatar. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

##### is_spammer: `bool`<a id="is_spammer-bool"></a>

Whether or not the contact is marked as a spammer

##### links: List[`str`]<a id="links-liststr"></a>

List of all the links of the contact

##### group_names: List[`str`]<a id="group_names-liststr"></a>

List of all the group names the contact belongs to. It will automatically create missing groups

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this contact. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContact`](./front_core_python_sdk/type/create_contact.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.create_teammate_contact`<a id="frontcorecontactscreate_teammate_contact"></a>

Create a contact for a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_teammate_contact_response = frontcore.contacts.create_teammate_contact(
    body=None,
    handles=[
        {
            "handle": "dwight@limitlesspaper.com",
            "source": "email",
        }
    ],
    teammate_id="tea_123",
    description="string_example",
    name="string_example",
    avatar=open('/path/to/file', 'rb'),
    is_spammer=True,
    links=[
        "string_example"
    ],
    group_names=[
        "string_example"
    ],
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### handles: List[`ContactHandle`]<a id="handles-listcontacthandle"></a>

List of the handles for this contact. Each handle object should include `handle` and `source` fields.

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### description: `str`<a id="description-str"></a>

Contact description

##### name: `str`<a id="name-str"></a>

Contact name

##### avatar: `IO`<a id="avatar-io"></a>

Binary data of avatar. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

##### is_spammer: `bool`<a id="is_spammer-bool"></a>

Whether or not the contact is marked as a spammer

##### links: List[`str`]<a id="links-liststr"></a>

List of all the links of the contact

##### group_names: List[`str`]<a id="group_names-liststr"></a>

List of all the group names the contact belongs to. It will automatically create missing groups

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this contact. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContact`](./front_core_python_sdk/type/create_contact.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.delete_contact`<a id="frontcorecontactsdelete_contact"></a>

Delete a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contacts.delete_contact(
    contact_id="crd_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.get_one_contact`<a id="frontcorecontactsget_one_contact"></a>

Fetch a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_contact_response = frontcore.contacts.get_one_contact(
    contact_id="crd_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.list_company_contacts`<a id="frontcorecontactslist_company_contacts"></a>

List the contacts of the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_contacts_response = frontcore.contacts.list_company_contacts(
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with the optional properties `updated_after` and `updated_before`, whose value should be a timestamp in seconds with up to 3 decimal places.

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the contacts. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListAccountContactsResponse`](./front_core_python_sdk/pydantic/accounts_list_account_contacts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.list_conversations_reverse_chronological_order`<a id="frontcorecontactslist_conversations_reverse_chronological_order"></a>

List the conversations for a contact in reverse chronological order (newest first). For more advanced filtering, see the [search endpoint](https://dev.frontapp.com/reference/conversations#search-conversations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_conversations_reverse_chronological_order_response = frontcore.contacts.list_conversations_reverse_chronological_order(
    contact_id="crd_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

The Contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `statuses`, whose value should be a list of conversation statuses (`assigned`, `unassigned`, `archived`, or `deleted`).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`ContactsListConversationsReverseChronologicalOrderResponse`](./front_core_python_sdk/pydantic/contacts_list_conversations_reverse_chronological_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}/conversations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.list_team_contacts`<a id="frontcorecontactslist_team_contacts"></a>

List the contacts of a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_contacts_response = frontcore.contacts.list_team_contacts(
    team_id="tim_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with the optional properties `updated_after` and `updated_before`, whose value should be a timestamp in seconds with up to 3 decimal places.

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the contacts. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListAccountContactsResponse`](./front_core_python_sdk/pydantic/accounts_list_account_contacts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.list_teammate_contacts`<a id="frontcorecontactslist_teammate_contacts"></a>

List the contacts of a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_contacts_response = frontcore.contacts.list_teammate_contacts(
    teammate_id="tea_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with the optional properties `updated_after` and `updated_before`, whose value should be a timestamp in seconds with up to 3 decimal places.

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the contacts. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListAccountContactsResponse`](./front_core_python_sdk/pydantic/accounts_list_account_contacts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.merge_contacts`<a id="frontcorecontactsmerge_contacts"></a>

Merges the contacts specified into a single contact, deleting the merged-in contacts.
If a target contact ID is supplied, the other contacts will be merged into that one.
Otherwise, some contact in the contact ID list will be treated as the target contact.
Merge conflicts will be resolved in the following ways:
  * name will prioritize manually-updated and non-private contact names
  * descriptions will be concatenated and separated by newlines in order from
    oldest to newest with the (optional) target contact's description first
  * all handles, groups, links, and notes will be preserved
  * other conflicts will use the most recently updated contact's value


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
merge_contacts_response = frontcore.contacts.merge_contacts(
    body=None,
    contact_ids=[
        "string_example"
    ],
    target_contact_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_ids: List[`str`]<a id="contact_ids-liststr"></a>

Array of all the contact IDs of the contacts to be merged.  If a target contact id is provided and that contact id is not in this array, the length of this array must be between 1 and 49.  If no target contact id is provided or it is contained in this array, the length must be between 2 and 50.

##### target_contact_id: `str`<a id="target_contact_id-str"></a>

Optional contact ID to merge the other contacts into.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MergeContacts`](./front_core_python_sdk/type/merge_contacts.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/merge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.contacts.update_contact`<a id="frontcorecontactsupdate_contact"></a>

Updates a contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.contacts.update_contact(
    body=None,
    contact_id="crd_123",
    description="string_example",
    name="string_example",
    avatar=open('/path/to/file', 'rb'),
    is_spammer=True,
    links=[
        "string_example"
    ],
    group_names=[
        "string_example"
    ],
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

The contact ID. Alternatively, you can supply the contact's source and handle as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### description: `str`<a id="description-str"></a>

Contact description

##### name: `str`<a id="name-str"></a>

Contact name

##### avatar: `IO`<a id="avatar-io"></a>

Binary data of avatar. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

##### is_spammer: `bool`<a id="is_spammer-bool"></a>

Whether or not the contact is marked as a spammer

##### links: List[`str`]<a id="links-liststr"></a>

List of all the links of the contact

##### group_names: List[`str`]<a id="group_names-liststr"></a>

List of all the group names the contact belongs to. It will automatically create missing groups

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this contact. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Contact`](./front_core_python_sdk/type/contact.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/{contact_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.add_followers`<a id="frontcoreconversationsadd_followers"></a>

Adds teammates to the list of followers of a conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.add_followers(
    teammate_ids=[
        "string_example"
    ],
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: [`ConversationsAddFollowersRequestTeammateIds`](./front_core_python_sdk/type/conversations_add_followers_request_teammate_ids.py)<a id="teammate_ids-conversationsaddfollowersrequestteammateidsfront_core_python_sdktypeconversations_add_followers_request_teammate_idspy"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConversationsAddFollowersRequest`](./front_core_python_sdk/type/conversations_add_followers_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/followers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.add_link`<a id="frontcoreconversationsadd_link"></a>

Adds one or more links to a conversation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.add_link(
    conversation_id="cnv_123",
    link_ids=[
        "string_example"
    ],
    link_external_urls=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### link_ids: [`ConversationsAddLinkRequestLinkIds`](./front_core_python_sdk/type/conversations_add_link_request_link_ids.py)<a id="link_ids-conversationsaddlinkrequestlinkidsfront_core_python_sdktypeconversations_add_link_request_link_idspy"></a>

##### link_external_urls: [`ConversationsAddLinkRequestLinkExternalUrls`](./front_core_python_sdk/type/conversations_add_link_request_link_external_urls.py)<a id="link_external_urls-conversationsaddlinkrequestlinkexternalurlsfront_core_python_sdktypeconversations_add_link_request_link_external_urlspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConversationsAddLinkRequest`](./front_core_python_sdk/type/conversations_add_link_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/links` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.add_tags_to_conversation`<a id="frontcoreconversationsadd_tags_to_conversation"></a>

Adds one or more tags to a conversation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.add_tags_to_conversation(
    tag_ids=[
        "string_example"
    ],
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_ids: List[`str`]<a id="tag_ids-liststr"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagIds`](./front_core_python_sdk/type/tag_ids.py)
Tag IDs to add

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.create_discussion`<a id="frontcoreconversationscreate_discussion"></a>

Create a new [conversation](https://dev.frontapp.com/reference/conversations#creating-a-new-conversation) that only supports comments (known as discussions in Front). If you want to create a conversation that supports messages, use the [Create message](https://dev.frontapp.com/reference/post_channels-channel-id-messages) endpoint. If you want to add a comment to an existing conversation, use the [Add comment](https://dev.frontapp.com/reference/post_conversations-conversation-id-comments) endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_discussion_response = frontcore.conversations.create_discussion(
    body=None,
    type="discussion",
    subject="string_example",
    comment={
        "body": "body_example",
    },
    inbox_id="string_example",
    teammate_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Conversation type

##### subject: `str`<a id="subject-str"></a>

Subject of the conversation

##### comment: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Details for the starter comment

##### inbox_id: `str`<a id="inbox_id-str"></a>

Inbox ID for the conversation. Either `inbox_id` OR `teammate_ids` must be provided (not both).

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

Teammates to add to the conversation. Either `inbox_id` OR `teammate_ids` must be provided (not both).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateConversation`](./front_core_python_sdk/type/create_conversation.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.get_by_id`<a id="frontcoreconversationsget_by_id"></a>

Fetch a conversation.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = frontcore.conversations.get_by_id(
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.list_events`<a id="frontcoreconversationslist_events"></a>

List the events that occured for a conversation in reverse chronological order (newest first). The order will respect your company's [bump settings](https://help.front.com/t/y729th/customize-when-conversations-bump-up), which determine when conversations bump to the top.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_events_response = frontcore.conversations.list_events(
    conversation_id="cnv_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsListEventsResponse`](./front_core_python_sdk/pydantic/conversations_list_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.list_followers`<a id="frontcoreconversationslist_followers"></a>

List the teammates following a conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_followers_response = frontcore.conversations.list_followers(
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsListMentionedTeammatesResponse`](./front_core_python_sdk/pydantic/comments_list_mentioned_teammates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/followers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.list_in_reverse_chronological_order`<a id="frontcoreconversationslist_in_reverse_chronological_order"></a>

List the conversations in the company in reverse chronological order (most recently updated first). The order will respect your company's [bump settings](https://help.front.com/t/y729th/customize-when-conversations-bump-up), which determine when conversations bump to the top. For more advanced filtering, see the [search endpoint](https://dev.frontapp.com/reference/conversations#search-conversations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_in_reverse_chronological_order_response = frontcore.conversations.list_in_reverse_chronological_order(
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `statuses`, whose value should be a list of conversation statuses (`assigned`, `unassigned`, `archived`, or `deleted`).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the conversations. Only supports `date`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`ContactsListConversationsReverseChronologicalOrderResponse`](./front_core_python_sdk/pydantic/contacts_list_conversations_reverse_chronological_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.list_inboxes`<a id="frontcoreconversationslist_inboxes"></a>

List the inboxes in which a conversation is listed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_inboxes_response = frontcore.conversations.list_inboxes(
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsListInboxesResponse`](./front_core_python_sdk/pydantic/conversations_list_inboxes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/inboxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.list_messages_in_reverse_chronological_order`<a id="frontcoreconversationslist_messages_in_reverse_chronological_order"></a>

List the messages in a conversation in reverse chronological order (newest first).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_messages_in_reverse_chronological_order_response = frontcore.conversations.list_messages_in_reverse_chronological_order(
    conversation_id="cnv_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the messages. Only supports `created_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`DraftsListConversationDraftsResponse`](./front_core_python_sdk/pydantic/drafts_list_conversation_drafts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/messages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.remove_followers`<a id="frontcoreconversationsremove_followers"></a>

Removes teammates from the list of followers of a conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.remove_followers(
    teammate_ids=[
        "string_example"
    ],
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: [`ConversationsRemoveFollowersRequestTeammateIds`](./front_core_python_sdk/type/conversations_remove_followers_request_teammate_ids.py)<a id="teammate_ids-conversationsremovefollowersrequestteammateidsfront_core_python_sdktypeconversations_remove_followers_request_teammate_idspy"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConversationsRemoveFollowersRequest`](./front_core_python_sdk/type/conversations_remove_followers_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/followers` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.remove_links`<a id="frontcoreconversationsremove_links"></a>

Removes one or more links to a conversation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.remove_links(
    link_ids=[
        "string_example"
    ],
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_ids: [`ConversationsRemoveLinksRequestLinkIds`](./front_core_python_sdk/type/conversations_remove_links_request_link_ids.py)<a id="link_ids-conversationsremovelinksrequestlinkidsfront_core_python_sdktypeconversations_remove_links_request_link_idspy"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConversationsRemoveLinksRequest`](./front_core_python_sdk/type/conversations_remove_links_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/links` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.remove_tag`<a id="frontcoreconversationsremove_tag"></a>

Removes one or more tags to a conversation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.remove_tag(
    tag_ids=[
        "string_example"
    ],
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_ids: List[`str`]<a id="tag_ids-liststr"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagIds`](./front_core_python_sdk/type/tag_ids.py)
Tag IDs to remove

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/tags` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.search_by_query`<a id="frontcoreconversationssearch_by_query"></a>

Search for conversations. Response will include a count of total matches and an array of conversations in descending order by last activity.
See the [search syntax documentation](https://dev.frontapp.com/docs/search-1) for usage examples.
**Note:** This endpoint is subject to [proportional rate limiting](https://dev.frontapp.com/docs/rate-limiting#additional-proportional-limiting) at 40% of your company's rate limit.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_by_query_response = frontcore.conversations.search_by_query(
    query="inbox:inb_123 tag:tag_345",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

Search query string. See [Search](https://dev.frontapp.com/docs/search-1) topic for usage details.

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsSearchByQueryResponse`](./front_core_python_sdk/pydantic/conversations_search_by_query_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/search/{query}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.update_assignee`<a id="frontcoreconversationsupdate_assignee"></a>

Assign or unassign a conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.update_assignee(
    body=None,
    assignee_id="string_example",
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### assignee_id: `str`<a id="assignee_id-str"></a>

ID of the teammate to assign the conversation to. Set it to null to unassign.

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateConversationAssignee`](./front_core_python_sdk/type/update_conversation_assignee.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/assignee` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.update_conversation_by_id`<a id="frontcoreconversationsupdate_conversation_by_id"></a>

Update a conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.update_conversation_by_id(
    body=None,
    conversation_id="cnv_123",
    assignee_id="string_example",
    inbox_id="string_example",
    status="archived",
    tag_ids=[
        "string_example"
    ],
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### assignee_id: `str`<a id="assignee_id-str"></a>

ID of the teammate to assign the conversation to. Set it to null to unassign.

##### inbox_id: `str`<a id="inbox_id-str"></a>

ID of the inbox to move the conversation to.

##### status: `str`<a id="status-str"></a>

New status of the conversation

##### tag_ids: List[`str`]<a id="tag_ids-liststr"></a>

List of all the tag IDs replacing the old conversation tags

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this conversation. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateConversation`](./front_core_python_sdk/type/update_conversation.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.conversations.update_reminders`<a id="frontcoreconversationsupdate_reminders"></a>

Snooze or unsnooze a conversation for the provided user.
For private conversations, reminders can only be created and edited through the API for teammates that own the conversation.
For shared conversations, reminders created and edited through the API are shared for all teammates within the shared inbox(es) that the conversation belongs to.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.conversations.update_reminders(
    body=None,
    teammate_id="string_example",
    scheduled_at=3.14,
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

ID of the teammate to create a reminder for. For a private conversation, specify the id of the teammate that owns the conversation. For a shared conversation, use the id of any teammate that has access to the conversation's shared inbox. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### scheduled_at: `Union[int, float]`<a id="scheduled_at-unionint-float"></a>

Timestamp to schedule the reminder for. Set to null to cancel.

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateConversationReminders`](./front_core_python_sdk/type/update_conversation_reminders.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/reminders` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.get_list`<a id="frontcorecustom_fieldsget_list"></a>

Lists the custom fields that can be attached to a Link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = frontcore.custom_fields.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.list_account_custom_fields`<a id="frontcorecustom_fieldslist_account_custom_fields"></a>

Lists the custom fields that can be attached to an Account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_account_custom_fields_response = frontcore.custom_fields.list_account_custom_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.list_contact_custom_fields`<a id="frontcorecustom_fieldslist_contact_custom_fields"></a>

Lists the custom fields that can be attached to a Contact.

> ⚠️ Deprecated endpoint
>
> This endpoint has been deprecated. Please use the fully compatible `GET /contacts/custom_fields` endpoint instead.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_contact_custom_fields_response = frontcore.custom_fields.list_contact_custom_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.list_contact_fields`<a id="frontcorecustom_fieldslist_contact_fields"></a>

Lists the custom fields that can be attached to a Contact.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_contact_fields_response = frontcore.custom_fields.list_contact_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.list_conversation_custom_fields`<a id="frontcorecustom_fieldslist_conversation_custom_fields"></a>

Lists the custom fields that can be attached to a Conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_conversation_custom_fields_response = frontcore.custom_fields.list_conversation_custom_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.list_inbox_custom_fields`<a id="frontcorecustom_fieldslist_inbox_custom_fields"></a>

Lists the custom fields that can be attached to an Inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_inbox_custom_fields_response = frontcore.custom_fields.list_inbox_custom_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.custom_fields.list_teammate_custom_fields`<a id="frontcorecustom_fieldslist_teammate_custom_fields"></a>

Lists the custom fields that can be attached to a Teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_custom_fields_response = frontcore.custom_fields.list_teammate_custom_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListAccountCustomFieldsResponse`](./front_core_python_sdk/pydantic/custom_fields_list_account_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.drafts.create_draft_reply`<a id="frontcoredraftscreate_draft_reply"></a>

Create a new draft as a reply to the last message in the conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_draft_reply_response = frontcore.drafts.create_draft_reply(
    body=None,
    author_id="string_example",
    body="string_example",
    channel_id="string_example",
    conversation_id="cnv_123",
    to=[
        "string_example"
    ],
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    subject="string_example",
    quote_body="string_example",
    attachments=[
        open('/path/to/file', 'rb')
    ],
    mode="private",
    signature_id="string_example",
    should_add_default_signature=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate on behalf of whom the draft will be created. Alternatively, you can supply the author ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### body: `str`<a id="body-str"></a>

Body of the draft

##### channel_id: `str`<a id="channel_id-str"></a>

ID of the channel from which the draft will be sent. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### to: List[`str`]<a id="to-liststr"></a>

List of recipient handles who will receive the message once the draft is sent

##### cc: List[`str`]<a id="cc-liststr"></a>

List of recipient handles who will receive a copy of the message once the draft is sent

##### bcc: List[`str`]<a id="bcc-liststr"></a>

List of the recipient handles who will receive a blind copy of the message once the draft is sent

##### subject: `str`<a id="subject-str"></a>

Subject of the draft.

##### quote_body: `str`<a id="quote_body-str"></a>

Body for the quote that the message is referencing. Only available on email channels.

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1). Max 25 MB.

##### mode: `str`<a id="mode-str"></a>

Mode of the draft to create. Can be 'private' (draft is visible to the author only) or 'shared' (draft is visible to all teammates with access to the conversation).

##### signature_id: `str`<a id="signature_id-str"></a>

ID of the signature to attach to this draft. If null, no signature is attached.

##### should_add_default_signature: `bool`<a id="should_add_default_signature-bool"></a>

Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReplyDraft`](./front_core_python_sdk/type/reply_draft.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/drafts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.drafts.create_new_draft_message`<a id="frontcoredraftscreate_new_draft_message"></a>

Create a draft message which is the first message of a new [conversation](https://dev.frontapp.com/reference/conversations).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_draft_message_response = frontcore.drafts.create_new_draft_message(
    body=None,
    author_id="string_example",
    body="string_example",
    channel_id="cha_123",
    to=[
        "string_example"
    ],
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    subject="string_example",
    quote_body="string_example",
    attachments=[
        open('/path/to/file', 'rb')
    ],
    mode="private",
    signature_id="string_example",
    should_add_default_signature=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate on behalf of whom the draft will be created. Alternatively, you can supply the author ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### body: `str`<a id="body-str"></a>

Body of the draft

##### channel_id: `str`<a id="channel_id-str"></a>

The channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### to: List[`str`]<a id="to-liststr"></a>

List of recipient handles who will receive the message once the draft is sent

##### cc: List[`str`]<a id="cc-liststr"></a>

List of recipient handles who will receive a copy of the message once the draft is sent

##### bcc: List[`str`]<a id="bcc-liststr"></a>

List of the recipient handles who will receive a blind copy of the message once the draft is sent

##### subject: `str`<a id="subject-str"></a>

Subject of the draft.

##### quote_body: `str`<a id="quote_body-str"></a>

Body for the quote that the message is referencing. Only available on email channels.

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1). Max 25 MB.

##### mode: `str`<a id="mode-str"></a>

Mode of the draft to create. Can be 'private' (draft is visible to the author only) or 'shared' (draft is visible to all teammates with access to the conversation).

##### signature_id: `str`<a id="signature_id-str"></a>

ID of the signature to attach to this draft. If null, no signature is attached.

##### should_add_default_signature: `bool`<a id="should_add_default_signature-bool"></a>

Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDraft`](./front_core_python_sdk/type/create_draft.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/drafts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.drafts.delete_draft_message`<a id="frontcoredraftsdelete_draft_message"></a>

Delete a draft message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.drafts.delete_draft_message(
    body=None,
    version="string_example",
    draft_id="msg_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### version: `str`<a id="version-str"></a>

Version of the draft

##### draft_id: `str`<a id="draft_id-str"></a>

The draft ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteDraft`](./front_core_python_sdk/type/delete_draft.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/drafts/{draft_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.drafts.edit_message`<a id="frontcoredraftsedit_message"></a>

Edit a draft message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_message_response = frontcore.drafts.edit_message(
    body=None,
    author_id="string_example",
    body="string_example",
    channel_id="string_example",
    message_id="msg_123",
    to=[
        "string_example"
    ],
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    subject="string_example",
    quote_body="string_example",
    attachments=[
        open('/path/to/file', 'rb')
    ],
    mode="shared",
    signature_id="string_example",
    should_add_default_signature=True,
    version="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate on behalf of whom the draft will be created. Alternatively, you can supply the author ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### body: `str`<a id="body-str"></a>

Body of the draft

##### channel_id: `str`<a id="channel_id-str"></a>

ID of the channel from which the draft will be sent. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### message_id: `str`<a id="message_id-str"></a>

The draft ID

##### to: List[`str`]<a id="to-liststr"></a>

List of recipient handles who will receive the message once the draft is sent

##### cc: List[`str`]<a id="cc-liststr"></a>

List of recipient handles who will receive a copy of the message once the draft is sent

##### bcc: List[`str`]<a id="bcc-liststr"></a>

List of the recipient handles who will receive a blind copy of the message once the draft is sent

##### subject: `str`<a id="subject-str"></a>

Subject of the draft.

##### quote_body: `str`<a id="quote_body-str"></a>

Body for the quote that the message is referencing. Only available on email channels.

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1). Max 25 MB.

##### mode: `str`<a id="mode-str"></a>

Mode of the draft to update. Can only be 'shared' (draft is visible to all teammates with access to the conversation).

##### signature_id: `str`<a id="signature_id-str"></a>

ID of the signature to attach to this draft. If null, no signature is attached.

##### should_add_default_signature: `bool`<a id="should_add_default_signature-bool"></a>

Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;

##### version: `str`<a id="version-str"></a>

Version of the draft

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EditDraft`](./front_core_python_sdk/type/edit_draft.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/drafts/{message_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.drafts.list_conversation_drafts`<a id="frontcoredraftslist_conversation_drafts"></a>

List the drafts in a conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_conversation_drafts_response = frontcore.drafts.list_conversation_drafts(
    conversation_id="cnv_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

#### 🔄 Return<a id="🔄-return"></a>

[`DraftsListConversationDraftsResponse`](./front_core_python_sdk/pydantic/drafts_list_conversation_drafts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/drafts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.events.get_event`<a id="frontcoreeventsget_event"></a>

Fetch an event.
Refer to the [Events](https://dev.frontapp.com/reference/events) topic for more information, including sorting and filtering.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_response = frontcore.events.get_event(
    event_id="evt_55c8c149",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### event_id: `str`<a id="event_id-str"></a>

The event ID

#### 🔄 Return<a id="🔄-return"></a>

[`EventResponse`](./front_core_python_sdk/pydantic/event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{event_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.events.list_detailed_inbox_events`<a id="frontcoreeventslist_detailed_inbox_events"></a>

Lists all the detailed events which occured in the inboxes of the company ordered in reverse chronological order (newest first).
Refer to the [Events](https://dev.frontapp.com/reference/events) topic for more information, including sorting and filtering.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_detailed_inbox_events_response = frontcore.events.list_detailed_inbox_events(
    q="string_example",
    limit=15,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with optional properties `before`, `after`, or `types`. `before` and `after` should be a timestamp in seconds with up to 3 decimal places. `types` should be a list of [event types](https://dev.frontapp.com/reference/events).

##### limit: `int`<a id="limit-int"></a>

Max number of results per page (max 15)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the events. Only supports `created_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsListEventsResponse`](./front_core_python_sdk/pydantic/conversations_list_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.add_teammate_access`<a id="frontcoreinboxesadd_teammate_access"></a>

Give access to one or more teammates to an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.inboxes.add_teammate_access(
    teammate_ids=[
        "string_example"
    ],
    inbox_id="inb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeammateIds`](./front_core_python_sdk/type/teammate_ids.py)
Teammate IDs to add. Alternatively, you can supply teammate emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/teammates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.create_default_team_inbox`<a id="frontcoreinboxescreate_default_team_inbox"></a>

Create an inbox in the default team (workspace). The default team will be the oldest team created that still exists at the time of the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.inboxes.create_default_team_inbox(
    name="string_example",
    teammate_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the inbox

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

An array of teammate IDs that should have access to the inbox. Alternatively, you can supply teammate emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateInbox`](./front_core_python_sdk/type/create_inbox.py)
Inbox details

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.create_team_inbox`<a id="frontcoreinboxescreate_team_inbox"></a>

Create an inbox for a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.inboxes.create_team_inbox(
    name="string_example",
    team_id="tim_123",
    teammate_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the inbox

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

An array of teammate IDs that should have access to the inbox. Alternatively, you can supply teammate emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateInbox`](./front_core_python_sdk/type/create_inbox.py)
Inbox details

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/inboxes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.get_inbox`<a id="frontcoreinboxesget_inbox"></a>

Fetch an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_inbox_response = frontcore.inboxes.get_inbox(
    inbox_id="inb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.list_channels`<a id="frontcoreinboxeslist_channels"></a>

List the channels in an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_channels_response = frontcore.inboxes.list_channels(
    inbox_id="inb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

#### 🔄 Return<a id="🔄-return"></a>

[`ChannelsListResponse`](./front_core_python_sdk/pydantic/channels_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/channels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.list_conversations_inbox`<a id="frontcoreinboxeslist_conversations_inbox"></a>

List the conversations in an inbox. For more advanced filtering, see the [search endpoint](https://dev.frontapp.com/reference/conversations#search-conversations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_conversations_inbox_response = frontcore.inboxes.list_conversations_inbox(
    inbox_id="inb_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `statuses`, whose value should be a list of conversation statuses (`assigned`, `unassigned`, `archived`, or `deleted`).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`ContactsListConversationsReverseChronologicalOrderResponse`](./front_core_python_sdk/pydantic/contacts_list_conversations_reverse_chronological_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/conversations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.list_inboxes`<a id="frontcoreinboxeslist_inboxes"></a>

List the inboxes of the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_inboxes_response = frontcore.inboxes.list_inboxes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsListInboxesResponse`](./front_core_python_sdk/pydantic/conversations_list_inboxes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.list_team_inboxes`<a id="frontcoreinboxeslist_team_inboxes"></a>

List the inboxes belonging to a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_inboxes_response = frontcore.inboxes.list_team_inboxes(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsListInboxesResponse`](./front_core_python_sdk/pydantic/conversations_list_inboxes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/inboxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.list_teammates_access`<a id="frontcoreinboxeslist_teammates_access"></a>

List the teammates with access to an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammates_access_response = frontcore.inboxes.list_teammates_access(
    inbox_id="inb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsListMentionedTeammatesResponse`](./front_core_python_sdk/pydantic/comments_list_mentioned_teammates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/teammates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.inboxes.remove_access`<a id="frontcoreinboxesremove_access"></a>

Remove access of one or more teammates from an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.inboxes.remove_access(
    teammate_ids=[
        "string_example"
    ],
    inbox_id="inb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeammateIds`](./front_core_python_sdk/type/teammate_ids.py)
Teammate IDs to remove. Alternatively, you can supply teammate emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/teammates` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.create_article_default_locale`<a id="frontcoreknowledge_basescreate_article_default_locale"></a>

Creates an article in a knowledge base in the default locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_article_default_locale_response = frontcore.knowledge_bases.create_article_default_locale(
    knowledge_base_id="knb_123",
    category_id="string_example",
    author_id="string_example",
    subject="string_example",
    content="string_example",
    status="draft",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to create the article in

##### category_id: `str`<a id="category_id-str"></a>

ID of the category this article belongs to

##### author_id: `str`<a id="author_id-str"></a>

Teammate ID of the article author

##### subject: `str`<a id="subject-str"></a>

Subject of the article

##### content: `str`<a id="content-str"></a>

HTML content of the article

##### status: `str`<a id="status-str"></a>

Article status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseArticleCreate`](./front_core_python_sdk/type/knowledge_base_article_create.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/articles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.create_article_locale`<a id="frontcoreknowledge_basescreate_article_locale"></a>

Create an article for a given locale in a knowledge base.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_article_locale_response = frontcore.knowledge_bases.create_article_locale(
    knowledge_base_id="knb_123",
    locale="en",
    category_id="string_example",
    author_id="string_example",
    subject="string_example",
    content="string_example",
    status="draft",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to create the article in

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the article's content

##### category_id: `str`<a id="category_id-str"></a>

ID of the category this article belongs to

##### author_id: `str`<a id="author_id-str"></a>

Teammate ID of the article author

##### subject: `str`<a id="subject-str"></a>

Subject of the article

##### content: `str`<a id="content-str"></a>

HTML content of the article

##### status: `str`<a id="status-str"></a>

Article status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseArticleCreate`](./front_core_python_sdk/type/knowledge_base_article_create.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/locales/{locale}/articles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.create_category_default_locale`<a id="frontcoreknowledge_basescreate_category_default_locale"></a>

Creates a knowledge base category in the default locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_category_default_locale_response = frontcore.knowledge_bases.create_category_default_locale(
    name="string_example",
    knowledge_base_id="knb_123",
    description="string_example",
    parent_category_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the knowledge base category

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to create the category in

##### description: `str`<a id="description-str"></a>

Description of the knowledge base category

##### parent_category_id: `str`<a id="parent_category_id-str"></a>

ID of the parent category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseCategoryCreate`](./front_core_python_sdk/type/knowledge_base_category_create.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/categories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.create_category_in_locale`<a id="frontcoreknowledge_basescreate_category_in_locale"></a>

Creates a knowledge base category for a given locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_category_in_locale_response = frontcore.knowledge_bases.create_category_in_locale(
    name="string_example",
    knowledge_base_id="knb_123",
    locale="en",
    description="string_example",
    parent_category_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the knowledge base category

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to create the category in

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the category's content

##### description: `str`<a id="description-str"></a>

Description of the knowledge base category

##### parent_category_id: `str`<a id="parent_category_id-str"></a>

ID of the parent category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseCategoryCreate`](./front_core_python_sdk/type/knowledge_base_category_create.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/locales/{locale}/categories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.create_new_knowledge_base`<a id="frontcoreknowledge_basescreate_new_knowledge_base"></a>

Creates a knowledge base.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_knowledge_base_response = frontcore.knowledge_bases.create_new_knowledge_base(
    name="string_example",
    type="internal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the knowledge base

##### type: `str`<a id="type-str"></a>

Determines if the knowledge base is publicly available or private only to your company

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseCreate`](./front_core_python_sdk/type/knowledge_base_create.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.delete_article`<a id="frontcoreknowledge_basesdelete_article"></a>

Deletes an article and all its content and translations.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_article_response = frontcore.knowledge_bases.delete_article(
    article_id="kba_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.delete_category`<a id="frontcoreknowledge_basesdelete_category"></a>

Deletes a knowledge base category.

> ⚠️ Warning
>
> When a category is deleted, all articles in the category are also deleted.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.knowledge_bases.delete_category(
    category_id="kbc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.download_attachment_article`<a id="frontcoreknowledge_basesdownload_attachment_article"></a>

Downloads the attachment from an article.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_attachment_article_response = frontcore.knowledge_bases.download_attachment_article(
    article_id="kba_123",
    attachment_id="attachment_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article

##### attachment_id: `str`<a id="attachment_id-str"></a>

The ID of the file to download

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}/download/{attachment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_article_by_id`<a id="frontcoreknowledge_basesget_article_by_id"></a>

Fetches a knowledge base article.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_article_by_id_response = frontcore.knowledge_bases.get_article_by_id(
    article_id="kba_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_article_content`<a id="frontcoreknowledge_basesget_article_content"></a>

Fetches a knowledge base article with content for a given locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_article_content_response = frontcore.knowledge_bases.get_article_content(
    article_id="kba_123",
    locale="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article to fetch

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the content to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}/locales/{locale}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_category`<a id="frontcoreknowledge_basesget_category"></a>

Fetches a knowledge base category.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_response = frontcore.knowledge_bases.get_category(
    category_id="kbc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_category_content_default_locale`<a id="frontcoreknowledge_basesget_category_content_default_locale"></a>

Fetches a knowledge base category with content in the default locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_content_default_locale_response = frontcore.knowledge_bases.get_category_content_default_locale(
    category_id="kbc_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_category_content_locale`<a id="frontcoreknowledge_basesget_category_content_locale"></a>

Fetches a knowledge base category with content for a given locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_category_content_locale_response = frontcore.knowledge_bases.get_category_content_locale(
    category_id="kbc_123",
    locale="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category to fetch

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the content to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}/locales/{locale}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_content_default_locale`<a id="frontcoreknowledge_basesget_content_default_locale"></a>

Fetches a knowledge base article with content in the default locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_default_locale_response = frontcore.knowledge_bases.get_content_default_locale(
    article_id="kba_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_content_default_locale_0`<a id="frontcoreknowledge_basesget_content_default_locale_0"></a>

Fetches a knowledge base with its content in the default locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_default_locale_0_response = frontcore.knowledge_bases.get_content_default_locale_0(
    knowledge_base_id="knb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_knowledge_base`<a id="frontcoreknowledge_basesget_knowledge_base"></a>

Fetches a knowledge base.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_knowledge_base_response = frontcore.knowledge_bases.get_knowledge_base(
    knowledge_base_id="knb_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.get_knowledge_base_content_in_locale`<a id="frontcoreknowledge_basesget_knowledge_base_content_in_locale"></a>

Fetches a knowledge base with its content for a given locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_knowledge_base_content_in_locale_response = frontcore.knowledge_bases.get_knowledge_base_content_in_locale(
    knowledge_base_id="knb_123",
    locale="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to fetch

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the content to fetch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/locales/{locale}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.list_articles_in_base`<a id="frontcoreknowledge_baseslist_articles_in_base"></a>

List articles in a knowledge base

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_articles_in_base_response = frontcore.knowledge_bases.list_articles_in_base(
    knowledge_base_id="knb_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`KnowledgeBasesListArticlesInCategoryResponse`](./front_core_python_sdk/pydantic/knowledge_bases_list_articles_in_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/articles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.list_articles_in_category`<a id="frontcoreknowledge_baseslist_articles_in_category"></a>

List articles in a category.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_articles_in_category_response = frontcore.knowledge_bases.list_articles_in_category(
    category_id="kbc_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`KnowledgeBasesListArticlesInCategoryResponse`](./front_core_python_sdk/pydantic/knowledge_bases_list_articles_in_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}/articles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.list_categories_in_base`<a id="frontcoreknowledge_baseslist_categories_in_base"></a>

List categories in a knowledge base.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_in_base_response = frontcore.knowledge_bases.list_categories_in_base(
    knowledge_base_id="knb_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`KnowledgeBasesListCategoriesInBaseResponse`](./front_core_python_sdk/pydantic/knowledge_bases_list_categories_in_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.list_knowledge_bases`<a id="frontcoreknowledge_baseslist_knowledge_bases"></a>

List the knowledge bases of the company.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_knowledge_bases_response = frontcore.knowledge_bases.list_knowledge_bases()
```

#### 🔄 Return<a id="🔄-return"></a>

[`KnowledgeBasesListKnowledgeBasesResponse`](./front_core_python_sdk/pydantic/knowledge_bases_list_knowledge_bases_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.update_article_content_default_locale`<a id="frontcoreknowledge_basesupdate_article_content_default_locale"></a>

Updates an article's content in the default locale

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_article_content_default_locale_response = frontcore.knowledge_bases.update_article_content_default_locale(
    article_id="kba_123",
    author_id="string_example",
    subject="string_example",
    content="string_example",
    status="draft",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article to update

##### author_id: `str`<a id="author_id-str"></a>

Teammate ID of the article author

##### subject: `str`<a id="subject-str"></a>

Subject of the article

##### content: `str`<a id="content-str"></a>

HTML content of the article

##### status: `str`<a id="status-str"></a>

Article status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseArticlePatch`](./front_core_python_sdk/type/knowledge_base_article_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}/content` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.update_article_content_locale`<a id="frontcoreknowledge_basesupdate_article_content_locale"></a>

Updates an article's content for a given locale.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_article_content_locale_response = frontcore.knowledge_bases.update_article_content_locale(
    article_id="kba_123",
    locale="en",
    author_id="string_example",
    subject="string_example",
    content="string_example",
    status="draft",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article_id: `str`<a id="article_id-str"></a>

The ID of the article to update

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the updated content

##### author_id: `str`<a id="author_id-str"></a>

Teammate ID of the article author

##### subject: `str`<a id="subject-str"></a>

Subject of the article

##### content: `str`<a id="content-str"></a>

HTML content of the article

##### status: `str`<a id="status-str"></a>

Article status

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseArticlePatch`](./front_core_python_sdk/type/knowledge_base_article_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_articles/{article_id}/locales/{locale}/content` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.update_category_content_locale`<a id="frontcoreknowledge_basesupdate_category_content_locale"></a>

Updates a knowledge base category for a given locale. Will republish the knowledge base if the knowledge base is currently published.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_category_content_locale_response = frontcore.knowledge_bases.update_category_content_locale(
    category_id="kbc_123",
    locale="en",
    description="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category to update

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the updated content

##### description: `str`<a id="description-str"></a>

Description of the knowledge base category

##### name: `str`<a id="name-str"></a>

Name of the knowledge base category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseCategoryPatch`](./front_core_python_sdk/type/knowledge_base_category_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}/locales/{locale}/content` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.update_category_default_locale`<a id="frontcoreknowledge_basesupdate_category_default_locale"></a>

Updates a knowledge base category in the default locale. Will republish the knowledge base if the knowledge base is currently published.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_category_default_locale_response = frontcore.knowledge_bases.update_category_default_locale(
    category_id="kbc_123",
    description="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `str`<a id="category_id-str"></a>

The ID of the category to update

##### description: `str`<a id="description-str"></a>

Description of the knowledge base category

##### name: `str`<a id="name-str"></a>

Name of the knowledge base category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBaseCategoryPatch`](./front_core_python_sdk/type/knowledge_base_category_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_base_categories/{category_id}/content` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.update_default_knowledge_base`<a id="frontcoreknowledge_basesupdate_default_knowledge_base"></a>

Updates a knowledge base in the default locale. Will republish the knowledge base if the knowledge base is currently published.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_default_knowledge_base_response = frontcore.knowledge_bases.update_default_knowledge_base(
    knowledge_base_id="knb_123",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to update

##### name: `str`<a id="name-str"></a>

Name of the knowledge base

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBasePatch`](./front_core_python_sdk/type/knowledge_base_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/content` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.knowledge_bases.update_knowledge_base_locale`<a id="frontcoreknowledge_basesupdate_knowledge_base_locale"></a>

Updates a knowledge base for a given locale. Will republish the knowledge base if the knowledge base is currently published.

**Note**: You must use an API token to authenticate. OAuth is not supported at this time.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_knowledge_base_locale_response = frontcore.knowledge_bases.update_knowledge_base_locale(
    knowledge_base_id="knb_123",
    locale="en",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_base_id: `str`<a id="knowledge_base_id-str"></a>

The ID of the knowledge base to update

##### locale: `str`<a id="locale-str"></a>

The [locale](https://dev.frontapp.com/reference/knowledge-bases#locales) of the updated content

##### name: `str`<a id="name-str"></a>

Name of the knowledge base

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`KnowledgeBasePatch`](./front_core_python_sdk/type/knowledge_base_patch.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge_bases/{knowledge_base_id}/locales/{locale}/content` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.links.create_link`<a id="frontcorelinkscreate_link"></a>

Create a link. You must supply either `pattern` or `external_url` in the request, but not both (`pattern` is for dynamic objects while `external_url` is for standard links). If `pattern` is provided, the API call updates the dynamic objects matching the exact pattern. If the link is resolved to an installed links integration, any name retrieved from the integration will override the provided name in the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_link_response = frontcore.links.create_link(
    name="string_example",
    external_url="string_example",
    pattern="ORDER-123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the link. If none is specified, the external_url is used as a default

##### external_url: `str`<a id="external_url-str"></a>

Underlying identifying url of the link

##### pattern: `str`<a id="pattern-str"></a>

The string that dynamic object configurations will match on to update a specific dynamic object. For example, if you've configured a dynamic object to match on ORDER-{Digits}, and you want to specifically update the dynamic objects for ORDER-777 to retrieve the latest information from external systems, send \\\"ORDER-777\\\". Repeat for other specific identifiers, such as \\\"ORDER-435\\\".

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateLink`](./front_core_python_sdk/type/create_link.py)
Link to create

#### 🔄 Return<a id="🔄-return"></a>

[`LinkResponse`](./front_core_python_sdk/pydantic/link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.links.get_link`<a id="frontcorelinksget_link"></a>

Fetch a link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_link_response = frontcore.links.get_link(
    link_id="top_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_id: `str`<a id="link_id-str"></a>

The link ID

#### 🔄 Return<a id="🔄-return"></a>

[`LinkResponse`](./front_core_python_sdk/pydantic/link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/{link_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.links.list_by_id_and_type`<a id="frontcorelinkslist_by_id_and_type"></a>

List the links of the company paginated by id. Allows filtering by link type via the q.types param.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_id_and_type_response = frontcore.links.list_by_id_and_type(
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `types`, whose value should be a list of link types (examples - `web`, `jira`, `asana` ).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the links. Only supports `id`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`LinksListByIdAndTypeResponse`](./front_core_python_sdk/pydantic/links_list_by_id_and_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.links.list_conversations`<a id="frontcorelinkslist_conversations"></a>

List the conversations linked to a specific link. For more advanced filtering, see the [search endpoint](https://dev.frontapp.com/reference/conversations#search-conversations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_conversations_response = frontcore.links.list_conversations(
    link_id="top_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_id: `str`<a id="link_id-str"></a>

The Link ID

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `statuses`, whose value should be a list of conversation statuses (`assigned`, `unassigned`, `archived`, or `deleted`).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the conversations. Only supports `date`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`ContactsListConversationsReverseChronologicalOrderResponse`](./front_core_python_sdk/pydantic/contacts_list_conversations_reverse_chronological_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/{link_id}/conversations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.links.update_link`<a id="frontcorelinksupdate_link"></a>

Update a link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.links.update_link(
    body=None,
    link_id="top_123",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_id: `str`<a id="link_id-str"></a>

The link ID

##### name: `str`<a id="name-str"></a>

Name of the link

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateLink`](./front_core_python_sdk/type/update_link.py)
Link fields to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/{link_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.create_child_folder`<a id="frontcoremessage_template_folderscreate_child_folder"></a>

Create a new message template folder as a child of the given folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_child_folder_response = frontcore.message_template_folders.create_child_folder(
    name="PTO templates",
    message_template_folder_id="rsf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template folder

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The parent message template folder ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageTemplateFolderAsChild`](./front_core_python_sdk/type/create_message_template_folder_as_child.py)
Message template folder to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}/message_template_folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.create_new_folder`<a id="frontcoremessage_template_folderscreate_new_folder"></a>

Create a new message template folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_folder_response = frontcore.message_template_folders.create_new_folder(
    name="PTO templates",
    parent_folder_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template folder

##### parent_folder_id: `str`<a id="parent_folder_id-str"></a>

ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageTemplateFolder`](./front_core_python_sdk/type/create_message_template_folder.py)
Message template folder to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.create_new_folder_0`<a id="frontcoremessage_template_folderscreate_new_folder_0"></a>

Create a new message template folder belonging to the requested teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_folder_0_response = frontcore.message_template_folders.create_new_folder_0(
    name="PTO templates",
    teammate_id="tea_123",
    parent_folder_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template folder

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### parent_folder_id: `str`<a id="parent_folder_id-str"></a>

ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageTemplateFolder`](./front_core_python_sdk/type/create_message_template_folder.py)
Message template folder to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/message_template_folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.create_new_folder_1`<a id="frontcoremessage_template_folderscreate_new_folder_1"></a>

Create a new message template folder belonging to the requested team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_folder_1_response = frontcore.message_template_folders.create_new_folder_1(
    name="PTO templates",
    team_id="tim_55c8c149",
    parent_folder_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template folder

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### parent_folder_id: `str`<a id="parent_folder_id-str"></a>

ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageTemplateFolder`](./front_core_python_sdk/type/create_message_template_folder.py)
Message template folder to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/message_template_folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.delete_folder`<a id="frontcoremessage_template_foldersdelete_folder"></a>

Delete a message template folder and child folders/templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_folder_response = frontcore.message_template_folders.delete_folder(
    message_template_folder_id="rsf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The message template folder id

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplateFoldersDeleteFolderResponse`](./front_core_python_sdk/pydantic/message_template_folders_delete_folder_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.get_child_folders`<a id="frontcoremessage_template_foldersget_child_folders"></a>

Fetch the child message templates folders of a message template folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_child_folders_response = frontcore.message_template_folders.get_child_folders(
    message_template_folder_id="rsf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The message template folder ID

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplateFoldersListFoldersResponse`](./front_core_python_sdk/pydantic/message_template_folders_list_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}/message_template_folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.get_folder`<a id="frontcoremessage_template_foldersget_folder"></a>

Fetch a message template folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_folder_response = frontcore.message_template_folders.get_folder(
    message_template_folder_id="rsf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The message template folder ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.list_folders`<a id="frontcoremessage_template_folderslist_folders"></a>

List the message template folders.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_folders_response = frontcore.message_template_folders.list_folders(
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the message template folders. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplateFoldersListFoldersResponse`](./front_core_python_sdk/pydantic/message_template_folders_list_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.list_team_folders`<a id="frontcoremessage_template_folderslist_team_folders"></a>

List the message template folders belonging to the requested team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_folders_response = frontcore.message_template_folders.list_team_folders(
    team_id="tim_55c8c149",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the message template folders. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplateFoldersListFoldersResponse`](./front_core_python_sdk/pydantic/message_template_folders_list_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/message_template_folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.list_teammate_folders`<a id="frontcoremessage_template_folderslist_teammate_folders"></a>

List the message template folders belonging to the requested teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_folders_response = frontcore.message_template_folders.list_teammate_folders(
    teammate_id="tea_123",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the message template folders. Either `created_at` or `updated_at`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplateFoldersListFoldersResponse`](./front_core_python_sdk/pydantic/message_template_folders_list_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/message_template_folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_template_folders.update_folder`<a id="frontcoremessage_template_foldersupdate_folder"></a>

Update message template folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_folder_response = frontcore.message_template_folders.update_folder(
    message_template_folder_id="rsf_123",
    name="string_example",
    parent_folder_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The message template folder ID

##### name: `str`<a id="name-str"></a>

Name of the message template folder

##### parent_folder_id: `str`<a id="parent_folder_id-str"></a>

ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateMessageTemplateFolder`](./front_core_python_sdk/type/update_message_template_folder.py)
Message template folder to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.add_new_teammate_template`<a id="frontcoremessage_templatesadd_new_teammate_template"></a>

Create a new message template for the given teammate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_teammate_template_response = frontcore.message_templates.add_new_teammate_template(
    name="Out of Office",
    body="Sorry, I'm OOO until October 25th.",
    teammate_id="tea_123",
    subject="Out of Office",
    folder_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template

##### body: `str`<a id="body-str"></a>

Body of the message template

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### subject: `str`<a id="subject-str"></a>

Subject of the message template. If not set, the name will be used to populate the subject.

##### folder_id: `str`<a id="folder_id-str"></a>

ID of the message template folder to place this message template in

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreatePrivateMessageTemplate`](./front_core_python_sdk/type/create_private_message_template.py)
Message template to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/message_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.create_child_template`<a id="frontcoremessage_templatescreate_child_template"></a>

Create a new message template as a child of the given folder

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_child_template_response = frontcore.message_templates.create_child_template(
    name="Out of Office",
    body="Sorry, I'm OOO until October 25th.",
    message_template_folder_id="rsf_123",
    subject="Out of Office",
    inbox_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template

##### body: `str`<a id="body-str"></a>

Body of the message template

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The parent message template folder ID

##### subject: `str`<a id="subject-str"></a>

Subject of the message template. If not set, the name will be used to populate the subject.

##### inbox_ids: [`CreateMessageTemplateAsChildInboxIds`](./front_core_python_sdk/type/create_message_template_as_child_inbox_ids.py)<a id="inbox_ids-createmessagetemplateaschildinboxidsfront_core_python_sdktypecreate_message_template_as_child_inbox_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageTemplateAsChild`](./front_core_python_sdk/type/create_message_template_as_child.py)
Message template to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}/message_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.create_new_template`<a id="frontcoremessage_templatescreate_new_template"></a>

Create a new message template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_template_response = frontcore.message_templates.create_new_template(
    name="Out of Office",
    body="Sorry, I'm OOO until October 25th.",
    subject="Out of Office",
    folder_id="string_example",
    inbox_ids=[
        "string_example"
    ],
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template

##### body: `str`<a id="body-str"></a>

Body of the message template

##### subject: `str`<a id="subject-str"></a>

Subject of the message template. If not set, the name will be used to populate the subject.

##### folder_id: `str`<a id="folder_id-str"></a>

ID of the message template folder to place this message template in

##### inbox_ids: [`CreateSharedMessageTemplateInboxIds`](./front_core_python_sdk/type/create_shared_message_template_inbox_ids.py)<a id="inbox_ids-createsharedmessagetemplateinboxidsfront_core_python_sdktypecreate_shared_message_template_inbox_idspy"></a>

##### attachments: [`CreateSharedMessageTemplateAttachments`](./front_core_python_sdk/type/create_shared_message_template_attachments.py)<a id="attachments-createsharedmessagetemplateattachmentsfront_core_python_sdktypecreate_shared_message_template_attachmentspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateSharedMessageTemplate`](./front_core_python_sdk/type/create_shared_message_template.py)
Message template to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.create_team_template`<a id="frontcoremessage_templatescreate_team_template"></a>

Create a new message template for the given team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_template_response = frontcore.message_templates.create_team_template(
    name="Out of Office",
    body="Sorry, I'm OOO until October 25th.",
    team_id="tim_55c8c149",
    subject="Out of Office",
    folder_id="string_example",
    inbox_ids=[
        "string_example"
    ],
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the message template

##### body: `str`<a id="body-str"></a>

Body of the message template

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### subject: `str`<a id="subject-str"></a>

Subject of the message template. If not set, the name will be used to populate the subject.

##### folder_id: `str`<a id="folder_id-str"></a>

ID of the message template folder to place this message template in

##### inbox_ids: [`CreateSharedMessageTemplateInboxIds`](./front_core_python_sdk/type/create_shared_message_template_inbox_ids.py)<a id="inbox_ids-createsharedmessagetemplateinboxidsfront_core_python_sdktypecreate_shared_message_template_inbox_idspy"></a>

##### attachments: [`CreateSharedMessageTemplateAttachments`](./front_core_python_sdk/type/create_shared_message_template_attachments.py)<a id="attachments-createsharedmessagetemplateattachmentsfront_core_python_sdktypecreate_shared_message_template_attachmentspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateSharedMessageTemplate`](./front_core_python_sdk/type/create_shared_message_template.py)
Message template to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/message_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.delete_template`<a id="frontcoremessage_templatesdelete_template"></a>

Delete a message template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.message_templates.delete_template(
    message_template_id="rsp_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_id: `str`<a id="message_template_id-str"></a>

The message template ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_templates/{message_template_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.get_child_templates`<a id="frontcoremessage_templatesget_child_templates"></a>

Fetch the child message templates of a message template folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_child_templates_response = frontcore.message_templates.get_child_templates(
    message_template_folder_id="rsf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_folder_id: `str`<a id="message_template_folder_id-str"></a>

The message template folder ID

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplateFoldersListFoldersResponse`](./front_core_python_sdk/pydantic/message_template_folders_list_folders_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_template_folders/{message_template_folder_id}/message_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.get_template_by_id`<a id="frontcoremessage_templatesget_template_by_id"></a>

Fetch a message template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_template_by_id_response = frontcore.message_templates.get_template_by_id(
    message_template_id="rsp_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_id: `str`<a id="message_template_id-str"></a>

The message template ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_templates/{message_template_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.list`<a id="frontcoremessage_templateslist"></a>

List the message templates.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = frontcore.message_templates.list(
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the message templates. Either `created_at`, `updated_at`, or `sort_order`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplatesListResponse`](./front_core_python_sdk/pydantic/message_templates_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.list_team_templates`<a id="frontcoremessage_templateslist_team_templates"></a>

List the message templates belonging to the requested team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_templates_response = frontcore.message_templates.list_team_templates(
    team_id="tim_55c8c149",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the message templates. Either `created_at`, `updated_at`, or `sort_order`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplatesListResponse`](./front_core_python_sdk/pydantic/message_templates_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/message_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.list_teammate_templates`<a id="frontcoremessage_templateslist_teammate_templates"></a>

List the message templates belonging to the requested teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_templates_response = frontcore.message_templates.list_teammate_templates(
    teammate_id="tea_123",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the message templates. Either `created_at`, `updated_at`, or `sort_order`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`MessageTemplatesListResponse`](./front_core_python_sdk/pydantic/message_templates_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/message_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.message_templates.update_template_by_id`<a id="frontcoremessage_templatesupdate_template_by_id"></a>

Update message template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_template_by_id_response = frontcore.message_templates.update_template_by_id(
    body=None,
    message_template_id="rsp_123",
    name="string_example",
    subject="string_example",
    body="string_example",
    folder_id="string_example",
    inbox_ids=[
        "string_example"
    ],
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_template_id: `str`<a id="message_template_id-str"></a>

The message template ID

##### name: `str`<a id="name-str"></a>

Name of the message template

##### subject: `str`<a id="subject-str"></a>

Subject of the message template

##### body: `str`<a id="body-str"></a>

Body of the message template

##### folder_id: `str`<a id="folder_id-str"></a>

ID of the parent folder to be placed into. Goes into the root folder if unspecified or if null.

##### inbox_ids: List[`str`]<a id="inbox_ids-liststr"></a>

The specific inboxes this template is available in. If null, then it will be available in all inboxes. Array should be non-empty. If unspecified, will retain previous value.

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://dev.frontapp.com/docs/attachments-1). Max 25 MB. Specify an empty array to delete all attachments from a message template. If unspecified, it will retain previous value.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateMessageTemplate`](./front_core_python_sdk/type/update_message_template.py)
Message template to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/message_templates/{message_template_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.create_message_reply`<a id="frontcoremessagescreate_message_reply"></a>

Reply to a conversation by sending a message and appending it to the conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_message_reply_response = frontcore.messages.create_message_reply(
    body=None,
    body="string_example",
    conversation_id="cnv_123",
    to=[
        "string_example"
    ],
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    sender_name="string_example",
    subject="string_example",
    author_id="string_example",
    channel_id="string_example",
    text="string_example",
    quote_body="string_example",
    options={
        "archive": True,
    },
    attachments=[
        open('/path/to/file', 'rb')
    ],
    signature_id="string_example",
    should_add_default_signature=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### body: `str`<a id="body-str"></a>

Body of the message

##### conversation_id: `str`<a id="conversation_id-str"></a>

The conversation ID

##### to: List[`str`]<a id="to-liststr"></a>

List of the recipient handles who will receive this message

##### cc: List[`str`]<a id="cc-liststr"></a>

List of the recipient handles who will receive a copy of this message

##### bcc: List[`str`]<a id="bcc-liststr"></a>

List of the recipient handles who will receive a copy of this message

##### sender_name: `str`<a id="sender_name-str"></a>

Name used for the sender info of the message

##### subject: `str`<a id="subject-str"></a>

Subject of the message for email message

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate on behalf of whom the answer is sent

##### channel_id: `str`<a id="channel_id-str"></a>

Channel ID the message is sent from

##### text: `str`<a id="text-str"></a>

Text version of the body for email messages

##### quote_body: `str`<a id="quote_body-str"></a>

Body for the quote that the message is referencing. Only available on email channels.

##### options: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

##### signature_id: `str`<a id="signature_id-str"></a>

ID of the signature to attach to this draft. If null, no signature is attached.

##### should_add_default_signature: `bool`<a id="should_add_default_signature-bool"></a>

Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OutboundReplyMessage`](./front_core_python_sdk/type/outbound_reply_message.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/conversations/{conversation_id}/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.create_new_message`<a id="frontcoremessagescreate_new_message"></a>

Send a new message from a channel. This is one of the ways to create a new [conversation](https://dev.frontapp.com/reference/conversations#creating-a-new-conversation). The new conversation will support both messages and comments (discussions).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_message_response = frontcore.messages.create_new_message(
    body=None,
    to=[
        "string_example"
    ],
    body="string_example",
    channel_id="cha_123",
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    sender_name="string_example",
    subject="string_example",
    author_id="string_example",
    text="string_example",
    options={
        "archive": True,
    },
    attachments=[
        open('/path/to/file', 'rb')
    ],
    signature_id="string_example",
    should_add_default_signature=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### to: List[`str`]<a id="to-liststr"></a>

List of the recipient handles who will receive this message

##### body: `str`<a id="body-str"></a>

Body of the message

##### channel_id: `str`<a id="channel_id-str"></a>

The sending channel ID. Alternatively, you can supply the sending channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### cc: List[`str`]<a id="cc-liststr"></a>

List of the recipient handles who will receive a copy of this message

##### bcc: List[`str`]<a id="bcc-liststr"></a>

List of the recipient handles who will receive a blind copy of this message

##### sender_name: `str`<a id="sender_name-str"></a>

Name used for the sender info of the message

##### subject: `str`<a id="subject-str"></a>

Subject of the message for email message

##### author_id: `str`<a id="author_id-str"></a>

ID of the teammate on behalf of whom the answer is sent

##### text: `str`<a id="text-str"></a>

Text version of the body for email messages

##### options: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="options-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1). Max 25 MB.

##### signature_id: `str`<a id="signature_id-str"></a>

ID of the signature to attach to this draft. If null, no signature is attached.

##### should_add_default_signature: `bool`<a id="should_add_default_signature-bool"></a>

Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OutboundMessage`](./front_core_python_sdk/type/outbound_message.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.get_message_by_id`<a id="frontcoremessagesget_message_by_id"></a>

Fetch a message.

> ℹ️ The HTTP Header `Accept` can be used to request the message in a different format.
> By default, Front will return the documented JSON response. By requesting `message/rfc822`, the response will contain the message in the EML format (for email messages only).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_by_id_response = frontcore.messages.get_message_by_id(
    message_id="msg_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

The message ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messages/{message_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.get_message_seen_status`<a id="frontcoremessagesget_message_seen_status"></a>

Get the seen receipts for the given message. If no seen-by information is available, there will be a single entry for the first time the message was seen by any recipient. If seen-by information is available, there will be an entry for each recipient who has seen the message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_seen_status_response = frontcore.messages.get_message_seen_status(
    message_id="msg_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

The message ID

#### 🔄 Return<a id="🔄-return"></a>

[`MessagesGetMessageSeenStatusResponse`](./front_core_python_sdk/pydantic/messages_get_message_seen_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messages/{message_id}/seen` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.import_new_inbox_message`<a id="frontcoremessagesimport_new_inbox_message"></a>

Import a new message in an inbox.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_new_inbox_message_response = frontcore.messages.import_new_inbox_message(
    body=None,
    sender={
        "handle": "handle_example",
    },
    to=[
        "string_example"
    ],
    body="string_example",
    external_id="string_example",
    created_at=1,
    metadata={
        "is_inbound": True,
        "should_skip_rules": True,
    },
    inbox_id="inb_123",
    tags=[
        "string_example"
    ],
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    subject="string_example",
    body_format="markdown",
    type="email",
    assignee_id="string_example",
    conversation_id="string_example",
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sender: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sender-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Data of the sender

##### to: List[`str`]<a id="to-liststr"></a>

List of the recipient handles who will receive this message

##### body: `str`<a id="body-str"></a>

Body of the message

##### external_id: `str`<a id="external_id-str"></a>

External identifier of the message. Front won't import two messages with the same external ID.

##### created_at: `int`<a id="created_at-int"></a>

Date at which the message as been sent or received.

##### metadata: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### inbox_id: `str`<a id="inbox_id-str"></a>

The Inbox ID

##### tags: List[`str`]<a id="tags-liststr"></a>

List of tag names to add to the conversation

##### cc: List[`str`]<a id="cc-liststr"></a>

List of the recipient handles who will receive a copy of this message

##### bcc: List[`str`]<a id="bcc-liststr"></a>

List of the recipient handles who will receive a blind copy of this message

##### subject: `str`<a id="subject-str"></a>

Subject of the message

##### body_format: `str`<a id="body_format-str"></a>

Format of the message body. Can be `markdown` (default) or `html`, and can only be specified for `email` type.

##### type: `str`<a id="type-str"></a>

Type of the message to import. Default is `email`.

##### assignee_id: `str`<a id="assignee_id-str"></a>

ID of the teammate who will be assigned to the conversation.

##### conversation_id: `str`<a id="conversation_id-str"></a>

If supplied, Front will thread this message into conversation with the given ID. Note that including this parameter nullifies the `thread_ref` parameter _completely_.

##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportMessage`](./front_core_python_sdk/type/import_message.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MessagesReceiveCustomMessageResponse`](./front_core_python_sdk/pydantic/messages_receive_custom_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/inboxes/{inbox_id}/imported_messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.mark_message_seen`<a id="frontcoremessagesmark_message_seen"></a>

Mark an outbound message from Front as seen. Note, the message seen route should only be called in response to an actual end-user's message-seen action. In accordance with this behavior, the route is rate limited to 10 requests per hour. The request body should send an empty object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.messages.mark_message_seen(
    message_id="msg_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

The message ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messages/{message_id}/seen` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.messages.receive_custom_message`<a id="frontcoremessagesreceive_custom_message"></a>

Receive a custom message in Front. This endpoint is available for custom channels **ONLY**.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
receive_custom_message_response = frontcore.messages.receive_custom_message(
    body=None,
    sender={
        "handle": "handle_example",
    },
    body="string_example",
    channel_id="cha_123",
    subject="string_example",
    body_format="markdown",
    metadata={
    },
    attachments=[
        open('/path/to/file', 'rb')
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sender: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="sender-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Data of the sender

##### body: `str`<a id="body-str"></a>

Body of the message

##### channel_id: `str`<a id="channel_id-str"></a>

The channel ID. Alternatively, you can supply the channel address as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### subject: `str`<a id="subject-str"></a>

Subject of the message

##### body_format: `str`<a id="body_format-str"></a>

Format of the message body. Can be `markdown` (default) or `html`.

##### metadata: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./front_core_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonefront_core_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### attachments: List[`IO`]<a id="attachments-listio"></a>

Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1).  Max 25 MB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomMessage`](./front_core_python_sdk/type/custom_message.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MessagesReceiveCustomMessageResponse`](./front_core_python_sdk/pydantic/messages_receive_custom_message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/incoming_messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.rules.get_rule`<a id="frontcorerulesget_rule"></a>

Fetch a rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rule_response = frontcore.rules.get_rule(
    rule_id="rul_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

The Rule ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rules/{rule_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.rules.list_all_company_rules`<a id="frontcoreruleslist_all_company_rules"></a>

List the company rules.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_company_rules_response = frontcore.rules.list_all_company_rules()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RulesListAllCompanyRulesResponse`](./front_core_python_sdk/pydantic/rules_list_all_company_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.rules.list_company_rules`<a id="frontcoreruleslist_company_rules"></a>

List the rules of the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_rules_response = frontcore.rules.list_company_rules()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RulesListAllCompanyRulesResponse`](./front_core_python_sdk/pydantic/rules_list_all_company_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.rules.list_team_rules`<a id="frontcoreruleslist_team_rules"></a>

List the rules of a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_rules_response = frontcore.rules.list_team_rules(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### 🔄 Return<a id="🔄-return"></a>

[`RulesListAllCompanyRulesResponse`](./front_core_python_sdk/pydantic/rules_list_all_company_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.rules.list_teammate_rules`<a id="frontcoreruleslist_teammate_rules"></a>

List the rules of a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_rules_response = frontcore.rules.list_teammate_rules(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`RulesListAllCompanyRulesResponse`](./front_core_python_sdk/pydantic/rules_list_all_company_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.add_teammates_to_shift`<a id="frontcoreshiftsadd_teammates_to_shift"></a>

Add teammates to a shift. The selected teammates must be in the team that owns the shift.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.shifts.add_teammates_to_shift(
    teammate_ids=[
        "string_example"
    ],
    shift_id="shf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

##### shift_id: `str`<a id="shift_id-str"></a>

The Shift ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeammateIds`](./front_core_python_sdk/type/teammate_ids.py)
Teammate IDs to add. Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shift/{shift_id}/teammates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.create_shift`<a id="frontcoreshiftscreate_shift"></a>

Create a shift.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_shift_response = frontcore.shifts.create_shift(
    body=None,
    name="string_example",
    color="black",
    timezone="string_example",
    times={
    },
    teammate_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the shift

##### color: `str`<a id="color-str"></a>

Color of the shift

##### timezone: `str`<a id="timezone-str"></a>

A timezone name as defined in the IANA tz database

##### times: [`ShiftIntervals`](./front_core_python_sdk/type/shift_intervals.py)<a id="times-shiftintervalsfront_core_python_sdktypeshift_intervalspy"></a>


##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

List of all the teammate ids who will be part of this shift. Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateShift`](./front_core_python_sdk/type/create_shift.py)
Shift to create details

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftResponse`](./front_core_python_sdk/pydantic/shift_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shifts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.create_team_shift`<a id="frontcoreshiftscreate_team_shift"></a>

Create a shift for a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_shift_response = frontcore.shifts.create_team_shift(
    body=None,
    name="string_example",
    color="black",
    timezone="string_example",
    times={
    },
    teammate_ids=[
        "string_example"
    ],
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the shift

##### color: `str`<a id="color-str"></a>

Color of the shift

##### timezone: `str`<a id="timezone-str"></a>

A timezone name as defined in the IANA tz database

##### times: [`ShiftIntervals`](./front_core_python_sdk/type/shift_intervals.py)<a id="times-shiftintervalsfront_core_python_sdktypeshift_intervalspy"></a>


##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

List of all the teammate ids who will be part of this shift. Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### team_id: `str`<a id="team_id-str"></a>

The Team ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateShift`](./front_core_python_sdk/type/create_shift.py)
Shift to create details

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftResponse`](./front_core_python_sdk/pydantic/shift_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/shifts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.get_shift`<a id="frontcoreshiftsget_shift"></a>

Fetch a shift.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_shift_response = frontcore.shifts.get_shift(
    shift_id="shf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shift_id: `str`<a id="shift_id-str"></a>

The Shift ID

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftResponse`](./front_core_python_sdk/pydantic/shift_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shift/{shift_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.list_shift_teammates`<a id="frontcoreshiftslist_shift_teammates"></a>

List the teammates assigned to a shift.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_shift_teammates_response = frontcore.shifts.list_shift_teammates(
    shift_id="shf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shift_id: `str`<a id="shift_id-str"></a>

The Shift ID

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsListMentionedTeammatesResponse`](./front_core_python_sdk/pydantic/comments_list_mentioned_teammates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shift/{shift_id}/teammates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.list_shifts`<a id="frontcoreshiftslist_shifts"></a>

List the shifts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_shifts_response = frontcore.shifts.list_shifts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsListShiftsResponse`](./front_core_python_sdk/pydantic/shifts_list_shifts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.list_team_shifts`<a id="frontcoreshiftslist_team_shifts"></a>

List the shifts for a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_shifts_response = frontcore.shifts.list_team_shifts(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsListShiftsResponse`](./front_core_python_sdk/pydantic/shifts_list_shifts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/shifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.remove_teammates_from_shift`<a id="frontcoreshiftsremove_teammates_from_shift"></a>

Remove teammates from a shift.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.shifts.remove_teammates_from_shift(
    teammate_ids=[
        "string_example"
    ],
    shift_id="shf_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

##### shift_id: `str`<a id="shift_id-str"></a>

The Shift ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeammateIds`](./front_core_python_sdk/type/teammate_ids.py)
Teammate IDs to remove. Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shift/{shift_id}/teammates` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.teammate_shifts_list`<a id="frontcoreshiftsteammate_shifts_list"></a>

Lists all the shifts for the teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
teammate_shifts_list_response = frontcore.shifts.teammate_shifts_list(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsListShiftsResponse`](./front_core_python_sdk/pydantic/shifts_list_shifts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/shifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.shifts.update_shift`<a id="frontcoreshiftsupdate_shift"></a>

Update a shift.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.shifts.update_shift(
    shift_id="shf_123",
    name="string_example",
    color="black",
    timezone="string_example",
    times={
    },
    teammate_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shift_id: `str`<a id="shift_id-str"></a>

The Shift ID

##### name: `str`<a id="name-str"></a>

Name of the shift

##### color: `str`<a id="color-str"></a>

Color of the shift

##### timezone: `str`<a id="timezone-str"></a>

A timezone name as defined in the IANA tz database

##### times: [`ShiftIntervals`](./front_core_python_sdk/type/shift_intervals.py)<a id="times-shiftintervalsfront_core_python_sdktypeshift_intervalspy"></a>


##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

List of all the teammate ids who will be part of this shift. Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateShift`](./front_core_python_sdk/type/update_shift.py)
Updated Shift Body

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shifts/{shift_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.create_team_signature`<a id="frontcoresignaturescreate_team_signature"></a>

Create a new signature for the given team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_signature_response = frontcore.signatures.create_team_signature(
    name="string_example",
    body="string_example",
    team_id="tim_123",
    sender_info="string_example",
    is_visible_for_all_teammate_channels=True,
    is_default=False,
    channel_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the signature

##### body: `str`<a id="body-str"></a>

Body of the signature

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### sender_info: `str`<a id="sender_info-str"></a>

Sender info of the signature that will appear in the From line of emails sent.

##### is_visible_for_all_teammate_channels: `bool`<a id="is_visible_for_all_teammate_channels-bool"></a>

Whether or not the signature is visible in all individual channels for teammates in the given team.

##### is_default: `bool`<a id="is_default-bool"></a>

If true, the signature will be set as the default signature for the team.

##### channel_ids: [`CreateSharedSignatureChannelIds`](./front_core_python_sdk/type/create_shared_signature_channel_ids.py)<a id="channel_ids-createsharedsignaturechannelidsfront_core_python_sdktypecreate_shared_signature_channel_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateSharedSignature`](./front_core_python_sdk/type/create_shared_signature.py)
Signature to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/signatures` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.create_teammate_signature`<a id="frontcoresignaturescreate_teammate_signature"></a>

Create a new signature for the given teammate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_teammate_signature_response = frontcore.signatures.create_teammate_signature(
    name="string_example",
    body="string_example",
    teammate_id="tea_123",
    sender_info="string_example",
    is_default=False,
    channel_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the signature

##### body: `str`<a id="body-str"></a>

Body of the signature

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### sender_info: `str`<a id="sender_info-str"></a>

Sender info of the signature that will appear in the From line of emails sent.

##### is_default: `bool`<a id="is_default-bool"></a>

If true, the signature will be set as the default signature for the teammate.

##### channel_ids: [`CreatePrivateSignatureChannelIds`](./front_core_python_sdk/type/create_private_signature_channel_ids.py)<a id="channel_ids-createprivatesignaturechannelidsfront_core_python_sdktypecreate_private_signature_channel_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreatePrivateSignature`](./front_core_python_sdk/type/create_private_signature.py)
Signature to create

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/signatures` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.delete_signature`<a id="frontcoresignaturesdelete_signature"></a>

Delete signature

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.signatures.delete_signature(
    signature_id="sig_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signature_id: `str`<a id="signature_id-str"></a>

The signature ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/signatures/{signature_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.get_signature`<a id="frontcoresignaturesget_signature"></a>

Get the given signature.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_signature_response = frontcore.signatures.get_signature(
    signature_id="sig_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signature_id: `str`<a id="signature_id-str"></a>

The signature ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/signatures/{signature_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.list_team`<a id="frontcoresignatureslist_team"></a>

List the signatures belonging to the given team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_response = frontcore.signatures.list_team(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

#### 🔄 Return<a id="🔄-return"></a>

[`SignaturesListTeammateResponse`](./front_core_python_sdk/pydantic/signatures_list_teammate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/signatures` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.list_teammate`<a id="frontcoresignatureslist_teammate"></a>

List the signatures belonging to the given teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_response = frontcore.signatures.list_teammate(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`SignaturesListTeammateResponse`](./front_core_python_sdk/pydantic/signatures_list_teammate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/signatures` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.signatures.update_signature`<a id="frontcoresignaturesupdate_signature"></a>

Update signature

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_signature_response = frontcore.signatures.update_signature(
    signature_id="sig_123",
    name="string_example",
    sender_info="string_example",
    body="string_example",
    is_visible_for_all_teammate_channels=True,
    is_default=False,
    channel_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signature_id: `str`<a id="signature_id-str"></a>

The signature ID

##### name: `str`<a id="name-str"></a>

Name of the signature

##### sender_info: `str`<a id="sender_info-str"></a>

Sender info of the signature that will appear in the From line of emails sent.

##### body: `str`<a id="body-str"></a>

Body of the signature

##### is_visible_for_all_teammate_channels: `bool`<a id="is_visible_for_all_teammate_channels-bool"></a>

Whether or not the signature is visible in all individual channels for teammates in the given team. Can only be set for shared signatures.

##### is_default: `bool`<a id="is_default-bool"></a>

If true, the signature will be set as the default signature for the team or teammate.

##### channel_ids: [`UpdateSignatureChannelIds`](./front_core_python_sdk/type/update_signature_channel_ids.py)<a id="channel_ids-updatesignaturechannelidsfront_core_python_sdktypeupdate_signature_channel_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateSignature`](./front_core_python_sdk/type/update_signature.py)
Signature to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/signatures/{signature_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.create_child_tag`<a id="frontcoretagscreate_child_tag"></a>

Creates a child tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_child_tag_response = frontcore.tags.create_child_tag(
    name="string_example",
    tag_id="tag_123",
    description="string_example",
    highlight="grey",
    is_visible_in_conversation_lists=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the tag

##### tag_id: `str`<a id="tag_id-str"></a>

The tag ID

##### description: `str`<a id="description-str"></a>

Description of the tag

##### highlight: `str`<a id="highlight-str"></a>

Highlight color of the tag.

##### is_visible_in_conversation_lists: `bool`<a id="is_visible_in_conversation_lists-bool"></a>

Whether the tag is visible in conversation lists.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTag`](./front_core_python_sdk/type/create_tag.py)
Child Tag to create

#### 🔄 Return<a id="🔄-return"></a>

[`TagResponse`](./front_core_python_sdk/pydantic/tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_id}/children` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.create_company_tag`<a id="frontcoretagscreate_company_tag"></a>

Create a company tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_company_tag_response = frontcore.tags.create_company_tag(
    name="string_example",
    description="string_example",
    highlight="grey",
    is_visible_in_conversation_lists=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the tag

##### description: `str`<a id="description-str"></a>

Description of the tag

##### highlight: `str`<a id="highlight-str"></a>

Highlight color of the tag.

##### is_visible_in_conversation_lists: `bool`<a id="is_visible_in_conversation_lists-bool"></a>

Whether the tag is visible in conversation lists.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTag`](./front_core_python_sdk/type/create_tag.py)
Tag to create

#### 🔄 Return<a id="🔄-return"></a>

[`TagResponse`](./front_core_python_sdk/pydantic/tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.create_tag_oldest_team`<a id="frontcoretagscreate_tag_oldest_team"></a>

Create a tag in the oldest team (workspace). This is a legacy endpoint. Use the Create company tag, Create team tag, or Create teammate tag endpoints instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_tag_oldest_team_response = frontcore.tags.create_tag_oldest_team(
    name="string_example",
    description="string_example",
    highlight="grey",
    is_visible_in_conversation_lists=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the tag

##### description: `str`<a id="description-str"></a>

Description of the tag

##### highlight: `str`<a id="highlight-str"></a>

Highlight color of the tag.

##### is_visible_in_conversation_lists: `bool`<a id="is_visible_in_conversation_lists-bool"></a>

Whether the tag is visible in conversation lists.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTag`](./front_core_python_sdk/type/create_tag.py)
Tag to create

#### 🔄 Return<a id="🔄-return"></a>

[`TagResponse`](./front_core_python_sdk/pydantic/tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.create_team_tag`<a id="frontcoretagscreate_team_tag"></a>

Create a tag for a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_tag_response = frontcore.tags.create_team_tag(
    name="string_example",
    team_id="tim_123",
    description="string_example",
    highlight="grey",
    is_visible_in_conversation_lists=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the tag

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### description: `str`<a id="description-str"></a>

Description of the tag

##### highlight: `str`<a id="highlight-str"></a>

Highlight color of the tag.

##### is_visible_in_conversation_lists: `bool`<a id="is_visible_in_conversation_lists-bool"></a>

Whether the tag is visible in conversation lists.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTag`](./front_core_python_sdk/type/create_tag.py)
Tag to create

#### 🔄 Return<a id="🔄-return"></a>

[`TagResponse`](./front_core_python_sdk/pydantic/tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.create_teammate_tag`<a id="frontcoretagscreate_teammate_tag"></a>

Create a tag for a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_teammate_tag_response = frontcore.tags.create_teammate_tag(
    name="string_example",
    teammate_id="tea_123",
    description="string_example",
    highlight="grey",
    is_visible_in_conversation_lists=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the tag

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### description: `str`<a id="description-str"></a>

Description of the tag

##### highlight: `str`<a id="highlight-str"></a>

Highlight color of the tag.

##### is_visible_in_conversation_lists: `bool`<a id="is_visible_in_conversation_lists-bool"></a>

Whether the tag is visible in conversation lists.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateTag`](./front_core_python_sdk/type/create_tag.py)
Tag to create

#### 🔄 Return<a id="🔄-return"></a>

[`TagResponse`](./front_core_python_sdk/pydantic/tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.delete_tag`<a id="frontcoretagsdelete_tag"></a>

Delete a tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.tags.delete_tag(
    tag_id="tag_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_id: `str`<a id="tag_id-str"></a>

The ID of the tag to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.get_tag`<a id="frontcoretagsget_tag"></a>

Fetch a tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tag_response = frontcore.tags.get_tag(
    tag_id="tag_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_id: `str`<a id="tag_id-str"></a>

The tag ID

#### 🔄 Return<a id="🔄-return"></a>

[`TagResponse`](./front_core_python_sdk/pydantic/tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.list_all`<a id="frontcoretagslist_all"></a>

List all the tags of the company that the API token has access to, whether they be company tags, team tags, or teammate tags.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = frontcore.tags.list_all(
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the tags. Only supports `id`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListCompanyResponse`](./front_core_python_sdk/pydantic/tags_list_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.list_children`<a id="frontcoretagslist_children"></a>

List the children of a specific tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_children_response = frontcore.tags.list_children(
    tag_id="tag_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_id: `str`<a id="tag_id-str"></a>

The tag ID

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListCompanyResponse`](./front_core_python_sdk/pydantic/tags_list_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_id}/children` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.list_company`<a id="frontcoretagslist_company"></a>

List the company tags.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_response = frontcore.tags.list_company(
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the tags. Only supports `id`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListCompanyResponse`](./front_core_python_sdk/pydantic/tags_list_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/company/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.list_tagged_conversations`<a id="frontcoretagslist_tagged_conversations"></a>

List the conversations tagged with a tag. For more advanced filtering, see the [search endpoint](https://dev.frontapp.com/reference/conversations#search-conversations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tagged_conversations_response = frontcore.tags.list_tagged_conversations(
    tag_id="tag_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_id: `str`<a id="tag_id-str"></a>

The ID of the tag

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `statuses`, whose value should be a list of conversation statuses (`assigned`, `unassigned`, `archived`, or `deleted`).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`ContactsListConversationsReverseChronologicalOrderResponse`](./front_core_python_sdk/pydantic/contacts_list_conversations_reverse_chronological_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_id}/conversations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.list_team_tags`<a id="frontcoretagslist_team_tags"></a>

List the tags for a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_tags_response = frontcore.tags.list_team_tags(
    team_id="tim_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The team ID

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the tags. Only supports `id`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListCompanyResponse`](./front_core_python_sdk/pydantic/tags_list_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.list_teammate_tags`<a id="frontcoretagslist_teammate_tags"></a>

List the tags for a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teammate_tags_response = frontcore.tags.list_teammate_tags(
    teammate_id="tea_123",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
    sort_by="string_example",
    sort_order="asc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

##### sort_by: `str`<a id="sort_by-str"></a>

Field used to sort the tags. Only supports `id`.

##### sort_order: `str`<a id="sort_order-str"></a>

Order by which results should be sorted

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListCompanyResponse`](./front_core_python_sdk/pydantic/tags_list_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.tags.update_tag`<a id="frontcoretagsupdate_tag"></a>

Update a tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.tags.update_tag(
    body=None,
    tag_id="tag_123",
    description="string_example",
    name="string_example",
    highlight="grey",
    parent_tag_id="string_example",
    is_visible_in_conversation_lists=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_id: `str`<a id="tag_id-str"></a>

The tag ID

##### description: `str`<a id="description-str"></a>

Description of the tag

##### name: `str`<a id="name-str"></a>

Name of the tag

##### highlight: `str`<a id="highlight-str"></a>

Highlight color of the tag.

##### parent_tag_id: `str`<a id="parent_tag_id-str"></a>

ID of the parent of this tag. Set to `null` to remove  the parent tag.

##### is_visible_in_conversation_lists: `bool`<a id="is_visible_in_conversation_lists-bool"></a>

Whether the tag is visible in conversation lists.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTag`](./front_core_python_sdk/type/update_tag.py)
Child Tag to update

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teammates.get_inbox_list`<a id="frontcoreteammatesget_inbox_list"></a>

Returns list of inboxes the teammate has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_inbox_list_response = frontcore.teammates.get_inbox_list(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`ConversationsListInboxesResponse`](./front_core_python_sdk/pydantic/conversations_list_inboxes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/inboxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teammates.get_teammate_by_id`<a id="frontcoreteammatesget_teammate_by_id"></a>

Fetch a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_teammate_by_id_response = frontcore.teammates.get_teammate_by_id(
    teammate_id="tea_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🔄 Return<a id="🔄-return"></a>

[`TeammateResponse`](./front_core_python_sdk/pydantic/teammate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teammates.list_assigned_conversations`<a id="frontcoreteammateslist_assigned_conversations"></a>

List the conversations assigned to a teammate in reverse chronological order (most recently updated first). For more advanced filtering, see the [search endpoint](https://dev.frontapp.com/reference/conversations#search-conversations).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assigned_conversations_response = frontcore.teammates.list_assigned_conversations(
    teammate_id="tea_123",
    q="string_example",
    limit=25,
    page_token="https://yourCompany.api.frontapp.com/endpoint?limit=25&page_token=92f32bcd7625333caf4e0f8fc26d920c812f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### q: `str`<a id="q-str"></a>

[Search query object](https://dev.frontapp.com/docs/query-object-q) with a property `statuses`, whose value should be a list of conversation statuses (`assigned`, `unassigned`, `archived`, or `deleted`).

##### limit: `int`<a id="limit-int"></a>

Max number of results per [page](https://dev.frontapp.com/docs/pagination)

##### page_token: `str`<a id="page_token-str"></a>

Token to use to request the [next page](https://dev.frontapp.com/docs/pagination)

#### 🔄 Return<a id="🔄-return"></a>

[`ContactsListConversationsReverseChronologicalOrderResponse`](./front_core_python_sdk/pydantic/contacts_list_conversations_reverse_chronological_order_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}/conversations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teammates.list_company_members`<a id="frontcoreteammateslist_company_members"></a>

List the teammates in the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_company_members_response = frontcore.teammates.list_company_members()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsListMentionedTeammatesResponse`](./front_core_python_sdk/pydantic/comments_list_mentioned_teammates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teammates.update_teammate`<a id="frontcoreteammatesupdate_teammate"></a>

Update a teammate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.teammates.update_teammate(
    body=None,
    teammate_id="tea_123",
    username="string_example",
    first_name="string_example",
    last_name="string_example",
    is_available=True,
    custom_fields={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_id: `str`<a id="teammate_id-str"></a>

The teammate ID. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

##### username: `str`<a id="username-str"></a>

New username. It must be unique and can only contains lowercase letters, numbers and underscores.

##### first_name: `str`<a id="first_name-str"></a>

New first name

##### last_name: `str`<a id="last_name-str"></a>

New last name

##### is_available: `bool`<a id="is_available-bool"></a>

New availability status

##### custom_fields: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="custom_fields-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom field attributes for this teammate. If you want to keep all custom fields the same when updating this resource, do not include any custom fields in the update. If you want to update custom fields, make sure to include all custom fields, not just the fields you want to add or update. If you send only the custom fields you want to update, the other custom fields will be erased. You can retrieve the existing custom fields before making the update to note the current fields.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTeammate`](./front_core_python_sdk/type/update_teammate.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teammates/{teammate_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teams.add_teammates`<a id="frontcoreteamsadd_teammates"></a>

Add one or more teammates to a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.teams.add_teammates(
    teammate_ids=[
        "string_example"
    ],
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

##### team_id: `str`<a id="team_id-str"></a>

The Team ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeammateIds`](./front_core_python_sdk/type/teammate_ids.py)
Teammate IDs to add. Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/teammates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teams.get_workspace`<a id="frontcoreteamsget_workspace"></a>

Fetch a team (workspace).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workspace_response = frontcore.teams.get_workspace(
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

The Team ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teams.list_teams`<a id="frontcoreteamslist_teams"></a>

List the teams (workspaces) in the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_teams_response = frontcore.teams.list_teams()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsListTeamsResponse`](./front_core_python_sdk/pydantic/teams_list_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.teams.remove_teammates`<a id="frontcoreteamsremove_teammates"></a>

Remove one or more teammates from a team (workspace). Alternatively, you can supply emails as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
frontcore.teams.remove_teammates(
    teammate_ids=[
        "string_example"
    ],
    team_id="tim_123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### teammate_ids: List[`str`]<a id="teammate_ids-liststr"></a>

##### team_id: `str`<a id="team_id-str"></a>

The Team ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeammateIds`](./front_core_python_sdk/type/teammate_ids.py)
Teammate IDs to remove from the team

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_id}/teammates` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `frontcore.token_identity.get_details`<a id="frontcoretoken_identityget_details"></a>

Fetch the details of the API token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = frontcore.token_identity.get_details()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
