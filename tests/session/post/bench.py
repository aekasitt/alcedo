#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/post/bench.py
# VERSION:     0.1.4
# CREATED:     2024-03-27 16:29
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from json import dumps

### Local modules ###
from alcedo import Client, Response
from tests import *


def test_alcedo_post() -> None:
  client: Client = Client()
  for i in range(1_000):
    body: dict = {"hello": "world", "count": i}
    response: Response = client.post(f"{ TEST_ENDPOINT }/create", payload=body)
    assert response.json() == {"received": dumps(body).replace(" ", "").replace("'", '"')}
