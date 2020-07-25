import React, { useState } from "react";

import SatScore from "./SatScore";
import TwoOptions from "../twoOptions/TwoOptions";

const Sat = ({ next, previous, setAnswers }) => {
  const [didTakeSat, setDidTakeSat] = useState(false);

  return (
    <>
      {didTakeSat ? (
        <SatScore
          next={next}
          previous={() => setDidTakeSat(false)}
          setAnswers={setAnswers}
        />
      ) : (
        <div className="sat-container form-container">
          <div className="form-header">
            <h1>Have you taken the SAT yet?</h1>
          </div>
          <TwoOptions
            first="Yes"
            handleFirst={() => setDidTakeSat(true)}
            second="No"
            handleSecond={next}
          />
          <button className="secondary-button" onClick={previous}>
            Back
          </button>
        </div>
      )}
    </>
  );
};

export default Sat;
