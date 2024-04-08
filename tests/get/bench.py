#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/get/bench.py
# VERSION:     0.1.7
# CREATED:     2024-03-21 13:31
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Response, get
from tests import *


def test_alcedo_get_json_endpoint() -> None:
  for _ in range(RUNS):
    response: Response = get(f"{ TEST_ENDPOINT }/json")
    assert response.json() == {"detail": "OK", "float": 1.234, "integer": 200, "null": None}


def test_alcedo_get_orjson_endpoint() -> None:
  for _ in range(RUNS):
    response: Response = get(f"{ TEST_ENDPOINT }/orjson")
    assert response.json() == {"detail": "OK", "float": 1.234, "integer": 200, "null": None}


def test_alcedo_get_plaintext_endpoint() -> None:
  for _ in range(RUNS):
    response: Response = get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text() == "OK"
