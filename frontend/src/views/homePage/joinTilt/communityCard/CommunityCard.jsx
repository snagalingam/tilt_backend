import React from "react";

import "./community-card.scss";

const CommunityCard = ({ card, header, text, step, stepColor }) => {
  return (
    <div className="CommunityCard">
      <div className="CommunityCard__image">
        {card}
        <div className={`step ${stepColor}`}>{step}</div>
      </div>
      <h3>{header}</h3>
      <p>{text}</p>
    </div>
  );
};

export default CommunityCard;
