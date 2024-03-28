#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/get/bench_httpx.py
# VERSION:     0.1.5
# CREATED:     2024-03-21 13:31
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from httpx import Response, get
from pytest import mark

### Local modules ###
from tests import *


@mark.httpx
def test_httpx_get_json_endpoint() -> None:
  for _ in range(1_000):
    response: Response = get(f"{ TEST_ENDPOINT }/json")
    assert response.json() == {"detail": "OK", "float": 1.234, "integer": 200, "null": None}


@mark.httpx
def test_httpx_get_orjson_endpoint() -> None:
  for _ in range(1_000):
    response: Response = get(f"{ TEST_ENDPOINT }/orjson")
    assert response.json() == {"detail": "OK", "float": 1.234, "integer": 200, "null": None}


@mark.httpx
def test_httpx_get_plaintext_endpoint() -> None:
  for _ in range(1_000):
    response: Response = get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text == "OK"
