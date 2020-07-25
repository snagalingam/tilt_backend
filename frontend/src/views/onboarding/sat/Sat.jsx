import React, { useState } from "react";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";
import SatScore from "./SatScore";
import TwoOptions from "../twoOptions/TwoOptions";

const Sat = ({ next, previous, setAnswers, college }) => {
  const [didTakeSat, setDidTakeSat] = useState(false);

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.sat) delete copy.sat;
      return copy;
    });
    previous();
  }

  if (didTakeSat || college)
    return (
      <SatScore
        next={next}
        previous={college ? previous : () => setDidTakeSat(false)}
        setAnswers={setAnswers}
      />
    );

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
