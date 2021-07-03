#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from bot.translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = 6798244

API_HASH = "850318283159462a0c1af965dc466888"

BOT_TOKEN = "1895962546:AAFDt8uX2eS4sKdArX5-nGJkGqL27oWg-70"

DB_URI = "mongodb+srv://autofilter:autofilter@cluster0.fdffg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

USER_SESSION = "AQAdRjE5s6v0s7j6uqAMJhfpNaaeLmBzENoPV8dGpxAwla0aAZdzc4bAjGNa7HjrORHfcMNflY5j9Po0NNuRSNVLyOjEUNmFoIW8lARNNEkCp2UriZNEHxd60F3MWz4i2P3h2r994hBNK3GBlvtyicTtUHMKT1tH9a4ULUPVVm5d-PnDB3rJuEUYXVQACwFso58Ld0z-h7xXx0PdriwL2If_iWAzcviGpo1R0bjraHLViA0xdtsxaNR3AzkYSHuarmEiBU-FFNQmSCyjK2BCEEOMJMZAVInP5DFw_gzm1wqT2nc9ac63u64O4OU5Rt7sLWm67eMqpQpkeHv9-coswOm-bylVTQA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
