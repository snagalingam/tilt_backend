import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";
import { ETHNICITY } from "../../../helper/databaseVariables";

import "./ethnicity.scss";

const {
  AMERICAN_INDIAN,
  ASIAN,
  BLACK,
  HISPANIC,
  ISLANDER,
  WHITE,
  TWO_OR_MORE,
  OTHER,
} = ETHNICITY;

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

  const ethnicityButton = ({ display, value }) => {
    return (
      <button
        key={value}
        onClick={() => handleClick(value)}
        className="block-button"
      >
        {display}
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
          {[AMERICAN_INDIAN, ASIAN, BLACK, HISPANIC].map((object) =>
            ethnicityButton(object)
          )}
        </div>
        <div className="second-row">
          {[ISLANDER, WHITE, TWO_OR_MORE, OTHER].map((object) =>
            ethnicityButton(object)
          )}
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default Ethnicity;
