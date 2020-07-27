import React from "react";

import "./community-card.scss";

const CommunityCard = ({ img, header, text, step }) => {
  return (
    <div className="community-card">
      <div className="community-image">
        <img src={img} alt="community card" />
        <div>{step}</div>
      </div>
      <h3>{header}</h3>
      <p>{text}</p>
    </div>
  );
};

export default CommunityCard;
