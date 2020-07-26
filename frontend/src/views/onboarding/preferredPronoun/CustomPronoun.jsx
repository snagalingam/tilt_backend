import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const CustomPronoun = ({ previous, next }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { pronouns } = values;
    onboardingAnswersVar({ ...onboardingAnswers, pronouns });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.pronouns) {
      delete onboardingAnswers.pronouns;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  return (
    <OnboardingTemplate
      name="custom-pronoun"
      h1="What is your preferred pronoun?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="pronouns"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your preferred pronoun."
      />
    </OnboardingTemplate>
  );
};

export default CustomPronoun;
