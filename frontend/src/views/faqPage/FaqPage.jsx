import React, { useState, useRef } from "react";
import SearchIcon from "@material-ui/icons/Search";
import { debounce } from "throttle-debounce";
import anime from "animejs/lib/anime.es.js";

import FaqCard from "./faqCard/FaqCard";
import FaqSection from "../../components/faqSection/FaqSection";
import Footer from "../../components/footer/Footer";

import { faqs } from "../../helper/faqs";

import "./faq-page.scss";
import { useEffect } from "react";

function FaqPage() {
  const [searchResults, setSearchResults] = useState([]);
  const [searchString, setSearchString] = useState("");

  const searchFunction = debounce(500, (target) => {
    const { value } = target;
    setSearchString(value);
    if (!value) {
      setSearchResults([]);
    } else {
      const regex = new RegExp(value.toLowerCase());
      const results = faqs.filter((faq) => {
        if (
          faq.content.toLowerCase().match(regex) ||
          faq.preview.toLowerCase().match(regex)
        ) {
          return { ...faq };
        }
      });
      setSearchResults([...results]);
    }
  });

  const faqCardsRef = useRef(null);
  const searchResultsRef = useRef(null);
  useEffect(() => {
    if (searchResultsRef.current && faqCardsRef.current) {
      if (searchString) {
        console.log(searchResultsRef.current);
        anime({
          targets: searchResultsRef.current,
          translateX: 0,
          opacity: 1,
          easing: "linear",
          duration: 250,
        });
        anime({
          targets: faqCardsRef.current,
          translateX: 0,
          opacity: 0,
          easing: "linear",
          duration: 250,
        });
      } else {
        anime({
          targets: searchResultsRef.current,
          translateX: -searchResultsRef.current.clientWidth,
          opacity: 0,
          easing: "linear",
          duration: 250,
        });
        anime({
          targets: faqCardsRef.current,
          translateX: -faqCardsRef.current.clientWidth,
          opacity: 1,
          easing: "linear",
          duration: 250,
        });
      }
    }
  }, [searchResults]);

  return (
    <div className="FaqPage view-container">
      <div className="FaqPage__header">
        <h2>How Can We Help You?</h2>
      </div>
      <div className="FaqPage__search">
        <input
          placeholder="Search for questions"
          onChange={(e) => searchFunction(e.target)}
        />
        <div>
          <SearchIcon className="search-icon" />
        </div>
      </div>
      <div className="FaqPage__slide">
        <div className="FaqPage__search-results" ref={searchResultsRef}>
          <FaqSection searchResults={searchResults} />
        </div>
        <div className="FaqPage__cards" ref={faqCardsRef}>
          <FaqCard question="What is financial aid?" />
          <FaqCard question="How does financial aid work?" />
          <FaqCard question="Do I qualify for financial aid?" />
          <FaqCard question="Will this service always be free?" />
        </div>
      </div>

      <div className="FaqPage__faq-section">
        <FaqSection />
      </div>

      <div className="FaqPage__footer">
        <Footer />
      </div>
    </div>
  );
}

export default FaqPage;
