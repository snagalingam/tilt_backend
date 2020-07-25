import React, { useState } from "react";

import PreferredNameInput from "./PreferredNameInput";
import TwoOptions from "../twoOptions/TwoOptions";

import "./preferred-name.scss";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const PreferredName = ({ me, previous, next, setAnswers }) => {
  const { firstName } = me;
  const [showPreferredNameInput, toggleShowPreferredNameInput] = useState(
    false
  );

  function handleNext() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.preferredName) delete copy.preferredName;
      return copy;
    });
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.preferredName) delete copy.preferredName;
      return copy;
    });
    previous();
  }

  if (showPreferredNameInput)
    return (
      <PreferredNameInput
        next={next}
        previous={previous}
        setAnswers={setAnswers}
        toggleShowPreferredNameInput={toggleShowPreferredNameInput}
      />
    );

  return (
    <OnboardingTemplate
      name="preferred-name-options"
      h1={`Should we call you ${
        firstName || "default"
      }, or do you have another preferred name?`}
      previousFunc={handlePrevious}
    >
      <TwoOptions
        first="Yes"
        handleFirst={handleNext}
        second="Other Name"
        handleSecond={() => toggleShowPreferredNameInput(true)}
      />
    </OnboardingTemplate>
  );
};

export default PreferredName;
