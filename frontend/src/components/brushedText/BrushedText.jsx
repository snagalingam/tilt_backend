import React from "react";

import "./brushed-text.scss";

const BrushedText = ({ text }) => {
  return (
    <span className="stroke">
      <img src="https://res.cloudinary.com/dgbm9hshy/image/upload/v1595957271/path2987_lp398q.png" />
      <div className="stroke-text">{text}</div>
    </span>
  );
};

export default BrushedText;
