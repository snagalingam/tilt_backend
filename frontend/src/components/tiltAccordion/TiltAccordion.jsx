import React, { useState } from "react";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import AddCircleIcon from "@material-ui/icons/AddCircle";
import RemoveCircleIcon from "@material-ui/icons/RemoveCircle";

import "./tilt-accordion.scss";

const ExpandIcon = ({ isExpanded, handleClick }) => {
  return (
    <div className="expand-icon" onClick={handleClick}>
      {isExpanded ? (
        <RemoveCircleIcon className="custom" />
      ) : (
        <AddCircleIcon className="custom" />
      )}
    </div>
  );
};

const TiltAccordion = ({ preview, content }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <Accordion
      className="TiltAccordion"
      square={true}
      expanded={isExpanded}
      onChange={() => setIsExpanded(!isExpanded)}
    >
      <AccordionSummary aria-controls={`${preview}-content`}>
        {preview} <ExpandIcon isExpanded={isExpanded} />
      </AccordionSummary>
      <AccordionDetails>{content}</AccordionDetails>
    </Accordion>
  );
};

export default TiltAccordion;
