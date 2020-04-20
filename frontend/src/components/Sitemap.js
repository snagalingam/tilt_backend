import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

import Footer from './Footer';
import NavBar from './NavBar';

const Sitemap = () => {
  useEffect(() => {
    document.title = 'Sitemap: Tilt';
  });

  return (
    <div>
      <NavBar classList=" navbar-light bg-white" type="boxed" />
      {/* WELCOME
      ================================================== */}
      <section class="pt-8 pt-md-11 pb-8 pb-md-14">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-12 col-md">

              <h1 class="display-4 mb-2">
                Sitemap
              </h1>

            </div>
          </div>
          <div class="row">
            <div class="col-12">

              <h2 class="mt-7">
                  General
              </h2>

              <h3>
                <Link to="/">
                  Home
                </Link>
              </h3>

              <h3>
                <Link to="/contact">
                  Contact Us
                </Link>
              </h3>

              <h3>
                <Link to="/privacy-policy">
                  Privacy Policy
                </Link>
              </h3>

              <h3>
                <Link to="/terms-of-service">
                  Terms of Service
                </Link>
              </h3>
            </div>
          </div>
          <div class="row">
            <div class="col-12">

              {/* Divider */}
              <hr class="my-6 my-md-8" />

            </div>
          </div>
          <div class="row">
            <div class="col-12">

              <h2>
                  Resources
              </h2>

              <h3>
                <Link to="/resources">
                  Overview
                </Link>
              </h3>

              <h3>
                <Link to="/resources/faqs">
                  Financial Aid FAQs
                </Link>
              </h3>

              <h3>
                <Link to="/resources/scholarships">
                  Scholarships
                </Link>
              </h3>

              <h3>
                <Link to="/resources/terminology">
                  Terminology
                </Link>
              </h3>
            </div>
          </div>

        </div>
      </section>

      {/* SHAPE
      ================================================== */}
      <div class="position-relative">
        <div class="shape shape-bottom shape-fluid-x svg-shim text-dark">
          <svg viewBox="0 0 2880 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 48H1437.5H2880V0H2160C1442.5 52 720 0 720 0H0V48Z" fill="currentColor"/>
          </svg>
        </div>
      </div>
      <Footer classList=" bg-dark"/>
    </div>
  );
};

export default Sitemap;
