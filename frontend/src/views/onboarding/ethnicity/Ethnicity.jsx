import React, { useState } from "react";
import { Redirect } from "react-router-dom";

const Ethnicity = ({ previous }) => {
  return (
    <div className="ethnicity-container form-container">
      Ethnicity
      <button className="second-button" onClick={previous}>
        Back
      </button>
    </div>
  );
};

export default Ethnicity;
