import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";

const Gpa = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { gpa } = values;
    setAnswers((prev) => ({ ...prev, gpa }));
    next();
  }

  const schema = yup.object().shape({
    gpa: yup.number().min(0).max(6).required("Please enter a valid GPA"),
  });

  return (
    <div className="gpa-score-container form-container">
      <div className="form-header">
        <h1>What is your unweighted GPA?</h1>
      </div>
      <CustomTextInput
        field="gpa"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default Gpa;
