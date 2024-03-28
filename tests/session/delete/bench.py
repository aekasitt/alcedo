#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/delete/bench.py
# VERSION:     0.1.5
# CREATED:     2024-03-28 14:24
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Local modules ###
from alcedo import Client, Response
from tests import *


def test_alcedo_client_delete_endpoint() -> None:
  client: Client = Client()
  for _ in range(1_000):
    response: Response = client.delete(f"{ TEST_ENDPOINT }/delete")
    # assert response.status == 204
    assert response.text() == ""
