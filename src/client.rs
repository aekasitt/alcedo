// SPDX-License-Identifier: MIT

use crate::{response::Response, APP_USER_AGENT};
use pyo3::prelude::{pyclass, pymethods, PyResult};
use reqwest::blocking::Client as BlockingClient;
use reqwest::header::{HeaderMap, HeaderName, HeaderValue};
use reqwest::Method;

use std::{collections::HashMap, str::FromStr};

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

    fn request(
        &self,
        method: &str,
        url: &str,
        headers: Option<HashMap<String, String>>,
    ) -> Response {
        let _client = self
            .blocking_client
            .request(Method::from_bytes(method.as_bytes()).unwrap(), url)
            .headers(dict_to_headers(headers.unwrap_or(HashMap::new())))
            .send()
            .unwrap();
        let mut h: HashMap<String, String> = HashMap::with_capacity(_client.headers().len());
        for (key, value) in _client.headers().iter() {
            h.insert(key.to_string(), value.to_str().unwrap().to_string());
        }
        let status = _client.status();
        Response {
            status: status.as_u16(),
            headers: h,
            body: _client.text().unwrap(),
            reason: status.canonical_reason().unwrap().to_string(),
        }
    }

    fn get(&self, url: &str, headers: Option<HashMap<String, String>>) -> PyResult<Response> {
        Ok(self.request("GET", url, headers))
    }
}
