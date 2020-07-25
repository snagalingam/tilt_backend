import React, { useState } from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import OrganizationName from "./OrganizationName";
import TwoOptions from "../twoOptions/TwoOptions";

const Organization = ({ next, previous, setAnswers }) => {
  const [showOrgInput, toggleShowOrgInput] = useState(false);

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.organizationName) delete copy.organizationName;
      if (copy.graduationYear) delete copy.graduationYear;
      return copy;
    });
  }

  if (showOrgInput)
    return (
      <OrganizationName
        next={next}
        previous={previous}
        setAnswers={setAnswers}
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
