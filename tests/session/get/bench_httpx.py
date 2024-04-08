#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/get/bench_httpx.py
# VERSION:     0.1.7
# CREATED:     2024-03-25 02:00
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from httpx import Client, Response
from pytest import mark

### Local modules ###
from tests import *


@mark.httpx
def test_httpx_client_get_json_endpoint() -> None:
  client: Client = Client()
  for _ in range(RUNS):
    response: Response = client.get(f"{ TEST_ENDPOINT }/json")
    assert response.json() == {"detail": "OK", "float": 1.234, "integer": 200, "null": None}


@mark.httpx
def test_httpx_client_get_orjson_endpoint() -> None:
  client: Client = Client()
  for _ in range(RUNS):
    response: Response = client.get(f"{ TEST_ENDPOINT }/orjson")
    assert response.json() == {"detail": "OK", "float": 1.234, "integer": 200, "null": None}


@mark.httpx
def test_httpx_client_get_plaintext_endpoint() -> None:
  client: Client = Client()
  for _ in range(RUNS):
    response: Response = client.get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text == "OK"
