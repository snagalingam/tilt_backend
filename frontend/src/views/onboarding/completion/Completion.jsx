import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const Completion = () => {
  const [goToDashboard, setGoToDashboard] = useState(false);

  if (goToDashboard) return <Redirect push to="/dashboard" />;

  return (
    <OnboardingTemplate
      name="completion"
      h1="That's it!"
      p=" We are now set to find you some affordable colleges, so you don't
    graduate with $$$ in debt."
      nextFunc={() => setGoToDashboard(true)}
      nextText="Go to Dashboard"
    />
  );
};

export default Completion;
