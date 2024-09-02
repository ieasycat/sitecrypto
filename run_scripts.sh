#!/bin/bash

# Activation of the virtual environment (if required)
# source /path/to/your/venv/bin/activate

# The path to the Python interpreter in a virtual environment
PYTHON_PATH=".venv/bin/python"

# The path to the script and JSON files
MANAGE_PATH="sitecrypto/manage.py"
NETWORK_JSON="sitecrypto/crypto/data/network_data.json"
CRYPTO_JSON="sitecrypto/crypto/data/crypto_data.json"

# Running the first script with the command
$PYTHON_PATH $MANAGE_PATH import_network $NETWORK_JSON

# Running the second script with the command
$PYTHON_PATH $MANAGE_PATH import_crypto $CRYPTO_JSON
