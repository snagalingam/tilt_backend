import React, { useState } from "react";

import ActScore from "./ActScore";
import TwoOptions from "../twoOptions/TwoOptions";

const Act = ({ next, previous, setAnswers }) => {
  const [didTakeAct, setDidTakeAct] = useState(false);

  return (
    <>
      {didTakeAct ? (
        <ActScore
          next={next}
          previous={() => setDidTakeAct(false)}
          setAnswers={setAnswers}
        />
      ) : (
        <div className="act-container form-container">
          <div className="form-header">
            <h1>Have you taken the ACT yet?</h1>
          </div>
          <TwoOptions
            first="Yes"
            handleFirst={() => setDidTakeAct(true)}
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

export default Act;
