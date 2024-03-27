#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/get/bench.py
# VERSION: 	   0.1.4
# CREATED: 	   2024-03-25 02:00
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Client, Response
from tests import *


def test_alcedo_client_get_json_endpoint() -> None:
  client: Client = Client()
  for _ in range(1_000):
    response: Response = client.get(f"{ TEST_ENDPOINT }/json")
    assert response.json() == {"detail": "OK", "status": 200}


def test_alcedo_client_get_orjson_endpoint() -> None:
  client: Client = Client()
  for _ in range(1_000):
    response: Response = client.get(f"{ TEST_ENDPOINT }/orjson")
    assert response.json() == {"detail": "OK", "status": 200}


def test_alcedo_client_get_plaintext_endpoint() -> None:
  client: Client = Client()
  for _ in range(1_000):
    response: Response = client.get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text() == "OK"
