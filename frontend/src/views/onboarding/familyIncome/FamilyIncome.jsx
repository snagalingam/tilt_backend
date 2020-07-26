import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const FamilyIncome = ({ next, previous }) => {
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handleClick(familyIncome) {
    onboardingAnswersVar({ ...onboardingAnswers, familyIncome });
    next();
  }

  function handlePrevious() {
    if (onboardingAnswers?.familyIncome) {
      delete onboardingAnswers.familyIncome;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  const familyIncomeButton = (income) => (
    <button onClick={() => handleClick(income)}>{income}</button>
  );

  return (
    <OnboardingTemplate
      name="family-income"
      h1="What is your family income?"
      previousFunc={handlePrevious}
    >
      <div>{familyIncomeButton(10000)}</div>
    </OnboardingTemplate>
  );
};

export default FamilyIncome;
