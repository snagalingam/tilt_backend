import React from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const SchoolDistrict = ({ previous, next, setAnswers }) => {
  function handleSubmit(values) {
    const { schoolDistrict } = values;
    setAnswers((prev) => ({ ...prev, schoolDistrict }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.schoolDistrict) delete copy.schoolDistrict;
      return copy;
    });
    previous();
  }
  return (
    <OnboardingTemplate
      name="school-district"
      h1="What school or district do you work at?"
      previousFunc={handlePrevious}
    >
      <CustomTextInput
        field="schoolDistrict"
        handleSubmit={handleSubmit}
        errorMessage="Please enter a school or district name"
      />
    </OnboardingTemplate>
  );
};

export default SchoolDistrict;
