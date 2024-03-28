# Alcedo

[![Package vesion](https://img.shields.io/pypi/v/alcedo)](https://pypi.org/project/alcedo)
[![Format](https://img.shields.io/pypi/format/alcedo)](https://pypi.org/project/alcedo)
[![Python version](https://img.shields.io/pypi/pyversions/alcedo)](https://pypi.org/project/alcedo)
[![License](https://img.shields.io/pypi/l/alcedo)](https://pypi.org/project/alcedo)
[![Code size](https://img.shields.io/github/languages/code-size/aekasitt/alcedo)](.)
[![Top](https://img.shields.io/github/languages/top/aekasitt/alcedo)](.)
[![Languages](https://img.shields.io/github/languages/count/aekasitt/alcedo)](.)
[![Repository size](https://img.shields.io/github/repo-size/aekasitt/alcedo)](.)
[![Last commit](https://img.shields.io/github/last-commit/aekasitt/alcedo/master)](.)

![Alcedo banner](https://github.com/aekasitt/alcedo/blob/master/static/alcedo-banner.svg)

This project aims to be the feature-incomplete version of [httpx](https://github.com/encode/httpx)
and written in Rust.

Will this be a drop-in replacement for any of the leading packages like...

- 🐍 _aiohttp_ ?
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/aio-libs/aiohttp)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20aiohttp-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/aiohttp)
  [![Docs](https://img.shields.io/readthedocs/aiohttp?logo=readthedocs)](https://docs.aiohttp.org/en/stable/)
- 🐍 _httpx_ ?
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/encode/httpx)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20httpx-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/httpx)
  [![Docs](https://img.shields.io/badge/MkDocs-526CFE?logo=materialformkdocs&logoColor=white)](https://www.python-httpx.org/)
- 🐍 _requests_ ?
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/psf/requests)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20requests-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/requests)
  [![Docs](https://img.shields.io/readthedocs/requests?logo=readthedocs)](https://requests.readthedocs.io/en/latest/)

### Probably not.

But it aims to bring to Python the speed and feature-richness of Rust packages
like...

- 🦀 **hyper**
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/hyperium/hyper)
  [![Crates](https://img.shields.io/badge/-%F0%9F%93%A6%20Crates:%20hyper-264323)](https://crates.io/crates/hyper)
  [![Docs](https://img.shields.io/badge/Docs--rs-353535?logo=docs.rs)](https://docs.rs/hyper/latest/hyper/)
- 🦀 **reqwest**
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/seanmonstar/reqwest)
  [![Crates](https://img.shields.io/badge/-%F0%9F%93%A6%20Crates:%20reqwest-264323)](https://crates.io/crates/reqwest)
  [![Docs](https://img.shields.io/badge/Docs--rs-353535?logo=docs.rs)](https://docs.rs/reqwest/latest/reqwest/)
- 🦀 **serde**
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/serde-rs/serde)
  [![Crates](https://img.shields.io/badge/-%F0%9F%93%A6%20Crates:%20serde-264323)](https://crates.io/creates/serde)
  [![Docs](https://img.shields.io/badge/Docs--rs-353535?logo=docs.rs)](https://docs.rs/serde/latest/serde/)

## Getting started

TBD;

## Example usage

```py
print("Hello, World!")
```

## Do you even bench bro?

[Benchmarks](./benchmarks.md)

## Roadmap

- Write (actual) asynchronous tests for `aiohttp` benchmarks.
- Create asynchronous implementation for `alcedo.Client`.
- Write asynchronous tests.
- Write malformed-json test servers.
- Create implementation where POST body can be attached.
- Create implementation where DELETE requests can be made.
- Write asynchronous tests for `httpx` and `requests`

## Contributions

To contribute to the project, fork the repository and clone to your local device and development
dependencies including four extra libraries not included in final builds as such:

- **maturin** Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/PyO3/maturin)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20maturin-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/maturin)
  [![Docs](https://img.shields.io/badge/user-guide-brightgreen?logo=readthedocs)](https://maturin.rs)
- **mypy** Optional static typing for Python
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/python/mypy)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20mypy-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/mypy)
  [![Docs](https://img.shields.io/readthedocs/mypy?logo=readthedocs)](https://mypy.readthedocs.io/en/stable/) 
- **pytest** The pytest framework makes it easy to write small tests, yet scales to support complex functional testing
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/pytest-dev/pytest)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20pytest-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/pytest)
  [![Docs](https://img.shields.io/badge/Sphinx-0A507A?logo=sphinx)](https://docs.pytest.org/en/latest)
- **ruff** An extremely fast Python linter and code formatter, written in Rust.
  [![GitHub](https://img.shields.io/badge/GitHub-2B3137?logo=github&logoColor=white)](https://github.com/astral-sh/ruff)
  [![PyPI](https://img.shields.io/badge/-PyPI:%20ruff-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/ruff)
  [![Docs](https://img.shields.io/badge/MkDocs-526CFE?logo=materialformkdocs&logoColor=white)](https://docs.astral.sh/ruff) 

Use the following commands to setup your local environment with development dependencies:

```bash
pip install --user poetry
poetry install --with dev
```

## Acknowledgements

* [reqwest.py](https://github.com/thrzl/reqwest.py) by the amazing
  [@thrzl](https://github.com/thrzl) giving the easiest primer to oxidizing python interface.
* [hyperjson](https://github.com/mre/hyperjson) by the amazing
  [@mre](https://github.com/mre) even though has been archived since Sep 14, 2023 but really makes
  JSON deserialization from Rust -> Python really approachable compared to alternatives.
* [Kingfisher 2017042438](https://freesvg.org/kingfisher-2017042438) under
  [CC0 1.0 Public Domain Protection](https://creativecommons.org/publicdomain/) whoever made this 
  is an artist du juor.

## License

This project is licensed under the terms of the MIT license.
