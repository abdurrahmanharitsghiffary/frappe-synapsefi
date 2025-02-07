from ..utils.to_date import timestamp_to_frappe_date
from synapsepy import User
from .document import SynapseDocumentMapper


class SynapseUserMapper:
    @staticmethod
    def map_user(user: User):
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
            "documents": [
                SynapseDocumentMapper.map_doc(user) for user in user.body["documents"]
            ],
        }

        return user_temp
