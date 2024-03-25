# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.events_event_id.get import GetEvent
from front_core_python_sdk.paths.events.get import ListDetailedInboxEvents
from front_core_python_sdk.apis.tags.events_api_raw import EventsApiRaw


class EventsApi(
    GetEvent,
    ListDetailedInboxEvents,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EventsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EventsApiRaw(api_client)