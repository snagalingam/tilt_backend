import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./preferred-pronoun.scss";

const PreferredPronoun = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleClick(option) {
    onboardingAnswersVar({ ...onboardingAnswers, pronouns: option });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers.pronouns) {
      delete onboardingAnswers.pronouns;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const pronounButton = (option) => (
    <button
      key={option}
      onClick={() => handleClick(option)}
      className="block-button"
    >
      {option}
    </button>
  );

  return (
    <OnboardingTemplate
      name="preferred-pronoun"
      h1="What is your preferred pronoun?"
      previousFunc={handlePrevious}
    >
      <div>
        {["He", "She", "They"].map((pronoun) => pronounButton(pronoun))}
        <button
          onClick={() => setIsCustomPronoun(true)}
          className="block-button"
        >
          Other
        </button>
      </div>
    </OnboardingTemplate>
  );
};

export default PreferredPronoun;
