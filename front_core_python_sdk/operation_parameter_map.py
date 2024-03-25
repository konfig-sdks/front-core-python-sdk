operation_parameter_map = {
    '/accounts/{account_id}/contacts-POST': {
        'parameters': [
            {
                'name': 'contact_ids'
            },
            {
                'name': 'account_id'
            },
        ]
    },
    '/accounts-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'domains'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/accounts/{account_id}-DELETE': {
        'parameters': [
            {
                'name': 'account_id'
            },
        ]
    },
    '/accounts/{account_id}-GET': {
        'parameters': [
            {
                'name': 'account_id'
            },
        ]
    },
    '/accounts/{account_id}/contacts-GET': {
        'parameters': [
            {
                'name': 'account_id'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/accounts-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/accounts/{account_id}/contacts-DELETE': {
        'parameters': [
            {
                'name': 'contact_ids'
            },
            {
                'name': 'account_id'
            },
        ]
    },
    '/accounts/{account_id}-PATCH': {
        'parameters': [
            {
                'name': 'account_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'domains'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/analytics/exports-POST': {
        'parameters': [
            {
                'name': 'columns'
            },
        ]
    },
    '/analytics/reports-POST': {
        'parameters': [
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'metrics'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'filters'
            },
        ]
    },
    '/analytics/exports/{export_id}-GET': {
        'parameters': [
            {
                'name': 'export_id'
            },
        ]
    },
    '/analytics/reports/{report_uid}-GET': {
        'parameters': [
            {
                'name': 'report_uid'
            },
        ]
    },
    '/download/{attachment_link_id}-GET': {
        'parameters': [
            {
                'name': 'attachment_link_id'
            },
        ]
    },
    '/inboxes/{inbox_id}/channels-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'inbox_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'send_as'
            },
        ]
    },
    '/channels/{channel_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/channels-GET': {
        'parameters': [
        ]
    },
    '/teams/{team_id}/channels-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/teammates/{teammate_id}/channels-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/channels/{channel_id}-PATCH': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'inbox_id'
            },
            {
                'name': 'settings'
            },
        ]
    },
    '/channels/{channel_id}/validate-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
        ]
    },
    '/conversations/{conversation_id}/comments-POST': {
        'parameters': [
            {
                'name': 'body'
            },
            {
                'name': 'conversation_id'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/comments/{comment_id}-GET': {
        'parameters': [
            {
                'name': 'comment_id'
            },
        ]
    },
    '/conversations/{conversation_id}/comments-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/comments/{comment_id}/mentions-GET': {
        'parameters': [
            {
                'name': 'comment_id'
            },
        ]
    },
    '/contact_groups/{contact_group_id}/contacts-POST': {
        'parameters': [
            {
                'name': 'contact_ids'
            },
            {
                'name': 'contact_group_id'
            },
        ]
    },
    '/contact_groups-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/teams/{team_id}/contact_groups-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/teammates/{teammate_id}/contact_groups-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/contact_groups/{contact_group_id}-DELETE': {
        'parameters': [
            {
                'name': 'contact_group_id'
            },
        ]
    },
    '/contact_groups/{contact_group_id}/contacts-GET': {
        'parameters': [
            {
                'name': 'contact_group_id'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/contact_groups-GET': {
        'parameters': [
        ]
    },
    '/teams/{team_id}/contact_groups-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/teammates/{teammate_id}/contact_groups-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/contact_groups/{contact_group_id}/contacts-DELETE': {
        'parameters': [
            {
                'name': 'contact_ids'
            },
            {
                'name': 'contact_group_id'
            },
        ]
    },
    '/contacts/{contact_id}/handles-POST': {
        'parameters': [
            {
                'name': 'handle'
            },
            {
                'name': 'source'
            },
            {
                'name': 'contact_id'
            },
        ]
    },
    '/contacts/{contact_id}/handles-DELETE': {
        'parameters': [
            {
                'name': 'contact_id'
            },
            {
                'name': 'handle'
            },
            {
                'name': 'source'
            },
            {
                'name': 'force'
            },
        ]
    },
    '/contacts/{contact_id}/notes-POST': {
        'parameters': [
            {
                'name': 'author_id'
            },
            {
                'name': 'body'
            },
            {
                'name': 'contact_id'
            },
        ]
    },
    '/contacts/{contact_id}/notes-GET': {
        'parameters': [
            {
                'name': 'contact_id'
            },
        ]
    },
    '/contacts-POST': {
        'parameters': [
            {
                'name': 'handles'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'avatar'
            },
            {
                'name': 'is_spammer'
            },
            {
                'name': 'links'
            },
            {
                'name': 'group_names'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/teams/{team_id}/contacts-POST': {
        'parameters': [
            {
                'name': 'handles'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'avatar'
            },
            {
                'name': 'is_spammer'
            },
            {
                'name': 'links'
            },
            {
                'name': 'group_names'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/teammates/{teammate_id}/contacts-POST': {
        'parameters': [
            {
                'name': 'handles'
            },
            {
                'name': 'teammate_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'avatar'
            },
            {
                'name': 'is_spammer'
            },
            {
                'name': 'links'
            },
            {
                'name': 'group_names'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/contacts/{contact_id}-DELETE': {
        'parameters': [
            {
                'name': 'contact_id'
            },
        ]
    },
    '/contacts/{contact_id}-GET': {
        'parameters': [
            {
                'name': 'contact_id'
            },
        ]
    },
    '/contacts-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/contacts/{contact_id}/conversations-GET': {
        'parameters': [
            {
                'name': 'contact_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/teams/{team_id}/contacts-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/teammates/{teammate_id}/contacts-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/contacts/merge-POST': {
        'parameters': [
            {
                'name': 'contact_ids'
            },
            {
                'name': 'target_contact_id'
            },
        ]
    },
    '/contacts/{contact_id}-PATCH': {
        'parameters': [
            {
                'name': 'contact_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'avatar'
            },
            {
                'name': 'is_spammer'
            },
            {
                'name': 'links'
            },
            {
                'name': 'group_names'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/conversations/{conversation_id}/followers-POST': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/{conversation_id}/links-POST': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
            {
                'name': 'link_ids'
            },
            {
                'name': 'link_external_urls'
            },
        ]
    },
    '/conversations/{conversation_id}/tags-POST': {
        'parameters': [
            {
                'name': 'tag_ids'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'inbox_id'
            },
            {
                'name': 'teammate_ids'
            },
        ]
    },
    '/conversations/{conversation_id}-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/{conversation_id}/events-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/conversations/{conversation_id}/followers-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/conversations/{conversation_id}/inboxes-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/{conversation_id}/messages-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/conversations/{conversation_id}/followers-DELETE': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/{conversation_id}/links-DELETE': {
        'parameters': [
            {
                'name': 'link_ids'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/{conversation_id}/tags-DELETE': {
        'parameters': [
            {
                'name': 'tag_ids'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/search/{query}-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/conversations/{conversation_id}/assignee-PUT': {
        'parameters': [
            {
                'name': 'assignee_id'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/conversations/{conversation_id}-PATCH': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
            {
                'name': 'assignee_id'
            },
            {
                'name': 'inbox_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'tag_ids'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/conversations/{conversation_id}/reminders-PATCH': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'scheduled_at'
            },
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/links/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/accounts/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/contacts/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/conversations/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/inboxes/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/teammates/custom_fields-GET': {
        'parameters': [
        ]
    },
    '/conversations/{conversation_id}/drafts-POST': {
        'parameters': [
            {
                'name': 'author_id'
            },
            {
                'name': 'body'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'conversation_id'
            },
            {
                'name': 'to'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'quote_body'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'mode'
            },
            {
                'name': 'signature_id'
            },
            {
                'name': 'should_add_default_signature'
            },
        ]
    },
    '/channels/{channel_id}/drafts-POST': {
        'parameters': [
            {
                'name': 'author_id'
            },
            {
                'name': 'body'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'to'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'quote_body'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'mode'
            },
            {
                'name': 'signature_id'
            },
            {
                'name': 'should_add_default_signature'
            },
        ]
    },
    '/drafts/{draft_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'draft_id'
            },
        ]
    },
    '/drafts/{message_id}-PATCH': {
        'parameters': [
            {
                'name': 'author_id'
            },
            {
                'name': 'body'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'message_id'
            },
            {
                'name': 'to'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'quote_body'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'mode'
            },
            {
                'name': 'signature_id'
            },
            {
                'name': 'should_add_default_signature'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/conversations/{conversation_id}/drafts-GET': {
        'parameters': [
            {
                'name': 'conversation_id'
            },
        ]
    },
    '/events/{event_id}-GET': {
        'parameters': [
            {
                'name': 'event_id'
            },
        ]
    },
    '/events-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/inboxes/{inbox_id}/teammates-POST': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'inbox_id'
            },
        ]
    },
    '/inboxes-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teammate_ids'
            },
        ]
    },
    '/teams/{team_id}/inboxes-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'teammate_ids'
            },
        ]
    },
    '/inboxes/{inbox_id}-GET': {
        'parameters': [
            {
                'name': 'inbox_id'
            },
        ]
    },
    '/inboxes/{inbox_id}/channels-GET': {
        'parameters': [
            {
                'name': 'inbox_id'
            },
        ]
    },
    '/inboxes/{inbox_id}/conversations-GET': {
        'parameters': [
            {
                'name': 'inbox_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/inboxes-GET': {
        'parameters': [
        ]
    },
    '/teams/{team_id}/inboxes-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/inboxes/{inbox_id}/teammates-GET': {
        'parameters': [
            {
                'name': 'inbox_id'
            },
        ]
    },
    '/inboxes/{inbox_id}/teammates-DELETE': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'inbox_id'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/articles-POST': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'category_id'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/locales/{locale}/articles-POST': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'category_id'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/categories-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parent_category_id'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/locales/{locale}/categories-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parent_category_id'
            },
        ]
    },
    '/knowledge_bases-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/knowledge_base_articles/{article_id}-DELETE': {
        'parameters': [
            {
                'name': 'article_id'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}-DELETE': {
        'parameters': [
            {
                'name': 'category_id'
            },
        ]
    },
    '/knowledge_base_articles/{article_id}/download/{attachment_id}-GET': {
        'parameters': [
            {
                'name': 'article_id'
            },
            {
                'name': 'attachment_id'
            },
        ]
    },
    '/knowledge_base_articles/{article_id}-GET': {
        'parameters': [
            {
                'name': 'article_id'
            },
        ]
    },
    '/knowledge_base_articles/{article_id}/locales/{locale}/content-GET': {
        'parameters': [
            {
                'name': 'article_id'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}-GET': {
        'parameters': [
            {
                'name': 'category_id'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}/content-GET': {
        'parameters': [
            {
                'name': 'category_id'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}/locales/{locale}/content-GET': {
        'parameters': [
            {
                'name': 'category_id'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/knowledge_base_articles/{article_id}/content-GET': {
        'parameters': [
            {
                'name': 'article_id'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/content-GET': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}-GET': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/locales/{locale}/content-GET': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/articles-GET': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}/articles-GET': {
        'parameters': [
            {
                'name': 'category_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/categories-GET': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/knowledge_bases-GET': {
        'parameters': [
        ]
    },
    '/knowledge_base_articles/{article_id}/content-PATCH': {
        'parameters': [
            {
                'name': 'article_id'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/knowledge_base_articles/{article_id}/locales/{locale}/content-PATCH': {
        'parameters': [
            {
                'name': 'article_id'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}/locales/{locale}/content-PATCH': {
        'parameters': [
            {
                'name': 'category_id'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/knowledge_base_categories/{category_id}/content-PATCH': {
        'parameters': [
            {
                'name': 'category_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/content-PATCH': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/knowledge_bases/{knowledge_base_id}/locales/{locale}/content-PATCH': {
        'parameters': [
            {
                'name': 'knowledge_base_id'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/links-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'external_url'
            },
            {
                'name': 'pattern'
            },
        ]
    },
    '/links/{link_id}-GET': {
        'parameters': [
            {
                'name': 'link_id'
            },
        ]
    },
    '/links-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/links/{link_id}/conversations-GET': {
        'parameters': [
            {
                'name': 'link_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/links/{link_id}-PATCH': {
        'parameters': [
            {
                'name': 'link_id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}/message_template_folders-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'message_template_folder_id'
            },
        ]
    },
    '/message_template_folders-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'parent_folder_id'
            },
        ]
    },
    '/teammates/{teammate_id}/message_template_folders-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teammate_id'
            },
            {
                'name': 'parent_folder_id'
            },
        ]
    },
    '/teams/{team_id}/message_template_folders-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'parent_folder_id'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}-DELETE': {
        'parameters': [
            {
                'name': 'message_template_folder_id'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}/message_template_folders-GET': {
        'parameters': [
            {
                'name': 'message_template_folder_id'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}-GET': {
        'parameters': [
            {
                'name': 'message_template_folder_id'
            },
        ]
    },
    '/message_template_folders-GET': {
        'parameters': [
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/teams/{team_id}/message_template_folders-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/teammates/{teammate_id}/message_template_folders-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}-PATCH': {
        'parameters': [
            {
                'name': 'message_template_folder_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'parent_folder_id'
            },
        ]
    },
    '/teammates/{teammate_id}/message_templates-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
            {
                'name': 'teammate_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'folder_id'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}/message_templates-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
            {
                'name': 'message_template_folder_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'inbox_ids'
            },
        ]
    },
    '/message_templates-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'inbox_ids'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/teams/{team_id}/message_templates-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'inbox_ids'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/message_templates/{message_template_id}-DELETE': {
        'parameters': [
            {
                'name': 'message_template_id'
            },
        ]
    },
    '/message_template_folders/{message_template_folder_id}/message_templates-GET': {
        'parameters': [
            {
                'name': 'message_template_folder_id'
            },
        ]
    },
    '/message_templates/{message_template_id}-GET': {
        'parameters': [
            {
                'name': 'message_template_id'
            },
        ]
    },
    '/message_templates-GET': {
        'parameters': [
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/teams/{team_id}/message_templates-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/teammates/{teammate_id}/message_templates-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/message_templates/{message_template_id}-PATCH': {
        'parameters': [
            {
                'name': 'message_template_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'body'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'inbox_ids'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/conversations/{conversation_id}/messages-POST': {
        'parameters': [
            {
                'name': 'body'
            },
            {
                'name': 'conversation_id'
            },
            {
                'name': 'to'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'sender_name'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'text'
            },
            {
                'name': 'quote_body'
            },
            {
                'name': 'options'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'signature_id'
            },
            {
                'name': 'should_add_default_signature'
            },
        ]
    },
    '/channels/{channel_id}/messages-POST': {
        'parameters': [
            {
                'name': 'to'
            },
            {
                'name': 'body'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'sender_name'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'author_id'
            },
            {
                'name': 'text'
            },
            {
                'name': 'options'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'signature_id'
            },
            {
                'name': 'should_add_default_signature'
            },
        ]
    },
    '/messages/{message_id}-GET': {
        'parameters': [
            {
                'name': 'message_id'
            },
        ]
    },
    '/messages/{message_id}/seen-GET': {
        'parameters': [
            {
                'name': 'message_id'
            },
        ]
    },
    '/inboxes/{inbox_id}/imported_messages-POST': {
        'parameters': [
            {
                'name': 'sender'
            },
            {
                'name': 'to'
            },
            {
                'name': 'body'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'inbox_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'body_format'
            },
            {
                'name': 'type'
            },
            {
                'name': 'assignee_id'
            },
            {
                'name': 'conversation_id'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/messages/{message_id}/seen-POST': {
        'parameters': [
            {
                'name': 'message_id'
            },
        ]
    },
    '/channels/{channel_id}/incoming_messages-POST': {
        'parameters': [
            {
                'name': 'sender'
            },
            {
                'name': 'body'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'body_format'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/rules/{rule_id}-GET': {
        'parameters': [
            {
                'name': 'rule_id'
            },
        ]
    },
    '/company/rules-GET': {
        'parameters': [
        ]
    },
    '/rules-GET': {
        'parameters': [
        ]
    },
    '/teams/{team_id}/rules-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/teammates/{teammate_id}/rules-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/shift/{shift_id}/teammates-POST': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'shift_id'
            },
        ]
    },
    '/shifts-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'color'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'times'
            },
            {
                'name': 'teammate_ids'
            },
        ]
    },
    '/teams/{team_id}/shifts-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'color'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'times'
            },
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/shift/{shift_id}-GET': {
        'parameters': [
            {
                'name': 'shift_id'
            },
        ]
    },
    '/shift/{shift_id}/teammates-GET': {
        'parameters': [
            {
                'name': 'shift_id'
            },
        ]
    },
    '/shifts-GET': {
        'parameters': [
        ]
    },
    '/teams/{team_id}/shifts-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/shift/{shift_id}/teammates-DELETE': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'shift_id'
            },
        ]
    },
    '/teammates/{teammate_id}/shifts-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/shifts/{shift_id}-PATCH': {
        'parameters': [
            {
                'name': 'shift_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'color'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'times'
            },
            {
                'name': 'teammate_ids'
            },
        ]
    },
    '/teams/{team_id}/signatures-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'sender_info'
            },
            {
                'name': 'is_visible_for_all_teammate_channels'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'channel_ids'
            },
        ]
    },
    '/teammates/{teammate_id}/signatures-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
            {
                'name': 'teammate_id'
            },
            {
                'name': 'sender_info'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'channel_ids'
            },
        ]
    },
    '/signatures/{signature_id}-DELETE': {
        'parameters': [
            {
                'name': 'signature_id'
            },
        ]
    },
    '/signatures/{signature_id}-GET': {
        'parameters': [
            {
                'name': 'signature_id'
            },
        ]
    },
    '/teams/{team_id}/signatures-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/teammates/{teammate_id}/signatures-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/signatures/{signature_id}-PATCH': {
        'parameters': [
            {
                'name': 'signature_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sender_info'
            },
            {
                'name': 'body'
            },
            {
                'name': 'is_visible_for_all_teammate_channels'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'channel_ids'
            },
        ]
    },
    '/tags/{tag_id}/children-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'tag_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'is_visible_in_conversation_lists'
            },
        ]
    },
    '/company/tags-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'is_visible_in_conversation_lists'
            },
        ]
    },
    '/tags-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'is_visible_in_conversation_lists'
            },
        ]
    },
    '/teams/{team_id}/tags-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'is_visible_in_conversation_lists'
            },
        ]
    },
    '/teammates/{teammate_id}/tags-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teammate_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'is_visible_in_conversation_lists'
            },
        ]
    },
    '/tags/{tag_id}-DELETE': {
        'parameters': [
            {
                'name': 'tag_id'
            },
        ]
    },
    '/tags/{tag_id}-GET': {
        'parameters': [
            {
                'name': 'tag_id'
            },
        ]
    },
    '/tags-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/tags/{tag_id}/children-GET': {
        'parameters': [
            {
                'name': 'tag_id'
            },
        ]
    },
    '/company/tags-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/tags/{tag_id}/conversations-GET': {
        'parameters': [
            {
                'name': 'tag_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/teams/{team_id}/tags-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/teammates/{teammate_id}/tags-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
        ]
    },
    '/tags/{tag_id}-PATCH': {
        'parameters': [
            {
                'name': 'tag_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'parent_tag_id'
            },
            {
                'name': 'is_visible_in_conversation_lists'
            },
        ]
    },
    '/teammates/{teammate_id}/inboxes-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/teammates/{teammate_id}-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
        ]
    },
    '/teammates/{teammate_id}/conversations-GET': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'q'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/teammates-GET': {
        'parameters': [
        ]
    },
    '/teammates/{teammate_id}-PATCH': {
        'parameters': [
            {
                'name': 'teammate_id'
            },
            {
                'name': 'username'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'is_available'
            },
            {
                'name': 'custom_fields'
            },
        ]
    },
    '/teams/{team_id}/teammates-POST': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/teams/{team_id}-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
        ]
    },
    '/teams/{team_id}/teammates-DELETE': {
        'parameters': [
            {
                'name': 'teammate_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/me-GET': {
        'parameters': [
        ]
    },
};