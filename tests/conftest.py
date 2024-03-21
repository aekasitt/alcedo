#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2024 All rights reserved.
# FILENAME:    ~~/tests/conftest.py
# VERSION: 	   0.1.0
# CREATED: 	   2024-03-21 16:42
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from typing import List

### Third-party packages ###
from pytest import Config, Item, Parser, mark


def pytest_addoption(parser: Parser) -> None:
  """Add option to Pytest CLI parser

  ---
  :param Parser parser: pytest Parser instance passed when running via pytest cli
  """
  parser.addoption(
    "--bench-against-httpx",
    action="store_true",
    default=False,
    help="Include httpx when running benchmarks",
  )


def pytest_collection_modifyitems(config: Config, items: List[Item]) -> None:
  for item in items:
    if "httpx" in item.keywords and not config.getoption("--bench-against-httpx"):
      item.add_marker(
        mark.skip(reason="Test excluded without flag; Add --bench-against-httpx flag to run test.")
      )


__all__ = ["pytest_addoption", "pytest_collection_modifyitems"]
