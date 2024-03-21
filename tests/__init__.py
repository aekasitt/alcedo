#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/__init__.py
# VERSION: 	   0.1.0
# CREATED: 	   2024-03-21 13:31
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from multiprocessing import Process
from time import sleep
from typing import Generator

### Third-party packages ###
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pytest import fixture
from uvicorn import run

def run_test_server() -> None:
    app: FastAPI = FastAPI(openapi_url=False)
    @app.get("/", response_class=PlainTextResponse)
    async def generic_test_endpoint() -> str:
        return "OK"
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
    sleep(5e-1)  # setup-delay
    yield
    process.terminate()


__all__ = ["setup_teardown_api_server"]
