import React, { useState } from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import GradYear from "../graduationYear/GradYear";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const OrganizationName = ({ next, toggleShowOrgInput }) => {
  const [showGradYear, toggleShowGradYear] = useState(false);
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleSubmit(values) {
    const { organizationName } = values;
    onboardingAnswersVar({ ...onboardingAnswers, organizationName });
    toggleShowGradYear(true);
  }

  function handlePrevious() {
    if (onboardingAnswers?.organizationName) {
      delete onboardingAnswers.organizationName;
    }
    if (onboardingAnswers?.graduationYear) {
      delete onboardingAnswers.graduationYear;
    }
    onboardingAnswersVar(onboardingAnswers);
    toggleShowOrgInput(false);
  }

  if (showGradYear)
    return (
      <GradYear other next={next} previous={() => toggleShowGradYear(false)} />
    );

  return (
    <OnboardingTemplate
      name="organization-name"
      h1="What organization do you work at?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="organizationName"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your organization name."
      />
    </OnboardingTemplate>
  );
};

export default OrganizationName;
