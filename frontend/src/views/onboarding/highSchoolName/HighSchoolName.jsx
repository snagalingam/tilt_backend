import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./high-school-name.scss";

const HighSchoolName = ({ next, previous, highSchool, parent }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { highSchoolName } = values;
    onboardingAnswersVar({ ...onboardingAnswers, highSchoolName });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.highSchoolName) {
      delete onboardingAnswers.highSchoolName;
      onboardingAnswersVar({ ...onboardingAnswers });
    }
    previous();
  }

  return (
    <OnboardingTemplate
      name="high-school-name"
      h1={
        highSchool
          ? "What high school do you currently attend?"
          : parent
          ? "What high school does your child currently attend?"
          : "What high school did you graduate from?"
      }
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="highSchoolName"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your high school name."
      />
    </OnboardingTemplate>
  );
};

export default HighSchoolName;
