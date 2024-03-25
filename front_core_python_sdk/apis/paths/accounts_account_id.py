from front_core_python_sdk.paths.accounts_account_id.get import ApiForget
from front_core_python_sdk.paths.accounts_account_id.delete import ApiFordelete
from front_core_python_sdk.paths.accounts_account_id.patch import ApiForpatch


class AccountsAccountId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
