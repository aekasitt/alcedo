# Alcedo

[![Package vesion](https://img.shields.io/pypi/v/alcedo)](https://pypi.org/project/alcedo)
[![Format](https://img.shields.io/pypi/format/alcedo)](https://pypi.org/project/alcedo)
[![Python version](https://img.shields.io/pypi/pyversions/alcedo)](https://pypi.org/project/alcedo)
[![License](https://img.shields.io/pypi/l/alcedo)](https://pypi.org/project/alcedo)
[![Top](https://img.shields.io/github/languages/top/aekasitt/alcedo)](.)
[![Languages](https://img.shields.io/github/languages/count/aekasitt/alcedo)](.)
[![Size](https://img.shields.io/github/repo-size/aekasitt/alcedo)](.)
[![Last commit](https://img.shields.io/github/last-commit/aekasitt/alcedo/master)](.)

![Alcedo banner](https://github.com/aekasitt/alcedo/blob/master/static/alcedo-banner.svg)

This project aims to be the feature-incomplete version of [httpx](https://github.com/encode/httpx)
and written in Rust.

Will this be a drop-in replacement for any of the leading packages like...

- 🐍 __aiohttp__ ?
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/aio-libs/aiohttp)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/aiohttp)
  [![Docs](https://img.shields.io/readthedocs/aiohttp?logo=readthedocs)](https://docs.aiohttp.org/en/stable/)
- 🐍 __httpx__ ?
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/encode/httpx)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/httpx)
  [![Docs](https://img.shields.io/badge/MkDocs-526CFE?logo=materialformkdocs&logoColor=white)](https://www.python-httpx.org/)
- 🐍 __requests__ ?
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/psf/requests)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/requests)
  [![Docs](https://img.shields.io/readthedocs/requests?logo=readthedocs)](https://requests.readthedocs.io/en/latest/)

### Probably not.

But it aims to bring to Python the speed and feature-richness of Rust packages
like...

- 🦀 **hyper**
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/hyperium/hyper)
  [![Crates](https://img.shields.io/badge/hyper%20%F0%9F%93%A6-264323)](https://crates.io/crates/hyper)
  [![Docs](https://img.shields.io/badge/Docs--rs-353535?logo=docs.rs)](https://docs.rs/hyper/latest/hyper/)
- 🦀 **reqwest**
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/seanmonstar/reqwest)
  [![Crates](https://img.shields.io/badge/reqwest%20%F0%9F%93%A6-264323)](https://crates.io/crates/reqwest)
  [![Docs](https://img.shields.io/badge/Docs--rs-353535?logo=docs.rs)](https://docs.rs/reqwest/latest/reqwest/)
- 🦀 **serde**
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/serde-rs/serde)
  [![Crates](https://img.shields.io/badge/serde%20%F0%9F%93%A6-264323)](https://crates.io/creates/serde)
  [![Docs](https://img.shields.io/badge/Docs--rs-353535?logo=docs.rs)](https://docs.rs/serde/latest/serde/)

## Getting started

TBD;

## Example usage

```py
print("Hello, World!")
```

## Roadmap

- Write (actual) asynchronous tests for `aiohttp` benchmarks.
- Create asynchronous implementation for `alcedo.Client`.
- Write asynchronous tests.
- Write malformed-json test servers.
- Create implementation where POST body can be attached.
- Create implementation where DELETE requests can be made.
- Write asynchronous tests for `httpx` and `requests`
- Write benchmarks for `httpx.Client` and `requests.Session`

## Contributions

To contribute to the project, fork the repository and clone to your local device and development
dependencies including four extra libraries not included in final builds as such:

- **maturin** Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/PyO3/maturin)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/maturin)
- **mypy** Optional static typing for Python
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/python/mypy)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/mypy)
  [![Docs](https://img.shields.io/readthedocs/mypy?logo=readthedocs)](https://mypy.readthedocs.io/en/stable/) 
- **pytest** The pytest framework makes it easy to write small tests, yet scales to support complex functional testing
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/pytest-dev/pytest)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/pytest)
  [![Docs](https://img.shields.io/badge/Sphinx-0A507A?logo=sphinx)](https://docs.pytest.org/en/latest)
- **ruff** An extremely fast Python linter and code formatter, written in Rust.
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/astral-sh/ruff)
  [![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/ruff)
  [![Docs](https://img.shields.io/badge/MkDocs-526CFE?logo=materialformkdocs&logoColor=white)](https://docs.astral.sh/ruff) 

Use the following commands to setup your local environment with development dependencies:

```bash
pip install --user poetry
poetry install --with dev
```

## License

This project is licensed under the terms of the MIT license.
