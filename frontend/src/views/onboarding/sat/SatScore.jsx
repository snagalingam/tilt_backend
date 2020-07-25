import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";

import "./sat.scss";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const SatScore = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { sat } = values;
    setAnswers((prev) => ({ ...prev, sat }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.sat) delete copy.sat;
      return copy;
    });
    previous();
  }

  const schema = yup.object().shape({
    sat: yup.number().min(400).max(1600).required("Please enter a valid score"),
  });

  return (
    <OnboardingTemplate
      name="sat-score"
      h1="What was your highest score?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="sat"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default SatScore;
