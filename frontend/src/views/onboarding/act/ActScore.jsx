import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const ActScore = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { act } = values;
    setAnswers((prev) => ({ ...prev, act }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.act) delete copy.act;
      return copy;
    });
    previous();
  }

  const schema = yup.object().shape({
    act: yup.number().min(1).max(36).required("Please enter a valid score"),
  });

  return (
    <OnboardingTemplate
      name="act-score"
      h1="What was your highest ACT score?"
      previous={handlePrevious}
    >
      <CustomTextInput
        field="act"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default ActScore;
