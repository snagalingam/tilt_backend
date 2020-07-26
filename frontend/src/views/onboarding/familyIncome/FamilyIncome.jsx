import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";
import { INCOME_QUINTILE } from "../../../helper/databaseVariables";

import "./family-income.scss";

const { LO, M1, M2, H1, H2 } = INCOME_QUINTILE;

const FamilyIncome = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleClick(incomeQuintile) {
    onboardingAnswersVar({ ...onboardingAnswers, incomeQuintile });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.incomeQuintile) {
      delete onboardingAnswers.incomeQuintile;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const familyIncomeButton = ({ display, value }) => (
    <button
      className="block-button"
      key={value}
      onClick={() => handleClick(value)}
    >
      {display}
    </button>
  );

  return (
    <OnboardingTemplate
      name="family-income"
      h1="What is your family income?"
      previousFunc={handlePrevious}
    >
      <div>
        <div className="first-row">
          {[LO, M1, M2].map((object) => familyIncomeButton(object))}
        </div>
        <div className="second-row">
          {[H1, H2].map((object) => familyIncomeButton(object))}
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default FamilyIncome;
