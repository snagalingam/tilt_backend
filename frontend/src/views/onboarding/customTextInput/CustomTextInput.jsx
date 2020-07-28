import React, { useEffect } from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import "./custom-text-input.scss";

const CustomTextInput = ({
  field,
  handleSubmit,
  customSchema,
  buttonText = "Continue",
  errorMessage = "Please enter your information",
}) => {
  const defaultSchema = yup.object().shape({
    [field]: yup.string().required(errorMessage),
  });
  const schema = customSchema ? customSchema : defaultSchema;

  let inputRef;
  useEffect(() => {
    if (inputRef) {
      inputRef.focus();
    }
  });

  return (
    <Formik
      initialValues={{
        [field]: "",
      }}
      validationSchema={schema}
      onSubmit={handleSubmit}
    >
      {(state) => (
        <Form className="custom-text-input">
          <Field name={field} innerRef={(input) => (inputRef = input)}></Field>
          {/* {state.errors && state.touched && (
            <span className="custom-text-input-error">
              {state.errors[field]}
            </span>
          )} */}
          <button type="submit">{buttonText}</button>
        </Form>
      )}
    </Formik>
  );
};

export default CustomTextInput;
