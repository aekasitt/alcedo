#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/queried_get/bench_requests.py
# VERSION:     0.1.7
# CREATED:     2024-04-01 08:07
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from requests import Response, Session
from pytest import mark

### Local modules ###
from tests import *


@mark.requests
def test_requests_session_get_json_endpoint() -> None:
  session: Session = Session()
  for i in range(RUNS):
    response: Response = session.get(f"{ TEST_ENDPOINT }/json", params={"foo": "bar", "index": i})
    assert response.json() == {
      "detail": "OK",
      "float": 1.234,
      "integer": 200,
      "null": None,
      "query": {"foo": ["bar"], "index": [f"{ i }"]},
    }


@mark.requests
def test_requests_session_get_orjson_endpoint() -> None:
  session: Session = Session()
  for i in range(RUNS):
    response: Response = session.get(f"{ TEST_ENDPOINT }/orjson", params={"foo": "bar", "index": i})
    assert response.json() == {
      "detail": "OK",
      "float": 1.234,
      "integer": 200,
      "null": None,
      "query": {"foo": ["bar"], "index": [f"{ i }"]},
    }


@mark.requests
def test_requests_session_get_plaintext_endpoint() -> None:
  session: Session = Session()
  for _ in range(RUNS):
    response: Response = session.get(f"{ TEST_ENDPOINT }/plaintext")
    assert response.text == "OK"
