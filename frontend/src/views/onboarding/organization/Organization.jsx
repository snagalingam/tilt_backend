import React, { useState } from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import OrganizationName from "./OrganizationName";
import TwoOptions from "../twoOptions/TwoOptions";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const Organization = ({ next, previous }) => {
  const [showOrgInput, toggleShowOrgInput] = useState(false);
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handlePrevious() {
    if (onboardingAnswers?.organizationName) {
      delete onboardingAnswers.organizationName;
    }
    if (onboardingAnswers?.graduationYear) {
      delete onboardingAnswers.graduationYear;
    }
    onboardingAnswersVar(onboardingAnswers);
  }

  if (showOrgInput)
    return (
      <OrganizationName
        next={next}
        previous={previous}
        toggleShowOrgInput={toggleShowOrgInput}
      />
    );

  return (
    <OnboardingTemplate
      name="organization"
      h1="Do you work at an organization that supports students?"
      previousFunc={handlePrevious}
    >
      <TwoOptions
        first="Yes"
        handleFirst={() => toggleShowOrgInput(true)}
        second="No"
        handleSecond={next}
      />
    </OnboardingTemplate>
  );
};

export default Organization;
