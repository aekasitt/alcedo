#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/post/bench_httpx.py
# VERSION:     0.1.7
# CREATED:     2024-03-27 20:58
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
def test_httpx_client_post_create_endpoint() -> None:
  client: Client = Client()
  for i in range(RUNS):
    body: dict = {"hello": "world", "count": i}
    response: Response = client.post(f"{ TEST_ENDPOINT }/create", json=dumps(body))
    assert response.json() == {"created": body}
