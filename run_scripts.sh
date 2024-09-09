#!/bin/bash

# Activation of the virtual environment (if required)
# source /path/to/your/venv/bin/activate

# The path to the Python interpreter in a virtual environment
#PYTHON_PATH="/path/to/your/venv/bin/activate"

# The path to the script and JSON files
NETWORK_JSON="crypto/data/network_data.json"
CRYPTO_JSON="crypto/data/crypto_data.json"

# Running the first script with the command
python manage.py import_network $NETWORK_JSON

# Running the second script with the command
python manage.py import_crypto $CRYPTO_JSON
