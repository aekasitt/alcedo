// SPDX-License-Identifier: MIT

use pyo3::types::{PyAny, PyDict, PyFloat, PyList, PyTuple};
use pyo3::{FromPyObject, Python};
use serde::ser::{self, Serialize, SerializeMap, SerializeSeq, Serializer};
use std::string::String;

pub struct SerializePyObject<'p, 'a> {
    pub py: Python<'p>,
    pub obj: &'a PyAny,
}

impl<'p, 'a> Serialize for SerializePyObject<'p, 'a> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        macro_rules! cast {
            ($f:expr) => {
                if let Ok(val) = FromPyObject::extract(self.obj) {
                    return $f(val);
                }
            };
        }

        macro_rules! extract {
            ($t:ty) => {
                if let Ok(val) = <$t as FromPyObject>::extract(self.obj) {
                    return val.serialize(serializer);
                }
            };
        }

        cast!(|x: &PyDict| {
            let mut map = serializer.serialize_map(Some(x.len()))?;
            for (key, value) in x {
                if key.is_none() {
                    map.serialize_key("null")?;
                } else if let Ok(key) = key.extract::<bool>() {
                    map.serialize_key(if key { "true" } else { "false" })?;
                } else if let Ok(key) = key.str() {
                    // let key = key.to_string().map_err(debug_py_err)?;
                    let key = key.to_string().to_owned();
                    map.serialize_key(&key)?;
                } else {
                    return Err(ser::Error::custom(format_args!(
                        "Dictionary key is not a string: {:?}",
                        key
                    )));
                }
                map.serialize_value(&SerializePyObject {
                    py: self.py,
                    obj: value,
                })?;
            }
            map.end()
        });

        cast!(|x: &PyList| {
            let mut seq = serializer.serialize_seq(Some(x.len()))?;
            for element in x {
                seq.serialize_element(&SerializePyObject {
                    py: self.py,
                    obj: element,
                })?
            }
            seq.end()
        });
        cast!(|x: &PyTuple| {
            let mut seq = serializer.serialize_seq(Some(x.len()))?;
            for element in x {
                seq.serialize_element(&SerializePyObject {
                    py: self.py,
                    obj: element,
                })?
            }
            seq.end()
        });

        extract!(String);
        extract!(bool);

        cast!(|x: &PyFloat| x.value().serialize(serializer));
        extract!(u64);
        extract!(i64);

        if self.obj.is_none() {
            return serializer.serialize_unit();
        }

        match self.obj.repr() {
            Ok(repr) => Err(ser::Error::custom(format_args!(
                "Value is not JSON serializable: {}",
                repr,
            ))),
            Err(_) => Err(ser::Error::custom(format_args!(
                "Type is not JSON serializable: {}",
                self.obj.get_type().name().unwrap().to_owned(),
            ))),
        }
    }
}
