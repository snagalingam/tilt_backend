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
              content="Financial aid is any form of funding that helps you pay for college, including scholarships, grants, loans and work-study programs."
            />
            <TiltAccordion
              preview="Do I qualify for financial aid?"
              content="To qualify for financial aid, you have to be a U.S. citizen or eligible noncitizen and be enrolled in a degree or certificate program at your college or career school. That’s it! If you are an undocumented student, you might be able to apply for state financial aid."
            />
            <TiltAccordion
              preview="Don't only students with good grades receive financial aid?"
              content="That is a common misconception. You can receive financial aid for a variety of reasons, and good grades is only one reason. No matter what your grades are, you should always apply for financial aid."
            />
          </div>
          <div>
            <TiltAccordion
              preview="How does financial aid work?"
              content="To receive financial aid, you must submit financial aid forms, generally the FAFSA (Free Application for Federal Student Aid). Once you have been accepted to a college, they will send you a financial aid package. You can appeal and negotiate for more funds if you would like. When school starts, the financial aid is used to pay your student bills first, and then, you can take the leftover money to pay the rest of your expenses."
            />
            <TiltAccordion
              preview={`What if my parents make "too much money"?`}
              content="The reality is there’s no income cut-off to qualify for federal student aid. It doesn’t matter if you have a low or high income, you will still qualify for some type of financial aid, including low-interest student loans."
            />
            <TiltAccordion
              preview="Will this service always be free?"
              content="Yes, we are committed to helping students and families access financial aid free-of-charge. We only charge schools and organizations for additional services to help their students."
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default FaqSection;
