import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import "./high-school-name.scss";

const HighSchoolName = ({ next, previous, setAnswers, highSchool, parent }) => {
  function handleSubmit(values) {
    const { highSchoolName } = values;
    setAnswers((prev) => ({ ...prev, highSchoolName }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.highSchoolName) delete copy.highSchoolName;
      return copy;
    });
    previous();
  }

  return (
    <OnboardingTemplate
      name="high-school-name"
      h1={
        highSchool
          ? "What high school do you currently attend?"
          : parent
          ? "What high school does your child currently attend?"
          : "What high school did you graduate from?"
      }
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="highSchoolName"
        handleSubmit={handleSubmit}
        errorMessage="Please enter your high school name."
      />
    </OnboardingTemplate>
  );
};

export default HighSchoolName;
