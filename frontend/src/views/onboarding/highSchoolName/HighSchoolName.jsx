import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";

const HighSchoolName = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { highSchoolName } = values;
    setAnswers((prev) => ({ ...prev, highSchoolName }));
    next();
  }

  return (
    <div className="high-school-name-container form-container">
      <div className="form-header">
        <h1>What high school do you currently attend?</h1>
      </div>
      <CustomTextInput
        field="highSchoolName"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your high school name."
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default HighSchoolName;
