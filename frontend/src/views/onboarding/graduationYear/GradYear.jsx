import React, { useState } from "react";

import CustomGradYear from "./CustomGradYear";

import "./grad-year.scss";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const GradYear = ({ highSchool, parent, next, previous, setAnswers }) => {
  const [showCustomGradYear, toggleShowCustomGradYear] = useState(false);

  function handleNext(graduationYear) {
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

  const gradYearButton = (year) => (
    <button onClick={() => handleNext(year)} className="block-button ">
      {year}
    </button>
  );

  if (showCustomGradYear)
    return (
      <CustomGradYear
        next={next}
        previous={() => toggleShowCustomGradYear(false)}
        setAnswers={setAnswers}
      />
    );

  return (
    <OnboardingTemplate
      name="user-type"
      h1={
        highSchool
          ? "When will you be graduating high school?"
          : parent
          ? "When is your child graduating?"
          : "When did you graduate from high school?"
      }
      previousFunc={handlePrevious}
    >
      <div>
        <div className="first-row">
          {gradYearButton(2021)}
          {gradYearButton(2022)}
          {gradYearButton(2023)}
        </div>
        <div className="second-row">
          {gradYearButton(2023)}
          <button
            className="block-button"
            onClick={() => toggleShowCustomGradYear(true)}
          >
            Other
          </button>
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default GradYear;
