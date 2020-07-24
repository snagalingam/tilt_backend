import React, { useState } from "react";
import { Redirect } from "react-router-dom";

const SkipOnboarding = ({ me, next }) => {
  const { firstName = "default" } = me;
  const [isSkip, setIsSkip] = useState(false);

  if (isSkip) return <Redirect push to="/dashboard" />;

  return (
    <div className="skip-onboarding-container form-container">
      <div className="form-header">
        <h1>{`Hi, ${firstName}`}</h1>
        <p>
          To help personalize your experience, we need a bit more information
        </p>
      </div>
      <button onClick={next}>Let's Start</button>
      <button className="secondary-button" onClick={() => setIsSkip(true)}>
        Skip for Now
      </button>
    </div>
  );
};

export default SkipOnboarding;
