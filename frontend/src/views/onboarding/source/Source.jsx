import React, { useState } from "react";

import CustomSource from "./CustomSource";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import "./source.scss";

const Source = ({ previous, next, setAnswers, userTypes, flows, answers }) => {
  const [isCustomSource, toggleIsCustomSource] = useState(false);
  const [other, setOther] = useState(null);
  const [sources, selectSources] = useState([]);

  const { HIGH_SCHOOL, COLLEGE, PARENT, COUNSELOR } = userTypes;
  const { highSchool, college, parent, counselor } = flows;
  const { userType } = answers;
  console.log(userType);

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.source) delete copy.source;
      return copy;
    });

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
    const copy = [...sources];
    const index = copy.indexOf(option);
    if (index >= 0) {
      copy.splice(index, 1);
    } else {
      copy.push(option);
    }
    selectSources(copy);
  }

  const sourceButton = (option) => {
    const index = sources.indexOf(option);
    return (
      <button
        onClick={() => handleClick(option)}
        className={`block-button${index >= 0 ? " selected" : ""}`}
      >
        {option}
      </button>
    );
  };

  function handleSave() {
    const copy = [...sources];
    const index = copy.indexOf(other);
    if (index >= 0) {
      copy.splice(index, 1);
    } else {
      copy.push(other);
    }
    selectSources(copy);
    setAnswers((prev) => ({ ...prev, sources: copy }));
    next();
  }

  if (isCustomSource)
    return (
      <CustomSource
        previous={() => toggleIsCustomSource(false)}
        addCustomSource={setOther}
      />
    );

  return (
    <OnboardingTemplate
      name="source"
      h1="How did you hear about Tilt?"
      nextFunc={handleSave}
      previousFunc={handlePrevious}
    >
      <div>
        <div className="first-row">
          {["Instagram", "Facebook", "Parent"].map((source) =>
            sourceButton(source)
          )}
        </div>
        <div className="second-row">
          {["School or District Staff", "Friend"].map((source) =>
            sourceButton(source)
          )}
          <button
            className={`block-button${other ? " selected" : ""}`}
            onClick={() => toggleIsCustomSource(true)}
          >
            {other || "Other"}
          </button>
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default Source;
