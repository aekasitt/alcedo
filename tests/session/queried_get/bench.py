#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/queried_get/bench.py
# VERSION:     0.1.7
# CREATED:     2024-04-01 08:07
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Client, Response
from tests import *


def test_alcedo_client_get_json_endpoint() -> None:
  client: Client = Client()
  for i in range(RUNS):
    response: Response = client.get(f"{ TEST_ENDPOINT }/json", query={"foo": "bar", "index": i})
    assert response.json() == {
      "detail": "OK",
      "float": 1.234,
      "integer": 200,
      "null": None,
      "query": {"foo": ["bar"], "index": [f"{ i }"]},
    }


def test_alcedo_client_get_orjson_endpoint() -> None:
  client: Client = Client()
  for i in range(RUNS):
    response: Response = client.get(f"{ TEST_ENDPOINT }/orjson", query={"foo": "bar", "index": i})
    assert response.json() == {
      "detail": "OK",
      "float": 1.234,
      "integer": 200,
      "null": None,
      "query": {"foo": ["bar"], "index": [f"{ i }"]},
    }


def test_alcedo_client_get_plaintext_endpoint() -> None:
  client: Client = Client()
  for _ in range(RUNS):
    response: Response = client.get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text() == "OK"
