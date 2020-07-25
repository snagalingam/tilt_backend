import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";

const CustomGradYear = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { gradYear } = values;
    setAnswers((prev) => ({ ...prev, gradYear }));
    next();
  }

  const schema = yup.object().shape({
    gradYear: yup
      .number()
      .min("2000")
      .max("2025")
      .required("Please enter the year you graduated"),
  });

  return (
    <div className="high-school-input-container form-container">
      <div className="form-header">What year did you graduate?</div>
      <CustomTextInput
        field="gradYear"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default CustomGradYear;
