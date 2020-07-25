import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";

const CustomPronoun = ({ previous, next, setAnswers }) => {
  function handleSubmit(values) {
    const { preferredPronoun } = values;
    setAnswers((prev) => ({ ...prev, preferredPronoun }));
    next();
  }

  return (
    <div className="custom-pronoun-container form-container">
      <div className="form-header">
        <h1>What is your preferred pronoun?</h1>
      </div>
      <CustomTextInput
        field="preferredPronoun"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your preferred pronoun."
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default CustomPronoun;
