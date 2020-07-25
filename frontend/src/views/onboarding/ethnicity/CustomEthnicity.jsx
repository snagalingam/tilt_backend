import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const CustomEthnicity = ({ previous, setAnswers, next }) => {
  function handleSubmit(values) {
    const { ethnicity } = values;
    setAnswers((prev) => ({ ...prev, ethnicity }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.ethnicity) delete copy.ethnicity;
      return copy;
    });
    previous();
  }

  return (
    <OnboardingTemplate
      name="custom-ethnicity"
      h1="Which ethnicities do you identify with?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="ethnicity"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your ethnicity."
      />
    </OnboardingTemplate>
  );
};

export default CustomEthnicity;
