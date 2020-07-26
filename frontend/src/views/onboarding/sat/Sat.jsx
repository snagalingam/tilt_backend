import React, { useState } from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import SatScore from "./SatScore";
import TwoOptions from "../twoOptions/TwoOptions";

import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

const Sat = ({ next, previous, college }) => {
  const [didTakeSat, setDidTakeSat] = useState(false);
  const onboardingAnswers = { ...onboardingAnswersVar() };

  function handlePrevious() {
    if (onboardingAnswers?.satScore) {
      delete onboardingAnswers.satScore;
      onboardingAnswersVar(onboardingAnswers);
    }
    previous();
  }

  if (didTakeSat)
    return <SatScore next={next} previous={() => setDidTakeSat(false)} />;

  return (
    <OnboardingTemplate
      name="sat"
      h1="Have you taken the SAT yet?"
      previousFunc={handlePrevious}
    >
      <TwoOptions
        first="Yes"
        handleFirst={() => setDidTakeSat(true)}
        second="No"
        handleSecond={next}
      />
    </OnboardingTemplate>
  );
};

export default Sat;
