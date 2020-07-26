import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const CustomEthnicity = ({ previous, next }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { ethnicity } = values;
    onboardingAnswersVar({ ...onboardingAnswers, ethnicity });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.ethnicity) {
      delete onboardingAnswers.ethnicity;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  return (
    <OnboardingTemplate
      name="custom-ethnicity"
      h1="Which ethnicities do you identify with?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="ethnicity"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your ethnicity."
      />
    </OnboardingTemplate>
  );
};

export default CustomEthnicity;
