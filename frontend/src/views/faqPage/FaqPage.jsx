import React from "react";
import SearchIcon from "@material-ui/icons/Search";

import FaqCard from "./faqCard/FaqCard";
import TiltAccordion from "../../components/tiltAccordion/TiltAccordion";
import Footer from "../../components/footer/Footer";

import "./faq-page.scss";

function FaqPage() {
  return (
    <div className="faq-page-container">
      <h1>How Can We Help You?</h1>
      <div className="faq-search">
        <input placeholder="Search for questions" />
        <div>
          <SearchIcon className="search-icon" />
        </div>
      </div>
      <div className="faq-cards">
        <FaqCard />
        <FaqCard />
        <FaqCard />
        <FaqCard />
      </div>
      <div className="faq-accordions">
        <div>
          <TiltAccordion preview="What is financial aid?" content="money" />
          <TiltAccordion preview="What is financial aid?" content="money" />
          <TiltAccordion preview="What is financial aid?" content="money" />
          <TiltAccordion preview="What is financial aid?" content="money" />
        </div>
        <div>
          <TiltAccordion preview="What is financial aid?" content="money" />
          <TiltAccordion preview="What is financial aid?" content="money" />
          <TiltAccordion preview="What is financial aid?" content="money" />
          <TiltAccordion preview="What is financial aid?" content="money" />
        </div>
      </div>
      <div className="faq-footer">
        <Footer />
      </div>
    </div>
  );
}

export default FaqPage;
