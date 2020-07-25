import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import "./gpa.scss";

const Gpa = ({ next, previous, setAnswers }) => {
  function handleSubmit(values) {
    const { gpa } = values;
    setAnswers((prev) => ({ ...prev, gpa }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.gpa) delete copy.gpa;
      return copy;
    });
    previous();
  }

  const schema = yup.object().shape({
    gpa: yup.number().min(0).max(6).required("Please enter a valid GPA"),
  });

  return (
    <OnboardingTemplate
      name="gpa"
      h1="What is your unweighted GPA?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="gpa"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default Gpa;
