# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from front_core_python_sdk import schemas  # noqa: F401


class AnalyticsMetricId(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "avg_csat_survey_response": "AVG_CSAT_SURVEY_RESPONSE",
            "avg_first_response_time": "AVG_FIRST_RESPONSE_TIME",
            "avg_handle_time": "AVG_HANDLE_TIME",
            "avg_replies_to_resolution": "AVG_REPLIES_TO_RESOLUTION",
            "avg_resolution_time": "AVG_RESOLUTION_TIME",
            "avg_response_time": "AVG_RESPONSE_TIME",
            "avg_sla_breach_time": "AVG_SLA_BREACH_TIME",
            "avg_total_reply_time": "AVG_TOTAL_REPLY_TIME",
            "new_segments_count": "NEW_SEGMENTS_COUNT",
            "num_active_segments_full": "NUM_ACTIVE_SEGMENTS_FULL",
            "num_archived_segments": "NUM_ARCHIVED_SEGMENTS",
            "num_archived_segments_with_reply": "NUM_ARCHIVED_SEGMENTS_WITH_REPLY",
            "num_csat_survey_response": "NUM_CSAT_SURVEY_RESPONSE",
            "num_messages_received": "NUM_MESSAGES_RECEIVED",
            "num_messages_sent": "NUM_MESSAGES_SENT",
            "num_sla_breach": "NUM_SLA_BREACH",
            "pct_csat_survey_satisfaction": "PCT_CSAT_SURVEY_SATISFACTION",
            "pct_resolved_on_first_reply": "PCT_RESOLVED_ON_FIRST_REPLY",
            "pct_tagged_conversations": "PCT_TAGGED_CONVERSATIONS",
            "num_closed_segments": "NUM_CLOSED_SEGMENTS",
            "num_open_segments_start": "NUM_OPEN_SEGMENTS_START",
            "num_open_segments_end": "NUM_OPEN_SEGMENTS_END",
            "num_resolved_segments": "NUM_RESOLVED_SEGMENTS",
            "num_unresolved_active_segments": "NUM_UNRESOLVED_ACTIVE_SEGMENTS",
            "num_workload_segments": "NUM_WORKLOAD_SEGMENTS",
        }
    
    @schemas.classproperty
    def AVG_CSAT_SURVEY_RESPONSE(cls):
        return cls("avg_csat_survey_response")
    
    @schemas.classproperty
    def AVG_FIRST_RESPONSE_TIME(cls):
        return cls("avg_first_response_time")
    
    @schemas.classproperty
    def AVG_HANDLE_TIME(cls):
        return cls("avg_handle_time")
    
    @schemas.classproperty
    def AVG_REPLIES_TO_RESOLUTION(cls):
        return cls("avg_replies_to_resolution")
    
    @schemas.classproperty
    def AVG_RESOLUTION_TIME(cls):
        return cls("avg_resolution_time")
    
    @schemas.classproperty
    def AVG_RESPONSE_TIME(cls):
        return cls("avg_response_time")
    
    @schemas.classproperty
    def AVG_SLA_BREACH_TIME(cls):
        return cls("avg_sla_breach_time")
    
    @schemas.classproperty
    def AVG_TOTAL_REPLY_TIME(cls):
        return cls("avg_total_reply_time")
    
    @schemas.classproperty
    def NEW_SEGMENTS_COUNT(cls):
        return cls("new_segments_count")
    
    @schemas.classproperty
    def NUM_ACTIVE_SEGMENTS_FULL(cls):
        return cls("num_active_segments_full")
    
    @schemas.classproperty
    def NUM_ARCHIVED_SEGMENTS(cls):
        return cls("num_archived_segments")
    
    @schemas.classproperty
    def NUM_ARCHIVED_SEGMENTS_WITH_REPLY(cls):
        return cls("num_archived_segments_with_reply")
    
    @schemas.classproperty
    def NUM_CSAT_SURVEY_RESPONSE(cls):
        return cls("num_csat_survey_response")
    
    @schemas.classproperty
    def NUM_MESSAGES_RECEIVED(cls):
        return cls("num_messages_received")
    
    @schemas.classproperty
    def NUM_MESSAGES_SENT(cls):
        return cls("num_messages_sent")
    
    @schemas.classproperty
    def NUM_SLA_BREACH(cls):
        return cls("num_sla_breach")
    
    @schemas.classproperty
    def PCT_CSAT_SURVEY_SATISFACTION(cls):
        return cls("pct_csat_survey_satisfaction")
    
    @schemas.classproperty
    def PCT_RESOLVED_ON_FIRST_REPLY(cls):
        return cls("pct_resolved_on_first_reply")
    
    @schemas.classproperty
    def PCT_TAGGED_CONVERSATIONS(cls):
        return cls("pct_tagged_conversations")
    
    @schemas.classproperty
    def NUM_CLOSED_SEGMENTS(cls):
        return cls("num_closed_segments")
    
    @schemas.classproperty
    def NUM_OPEN_SEGMENTS_START(cls):
        return cls("num_open_segments_start")
    
    @schemas.classproperty
    def NUM_OPEN_SEGMENTS_END(cls):
        return cls("num_open_segments_end")
    
    @schemas.classproperty
    def NUM_RESOLVED_SEGMENTS(cls):
        return cls("num_resolved_segments")
    
    @schemas.classproperty
    def NUM_UNRESOLVED_ACTIVE_SEGMENTS(cls):
        return cls("num_unresolved_active_segments")
    
    @schemas.classproperty
    def NUM_WORKLOAD_SEGMENTS(cls):
        return cls("num_workload_segments")
