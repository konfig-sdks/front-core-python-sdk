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


class CreateDraft(BaseModel):
    # ID of the teammate on behalf of whom the draft will be created. Alternatively, you can supply the author ID as a [resource alias](https://dev.frontapp.com/docs/resource-aliases-1).
    author_id: str = Field(alias='author_id')

    # Body of the draft
    body: str = Field(alias='body')

    # List of recipient handles who will receive the message once the draft is sent
    to: typing.Optional[typing.List[str]] = Field(None, alias='to')

    # List of recipient handles who will receive a copy of the message once the draft is sent
    cc: typing.Optional[typing.List[str]] = Field(None, alias='cc')

    # List of the recipient handles who will receive a blind copy of the message once the draft is sent
    bcc: typing.Optional[typing.List[str]] = Field(None, alias='bcc')

    # Subject of the draft.
    subject: typing.Optional[str] = Field(None, alias='subject')

    # Body for the quote that the message is referencing. Only available on email channels.
    quote_body: typing.Optional[str] = Field(None, alias='quote_body')

    # Binary data of attached files. Must use `Content-Type: multipart/form-data` if specified. See [example](https://gist.github.com/hdornier/e04d04921032e98271f46ff8a539a4cb) or read more about [Attachments](https://dev.frontapp.com/docs/attachments-1). Max 25 MB.
    attachments: typing.Optional[typing.List[typing.IO]] = Field(None, alias='attachments')

    # Mode of the draft to create. Can be 'private' (draft is visible to the author only) or 'shared' (draft is visible to all teammates with access to the conversation).
    mode: typing.Optional[Literal["private", "shared"]] = Field(None, alias='mode')

    # ID of the signature to attach to this draft. If null, no signature is attached.
    signature_id: typing.Optional[str] = Field(None, alias='signature_id')

    # Whether or not Front should try to resolve a signature for the message. Is ignored if signature_id is included. Default false;
    should_add_default_signature: typing.Optional[bool] = Field(None, alias='should_add_default_signature')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
