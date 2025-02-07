# Copyright (c) 2025, ME and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from synapsefi_baas.libs.synapsefi_client import SYNAPSEFI_CLIENT
from synapsefi_baas.mapper.user import SynapseUserMapper
from synapsefi_baas.utils.pagination_parser import parse_pagination
import os
import frappe


class SynapticUser(Document):

    users_count = 0

    def db_insert(self, *args, **kwargs):
        d = self.get_valid_dict()
        print(f"DATA: {d}")
        user = SynapseUserMapper.map_user(d)
        print(f"{user}")

        created_user = SYNAPSEFI_CLIENT.create_user(
            user, frappe.conf.get("synapsefi_ip")
        )

    def load_from_db(self):
        user = SYNAPSEFI_CLIENT.get_user(self.name)

        return super(Document, self).__init__(SynapseUserMapper.map_user(user))

    def db_update(self):
        pass

    # using %% not valid in synaptic
    @staticmethod
    def get_list(args):
        pagination = parse_pagination(args)
        print(args)
        users = SYNAPSEFI_CLIENT.get_all_users(
            per_page=pagination.per_page, page=pagination.page
        )

        SynapticUser.users_count = users.users_count

        user_lists = []

        for user in users.list_of_users:
            user_temp = SynapseUserMapper.map_user(user)

            user_lists.append(user_temp)

        return user_lists

    @staticmethod
    def get_count(args):
        return SynapticUser.users_count

    @staticmethod
    def get_stats(args):
        pass
