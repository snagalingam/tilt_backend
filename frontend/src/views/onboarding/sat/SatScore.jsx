import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";

const SatScore = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { sat } = values;
    setAnswers((prev) => ({ ...prev, sat }));
    next();
  }

  const schema = yup.object().shape({
    sat: yup.number().min(400).max(1600).required("Please enter a valid score"),
  });

  return (
    <div className="sat-score-container form-container">
      <div className="form-header">
        <h1>What was your highest score?</h1>
      </div>
      <CustomTextInput
        field="sat"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default SatScore;
