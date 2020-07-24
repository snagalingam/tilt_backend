import React, { useState } from "react";
import { Redirect } from "react-router-dom";

const PreferredPronoun = ({
  answers,
  userTypes,
  highSchool,
  college,
  parent,
  counselor,
  previous,
}) => {
  const { HIGH_SCHOOL, COLLEGE, PARENT, COUNSELOR } = userTypes;
  const { userType } = answers;

  function goBack() {
    if (userType === HIGH_SCHOOL) {
      previous(highSchool);
    }
    if (userType === COLLEGE) {
      previous(college);
    }
    if (userType === PARENT) {
      previous(parent);
    }
    if (userType === COUNSELOR) {
      previous(counselor);
    }
  }

  return (
    <div className="preferred-pronoun-container form-container">
      Preferred Pronoun
      <button className="secondary-button" onClick={goBack}>
        Back
      </button>
    </div>
  );
};

export default PreferredPronoun;
