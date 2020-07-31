import React from "react";
import SearchIcon from "@material-ui/icons/Search";

import FaqCard from "./faqCard/FaqCard";
import FaqSection from "../../components/faqSection/FaqSection";
import TiltAccordion from "../../components/tiltAccordion/TiltAccordion";
import Footer from "../../components/footer/Footer";

import "./faq-page.scss";

function FaqPage() {
  const searchFunction = (value) => {};

  return (
    <div className="FaqPage view-container">
      <div className="FaqPage__header">
        <h2>How Can We Help You?</h2>
      </div>
      <div className="FaqPage__search">
        <input placeholder="Search for questions" />
        <div>
          <SearchIcon className="search-icon" />
        </div>
      </div>
      <div className="FaqPage__cards">
        <FaqCard />
        <FaqCard />
        <FaqCard />
        <FaqCard />
      </div>

      <FaqSection />

      <div className="FaqPage__footer">
        <Footer />
      </div>
    </div>
  );
}

export default FaqPage;
