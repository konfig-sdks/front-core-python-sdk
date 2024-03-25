# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredUpdateConversationReminders(TypedDict):
    # ID of the teammate to create a reminder for. For a private conversation, specify the id of the teammate that owns the conversation. For a shared conversation, use the id of any teammate that has access to the conversation's shared inbox. Alternatively, you can supply an email as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).
    teammate_id: str

    # Timestamp to schedule the reminder for. Set to null to cancel.
    scheduled_at: typing.Union[int, float]

class OptionalUpdateConversationReminders(TypedDict, total=False):
    pass

class UpdateConversationReminders(RequiredUpdateConversationReminders, OptionalUpdateConversationReminders):
    pass
