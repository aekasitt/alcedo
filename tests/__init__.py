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
from asyncio import run, sleep
from threading import Thread
from typing import Generator

### Third-party packages ###
from fastapi import FastAPI
from pytest import fixture
from uvicorn import Config, Server


class TestServer:
    def __init__(self, config: Config):
        self.server = Server(config)
        self.thread = Thread(daemon=True, target=self.server.run)

    def start(self):
        self.thread.start()
        run(self.wait_for_started())

    async def wait_for_started(self):
        while not self.server.started:
            await sleep(1e-3)

    def stop(self):
        if self.thread.is_alive():
            self.server.should_exit = True
            while self.thread.is_alive():
                continue


@fixture(scope="session", autouse=True)
def setup_teardown_api_server() -> Generator:
    """
    Sets up a FastAPI server with a

    ---
    :returns: TestClient
    """
    print("setup")
    app: FastAPI = FastAPI()

    @app.get("/")
    async def generic_endpoint() -> str:
        return "OK"

    server: TestServer = TestServer(Config(app, host='localhost', port=6969))
    server.start()

    yield

    server.stop()
    print("teardown")


__all__ = ["setup_teardown_api_server"]
