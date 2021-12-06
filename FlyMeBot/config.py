#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = "c4cb4b1a-f70d-4575-a4d5-b04c7e1d4812"
    LUIS_API_KEY = "6b8d76e7fde4489cb8c8a2181b365923"
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = "lasta.cognitiveservices.azure.com/"
    APPINSIGHTS_INSTRUMENTATION_KEY = "b67c8daf-f3af-4c3b-b135-e27c2723840d"
    


