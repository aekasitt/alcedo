#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/bench_aiohttp.py
# VERSION: 	   0.1.0
# CREATED: 	   2024-03-21 16:58
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from aiohttp import ClientSession
from pytest import mark

### Local modules ###
from tests import *


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_get_json_endpoint() -> None:
  for _ in range(1_000):
    async with ClientSession() as session:
      async with session.get(f"{ TEST_ENDPOINT }/json") as response:
        assert await response.json() == {"detail": "OK", "status": 200}


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_get_orjson_endpoint() -> None:
  for _ in range(1_000):
    async with ClientSession() as session:
      async with session.get(f"{ TEST_ENDPOINT }/orjson") as response:
        assert await response.json() == {"detail": "OK", "status": 200}


@mark.aiohttp
@mark.asyncio
async def test_aiohttp_get_plaintext_endpoint() -> None:
  for _ in range(1_000):
    async with ClientSession() as session:
      async with session.get(f"{ TEST_ENDPOINT }/plaintext") as response:
        assert await response.text() == "OK"
