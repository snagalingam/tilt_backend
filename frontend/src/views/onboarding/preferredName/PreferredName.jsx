import React, { useEffect, useState } from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import "./preferred-name.scss";

const preferredNameSchema = yup.object().shape({
  preferredName: yup.string().required("Please enter your preferred name"),
});

const PreferredName = ({ firstName, previous, next, answer }) => {
  const [isEnterPreferredName, setIsEnterPreferredName] = useState(false);

  function handleSubmit(values) {
    answer(values.preferredName);
    next();
  }

  let inputRef;

  useEffect(() => {
    if (inputRef) {
      inputRef.focus();
    }
  });

  return (
    <div className="preferred-name-container form-container">
      {isEnterPreferredName ? (
        <div className="preferred-name-update">
          <div className="form-header">
            <h1>Please enter your preferred name</h1>
          </div>
          <Formik
            initialValues={{
              preferredName: "",
            }}
            validationSchema={preferredNameSchema}
            onSubmit={handleSubmit}
          >
            {(state) => (
              <Form className="preferred-name-form">
                <Field
                  name="preferredName"
                  innerRef={(input) => (inputRef = input)}
                ></Field>
                <button type="submit">Continue</button>
              </Form>
            )}
          </Formik>
          <button
            className="secondary-button"
            onClick={() => setIsEnterPreferredName(false)}
          >
            Back
          </button>
        </div>
      ) : (
        <div className="preferred-name-options">
          <div className="form-header">
            <h1>{`Should we call you ${
              firstName || "default"
            }, or do you have another preferred name?`}</h1>
          </div>
          <div className="preferred-name-buttons">
            <button className="block-button" onClick={next}>
              Yes
            </button>
            <button
              className="block-button"
              onClick={() => setIsEnterPreferredName(true)}
            >
              Other Name
            </button>
          </div>

          <button className="secondary-button" onClick={previous}>
            Back
          </button>
        </div>
      )}
    </div>
  );
};

export default PreferredName;
