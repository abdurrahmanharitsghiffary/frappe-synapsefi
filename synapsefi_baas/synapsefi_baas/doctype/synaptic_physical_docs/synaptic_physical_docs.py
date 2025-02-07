# Copyright (c) 2025, ME and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from synapsefi_baas.utils.to_date import timestamp_to_frappe_date


class SynapticPhysicalDocs(Document):

    def db_insert(self, *args, **kwargs):
        pass

    def load_from_db(self):
        pass

    def db_update(self):
        pass

    @staticmethod
    def get_list(args):
        pass

    @staticmethod
    def get_count(args):
        pass

    @staticmethod
    def get_stats(args):
        pass

    @staticmethod
    def physical_docs_to_doc(physical_doc):

        frappe_doc = {
            "document_type": physical_doc.get("document_type"),
            "id": physical_doc.get("id"),
            "last_updated": timestamp_to_frappe_date(physical_doc.get("last_updated")),
            "country_code": physical_doc.get("country_code"),
            "state_code": physical_doc.get("state_code"),
            "status": physical_doc.get("status"),
            "document_value": physical_doc.get("document_value"),
            "sub_type": physical_doc.get("sub_type"),
        }

        return frappe_doc
