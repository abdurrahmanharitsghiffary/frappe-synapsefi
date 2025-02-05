from synapsefi_baas import get_default_company
from frappe import _


def welcome_email():
    site_name = get_default_company() or "ERPNext"
    title = _("Welcome to {0}").format(site_name)
    return title
