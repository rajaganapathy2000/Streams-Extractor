#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1723222143:AAGJ6h8QDMLukcpgigA-ATM9gk9Wzpcaenk")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "2842684"))
    API_HASH = os.environ.get("API_HASH", "795e3027e6144207a130966d96a93f00")
    
