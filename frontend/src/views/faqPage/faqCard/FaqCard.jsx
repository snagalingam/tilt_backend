import React from "react";

import "./faq-card.scss";

function FaqCard({ question }) {
  return (
    <div className="FaqCard">
      <div className="FaqCard__help-icon">
        <div>?</div>
      </div>
      <div className="FaqCard__question">{question}</div>
    </div>
  );
}

export default FaqCard;
