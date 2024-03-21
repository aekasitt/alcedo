#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/bench.py
# VERSION: 	   0.1.0
# CREATED: 	   2024-03-21 13:31
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Response, get
from tests import setup_teardown_api_server


def test_generic_endpoint() -> None:
    response: Response = get("http://localhost:6969")
    print(response)
