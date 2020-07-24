import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import "./user-type.scss";

const UserType = ({
  answers,
  setAnswers,
  previous,
  next,
  highSchool,
  college,
  parent,
  counselor,
}) => {
  const { preferredName } = answers;

  function handleHighSchool() {
    next(highSchool);
    setAnswers((prev) => ({ ...prev, userType: "high school student" }));
  }

  function handleCollege() {
    next(college);
    setAnswers((prev) => ({ ...prev, userType: "college student" }));
  }

  function handleParent() {
    next(parent);
    setAnswers((prev) => ({ ...prev, highSchoolName: "parent" }));
  }

  function handleCounselor() {
    next(counselor);
    setAnswers((prev) => ({ ...prev, highSchoolName: "counselor" }));
  }

  return (
    <div className="user-type-container form-container">
      <div className="form-header">
        <h1>{`Thanks ${preferredName}!`}</h1>
        <h1>So, are you a...?</h1>
      </div>
      <div className="user-type-buttons">
        <div className="user-type-buttons-absolute">
          <div className="first-row">
            <button onClick={handleHighSchool} className="block-button ">
              High School Student
            </button>
            <button onClick={handleCollege} className="block-button ">
              College Student
            </button>
            <button onClick={handleParent} className="block-button ">
              Parent
            </button>
          </div>
          <div className="second-row">
            <button onClick={handleCounselor} className="block-button ">
              Counselor, Teacher or Administrator
            </button>
            <button className="block-button ">Other</button>
          </div>
        </div>
      </div>
      <div className="user-type-back-button">
        <button className="secondary-button" onClick={previous}>
          Back
        </button>
      </div>
    </div>
  );
};

export default UserType;
