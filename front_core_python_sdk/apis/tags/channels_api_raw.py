# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.inboxes_inbox_id_channels.post import CreateInboxChannelRaw
from front_core_python_sdk.paths.channels_channel_id.get import GetChannelRaw
from front_core_python_sdk.paths.channels.get import ListRaw
from front_core_python_sdk.paths.teams_team_id_channels.get import ListTeamRaw
from front_core_python_sdk.paths.teammates_teammate_id_channels.get import ListTeammateRaw
from front_core_python_sdk.paths.channels_channel_id.patch import UpdateChannelRaw
from front_core_python_sdk.paths.channels_channel_id_validate.post import ValidateSmtpSettingsRaw


class ChannelsApiRaw(
    CreateInboxChannelRaw,
    GetChannelRaw,
    ListRaw,
    ListTeamRaw,
    ListTeammateRaw,
    UpdateChannelRaw,
    ValidateSmtpSettingsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass