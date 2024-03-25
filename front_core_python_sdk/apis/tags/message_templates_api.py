# coding: utf-8

"""
    Core API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from front_core_python_sdk.paths.teammates_teammate_id_message_templates.post import AddNewTeammateTemplate
from front_core_python_sdk.paths.message_template_folders_message_template_folder_id_message_templates.post import CreateChildTemplate
from front_core_python_sdk.paths.message_templates.post import CreateNewTemplate
from front_core_python_sdk.paths.teams_team_id_message_templates.post import CreateTeamTemplate
from front_core_python_sdk.paths.message_templates_message_template_id.delete import DeleteTemplate
from front_core_python_sdk.paths.message_template_folders_message_template_folder_id_message_templates.get import GetChildTemplates
from front_core_python_sdk.paths.message_templates_message_template_id.get import GetTemplateById
from front_core_python_sdk.paths.message_templates.get import List
from front_core_python_sdk.paths.teams_team_id_message_templates.get import ListTeamTemplates
from front_core_python_sdk.paths.teammates_teammate_id_message_templates.get import ListTeammateTemplates
from front_core_python_sdk.paths.message_templates_message_template_id.patch import UpdateTemplateById
from front_core_python_sdk.apis.tags.message_templates_api_raw import MessageTemplatesApiRaw


class MessageTemplatesApi(
    AddNewTeammateTemplate,
    CreateChildTemplate,
    CreateNewTemplate,
    CreateTeamTemplate,
    DeleteTemplate,
    GetChildTemplates,
    GetTemplateById,
    List,
    ListTeamTemplates,
    ListTeammateTemplates,
    UpdateTemplateById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MessageTemplatesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MessageTemplatesApiRaw(api_client)
