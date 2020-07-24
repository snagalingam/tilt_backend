import React, { useEffect, useState } from "react";
import { Formik, Form, Field } from "formik";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";

import "./preferred-name.scss";

const PreferredName = ({ me, previous, next, setAnswers }) => {
  const { firstName } = me;
  const [isEnterPreferredName, setIsEnterPreferredName] = useState(false);

  function handleSubmit(values) {
    setAnswers((prev) => ({ ...prev, preferredName: values.preferredName }));
    next();
  }

  return (
    <div className="preferred-name-container form-container">
      {isEnterPreferredName ? (
        <div className="preferred-name-update">
          <div className="form-header">
            <h1>Please enter your preferred name</h1>
          </div>
          <CustomTextInput
            field="preferredName"
            handleSubmit={handleSubmit}
            errorMessage="Please enter your preferred name."
          />
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
