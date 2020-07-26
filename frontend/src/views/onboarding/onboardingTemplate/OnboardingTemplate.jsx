import React from "react";

const OnboardingTemplate = ({
  name,
  h1,
  h1Array,
  p,
  children,
  previousFunc,
  previousText = "Back",
  nextFunc,
  nextText = "Continue",
}) => {
  return (
    <div className={`${name}-container form-container`}>
      <div className="form-header">
        {h1 && <h1>{h1}</h1>}
        {h1Array?.length > 0 && h1Array.map((h1x) => <h1 key={h1x}>{h1x}</h1>)}
        {p && <p>{p}</p>}
      </div>
      {children && <div className="form-body">{children}</div>}
      <div className="onboarding-buttons">
        {nextFunc && <button onClick={nextFunc}>{nextText}</button>}
        {previousFunc && (
          <button className="secondary-button" onClick={previousFunc}>
            {previousText}
          </button>
        )}
      </div>
    </div>
  );
};

export default OnboardingTemplate;
