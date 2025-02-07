import os
from synapsepy import Client
import frappe

args = {
    "client_id": frappe.conf.get("synapsefi_client_id"),
    "client_secret": frappe.conf.get("synapsefi_client_secret"),
    "fingerprint": frappe.conf.get("synapsefi_fp"),
    "ip_address": frappe.conf.get("synapsefi_ip"),  # user's IP
    "devmode": frappe.conf.get(
        "synapsefi_development_mode"
    ),  # (optional) default False
    "logging": frappe.conf.get(
        "synapsefi_logging"
    ),  # (optional) logs to stdout if True
}

SYNAPSEFI_CLIENT = Client(**args)
