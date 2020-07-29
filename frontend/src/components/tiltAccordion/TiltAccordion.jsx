import React from "react";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";

import "./tilt-accordion.scss";

const TiltAccordion = ({ preview, content }) => {
  return (
    <Accordion className="tilt-accordion" square={true}>
      <AccordionSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls={`${preview}-content`}
      >
        {preview}
      </AccordionSummary>
      <AccordionDetails>{content}</AccordionDetails>
    </Accordion>
  );
};

export default TiltAccordion;
