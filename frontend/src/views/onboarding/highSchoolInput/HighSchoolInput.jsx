import React, { useEffect, useState } from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import "../preferredName/preferred-name.scss";

const highSchoolNameSchema = yup.object().shape({
  highSchoolName: yup.string().required("Please enter your high school name"),
});

const HighSchoolInput = ({ next }) => {
  function handleSubmit(values) {
    console.log(values);
    next();
  }

  let inputRef;

  useEffect(() => {
    if (inputRef) {
      inputRef.focus();
    }
  });

  return (
    <div className="high-school-input-container form-container">
      <div className="form-header">
        What high school do you currently attend?
      </div>
      <Formik
        initialValues={{
          highSchoolName: "",
        }}
        validationSchema={highSchoolNameSchema}
        onSubmit={handleSubmit}
      >
        {(state) => (
          <Form className="preferred-name-form">
            <Field
              name="highSchoolName"
              innerRef={(input) => (inputRef = input)}
            ></Field>
            <button type="submit">Continue</button>
          </Form>
        )}
      </Formik>
    </div>
  );
};

export default HighSchoolInput;
