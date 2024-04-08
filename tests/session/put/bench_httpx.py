#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/put/bench_httpx.py
# VERSION:     0.1.7
# CREATED:     2024-03-28 14:18
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from json import dumps

### Third-party packages ###
from httpx import Client, Response
from pytest import mark

### Local modules ###
from tests import *


@mark.httpx
def test_httpx_client_put_update_endpoint() -> None:
  client: Client = Client()
  for i in range(RUNS):
    body: dict = {"hello": "world", "count": i}
    response: Response = client.put(f"{ TEST_ENDPOINT }/update", json=dumps(body))
    assert response.json() == {"updated": body}
