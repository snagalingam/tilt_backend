import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";

const ActScore = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { act } = values;
    setAnswers((prev) => ({ ...prev, act }));
    next();
  }

  const schema = yup.object().shape({
    act: yup.number().min(1).max(36).required("Please enter a valid score"),
  });

  return (
    <div className="act-score-container form-container">
      <div className="form-header">
        <h1>What was your highest score?</h1>
      </div>
      <CustomTextInput
        field="act"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default ActScore;
