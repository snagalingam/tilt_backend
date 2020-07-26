import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./ethnicity.scss";

const Ethnicity = ({ previous, next }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleClick(ethnicity) {
    onboardingAnswersVar({ ...onboardingAnswers, ethnicity });
    next();
  }

  function handlePreferNotToAnswer() {
    onboardingAnswersVar({
      ...onboardingAnswers,
      ethnicity: "Prefer not to answer",
    });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.ethnicity) {
      delete onboardingAnswers.ethnicity;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const ethnicityButton = (option) => {
    return (
      <button
        key={option}
        onClick={() => handleClick(option)}
        className="block-button"
      >
        {option}
      </button>
    );
  };

  return (
    <OnboardingTemplate
      name="ethnicity"
      h1="Which ethnicities do you identify with?"
      previousFunc={handlePrevious}
      nextText={"Prefer not to answer"}
      nextFunc={handlePreferNotToAnswer}
    >
      <div>
        <div className="first-row">
          {[
            "Pacific Islander",
            "Black/African",
            "Hispanic/Latinx",
            "Native American",
          ].map((ethnicity) => ethnicityButton(ethnicity))}
        </div>
        <div className="second-row">
          {["Asian", "White"].map((ethnicity) => ethnicityButton(ethnicity))}
          <button
            className="block-button"
            onClick={() => setOtherEthnicity(true)}
          >
            Other
          </button>
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default Ethnicity;
