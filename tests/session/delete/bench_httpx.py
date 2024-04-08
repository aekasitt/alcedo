#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/delete/bench_httpx.py
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
from httpx import Client, Response
from pytest import mark

### Local modules ###
from tests import *


@mark.httpx
def test_httpx_client_delete_endpoint() -> None:
  client: Client = Client()
  for _ in range(RUNS):
    response: Response = client.delete(f"{ TEST_ENDPOINT }/delete")
    assert response.status_code == 204
    assert response.content == b""
