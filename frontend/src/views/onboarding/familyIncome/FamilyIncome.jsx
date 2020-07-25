import React from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const FamilyIncome = ({ next, previous, setAnswers }) => {
  function handleClick(familyIncome) {
    setAnswers((prev) => ({ ...prev, familyIncome }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.familyIncome) delete copy.familyIncome;
      return copy;
    });
    previous();
  }

  const familyIncomeButton = (income) => (
    <button onClick={() => handleClick(income)}>{income}</button>
  );

  return (
    <OnboardingTemplate
      name="family-income"
      h1="What is your familyIncome?"
      previousFunc={handlePrevious}
    >
      <div>{familyIncomeButton(10000)}</div>
    </OnboardingTemplate>
  );
};

export default FamilyIncome;
