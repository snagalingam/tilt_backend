import React, { useState } from "react";

import CustomEthnicity from "./CustomEthnicity";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import "./ethnicity.scss";

const Ethnicity = ({ previous, next, setAnswers }) => {
  const [otherEthnicity, setOtherEthnicity] = useState(false);

  function handleClick(ethnicity) {
    setAnswers((prev) => ({ ...prev, ethnicity }));
    next();
  }

  function handlePrevious() {
    setAnswers((prev) => {
      const copy = { ...prev };
      if (copy.ethnicity) delete copy.ethnicity;
      return copy;
    });
    previous();
  }

  const ethnicityButton = (option) => {
    return (
      <button onClick={() => handleClick(option)} className="block-button">
        {option}
      </button>
    );
  };

  if (otherEthnicity)
    return (
      <CustomEthnicity
        previous={previous}
        next={next}
        setAnswers={setAnswers}
      />
    );

  return (
    <OnboardingTemplate
      name="ethnicity"
      h1="Which ethnicities do you identify with?"
      previousFunc={handlePrevious}
    >
      <div>
        <div className="first-row">
          {[
            "Pacific Islander",
            "Black/African",
            "Hispanic/Latinx",
            "Native American",
          ].map((ethnicity) => ethnicityButton(ethnicity))}
        </div>
        <div className="second-row">
          {["Asian", "White"].map((ethnicity) => ethnicityButton(ethnicity))}
          <button
            className="block-button"
            onClick={() => setOtherEthnicity(true)}
          >
            Other
          </button>
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default Ethnicity;
