#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/bench.py
# VERSION: 	   0.1.0
# CREATED: 	   2024-03-21 13:31
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Response, get
from tests import *


def test_alcedo_get_json_endpoint() -> None:
  for _ in range(1_000):
    response: Response = get(f"{ TEST_ENDPOINT }/json")
    assert response.json() == {"detail": "OK", "status": 200}


def test_alcedo_get_orjson_endpoint() -> None:
  for _ in range(1_000):
    response: Response = get(f"{ TEST_ENDPOINT }/orjson")
    assert response.json() == {"detail": "OK", "status": 200}


def test_alcedo_get_plaintext_endpoint() -> None:
  for _ in range(1_000):
    response: Response = get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text() == "OK"
