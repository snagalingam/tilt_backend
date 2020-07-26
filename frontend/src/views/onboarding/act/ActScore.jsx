import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const ActScore = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { act } = values;
    onboardingAnswersVar({ ...onboardingAnswers, act });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.act) {
      delete onboardingAnswers.act;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const schema = yup.object().shape({
    act: yup.number().min(1).max(36).required("Please enter a valid score"),
  });

  return (
    <OnboardingTemplate
      name="act-score"
      h1="What was your highest ACT score?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="act"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default ActScore;
