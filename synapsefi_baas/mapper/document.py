from ..utils.to_date import timestamp_to_frappe_date


class SynapseDocumentMapper:
    @staticmethod
    def map_doc(synapse_user):
        frappe_doc = {
            "name1": synapse_user.get("name"),
            "phone_number": synapse_user.get("phone_number"),
            "email": synapse_user.get("email"),
            "ip": synapse_user.get("ip"),
            "year": synapse_user.get("year"),
            "month": synapse_user.get("month"),
            "day": synapse_user.get("day"),
            "title": synapse_user.get("title"),
            "entity_relationship": synapse_user.get("entity_relationship"),
            "id_score": synapse_user.get("is_score"),
            "is_active": synapse_user.get("is_active"),
            "address_city": synapse_user.get("address_city"),
            "address_country_code": synapse_user.get("address_country_code"),
            "address_postal_code": synapse_user.get("address_postal_code"),
            "address_subdivision": synapse_user.get("address_subdivision"),
            "trust_level": synapse_user.get("trust_level"),
            "company_activity": ",".join(synapse_user.get("company_activity", [])),
            "ownership_percentage": synapse_user.get("ownership_percentage"),
            "desired_scope": synapse_user.get("desired_scope"),
            "permission_scope": synapse_user.get("permission_scope"),
            "required_edd_docs": ",".join(synapse_user.get("required_edd_docs", [])),
            "entity_scope": synapse_user.get("entity_scope"),
            "entity_type": synapse_user.get("entity_type"),
            "id": synapse_user.get("id"),
            "docs_title": synapse_user.get("docs_title"),
            "docs_key": synapse_user.get("docs_key"),
            "doc_option_key": synapse_user.get("doc_option_key"),
            "alias_optional": synapse_user.get("alias"),
            "edd_status": synapse_user.get("edd_status"),
            "maiden_name": synapse_user.get("maiden_name"),
            "watchlists": synapse_user.get("watchlists"),
            "physical_docs": [
                SynapseDocumentMapper.physical_docs_to_doc(doc)
                for doc in synapse_user.get("documents", [])
                if doc.get("physical_docs")
            ],
            "social_docs": [
                SynapseDocumentMapper.social_docs_to_doc(doc)
                for doc in synapse_user.get("documents", [])
                if doc.get("social_docs")
            ],
            "virtual_docs": [
                SynapseDocumentMapper.virtual_docs_to_doc(doc)
                for doc in synapse_user.get("documents", [])
                if doc.get("virtual_docs")
            ],
        }

        return frappe_doc

    @staticmethod
    def physical_docs_to_doc(physical_doc):

        frappe_doc = {
            "document_type": physical_doc.get("document_type"),
            "id": physical_doc.get("id"),
            "last_updated": timestamp_to_frappe_date(physical_doc.get("last_updated")),
            "country_code": physical_doc.get("meta").get("country_code"),
            "state_code": physical_doc.get("meta").get("state_code"),
            "status": physical_doc.get("status"),
            "document_value": physical_doc.get("document_value"),
        }

        return frappe_doc

    @staticmethod
    def virtual_docs_to_doc(virtual_doc):
        frappe_doc = {
            "document_type": virtual_doc.get("document_type"),
            "id": virtual_doc.get("id"),
            "last_updated": timestamp_to_frappe_date(virtual_doc.get("last_updated")),
            "status": virtual_doc.get("status"),
            "document_value": virtual_doc.get("document_value"),
            "meta_country_code": virtual_doc.get("meta").get("country_code"),
            "meta_sub_type": virtual_doc.get("meta").get("sub_type"),
        }

        return frappe_doc

    @staticmethod
    def social_docs_to_doc(social_doc):
        frappe_doc = {
            "document_type": social_doc.get("document_type"),
            "document_id": social_doc.get("document_id"),
            "last_updated": timestamp_to_frappe_date(social_doc.get("last_updated")),
            "document_value": social_doc.get("document_value"),
            "info_valid_reasons": social_doc.get("info_valid_reasons"),
        }

        return frappe_doc

    @staticmethod
    def map_user(doc):
        new_user = {}

        fields = [
            "_id",
            "account_closure_date",
            "flag",
            "flag_code",
            "permission",
            "permission_code",
            "cip_tag",
            "watchlists",
            "date_joined",
            "last_updated",
            "supp_id",
            "is_trusted",
            "is_hidden",
            "is_business",
            "extra_security",
            "public_note",
            "documents",
            "legal_names",
            "logins",
            "phone_numbers",
        ]

        for field in fields:
            if field in doc:
                if field == "phone_numbers" or field == "legal_names":
                    new_user[field] = [item for item in doc[field]]
                elif field == "documents":
                    new_user[field] = []
                else:
                    new_user[field] = doc[field]

        return new_user
