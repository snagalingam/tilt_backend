import React, { useState } from "react";

import ActScore from "./ActScore";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import TwoOptions from "../twoOptions/TwoOptions";

const Act = ({ next, previous, setAnswers, highScool, college }) => {
  const [didTakeAct, setDidTakeAct] = useState(false);

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.act) delete copy.act;
      return copy;
    });
    previous();
  }

  if (didTakeAct || college)
    return (
      <ActScore
        next={next}
        previous={() => setDidTakeAct(false)}
        setAnswers={setAnswers}
      />
    );

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
