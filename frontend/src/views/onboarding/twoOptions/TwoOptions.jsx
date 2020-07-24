import React from "react";

import "./two-options.scss";

const TwoOptions = ({ first, handleFirst, second, handleSecond }) => {
  return (
    <div className="two-options">
      <button className="block-button" onClick={handleFirst}>
        {first}
      </button>
      <button className="block-button" onClick={handleSecond}>
        {second}
      </button>
    </div>
  );
};

export default TwoOptions;
