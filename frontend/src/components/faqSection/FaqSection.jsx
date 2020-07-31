import React, { useEffect, useState } from "react";

import TiltAccordion from "../tiltAccordion/TiltAccordion";
import { faqs } from "../../helper/faqs";

import "./faq-section.scss";

function FaqSection() {
  const [columnOne, setColumnOne] = useState([]);
  const [columnTwo, setColumnTwo] = useState([]);

  const divideFaqs = () => {
    const one = [];
    const two = [];
    for (let i = 0; i < faqs.length; i++) {
      const { preview, content } = faqs[i];
      if (i % 2 === 0) {
        one.push(
          <TiltAccordion key={preview} preview={preview} content={content} />
        );
      } else {
        two.push(
          <TiltAccordion key={preview} preview={preview} content={content} />
        );
      }
    }
    setColumnOne((prev) => [...prev, ...one]);
    setColumnTwo((prev) => [...prev, ...two]);
  };

  useEffect(() => {
    divideFaqs();
  }, []);

  return (
    <div className="FaqSection">
      <h2>Frequently Asked Questions</h2>
      <div className="FaqSection_columns">
        <div className="FaqSection_column-1">{columnOne}</div>
        <div className="FaqSection_column-2">{columnTwo}</div>
      </div>
    </div>
  );
}

export default FaqSection;
