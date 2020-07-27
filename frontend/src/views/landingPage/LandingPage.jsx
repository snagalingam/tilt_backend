import React from "react";

import Banner from "../../components/banner/Banner";
import Community from "./community/Community";
import NavBar from "../../components/navBar/NavBar";
import Testimonial from "./testimonial/Testimonial";
import TiltButton from "../../components/tiltButton/TiltButton";

import "./landing-page.scss";
import dog from "../../img/dog.png";

const LandingPage = () => {
  return (
    <div className="landing-page-container">
      <NavBar />
      <Banner />
      <Community />
      <div className="tilt-couple">
        <div className="text">
          <h2>Find &#38; select affordable colleges</h2>
          <p>
            Using Tilt to analyze your financial aid packages means never being
            confused again about the loans, scholarships, and costs fr each
            college you have been acepted into. Our reports will provide you
            truee transparency into the cost of college.
          </p>
          <div className="get-started">
            <button className="tilt-button dark">Get Started</button>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
        <div className="image">
          <img src={dog} />
        </div>
      </div>
      <div className="tilt-couple">
        <div className="image">
          <img src={dog} />
        </div>
        <div className="text">
          <h2>Understand financial aid packages</h2>
          <p>
            Using Tilt to analyze your financial aid packages means never beging
            confused again about the loans, scholarships, and costs for each
            college you have been accepted into. Our reports will provide you
            true transparency into the cost of college.
          </p>
          <div className="get-started">
            <TiltButton classes={["dark"]}>Get Started</TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
      </div>
      <div className="black-box">
        <div className="text">
          <h2>The most useful resource ever created</h2>
          <p>
            Using Tilt to analyze your financial aid packages means never beging
            confused again about the loans, scholarships, and costs for each
            college you have been accepted into. Our reports will provide you
            true transparency into the cost of college.
          </p>
          <TiltButton classes={["light"]}>Download Sample</TiltButton>
        </div>
        <div className="image"></div>
      </div>
      <div className="tilt-couple">
        <div className="image">
          <img src={dog} />
        </div>
        <div className="text">
          <h2>Database of vetted scholarships</h2>
          <p>
            Using Tilt to analyze your financial aid packages means never beging
            confused again about the loans, scholarships, and costs for each
            college you have been accepted into. Our reports will provide you
            true transparency into the cost of college.
          </p>
          <div className="get-started">
            <TiltButton classes={["dark"]}>Get Started</TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
      </div>
      <div className="tilt-couple">
        <div className="text">
          <h2>On-demand advisors to answer questions</h2>
          <p>
            Using Tilt to analyze your financial aid packages means never beging
            confused again about the loans, scholarships, and costs for each
            college you have been accepted into. Our reports will provide you
            true transparency into the cost of college.
          </p>
          <div className="get-started">
            <TiltButton classes={["dark"]}>Get Started</TiltButton>
            <div>
              <p>"We tripled our direct orders with Tilt"</p>
              <span>Tamer, Owner of Harvard University</span>
            </div>
          </div>
        </div>
        <div className="image">
          <img src={dog} />
        </div>
      </div>

      <div className="tilt-couple">
        <div classSName="text">
          <h2>Financial aid for students</h2>
        </div>
      </div>

      <Testimonial />
    </div>
  );
};

export default LandingPage;
