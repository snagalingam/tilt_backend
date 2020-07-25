import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";

const CustomEthnicity = ({
  next,
  previous,
  setAnswers,
  addCustomEthnicity,
}) => {
  function handleSubmit(values) {
    const { ethnicity } = values;
    addCustomEthnicity(ethnicity);
    previous();
  }

  return (
    <div className="ethnicity-container form-container">
      <div className="form-header">
        <h1>What is your ethnicity?</h1>
      </div>
      <CustomTextInput
        field="ethnicity"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your ethnicity."
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default CustomEthnicity;
