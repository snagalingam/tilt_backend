import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const PreferredNameInput = ({
  next,
  setAnswers,
  toggleShowPreferredNameInput,
}) => {
  function handleSubmit(values) {
    setAnswers((prev) => ({ ...prev, preferredName: values.preferredName }));
    next();
  }

  function handlePrevious() {
    console.log("preferredname");
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.preferredName) delete copy.preferredName;
      return copy;
    });
    toggleShowPreferredNameInput(false);
  }

  return (
    <OnboardingTemplate
      name="preferred-name"
      h1="Please enter your preferred name"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="preferredName"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your preferred name."
      />
    </OnboardingTemplate>
  );
};

export default PreferredNameInput;
