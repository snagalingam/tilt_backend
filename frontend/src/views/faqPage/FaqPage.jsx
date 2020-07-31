import React from "react";
import SearchIcon from "@material-ui/icons/Search";

import FaqCard from "./faqCard/FaqCard";
import TiltAccordion from "../../components/tiltAccordion/TiltAccordion";
import Footer from "../../components/footer/Footer";

import "./faq-page.scss";

function FaqPage() {
  return (
    <div className="faq-page-container view-container">
      <div>
        <h2>How Can We Help You?</h2>
      </div>
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
          <TiltAccordion
            preview="What is financial aid?"
            content="Financial aid is any form of funding that helps you pay for college, including scholarships, grants, loans and work-study programs."
          />
          <TiltAccordion
            preview="What’s the difference between loans, grants, and scholarships?"
            content="A scholarship is a money-based award specifically designated for education-related expenses. Grants are gift aid awarded to students often based on financial need. They typically come from state government, federal government, non-profit organizations, and schools. A student loan is a type of loan designed to help students pay for post-secondary education. Students must pay back the loan."
          />
          <TiltAccordion
            preview="My parents make “too much money: I won’t qualify."
            content="The reality is there’s no income cut-off to qualify for federal student aid. It doesn’t matter if you have a low or high income, you will still qualify for some type of financial aid, including low-interst student loans."
          />
          <TiltAccordion
            preview="What can I get from financial aid?"
            content="Financial aid helps students and their families pay for college by covering higher education expenses, such as tuition and fees, room and board, books and supplies, and transportation."
          />
        </div>
        <div>
          <TiltAccordion
            preview="Do I qualify for financial aid?"
            content="Requirements includ that you have financial need, are a U.S. citizen or eligible noncitizen, be enrolled in an eligible degree or certificate program at your college or career school, and more."
          />
          <TiltAccordion
            preview="Subsidized vs. Unsubsidized loans?"
            content="money"
          />
          <TiltAccordion
            preview="Only students with good grades get financial aid."
            content="While a high grade point average will help a student get into a good school and may help with academic scholarships, most of the federal student aid programs do not take a student’s grades into consideration."
          />
        </div>
      </div>
      <div className="faq-footer">
        <Footer />
      </div>
    </div>
  );
}

export default FaqPage;
