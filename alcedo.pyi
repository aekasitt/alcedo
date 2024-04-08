#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/alcedo.pyi
# VERSION:     0.1.7
# CREATED:     2024-03-21 00:20
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from typing import Optional, Union

class Client:
  def __init__(
    self, headers: Optional[dict] = None, **kwargs: Union[bool, bytes, float, int, str]
  ) -> None: ...
  def delete(
    self, url: str, headers: Optional[dict] = None, payload: dict = {}, query: Optional[dict] = None
  ) -> Response: ...
  def get(
    self, url: str, headers: Optional[dict] = None, query: Optional[dict] = None
  ) -> Response: ...
  def post(
    self, url: str, headers: Optional[dict] = None, payload: dict = {}, query: Optional[dict] = None
  ) -> Response: ...
  def put(
    self, url: str, headers: Optional[dict] = None, payload: dict = {}, query: Optional[dict] = None
  ) -> Response: ...
  def request(
    self, method: str, url: str, headers: Optional[dict] = None, query: Optional[dict] = None
  ) -> Response: ...

class Response:
  def __init__(self, **kwargs: Union[bool, bytes, float, int, str]) -> None: ...
  def json(self) -> dict: ...
  def text(self) -> str: ...
  def raise_for_status(self) -> None: ...
  def status(self) -> int: ...
  def headers(self) -> dict: ...

def get(url: str, **kwargs: Any) -> Response: ...
