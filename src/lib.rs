// SPDX-License-Identifier: MIT

use pyo3::exceptions::PyException;
use pyo3::types::PyModule;
use pyo3::{create_exception, pyfunction, pymodule, wrap_pyfunction, PyResult, Python};
use reqwest::blocking::get as r_get;
use std::collections::HashMap;
use std::str::FromStr;
static APP_USER_AGENT: &str = concat!(env!("CARGO_PKG_NAME"), "/", env!("CARGO_PKG_VERSION"),);

mod client;
mod dictionary;
mod json_value;
mod response;
use response::Response;

create_exception!(reqwest, HTTPError, PyException);

#[pyfunction]
fn get(url: &str) -> PyResult<Response> {
    let response = r_get(url).unwrap();
    Ok(Response {
        status: response.status().as_u16(),
        headers: response
            .headers()
            .into_iter()
            .map(|item| {
                (
                    item.0.to_string(),
                    String::from_str(item.1.to_str().unwrap()).unwrap(),
                )
            })
            .collect::<HashMap<String, String>>(),
        body: response.text().unwrap(),
        reason: "lol".to_string(), // TODO: give me a reason
    })
}

#[pymodule]
fn alcedo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get, m)?)?;
    m.add_class::<client::Client>()?;
    m.add_class::<Response>()?;
    Ok(())
}
