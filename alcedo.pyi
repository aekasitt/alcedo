#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/alcedo.pyi
# VERSION: 	   0.1.4
# CREATED: 	   2024-03-21 00:20
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from typing import Any, Optional

class Client:
  def __init__(self, headers: Optional[dict] = None, **kwargs: Any) -> None: ...
  def get(self, url: str, headers: Optional[dict] = None, **kwargs: Any) -> Response: ...
  def request(
    self, method: str, url: str, headers: Optional[dict] = None, **kwargs: Any
  ) -> Response: ...

class Response:
  def __init__(self, **kwargs: Any) -> None: ...
  def json(self) -> dict: ...
  def text(self) -> str: ...
  def raise_for_status(self) -> None: ...
  def status(self) -> int: ...
  def headers(self) -> dict: ...

def get(url: str, **kwargs: Any) -> Response: ...
