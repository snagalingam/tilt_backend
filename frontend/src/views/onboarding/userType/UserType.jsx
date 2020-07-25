import React from "react";

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
  other,
  userTypes,
}) => {
  const { preferredName } = answers;
  const { HIGH_SCHOOL, COLLEGE, PARENT, COUNSELOR, OTHER } = userTypes;

  function handleHighSchool() {
    next(highSchool);
    setAnswers((prev) => ({ ...prev, userType: HIGH_SCHOOL }));
  }

  function handleCollege() {
    next(college);
    setAnswers((prev) => ({ ...prev, userType: COLLEGE }));
  }

  function handleParent() {
    next(parent);
    setAnswers((prev) => ({ ...prev, userType: PARENT }));
  }

  function handleCounselor() {
    next(counselor);
    setAnswers((prev) => ({ ...prev, userType: COUNSELOR }));
  }

  function handleOther() {
    next(other);
    setAnswers((prev) => ({ ...prev, userType: OTHER }));
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.userType) delete copy.userType;
      return copy;
    });
    previous();
  }

  return (
    <div className="user-type-container form-container">
      <div className="form-header">
        <h1>{`Thanks ${preferredName}!`}</h1>
        <h1>So, are you a...?</h1>
      </div>
      <div className="form-body">
        <div>
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
            <button className="block-button" onClick={handleOther}>
              Other
            </button>
          </div>
        </div>
      </div>
      <div className="onboarding-buttons">
        <button className="secondary-button" onClick={handlePrevious}>
          Back
        </button>
      </div>
    </div>
  );
};

export default UserType;
