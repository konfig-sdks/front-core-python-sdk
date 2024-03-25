from front_core_python_sdk.paths.contacts_contact_id.get import ApiForget
from front_core_python_sdk.paths.contacts_contact_id.delete import ApiFordelete
from front_core_python_sdk.paths.contacts_contact_id.patch import ApiForpatch


class ContactsContactId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
