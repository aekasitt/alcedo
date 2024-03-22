// SPDX-License-Identifier: MIT

use crate::HTTPError;

use pyo3::exceptions::PyValueError;
use pyo3::{import_exception, pyclass, pymethods, IntoPy, PyErr, PyObject, PyResult, Python};
use serde::de::{self, DeserializeSeed, Deserializer, MapAccess, SeqAccess, Visitor};
use std::collections::{BTreeMap, HashMap};
use std::fmt::{self, Formatter};
use std::marker::PhantomData;

import_exception!(json, JSONDecodeError);

#[pyclass]
pub struct Response {
    pub status: u16,
    pub headers: HashMap<String, String>,
    pub body: String,
    pub reason: String,
}

#[derive(Copy, Clone)]
pub struct JSONValue<'a> {
    py: Python<'a>,
}

impl<'a> JSONValue<'a> {
    pub fn new(py: Python<'a>) -> JSONValue<'a> {
        JSONValue { py }
    }
}

impl<'de, 'a> DeserializeSeed<'de> for JSONValue<'a> {
    type Value = PyObject;
    fn deserialize<D>(self, deserializer: D) -> Result<Self::Value, D::Error>
    where
        D: Deserializer<'de>,
    {
        deserializer.deserialize_any(self)
    }
}

impl<'de, 'a> Visitor<'de> for JSONValue<'a> {
    type Value = PyObject;

    fn expecting(&self, formatter: &mut Formatter) -> fmt::Result {
        formatter.write_str("any valid JSON value")
    }

    fn visit_bool<E>(self, value: bool) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(value.into_py(self.py))
    }

    fn visit_i64<E>(self, value: i64) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(value.into_py(self.py))
    }

    fn visit_u64<E>(self, value: u64) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(value.into_py(self.py))
    }

    fn visit_f64<E>(self, value: f64) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(value.into_py(self.py))
    }

    fn visit_str<E>(self, value: &str) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(value.into_py(self.py))
    }

    fn visit_unit<E>(self) -> Result<Self::Value, E> {
        Ok(self.py.None())
    }

    fn visit_seq<A>(self, mut seq: A) -> Result<Self::Value, A::Error>
    where
        A: SeqAccess<'de>,
    {
        let mut elements = Vec::new();
        while let Some(elem) = seq.next_element_seed(self)? {
            elements.push(elem);
        }
        Ok(elements.into_py(self.py))
    }

    fn visit_map<A>(self, mut map: A) -> Result<Self::Value, A::Error>
    where
        A: MapAccess<'de>,
    {
        let mut entries = BTreeMap::new();
        while let Some((key, value)) = map.next_entry_seed(PhantomData::<String>, self)? {
            entries.insert(key, value);
        }
        Ok(entries.into_py(self.py))
    }
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
