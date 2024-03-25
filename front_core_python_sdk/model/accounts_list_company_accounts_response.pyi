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


class AccountsListCompanyAccountsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def _pagination() -> typing.Type['AccountsListCompanyAccountsResponsePagination']:
                return AccountsListCompanyAccountsResponsePagination
        
            @staticmethod
            def _links() -> typing.Type['AccountsListCompanyAccountsResponseLinks']:
                return AccountsListCompanyAccountsResponseLinks
            
            
            class _results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccountResponse']:
                        return AccountResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AccountResponse'], typing.List['AccountResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '_results':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccountResponse':
                    return super().__getitem__(i)
            __annotations__ = {
                "_pagination": _pagination,
                "_links": _links,
                "_results": _results,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_pagination"]) -> 'AccountsListCompanyAccountsResponsePagination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'AccountsListCompanyAccountsResponseLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_results"]) -> MetaOapg.properties._results: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_pagination", "_links", "_results", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_pagination"]) -> typing.Union['AccountsListCompanyAccountsResponsePagination', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['AccountsListCompanyAccountsResponseLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_results"]) -> typing.Union[MetaOapg.properties._results, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_pagination", "_links", "_results", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _pagination: typing.Union['AccountsListCompanyAccountsResponsePagination', schemas.Unset] = schemas.unset,
        _links: typing.Union['AccountsListCompanyAccountsResponseLinks', schemas.Unset] = schemas.unset,
        _results: typing.Union[MetaOapg.properties._results, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountsListCompanyAccountsResponse':
        return super().__new__(
            cls,
            *args,
            _pagination=_pagination,
            _links=_links,
            _results=_results,
            _configuration=_configuration,
            **kwargs,
        )

from front_core_python_sdk.model.account_response import AccountResponse
from front_core_python_sdk.model.accounts_list_company_accounts_response_links import AccountsListCompanyAccountsResponseLinks
from front_core_python_sdk.model.accounts_list_company_accounts_response_pagination import AccountsListCompanyAccountsResponsePagination
