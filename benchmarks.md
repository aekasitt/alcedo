# Benchmarks

These benchmarks are run on Macbook Pro (Apple M1 Pro) 2022

### Python 3.9

```sh
0.90s call     tests/get/bench.py::test_alcedo_get_json_endpoint
0.87s call     tests/get/bench.py::test_alcedo_get_orjson_endpoint
0.86s call     tests/get/bench.py::test_alcedo_get_plaintext_endpoint
0.68s call     tests/session/delete/bench.py::test_alcedo_client_delete_endpoint
0.38s call     tests/session/post/bench.py::test_alcedo_client_post_create
0.37s call     tests/session/put/bench.py::test_alcedo_client_put_update_endpoint
0.35s call     tests/session/get/bench.py::test_alcedo_client_get_json_endpoint
0.34s call     tests/session/get/bench.py::test_alcedo_client_get_orjson_endpoint
0.33s call     tests/session/get/bench.py::test_alcedo_client_get_plaintext_endpoint
```

### PyPy 3.10

```sh
1.59s call     tests/get/bench.py::test_alcedo_get_json_endpoint
1.24s call     tests/get/bench.py::test_alcedo_get_plaintext_endpoint
0.56s call     tests/session/post/bench.py::test_alcedo_client_post_create
0.47s call     tests/session/delete/bench.py::test_alcedo_client_delete_endpoint
0.46s call     tests/session/put/bench.py::test_alcedo_client_put_update_endpoint
0.46s call     tests/session/get/bench.py::test_alcedo_client_get_json_endpoint
0.40s call     tests/session/get/bench.py::test_alcedo_client_get_plaintext_endpoint
```

### Python 3.12

```sh
0.85s call     tests/get/bench.py::test_alcedo_get_json_endpoint
0.82s call     tests/get/bench.py::test_alcedo_get_plaintext_endpoint
0.79s call     tests/get/bench.py::test_alcedo_get_orjson_endpoint
0.32s call     tests/session/put/bench.py::test_alcedo_client_put_update_endpoint
0.32s call     tests/session/post/bench.py::test_alcedo_client_post_create
0.26s call     tests/session/get/bench.py::test_alcedo_client_get_json_endpoint
0.24s call     tests/session/get/bench.py::test_alcedo_client_get_orjson_endpoint
0.23s call     tests/session/get/bench.py::test_alcedo_client_get_plaintext_endpoint
0.22s call     tests/session/delete/bench.py::test_alcedo_client_delete_endpoint
```
