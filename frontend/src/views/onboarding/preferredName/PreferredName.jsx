import React, { useState } from "react";

import CustomTextInput from "../customTextInput/CustomTextInput";
import TwoOptions from "../twoOptions/TwoOptions";

import "./preferred-name.scss";

const PreferredName = ({ me, previous, next, setAnswers }) => {
  const { firstName } = me;
  const [isEnterPreferredName, setIsEnterPreferredName] = useState(false);

  function handleSubmit(values) {
    setAnswers((prev) => ({ ...prev, preferredName: values.preferredName }));
    next();
  }

  return (
    <div className="preferred-name-container form-container">
      {isEnterPreferredName ? (
        <div className="preferred-name-update">
          <div className="form-header">
            <h1>Please enter your preferred name</h1>
          </div>
          <CustomTextInput
            field="preferredName"
            handleSubmit={handleSubmit}
            errorMessage="Please enter your preferred name."
          />
          <button
            className="secondary-button"
            onClick={() => setIsEnterPreferredName(false)}
          >
            Back
          </button>
        </div>
      ) : (
        <div className="preferred-name-options">
          <div className="form-header">
            <h1>{`Should we call you ${
              firstName || "default"
            }, or do you have another preferred name?`}</h1>
          </div>
          <TwoOptions
            first="Yes"
            handleFirst={next}
            second="Other Name"
            handleSecond={() => setIsEnterPreferredName(true)}
          />
          <button className="secondary-button" onClick={previous}>
            Back
          </button>
        </div>
      )}
    </div>
  );
};

export default PreferredName;
