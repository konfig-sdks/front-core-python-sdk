# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.contact_groups_contact_group_id_contacts.post import AddContactsToGroup
from front_core_python_sdk.paths.contact_groups.post import CreateNewGroup
from front_core_python_sdk.paths.teams_team_id_contact_groups.post import CreateNewGroup0
from front_core_python_sdk.paths.teammates_teammate_id_contact_groups.post import CreateTeammateGroup
from front_core_python_sdk.paths.contact_groups_contact_group_id.delete import DeleteGroup
from front_core_python_sdk.paths.contact_groups_contact_group_id_contacts.get import ListGroupContacts
from front_core_python_sdk.paths.contact_groups.get import ListGroups
from front_core_python_sdk.paths.teams_team_id_contact_groups.get import ListTeamGroups
from front_core_python_sdk.paths.teammates_teammate_id_contact_groups.get import ListTeammateGroups
from front_core_python_sdk.paths.contact_groups_contact_group_id_contacts.delete import RemoveContacts
from front_core_python_sdk.apis.tags.contact_groups_api_raw import ContactGroupsApiRaw


class ContactGroupsApi(
    AddContactsToGroup,
    CreateNewGroup,
    CreateNewGroup0,
    CreateTeammateGroup,
    DeleteGroup,
    ListGroupContacts,
    ListGroups,
    ListTeamGroups,
    ListTeammateGroups,
    RemoveContacts,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContactGroupsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContactGroupsApiRaw(api_client)
