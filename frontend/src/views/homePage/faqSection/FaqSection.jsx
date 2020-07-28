import React from "react";

import TiltAccordion from "../../../components/tiltAccordion/TiltAccordion";

import "./faq-section.scss";

const FaqSection = () => {
  return (
    <div className="tilt-faq">
      <h2>Frequently Asked Questions</h2>
      <div>
        <div>
          <TiltAccordion
            preview="What is financial aid?"
            content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
          />
          <TiltAccordion
            preview="What is financial aid?"
            content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
          />
        </div>
        <div>
          <TiltAccordion
            preview="What is financial aid?"
            content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
          />
          <TiltAccordion
            preview="What is financial aid?"
            content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
          />
        </div>
        <div>
          <TiltAccordion
            preview="What is financial aid?"
            content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
          />
          <TiltAccordion
            preview="What is financial aid?"
            content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
          />
        </div>
      </div>
      <div></div>
    </div>
  );
};

export default FaqSection;
