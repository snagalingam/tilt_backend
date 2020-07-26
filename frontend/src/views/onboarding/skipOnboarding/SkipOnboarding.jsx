import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const SkipOnboarding = ({ me = {}, next }) => {
  const { firstName = "default" } = me;
  const [isSkip, setIsSkip] = useState(false);

  if (isSkip) return <Redirect push to="/dashboard" />;

  return (
    <OnboardingTemplate
      name="skip-onboarding"
      h1={`Hi, ${firstName}`}
      p="To help personalize your experience, we need a bit more information"
      nextFunc={next}
      nextText="Let's Start"
      previousFunc={() => setIsSkip(true)}
      previousText="Skip for Now"
    />
  );
};

export default SkipOnboarding;
