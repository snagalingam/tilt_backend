import React, { useState } from "react";

import CustomPronoun from "../customPronoun/CustomPronoun";

import "./preferred-pronoun.scss";

const PreferredPronoun = ({
  answers,
  userTypes,
  highSchool,
  college,
  parent,
  counselor,
  next,
  previous,
  setAnswers,
}) => {
  const [isCustomPronoun, setIsCustomPronoun] = useState(false);

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

  function handleClick(option) {
    setAnswers((prev) => ({ ...prev, preferredPronoun: option }));
    next();
  }

  const pronounButton = (option) => (
    <button onClick={() => handleClick(option)} className="block-button">
      {option}
    </button>
  );

  return (
    <>
      {isCustomPronoun ? (
        <CustomPronoun
          previous={() => setIsCustomPronoun(false)}
          next={next}
          setAnswers={setAnswers}
        />
      ) : (
        <div className="preferred-pronoun-container form-container">
          <div className="form-header">What are your preferred pronouns</div>
          <div className="preferred-pronoun-options">
            <div>
              {["He", "She", "They"].map((pronoun) => pronounButton(pronoun))}
              <button
                onClick={() => setIsCustomPronoun(true)}
                className="block-button"
              >
                Other
              </button>
            </div>
          </div>
          <button className="secondary-button" onClick={goBack}>
            Back
          </button>
        </div>
      )}
    </>
  );
};

export default PreferredPronoun;
