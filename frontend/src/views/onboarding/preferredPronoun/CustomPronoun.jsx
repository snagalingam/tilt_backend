import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const CustomPronoun = ({ previous, next, setAnswers }) => {
  function handleSubmit(values) {
    const { preferredPronoun } = values;
    setAnswers((prev) => ({ ...prev, preferredPronoun }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.preferredPronoun) delete copy.preferredPronoun;
      return copy;
    });
    previous();
  }

  return (
    <OnboardingTemplate
      name="custom-pronoun"
      h1="What is your preferred pronoun?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="preferredPronoun"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your preferred pronoun."
      />
    </OnboardingTemplate>
  );
};

export default CustomPronoun;
