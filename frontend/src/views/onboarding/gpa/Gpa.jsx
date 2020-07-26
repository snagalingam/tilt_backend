import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./gpa.scss";

const Gpa = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { gpa } = values;
    onboardingAnswersVar({ ...onboardingAnswers, gpa });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.gpa) {
      delete onboardingAnswers.gpa;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const schema = yup.object().shape({
    gpa: yup.number().min(0).max(6).required("Please enter a valid GPA"),
  });

  return (
    <OnboardingTemplate
      name="gpa"
      h1="What is your unweighted GPA?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="gpa"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default Gpa;
