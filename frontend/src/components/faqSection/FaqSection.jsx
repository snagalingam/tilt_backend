import React, { memo, useEffect, useState } from "react";

import TiltAccordion from "../tiltAccordion/TiltAccordion";
import { faqs } from "../../helper/faqs";

import "./faq-section.scss";

function FaqSection({ searchResults }) {
  const [columnOne, setColumnOne] = useState([]);
  const [columnTwo, setColumnTwo] = useState([]);

  const toBeDisplayed = searchResults ? searchResults : faqs;

  const divideFaqs = () => {
    const one = [];
    const two = [];

    for (let i = 0; i < toBeDisplayed.length; i++) {
      const { preview, content } = toBeDisplayed[i];
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
    setColumnOne(one);
    setColumnTwo(two);
  };

  useEffect(() => {
    divideFaqs();
  }, [searchResults]);

  return (
    <div className="FaqSection">
      <h2>{searchResults ? "Search Results" : "Frequently Asked Questions"}</h2>
      <div className="FaqSection_columns">
        {columnOne.length > 0 && (
          <>
            <div className="FaqSection_column-1">{columnOne}</div>
            <div className="FaqSection_column-2">{columnTwo}</div>
          </>
        )}
        {searchResults?.length === 0 && <h3>No Search Results</h3>}
      </div>
    </div>
  );
}

function areEqual(prevProps, props) {
  return prevProps.searchResults === props.searchResults;
}

export default memo(FaqSection, areEqual);
