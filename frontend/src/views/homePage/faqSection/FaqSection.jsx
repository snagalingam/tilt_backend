import React from "react";

import TiltAccordion from "../../../components/tiltAccordion/TiltAccordion";

import "./faq-section.scss";

const FaqSection = () => {
  return (
    <div className="tilt-faq">
      <div className="faq-container">
        <h2>Frequently Asked Questions</h2>
        <div>
          <div>
            <TiltAccordion
              preview="What is financial aid?"
              content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
            <TiltAccordion
              preview="Do I qualify for financial aid?"
              content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
            <TiltAccordion
              preview="Don't only students with good grades receive financial aid?"
              content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
          </div>
          <div>
            <TiltAccordion
              preview="How does financial aid work?"
              content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
            <TiltAccordion
              preview={`What if my parents make "too much money"?`}
              content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
            <TiltAccordion
              preview="Will this service always be free?"
              content="Yes, we are commited to helping students access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default FaqSection;
