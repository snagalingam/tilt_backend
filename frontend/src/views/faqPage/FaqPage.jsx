import React, { useEffect, useRef, useState } from "react";
import SearchIcon from "@material-ui/icons/Search";
import { debounce } from "throttle-debounce";
import anime from "animejs/lib/anime.es.js";

import FaqCard from "./faqCard/FaqCard";
import FaqSection from "../../components/faqSection/FaqSection";
import Footer from "../../components/footer/Footer";

import { faqs } from "../../helper/faqs";

import "./faq-page.scss";

function FaqPage() {
  const [searchResults, setSearchResults] = useState([]);
  const [searchString, setSearchString] = useState("");

  const faqCardsRef = useRef(null);
  const searchResultsRef = useRef(null);

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

  const handleAnimation = (zeroDuration) => {
    if (searchResultsRef.current && faqCardsRef.current) {
      if (searchString) {
        anime({
          targets: searchResultsRef.current,
          translateX: -searchResultsRef.current.clientWidth,
          opacity: 1,
          easing: "linear",
          duration: zeroDuration ? 0 : 300,
        });
        anime({
          targets: faqCardsRef.current,
          translateX: -searchResultsRef.current.clientWidth,
          opacity: 0,
          easing: "linear",
          duration: zeroDuration ? 0 : 300,
        });
      } else {
        anime({
          targets: searchResultsRef.current,
          translateX: 0,
          opacity: 0,
          easing: "linear",
          duration: zeroDuration ? 0 : 300,
        });
        anime({
          targets: faqCardsRef.current,
          translateX: 0,
          opacity: 1,
          easing: "linear",
          duration: zeroDuration ? 0 : 300,
        });
      }
    }
  };

  const handleResize = () => {
    handleAnimation(true);
  };

  useEffect(() => {
    handleAnimation();
  }, [searchResults]);

  useEffect(() => {
    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

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
        <div className="FaqPage__cards" ref={faqCardsRef}>
          <FaqCard question="What is financial aid?" />
          <FaqCard question="How does financial aid work?" />
          <FaqCard question="Do I qualify for financial aid?" />
          <FaqCard question="Will this service always be free?" />
        </div>
        <div className="FaqPage__search-results" ref={searchResultsRef}>
          <FaqSection searchResults={searchResults} />
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
