import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const PreferredNameInput = ({ next, toggleShowPreferredNameInput }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { preferredName } = values;
    if (onboardingAnswers) {
      onboardingAnswersVar({ ...onboardingAnswers, preferredName });
    } else {
      onboardingAnswersVar({ preferredName });
    }
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.preferredName) {
      delete onboardingAnswers.preferredName;
      onboardingAnswersVar({ ...onboardingAnswers });
    }
    toggleShowPreferredNameInput(false);
  }

  return (
    <OnboardingTemplate
      name="preferred-name"
      h1="Please enter your preferred name"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="preferredName"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your preferred name."
      />
    </OnboardingTemplate>
  );
};

export default PreferredNameInput;
