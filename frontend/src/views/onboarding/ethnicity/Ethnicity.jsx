import React, { useState } from "react";

import CustomEthnicity from "./CustomEthnicity";

import "./ethnicity.scss";

const Ethnicity = ({ previous, next, setAnswers }) => {
  const [otherEthnicity, setOtherEthnicity] = useState(false);
  const [selectedEthnicities, selectEthnicities] = useState([]);

  function handleClick(option) {
    console.log(option);
    const copy = [...selectedEthnicities];
    const index = copy.indexOf(option);
    if (index >= 0) {
      copy.splice(index, 1);
    } else {
      copy.push(option);
    }
    selectEthnicities(copy);
  }

  const ethnicityButton = (option) => {
    const index = selectedEthnicities.indexOf(option);
    return (
      <button
        onClick={() => handleClick(option)}
        className={`block-button${index >= 0 ? " selected" : ""}`}
      >
        {option}
      </button>
    );
  };

  function handleSave() {
    setAnswers((prev) => ({ ...prev, ethnicity: selectedEthnicities }));
    next();
  }

  return (
    <>
      {otherEthnicity ? (
        <CustomEthnicity
          previous={() => setOtherEthnicity(false)}
          next={next}
          setAnswers={setAnswers}
          addCustomEthnicity={handleClick}
        />
      ) : (
        <div className="ethnicity-container form-container">
          <div className="form-header">
            <h1>Which ethnicities do you identify with?</h1>
          </div>

          <div className="ethnicity-options">
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
                {["Asian", "White"].map((ethnicity) =>
                  ethnicityButton(ethnicity)
                )}
                <button
                  className="block-button"
                  onClick={() => setOtherEthnicity(true)}
                >
                  Other
                </button>
              </div>
            </div>
          </div>
          <button onClick={handleSave}>Continue</button>
          <button className="secondary-button" onClick={previous}>
            Back
          </button>
        </div>
      )}
    </>
  );
};

export default Ethnicity;
