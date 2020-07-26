import React, { useState } from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import PreferredNameInput from "./PreferredNameInput";
import TwoOptions from "../twoOptions/TwoOptions";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./preferred-name.scss";

const PreferredName = ({ me, previous, next }) => {
  const { firstName } = me;
  const [showPreferredNameInput, toggleShowPreferredNameInput] = useState(
    false
  );
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleNext() {
    if (onboardingAnswers?.preferredName) {
      delete onboardingAnswers.preferredName;
      onboardingAnswersVar(onboardingAnswers);
    }
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.preferredName) {
      delete onboardingAnswers.preferredName;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  if (showPreferredNameInput)
    return (
      <PreferredNameInput
        next={next}
        previous={previous}
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
