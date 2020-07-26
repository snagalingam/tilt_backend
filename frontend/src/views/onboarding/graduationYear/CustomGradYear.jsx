import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const CustomGradYear = ({ next, previous, highSchool }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { highschoolGraduationYear } = values;
    onboardingAnswersVar({ ...onboardingAnswers, highschoolGraduationYear });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.highschoolGraduationYear) {
      delete onboardingAnswers.highschoolGraduationYear;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const schema = yup.object().shape({
    highschoolGraduationYear: yup
      .number()
      .min("2000")
      .max("2025")
      .required("Please enter the year you graduated"),
  });

  return (
    <OnboardingTemplate
      name="grad-year"
      h1={
        highSchool ? "When are you graduating?" : "What year did you graduate?"
      }
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="highschoolGraduationYear"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default CustomGradYear;
