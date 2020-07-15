import React from "react";

import "./tilt-button.scss";

const TiltButton = ({ type = "button", handleClick, children, disabled }) => {
  return (
    <button
      disabled={disabled}
      className="tilt-button"
      onClick={handleClick}
      type={type}
    >
      {children}
    </button>
  );
};

export default TiltButton;
