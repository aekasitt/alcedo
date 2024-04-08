#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/session/queried_get/bench_aiohttp.py
# VERSION:     0.1.7
# CREATED:     2024-04-01 08:07
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from aiohttp.client import ClientSession
from pytest import mark

### Local modules ###
from tests import *


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_client_session_get_json_endpoint() -> None:
  async with ClientSession() as session:
    for i in range(RUNS):
      async with session.get(
        f"{ TEST_ENDPOINT }/json", params={"foo": "bar", "index": i}
      ) as response:
        assert await response.json() == {
          "detail": "OK",
          "float": 1.234,
          "integer": 200,
          "null": None,
          "query": {"foo": ["bar"], "index": [f"{ i }"]},
        }


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_client_session_get_orjson_endpoint() -> None:
  async with ClientSession() as session:
    for i in range(RUNS):
      async with session.get(
        f"{ TEST_ENDPOINT }/orjson", params={"foo": "bar", "index": i}
      ) as response:
        assert await response.json() == {
          "detail": "OK",
          "float": 1.234,
          "integer": 200,
          "null": None,
          "query": {"foo": ["bar"], "index": [f"{ i }"]},
        }


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_client_session_get_plaintext_endpoint() -> None:
  async with ClientSession() as session:
    for _ in range(RUNS):
      async with session.get(f"{ TEST_ENDPOINT }/plaintext") as response:
        assert await response.text() == "OK"
