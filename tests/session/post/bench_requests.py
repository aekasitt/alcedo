#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/post/bench_requests.py
# VERSION:     0.1.7
# CREATED:     2024-03-27 19:25
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from json import dumps

### Third-party packages ###
from requests import Response, Session
from pytest import mark

### Local modules ###
from tests import *


@mark.requests
def test_requests_session_client_post_endpoint() -> None:
  session: Session = Session()
  for i in range(RUNS):
    body: dict = {"hello": "world", "count": i}
    response: Response = session.post(f"{ TEST_ENDPOINT }/create", json=dumps(body))
    assert response.json() == {"created": body}
