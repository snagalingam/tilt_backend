import React from "react";
import { Field } from "formik";

const FieldSet = ({ name, label, fieldType, children, type }) => (
  <fieldset>
    <label htmlFor={`signup-${name}`}>{label}</label>
    <Field as={fieldType} name={name} type={type}>
      {children}
    </Field>
  </fieldset>
);

export default FieldSet;
