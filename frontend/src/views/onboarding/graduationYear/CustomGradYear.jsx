import React from "react";
import * as yup from "yup";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const CustomGradYear = ({ next, previous, setAnswers, highSchool }) => {
  function handleSubmit(values) {
    const { graduationYear } = values;
    setAnswers((prev) => ({ ...prev, graduationYear }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.graduationYear) delete copy.graduationYear;
      return copy;
    });
    previous();
  }

  const schema = yup.object().shape({
    graduationYear: yup
      .number()
      .min("2000")
      .max("2025")
      .required("Please enter the year you graduated"),
  });

  return (
    <OnboardingTemplate
      name="grad-year"
      h1={
        highSchool ? "When are you graduating?" : "What year did you graduate?"
      }
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="graduationYear"
        handleSubmit={handleSubmit}
        customSchema={schema}
      />
    </OnboardingTemplate>
  );
};

export default CustomGradYear;
