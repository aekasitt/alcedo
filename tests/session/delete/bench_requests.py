#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/delete/bench_requests.py
# VERSION:     0.1.7
# CREATED:     2024-03-28 14:24
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
def test_requests_session_client_delete_endpoint() -> None:
  session: Session = Session()
  for _ in range(RUNS):
    response: Response = session.delete(f"{ TEST_ENDPOINT }/delete")
    assert response.status_code == 204
    assert response.content == b""
