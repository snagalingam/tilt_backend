import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const CustomSource = ({ previous, addCustomSource }) => {
  function handleSubmit(value) {
    const { source } = value;
    addCustomSource(source);
    previous();
  }

  return (
    <OnboardingTemplate
      name="custom-source"
      h1="How did you hear about Tilt?"
      previousFunc={previous}
    >
      <CustomTextInput
        field="source"
        handleSubmit={handleSubmit}
        errorMessage="Source missing."
      />
    </OnboardingTemplate>
  );
};

export default CustomSource;
