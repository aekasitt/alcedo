// SPDX-License-Identifier: MIT

use crate::{json_value::JSONValue, HTTPError};
use pyo3::exceptions::PyValueError;
use pyo3::{import_exception, pyclass, pymethods, PyErr, PyObject, PyResult, Python};
use serde::de::DeserializeSeed;
use std::collections::HashMap;

import_exception!(json, JSONDecodeError);
import_exception!(json, JSONEncodeError);

#[pyclass]
pub struct Response {
    pub status: u16,
    pub headers: HashMap<String, String>,
    pub body: String,
    pub reason: String,
}

#[pymethods]
impl Response {
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("<Request status={}>", self.status))
    }

    fn json(&self) -> PyResult<PyObject> {
        let mut deserializer = serde_json::Deserializer::from_str(&self.body);
        Python::with_gil(|py| {
            let seed = JSONValue::new(py);
            match seed.deserialize(&mut deserializer) {
                Ok(py_object) => {
                    deserializer.end().map_err(|e| {
                        JSONDecodeError::new_err((e.to_string(), self.body.clone(), 0))
                    })?;
                    Ok(py_object)
                }
                Err(e) => Err(PyValueError::new_err(format!("Value: {:?}", e))),
            }
        })
    }

    fn headers(&self) -> PyResult<HashMap<String, String>> {
        Ok(self.headers.clone())
    }

    #[new]
    fn new(status: u16, headers: HashMap<String, String>, body: String, reason: String) -> Self {
        Self {
            status,
            headers,
            body,
            reason,
        }
    }

    fn raise_for_status(&self) -> PyResult<Option<PyErr>> {
        if 400 <= self.status && self.status < 600 {
            Err(PyErr::new::<HTTPError, _>(format!(
                "{} {}",
                self.status,
                self.reason.clone()
            )))
        } else {
            Ok(None)
        }
    }

    fn text(&self) -> PyResult<String> {
        Ok(self.body.clone())
    }
}
