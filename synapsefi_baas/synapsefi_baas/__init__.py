import frappe


def get_default_company(user=None):
    """Get default company for user"""
    from frappe.defaults import get_user_default_as_list

    if not user:
        user = frappe.session.user

    companies = get_user_default_as_list("company", user)
    if companies:
        default_company = companies[0]
    else:
        default_company = frappe.db.get_single_value(
            "Global Defaults", "default_company"
        )

    return default_company
