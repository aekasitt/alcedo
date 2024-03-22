# Alcedo

[![Package vesion](https://img.shields.io/pypi/v/alcedo)](https://pypi.org/project/alcedo)
[![Format](https://img.shields.io/pypi/format/alcedo)](https://pypi.org/project/alcedo)
[![Python version](https://img.shields.io/pypi/pyversions/alcedo)](https://pypi.org/project/alcedo)
[![License](https://img.shields.io/pypi/l/alcedo)](https://pypi.org/project/alcedo)
[![Top](https://img.shields.io/github/languages/top/aekasitt/alcedo)](.)
[![Languages](https://img.shields.io/github/languages/count/aekasitt/alcedo)](.)
[![Size](https://img.shields.io/github/repo-size/aekasitt/alcedo)](.)
[![Last commit](https://img.shields.io/github/last-commit/aekasitt/alcedo/master)](.)

![Alcedo banner](static/alcedo-banner.svg)

This project aims to be the feature-incomplete version of [httpx](https://github.com/encode/httpx)
and written in Rust.

Will this be a drop-in replacement for any of the leading packages like...

* 🐍 aiohttp ?
* 🐍 httpx ?
* 🐍 requests ?

### Probably not.

But it aims to bring to Python the speed and feature-richness of Rust packages
like...

* 🦀 hyper
* 🦀 reqwest
* 🦀 serde

## Getting started

TBD;

## Example usage

```py
print("Hello, World!")
```

## Roadmap

* Write (actual) asynchronous tests for `aiohttp` benchmarks.
* Create asynchronous implementation for `alcedo.Client`.
* Write asynchronous tests.
* Write malformed-json test servers.
* Create implementation where POST body can be attached.
* Create implementation where DELETE requests can be made.
* Write asynchronous tests for `httpx` and `requests`
* Write benchmarks for `httpx.Client` and `requests.Session`

## Contributions

I indent by 2 by the way, are you sure you want to contribute ?

## License

This project is licensed under the terms of the MIT license.
