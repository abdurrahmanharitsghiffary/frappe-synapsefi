# Copyright (c) 2025, ME and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from synapsefi_baas.libs.synapsefi_client import SYNAPSEFI_CLIENT
from synapsefi_baas.utils.to_date import timestamp_to_frappe_date
from synapsepy.user import User


class SynapticUser(Document):

    def db_insert(self, *args, **kwargs):
        pass

    def load_from_db(self):
        user = SYNAPSEFI_CLIENT.get_user(self.name)

        return super(Document, self).__init__(SynapticUser.user_to_userdoc(user))

    def db_update(self):
        pass

    @staticmethod
    def get_list(args):
        print(f"ARGS: {args}")

        users = SYNAPSEFI_CLIENT.get_all_users()

        user_lists = []

        print(f"Users: {users.list_of_users[0].body}")

        for user in users.list_of_users:
            user_temp = SynapticUser.user_to_userdoc(user)
            # "documerts",

            user_lists.append(user_temp)

        return user_lists

    @staticmethod
    def get_count(args):
        users = SYNAPSEFI_CLIENT.get_all_users()

        return users.users_count

    @staticmethod
    def get_stats(args):
        pass

    @staticmethod
    def user_to_userdoc(user: User):
        user_temp = {
            "name": user.body["_id"],
            "_id": user.body["_id"],
            "flag": user.body["flag"],
            "flag_code": user.body["flag_code"],
            "is_trusted": user.body["extra"]["is_trusted"],
            "supp_id": user.body["extra"]["supp_id"],
            "is_hidden": user.body["is_hidden"],
            "is_business": user.body["extra"]["is_business"],
            "extra_security": user.body["extra"]["extra_security"],
            "public_note": user.body["extra"]["public_note"],
            "permission": user.body["permission"],
            "permission_code": user.body["permission_code"],
            "watchlists": user.body["watchlists"],
            "date_joined": timestamp_to_frappe_date(user.body["extra"]["date_joined"]),
            "last_updated": timestamp_to_frappe_date(
                user.body["extra"]["last_updated"]
            ),
            "account_closure_date": timestamp_to_frappe_date(
                user.body["account_closure_date"]
            ),
            "legal_names": [
                {"legal_name": legal_name} for legal_name in user.body["legal_names"]
            ],
            "phone_numbers": [
                {"phone_number": phone_number}
                for phone_number in user.body["phone_numbers"]
            ],
            "logins": user.body["logins"],
            "documerts": [],
        }

        return user_temp
