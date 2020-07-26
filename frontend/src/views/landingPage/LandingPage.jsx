import React from "react";

import Banner from "../../components/banner/Banner";
import NavBar from "../../components/navBar/NavBar";

import "./landing-page.scss";

const LandingPage = () => {
  return (
    <div className="landing-page-container">
      <NavBar />
      <Banner />
      {/* <Community />
      <div>
        <Information />
        <Information />
        <BlackBox />
        <Information />
        <Information />
        <Testimonials />
      </div>
      <FrequentlyAskedQuestions />
      <BlackBox />
      <Footer /> */}
    </div>
  );
};

export default LandingPage;
