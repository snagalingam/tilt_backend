import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const ActScore = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { actScore } = values;
    onboardingAnswersVar({ ...onboardingAnswers, actScore });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.actScore) {
      delete onboardingAnswers.actScore;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const schema = yup.object().shape({
    actScore: yup
      .number()
      .min(1)
      .max(36)
      .required("Please enter a valid score"),
  });

  return (
    <OnboardingTemplate
      name="act-score"
      h1="What was your highest ACT score?"
      previous={handlePrevious}
    >
      <CustomTextInput
        field="actScore"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default ActScore;
