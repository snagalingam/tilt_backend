import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";

const HighSchoolName = ({ next, previous }) => {
  function handleSubmit(values) {
    console.log(values);
    next();
  }

  return (
    <div className="high-school-input-container form-container">
      <div className="form-header">
        What high school do you currently attend?
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
