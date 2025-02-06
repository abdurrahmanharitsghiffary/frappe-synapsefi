import os
from synapsepy import Client

args = {
    "client_id": os.getenv("SYNAPSEFI_CLIENT_ID"),
    "client_secret": os.getenv("SYNAPSEFI_CLIENT_SECRET"),
    "fingerprint": os.getenv("SYNAPSEFI_FP"),
    "ip_address": os.getenv("SYNAPSEFI_IP"),  # user's IP
    "devmode": os.getenv("SYNAPSEFI_DEVELOPMENT_MODE"),  # (optional) default False
    "logging": os.getenv("SYNAPSEFI_LOGGING"),  # (optional) logs to stdout if True
}

SYNAPSEFI_CLIENT = Client(**args)
