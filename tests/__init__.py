#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/__init__.py
# VERSION:     0.1.7
# CREATED:     2024-03-21 13:31
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION: https://www.w3docs.com/snippets/python/what-is-init-py-for.html
#
# HISTORY:
# *************************************************************
"""Module indicating that `~~/tests` directory is present in is a Python package."""

### Standard packages ###
from json import loads
from multiprocessing import Process
from urllib.parse import parse_qs
from time import sleep
from typing import Generator

### Third-party packages ###
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse, PlainTextResponse, ORJSONResponse
from pytest import fixture
from uvicorn import run

RUNS: int = 1_000
TEST_HOST: str = "localhost"
TEST_PORT: int = 6969
TEST_ENDPOINT: str = f"http://{ TEST_HOST }:{ TEST_PORT }"


def run_test_server() -> None:
  app: FastAPI = FastAPI()

  @app.get("/plaintext", response_class=PlainTextResponse)
  async def plaintext_endpoint() -> str:
    return "OK"

  @app.get("/json", response_class=JSONResponse)
  async def json_endpoint(request: Request) -> dict:
    response = {
      "detail": "OK",
      "float": 1.234,
      "integer": 200,
      "null": None,
    }
    if len(request.query_params) > 0:
      response["query"] = parse_qs(str(request.query_params))
    return response

  @app.get("/orjson", response_class=ORJSONResponse)
  async def orjson_endpoint(request: Request) -> dict:
    response = {
      "detail": "OK",
      "float": 1.234,
      "integer": 200,
      "null": None,
    }
    if len(request.query_params) > 0:
      response["query"] = parse_qs(str(request.query_params))
    return response

  @app.post("/create", response_class=JSONResponse, status_code=201)
  async def create_post(request: Request) -> dict:
    return {"created": loads(await request.json())}

  @app.put("/update", response_class=JSONResponse)
  async def update_post(request: Request) -> dict:
    return {"updated": loads(await request.json())}

  @app.delete("/delete", response_class=PlainTextResponse, status_code=204)
  async def delete_post() -> None: ...

  run(app, host="localhost", port=6969)


@fixture(scope="session", autouse=True)
def setup_teardown_api_server() -> Generator:
  """
  Sets up a FastAPI server with a generic get-endpoint

  ---
  :returns: Generator
  """
  process: Process = Process(daemon=True, target=run_test_server)
  process.start()
  sleep(0.5)  # setup-delay
  yield
  process.terminate()


__all__ = ("RUNS", "TEST_ENDPOINT", "setup_teardown_api_server")
