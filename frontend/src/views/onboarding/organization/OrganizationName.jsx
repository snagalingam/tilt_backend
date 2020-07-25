import React, { useState } from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import GradYear from "../graduationYear/GradYear";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const OrganizationName = ({ next, setAnswers, toggleShowOrgInput }) => {
  const [showGradYear, toggleShowGradYear] = useState(false);

  function handleSubmit(values) {
    const { organizationName } = values;
    setAnswers((prev) => ({ ...prev, organizationName }));
    toggleShowGradYear(true);
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.organizationName) delete copy.organizationName;
      if (copy.graduationYear) delete copy.graduationYear;
      return copy;
    });
    toggleShowOrgInput(false);
  }

  if (showGradYear)
    return (
      <GradYear
        other
        next={next}
        previous={() => toggleShowGradYear(false)}
        setAnswers={setAnswers}
      />
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
