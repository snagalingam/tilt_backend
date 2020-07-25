import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";

const CustomSource = ({ previous, addCustomSource }) => {
  function handleSubmit(values) {
    const { source } = values;
    addCustomSource(source);
    previous();
  }

  return (
    <div className="custom-source-container form-container">
      <div className="form-header">
        <h1>How did you hear about Tilt?</h1>
      </div>
      <CustomTextInput
        field="source"
        handleSubmit={handleSubmit}
        errorMessage="Source missing."
      />
      <button className="secondary-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default CustomSource;
