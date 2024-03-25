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
from pydantic import BaseModel, Field, RootModel, ConfigDict


AnalyticsActivitiesColumns = Literal["Activity ID", "Type", "Source", "Message ID", "Conversation ID", "Segment", "Segment start", "Segment end", "Direction", "Status", "Status at activity time", "Inbox", "Inbox API ID", "Inbox at activity time", "Inbox API IDs at activity time", "Previous inbox IDs", "Message date", "Autoreply", "Reaction time", "Total reply time", "Handle time", "Response time", "Stage resolution time", "Replies to resolution", "Attributed to", "Assignee", "Author", "Contact name", "Contact handle", "Account names", "To", "Cc", "Bcc", "Extract", "Tags", "Tag API IDs", "Tags at activity time", "Tag API IDs at activity time", "Tag application duration", "Activity API ID", "Message API ID", "Comment API ID", "Conversation API ID", "Message original ID", "New Conversation", "First response", "Business hours", "Subject", "Account name", "Survey rating", "Survey comment", "Segment closed", "Segment contains messages", "Last segment activity", "Added tag", "Added tag API ID", "Removed tag", "Removed tag API ID"]
