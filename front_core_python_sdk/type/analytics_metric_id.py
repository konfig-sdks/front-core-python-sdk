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


AnalyticsMetricId = Literal["avg_csat_survey_response", "avg_first_response_time", "avg_handle_time", "avg_replies_to_resolution", "avg_resolution_time", "avg_response_time", "avg_sla_breach_time", "avg_total_reply_time", "new_segments_count", "num_active_segments_full", "num_archived_segments", "num_archived_segments_with_reply", "num_csat_survey_response", "num_messages_received", "num_messages_sent", "num_sla_breach", "pct_csat_survey_satisfaction", "pct_resolved_on_first_reply", "pct_tagged_conversations", "num_closed_segments", "num_open_segments_start", "num_open_segments_end", "num_resolved_segments", "num_unresolved_active_segments", "num_workload_segments"]
