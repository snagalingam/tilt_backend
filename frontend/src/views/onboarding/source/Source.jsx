import React, { useState } from "react";

import CustomSource from "./CustomSource";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import "./source.scss";

const Source = ({ previous, next, setAnswers, userTypes, flows, answers }) => {
  const [isCustomSource, toggleIsCustomSource] = useState(false);
  const [otherSource, setOther] = useState(null);
  const [sources, selectSources] = useState([]);

  const { HIGH_SCHOOL, COLLEGE, PARENT, COUNSELOR, OTHER } = userTypes;
  const {
    highSchoolFlow,
    collegeFlow,
    parentFlow,
    counselorFlow,
    otherFlow,
  } = flows;
  const { userType } = answers;

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (userType === OTHER) {
        if (copy.organizationName) delete copy.organizationName;
        if (copy.graduationYear) delete copy.graduationYear;
      }
      if (copy.source) delete copy.source;
      return copy;
    });

    if (userType === HIGH_SCHOOL) {
      previous(highSchoolFlow);
    }
    if (userType === COLLEGE) {
      previous(collegeFlow);
    }
    if (userType === PARENT) {
      previous(parentFlow);
    }
    if (userType === COUNSELOR) {
      previous(counselorFlow);
    }
    if (userType === OTHER) {
      previous(otherFlow);
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
    const index = copy.indexOf(otherSource);
    if (index >= 0) {
      copy.splice(index, 1);
    } else {
      copy.push(otherSource);
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
            className={`block-button${otherSource ? " selected" : ""}`}
            onClick={() => toggleIsCustomSource(true)}
          >
            {otherSource || "Other"}
          </button>
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default Source;
