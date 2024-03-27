// SPDX-License-Identifier: MIT

use crate::{dictionary::Dictionary, response::Response, APP_USER_AGENT};
use pyo3::{pyclass, pymethods, PyObject, PyResult, Python};
use reqwest::blocking::{Client as BlockingClient, RequestBuilder};
use reqwest::header::{HeaderMap, HeaderName, HeaderValue};
use reqwest::Method;
use serde_json::{json, to_string};
use std::collections::HashMap;
use std::str::FromStr;

fn dict_to_headers(dict: HashMap<String, String>) -> HeaderMap {
    let mut headers = HeaderMap::with_capacity(dict.len());
    for (key, value) in dict {
        headers.insert(
            HeaderName::from_str(&key).unwrap(),
            HeaderValue::from_str(&value).unwrap(),
        );
    }
    headers
}

#[pyclass]
pub struct Client {
    blocking_client: BlockingClient,
}

#[pymethods]
impl Client {
    #[new]
    fn new(h: Option<HashMap<String, String>>) -> Self {
        let headers = h.unwrap_or(HashMap::new());
        let hmap = dict_to_headers(headers);
        Self {
            blocking_client: BlockingClient::builder()
                .default_headers(hmap)
                .user_agent(APP_USER_AGENT)
                .build()
                .unwrap(),
        }
    }

    fn get(&self, url: &str, headers: Option<HashMap<String, String>>) -> PyResult<Response> {
        Ok(self.request("GET", url, headers, None))
    }

    fn post(
        &self,
        url: &str,
        headers: Option<HashMap<String, String>>,
        payload: Option<PyObject>,
    ) -> PyResult<Response> {
        Ok(self.request("POST", url, headers, payload))
    }

    fn request(
        &self,
        method: &str,
        url: &str,
        headers: Option<HashMap<String, String>>,
        payload: Option<PyObject>,
    ) -> Response {
        let builder = self
            .blocking_client
            .request(Method::from_bytes(method.as_bytes()).unwrap(), url)
            .headers(dict_to_headers(headers.unwrap_or(HashMap::new())));
        let req: Result<RequestBuilder, RequestBuilder> = match payload {
            None => Ok(builder),
            Some(value) => Python::with_gil(|py| {
                let d = Dictionary {
                    py,
                    obj: value.extract(py).unwrap(),
                };
                // let body = to_string(&d).map_err(ser::Error::custom);
                let body = to_string(&d).unwrap();
                Ok(builder
                    .header("Content-Type", "application/json")
                    .json(&json!(body)))
            }),
        };
        let response = req.unwrap().send().unwrap();
        let mut h: HashMap<String, String> = HashMap::with_capacity(response.headers().len());
        for (key, value) in response.headers().iter() {
            h.insert(key.to_string(), value.to_str().unwrap().to_string());
        }
        let status = response.status();
        Response {
            status: status.as_u16(),
            headers: h,
            body: response.text().unwrap(),
            reason: status.canonical_reason().unwrap().to_string(),
        }
    }
}
