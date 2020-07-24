import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import "../userType/user-type.scss";

const GraduationYear = ({ highSchool, college, next, answer }) => {
  function handleClick(value) {
    answer(value);
    next();
  }

  const gradYearButton = (year) => (
    <button onClick={() => handleClick(year)} className="block-button ">
      {year}
    </button>
  );

  return (
    <div className="user-type-container form-container">
      <div className="form-header">
        {highSchool && <h1>When will you be graduating high school?</h1>}
        {college && <h1>When did you graduate from high school?</h1>}
      </div>
      <div className="user-type-buttons">
        <div className="user-type-buttons-absolute">
          <div className="first-row">
            {gradYearButton(2021)}
            {gradYearButton(2022)}
            {gradYearButton(2023)}
          </div>
          <div className="second-row">
            {gradYearButton(2023)}
            <button className="block-button ">Other</button>
          </div>
        </div>
      </div>
      <div className="user-type-back-button">
        <button className="secondary-button">Back</button>
      </div>
    </div>
  );
};

export default GraduationYear;
