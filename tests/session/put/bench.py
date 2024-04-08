#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/put/bench.py
# VERSION:     0.1.7
# CREATED:     2024-03-28 14:18
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Client, Response
from tests import *


def test_alcedo_client_put_update_endpoint() -> None:
  client: Client = Client()
  for i in range(RUNS):
    body: dict = {"hello": "world", "count": i + 1}
    response: Response = client.put(f"{ TEST_ENDPOINT }/update", payload=body)
    assert response.json() == {"updated": body}
