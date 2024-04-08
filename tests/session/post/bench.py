#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/post/bench.py
# VERSION:     0.1.7
# CREATED:     2024-03-27 16:29
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Client, Response
from tests import *


def test_alcedo_client_post_create() -> None:
  client: Client = Client()
  for i in range(RUNS):
    body: dict = {"hello": "world", "count": i + 1}
    response: Response = client.post(f"{ TEST_ENDPOINT }/create", payload=body)
    assert response.json() == {"created": body}
