import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./preferred-pronoun.scss";

const pronouns = {
  he: "He",
  she: "She",
  they: "They",
  other: "Other",
};

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

  const pronounButton = (key, value) => (
    <button
      key={`${key}:${value}`}
      onClick={() => handleClick(key)}
      className="block-button"
    >
      {value}
    </button>
  );

  return (
    <OnboardingTemplate
      name="preferred-pronoun"
      h1="What is your preferred pronoun?"
      previousFunc={handlePrevious}
    >
      <div>
        {Object.entries(pronouns).map(([key, value]) =>
          pronounButton(key, value)
        )}
      </div>
    </OnboardingTemplate>
  );
};

export default PreferredPronoun;
