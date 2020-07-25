import React, { useState } from "react";

import CustomPronoun from "./CustomPronoun";

import "./preferred-pronoun.scss";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const PreferredPronoun = ({ next, previous, setAnswers }) => {
  const [isCustomPronoun, setIsCustomPronoun] = useState(false);

  function handleClick(option) {
    setAnswers((prev) => ({ ...prev, preferredPronoun: option }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.preferredPronoun) delete copy.preferredPronoun;
      return copy;
    });
    previous();
  }

  const pronounButton = (option) => (
    <button onClick={() => handleClick(option)} className="block-button">
      {option}
    </button>
  );

  if (isCustomPronoun)
    return (
      <CustomPronoun
        previous={() => setIsCustomPronoun(false)}
        next={next}
        setAnswers={setAnswers}
      />
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
