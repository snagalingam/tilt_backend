import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./sat.scss";

const SatScore = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { satScore } = values;
    onboardingAnswersVar({ ...onboardingAnswers, satScore });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.satScore) {
      delete onboardingAnswers.satScore;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const schema = yup.object().shape({
    satScore: yup
      .number()
      .min(400)
      .max(1600)
      .required("Please enter a valid score"),
  });

  return (
    <OnboardingTemplate
      name="sat-score"
      h1="What was your highest SAT score?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="satScore"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default SatScore;
