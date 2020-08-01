import React from "react";

import "./brushed-text.scss";

const BrushedText = ({ text }) => {
  return (
    <span className="BrushedText">
      <img
        src="https://res.cloudinary.com/dgbm9hshy/image/upload/v1595957271/path2987_lp398q.png"
        alt="purple brush stroke"
      />
      <div className="BrushedText__text">{text}</div>
    </span>
  );
};

export default BrushedText;
