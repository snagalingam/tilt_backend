import React, { useEffect } from 'react';

import NavBar from '../NavBar';
import ResourcesSideNav from './ResourcesSideNav';


const BG_LIGHT = "bg-light";
const BODY_PADDING = "body-padding";

const ResourcesIntro = () => {
  useEffect(() => {
    document.title = 'Tilt: Resources Introduction';
    document.body.classList.add(BG_LIGHT, BODY_PADDING);
  });

  return (
    <div>
      <NavBar classList=" navbar-light fixed-top bg-white border-bottom" type="fluid" />

      {/* BREADCRUMB
      ================================================== */}
      <nav class="d-lg-none bg-gray-800">
        <div class="container-fluid">
          <div class="row align-items-center">
            <div class="col">

              {/* Breadcrumb */}
              <ol class="breadcrumb">
                <li class="breadcrumb-item">
                  <span class="text-white">
                    Introduction
                  </span>
                </li>
              </ol>

            </div>
            <div class="col-auto">

              {/* Toggler */}
              <div class="navbar-dark">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#sidenavCollapse" aria-controls="sidenavCollapse" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              </div>

            </div>
          </div>
        </div>
      </nav>

      {/* CONTENT
      ================================================== */}
      <section>
        <div class="container-fluid">
          <div class="row">
            <div class="col-12 col-lg-3 col-xl-2 px-lg-0 border-bottom border-bottom-lg-0 border-right-lg border-gray-300 sidenav sidenav-left">

              <ResourcesSideNav />

            </div>
            <div class="col-12 col-lg-8 col-xl-8 offset-lg-3 offset-xl-2 py-7 py-lg-9 px-lg-7">

              {/* Heading */}
              <h1 class="mb-1">Introduction</h1>

              {/* Text */}
              <p class="text-gray-700">
                We have put together some resource to help you navigate financial aid and scholarships.
                <br /><br />
                We will continue to add more throughout the year. If you have any questions, reach out to us at <a href="mailto:hello@tiltaccess.com">hello@tiltaccess.com</a>.
              </p>

              {/* Divider */}
              <hr class="border-gray-300 my-6" />

              {/* Heading */}
              <h2 class="mb-1">Coronavirus Updates & Resources </h2>

              {/* Text */}
              <p class="text-gray-700">
                We know that this is a crazy time, and many of you have questions about college admissions and decisions. We will post whatever resources we can find here to support you through the process.
              </p>

              <div class="row">

                {/* Card */}
                <div class="card mb-4">
                  <div class="card-body">
                    {/* Link */}
                    <h3>
                      Expect Financial Aid Package Delays
                    </h3>

                    {/* Text */}
                    <p class="text-gray-700">
                      Although acceptance decisions have been made, colleges might have to revisit their financial aid packages due to the coronavirus turmoil, so expect delays.
                      <span class="font-weight-bold">Colleges will not revoke a financial offer that has already been sent.</span>
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div class="card mb-4">
                  <div class="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://www.nacacnet.org/college-admission-status-coronavirus" target="_blank" rel="noopener noreferrer">
                        NACAC College Admission Status Update: Coronavirus Impact
                      </a>
                    </h3>

                    {/* Text */}
                    <p class="text-gray-700">
                      This is a central resource for information about changes in college admission events, deposit dates and more as a result of the outbreak.
                      It is curated by the association for college admission counselors.
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div class="card mb-4">
                  <div class="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/document/d/1RIlDMwtaOmudGxMuZsuEfjDW_wH89A_v6EHza5K5HtU/edit" target="_blank" rel="noopener noreferrer">
                        Colleges That Have Changed Deposit Deadline to June 1, 2020
                      </a>
                    </h3>

                    {/* Text */}
                    <p class="text-gray-700">
                      This is a list of colleges that have committed to pushing back their deposit deadline to June 1, 2020.
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div class="card mb-4">
                  <div class="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/spreadsheets/d/1ZOAtzZNAjwxoOQbKzMY2JvMll24LQHBXlpV158qQi0U/htmlview?usp=sharing&fbclid=IwAR1_aaTmZIzngtAQCeJ1m26RsmhO3ARbq67TX9GOYzO4KVSQ-dSFIt42YLU&sle=true&urp=gmail_link#" target="_blank" rel="noopener noreferrer">
                        Upcoming Virtual College Admission Events
                      </a>
                    </h3>

                    {/* Text */}
                    <p class="text-gray-700">
                      This is a list of virtual tour resources and upcoming virtual events put on by colleges.
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div class="card mb-4">
                  <div class="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/spreadsheets/d/13yRLukZxg8EotJWaz9YnH_S-iPEM8QNQY3Xxdv3Kg_E/edit#gid=1908149057" target="_blank" rel="noopener noreferrer">
                        College/University CyberGuidance for Illinois Students
                      </a>
                    </h3>

                    {/* Text */}
                    <p class="text-gray-700">
                      This is a CyberGuidance spreadsheet for colleges and universities to share information with Illinois high school students during their time away from school. 
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default ResourcesIntro;
