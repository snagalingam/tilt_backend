import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./school-district.scss";

const SchoolDistrict = ({ previous, next }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { schoolDistrict } = values;
    onboardingAnswersVar({ ...onboardingAnswers, schoolDistrict });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.schoolDistrict) {
      delete onboardingAnswers.schoolDistrict;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }
  return (
    <OnboardingTemplate
      name="school-district"
      h1="What school or district do you work at?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="schoolDistrict"
        handleSubmit={handleSubmit}
        errorMessage="Please enter a school or district name"
      />
    </OnboardingTemplate>
  );
};

export default SchoolDistrict;
