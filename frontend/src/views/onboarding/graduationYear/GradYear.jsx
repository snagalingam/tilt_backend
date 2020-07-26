import React, { useState } from "react";

import CustomGradYear from "./CustomGradYear";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./grad-year.scss";

const GradYear = ({ highSchool, parent, counselor, other, next, previous }) => {
  const [showCustomGradYear, toggleShowCustomGradYear] = useState(false);
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleNext(highschoolGraduationYear) {
    onboardingAnswersVar({ ...onboardingAnswers, highschoolGraduationYear });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.highschoolGraduationYear) {
      delete onboardingAnswers.highschoolGraduationYear;
      onboardingAnswersVar(onboardingAnswers);
    }
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
          : counselor || other
          ? "What year will your students graduate high school in?"
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
