#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "66db8322-acfe-40c4-b03d-fc75fcf7fbbc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "#3T07c-Gm05vInUQ$nUGad;XWK")
    LUIS_APP_ID = os.environ.get("LuisAppId","c4cb4b1a-f70d-4575-a4d5-b04c7e1d4812")
    LUIS_API_KEY = os.environ.get("LuisAPIKey","6b8d76e7fde4489cb8c8a2181b365923")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME =os.environ.get("LuisAPIHostName", "lasta.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey","40778be4-e5a8-48cc-a961-50629c3e0ef9")
    


