#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/post/bench_aiohttp.py
# VERSION:     0.1.7
# CREATED:     2024-03-25 02:00
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from json import dumps

### Third-party packages ###
from aiohttp.client import ClientSession
from pytest import mark

### Local modules ###
from tests import *


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_client_session_post_create_endpoint() -> None:
  async with ClientSession() as session:
    for i in range(RUNS):
      body: dict = {"hello": "world", "count": i}
      async with session.post(f"{ TEST_ENDPOINT }/create", json=dumps(body)) as response:
        assert await response.json() == {"created": body}
