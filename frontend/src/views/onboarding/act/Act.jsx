import React, { useState } from "react";

import ActScore from "./ActScore";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import TwoOptions from "../twoOptions/TwoOptions";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const Act = ({ next, previous, college }) => {
  const [didTakeAct, setDidTakeAct] = useState(false);
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handlePrevious() {
    if (onboardingAnswers?.act) {
      delete onboardingAnswers.act;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  if (didTakeAct || college)
    return <ActScore next={next} previous={() => setDidTakeAct(false)} />;

  return (
    <OnboardingTemplate
      name="act"
      h1="Have you taken the ACT yet?"
      previousFunc={handlePrevious}
    >
      <TwoOptions
        first="Yes"
        handleFirst={() => setDidTakeAct(true)}
        second="No"
        handleSecond={next}
      />
    </OnboardingTemplate>
  );
};

export default Act;
