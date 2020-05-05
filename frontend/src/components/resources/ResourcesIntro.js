import React, { useEffect, useState } from 'react';

import NavBar from '../NavBar';
import ResourcesSideNav from './ResourcesSideNav';


const BG_LIGHT = "bg-light";
const BODY_PADDING = "body-padding";

const ResourcesIntro = () => {
  const [sideNavCollapsed, setSideNavCollapsed] = useState(true);
  const toggleSideNav = () => setSideNavCollapsed(!sideNavCollapsed);
  const classSideNavCollapsed = sideNavCollapsed ? 'collapse d-lg-block' : 'collapse d-lg-block show';
  const classSideNavToggler = sideNavCollapsed ? 'navbar-toggler collapsed' : 'navbar-toggler';

  useEffect(() => {
    document.title = 'Tilt: Resources Introduction';
    document.body.classList.add(BG_LIGHT, BODY_PADDING);

    return () => { document.body.classList.remove(BG_LIGHT, BODY_PADDING) }
  });

  return (
    <div>
      <NavBar classList=" navbar-light fixed-top bg-white border-bottom" type="fluid" />

      {/* BREADCRUMB
      ================================================== */}
      <nav className="d-lg-none bg-gray-800">
        <div className="container-fluid">
          <div className="row align-items-center">
            <div className="col">

              {/* Breadcrumb */}
              <ol className="breadcrumb">
                <li className="breadcrumb-item">
                  <span className="text-white">
                    Introduction
                  </span>
                </li>
              </ol>

            </div>
            <div className="col-auto">

              {/* Toggler */}
              <div className="navbar-dark">
                <button className={classSideNavToggler} type="button" onClick={toggleSideNav} data-toggle="collapse" data-target="#sidenavCollapse" aria-controls="sidenavCollapse" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>
              </div>

            </div>
          </div>
        </div>
      </nav>

      {/* CONTENT
      ================================================== */}
      <section>
        <div className="container-fluid">
          <div className="row">
            <div className="col-12 col-lg-3 col-xl-2 px-lg-0 border-bottom border-bottom-lg-0 border-right-lg border-gray-300 sidenav sidenav-left">

            <div className={classSideNavCollapsed} id="sidenavCollapse">
              <ResourcesSideNav />
            </div>

            </div>
            <div className="col-12 col-lg-8 col-xl-8 offset-lg-3 offset-xl-2 py-7 py-lg-9 px-lg-7">

              {/* Heading */}
              <h1 className="mb-1">Introduction</h1>

              {/* Text */}
              <p className="text-gray-700">
                We have put together some resource to help you navigate financial aid and scholarships.
                <br /><br />
                We will continue to add more throughout the year. If you have any questions, reach out to us at <a href="mailto:hello@tiltaccess.com">hello@tiltaccess.com</a>.
              </p>

              {/* Divider */}
              <hr className="border-gray-300 my-6" />

              {/* Heading */}
              <h2 className="mb-1">Coronavirus Updates & Resources </h2>

              {/* Text */}
              <p className="text-gray-700">
                We know that this is a crazy time, and many of you have questions about college admissions and decisions. We will post whatever resources we can find here to support you through the process.
              </p>

              <div className="row">

              {/* Card */}
              <div className="card mb-4">
                <div className="card-body">
                  {/* Link */}
                  <h3>
                    <a href="https://www.chronicle.com/article/Here-s-a-List-of-Colleges-/248626?cid=wcontentgrid_hp_1b" target="_blank" rel="noopener noreferrer">
                      Here's a List of Colleges' Plans for Reopening in the Fall
                    </a>
                  </h3>

                  {/* Text */}
                  <p className="text-gray-700">
                    The Chronicle of Higher Education has put together a list of what colleges are planning to do this Fall.
                  </p>
                </div>
              </div>

                {/* Card */}
                <div className="card mb-4">
                  <div className="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/spreadsheets/d/1woEx8bil0ren77H6x-TSje1y_hyJxjnmCiBwa8NTYEQ/edit#gid=0" target="_blank" rel="noopener noreferrer">
                        Virtual Webinars & College Fairs
                      </a>
                    </h3>

                    {/* Text */}
                    <p className="text-gray-700">
                      A list of virtual webinars that are currently going on!
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div className="card mb-4">
                  <div className="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/spreadsheets/d/1woEx8bil0ren77H6x-TSje1y_hyJxjnmCiBwa8NTYEQ/edit#gid=0" target="_blank" rel="noopener noreferrer">
                        Virtual Webinars & College Fairs
                      </a>
                    </h3>

                    {/* Text */}
                    <p className="text-gray-700">
                      A list of virtual webinars that are currently going on!
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div className="card mb-4">
                  <div className="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/document/d/14Mn1CrA-CV5YZAkOZtrMKTmn2O4oL-2EhIXhzXZbO0A/edit?_hsenc=p2ANqtz-93yS8kqKmff-cyAu6H6-DHtrx253JuOkDZm-o3QrIa3m9eYp8MbzZYUuZKl1y5LIP3vd3U8tqeEXJAW_wKce3BhWbidg&_hsmi=86282518#bookmark=id.ymao8324o4p" target="_blank" rel="noopener noreferrer">
                        College Perspectives by Current Students
                      </a>
                    </h3>

                    {/* Text */}
                    <p className="text-gray-700">
                      In response to coronavirus, a group of current students wrote their opinions on each college they are attending.
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div className="card mb-4">
                  <div className="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://www.strivescan.com/virtual/" target="_blank" rel="noopener noreferrer">
                        Strive Virtual College Fair
                      </a>
                    </h3>

                    {/* Text */}
                    <p className="text-gray-700">
                      From Monday, April 20 to Thursday, April 23, 2020, four full days of virtual presentations for juniors to explore college opportunities. 300+ colleges participating.
                    </p>
                  </div>
                </div>

                {/* Card */}
                <div className="card mb-4">
                  <div className="card-body">
                    {/* Link */}
                    <h3>
                      <a href="https://docs.google.com/spreadsheets/u/1/d/1sO7pVos0EvK0BvXoMbnyg00K6r7hXbOQE0HNXF4N4eM/htmlview?usp=sharing&fbclid=IwAR2Kg_sYSYPXB7Fmrfj7YEQS7rQe3AnSYqpGHORtHW5L0WYiIYbfa14S-Y4&utm_campaign=Content&utm_source=hs_email&utm_medium=email&utm_content=85334513&_hsenc=p2ANqtz-9aMHcq6m3jUeYn46lPkNTrvg1fT727me_voMcdhLYOXo7wQpUMT326QfYMo3ZSFVIks4UnWfHNvzHAvLXz2yd-22FpFQ&_hsmi=85334513#" target="_blank" rel="noopener noreferrer">
                        College Virtual Tours
                      </a>
                    </h3>

                    {/* Text */}
                    <p className="text-gray-700">
                      This is a spreadsheet that lists out multiple types of virtual resources to tour colleges.
                    </p>
                  </div>
                </div>

                  {/* Card */}
                  <div className="card mb-4">
                    <div className="card-body">
                      {/* Link */}
                      <h3>
                        Expect Financial Aid Package Delays
                      </h3>

                      {/* Text */}
                      <p className="text-gray-700">
                        Although acceptance decisions have been made, colleges might have to revisit their financial aid packages due to the coronavirus turmoil, so expect delays.
                        <span className="font-weight-bold">Colleges will not revoke a financial offer that has already been sent.</span>
                      </p>
                    </div>
                  </div>

                  {/* Card */}
                  <div className="card mb-4">
                    <div className="card-body">
                      {/* Link */}
                      <h3>
                        <a href="https://www.nacacnet.org/college-admission-status-coronavirus" target="_blank" rel="noopener noreferrer">
                          NACAC College Admission Status Update: Coronavirus Impact
                        </a>
                      </h3>

                      {/* Text */}
                      <p className="text-gray-700">
                        This is a central resource for information about changes in college admission events, deposit dates and more as a result of the outbreak.
                        It is curated by the association for college admission counselors.
                      </p>
                    </div>
                  </div>

                  {/* Card */}
                  <div className="card mb-4">
                    <div className="card-body">
                      {/* Link */}
                      <h3>
                        <a href="https://docs.google.com/document/d/1RIlDMwtaOmudGxMuZsuEfjDW_wH89A_v6EHza5K5HtU/edit" target="_blank" rel="noopener noreferrer">
                          Colleges That Have Changed Deposit Deadline to June 1, 2020
                        </a>
                      </h3>

                      {/* Text */}
                      <p className="text-gray-700">
                        This is a list of colleges that have committed to pushing back their deposit deadline to June 1, 2020.
                      </p>
                    </div>
                  </div>

                  {/* Card */}
                  <div className="card mb-4">
                    <div className="card-body">
                      {/* Link */}
                      <h3>
                        <a href="https://docs.google.com/spreadsheets/d/1ZOAtzZNAjwxoOQbKzMY2JvMll24LQHBXlpV158qQi0U/htmlview?usp=sharing&fbclid=IwAR1_aaTmZIzngtAQCeJ1m26RsmhO3ARbq67TX9GOYzO4KVSQ-dSFIt42YLU&sle=true&urp=gmail_link#" target="_blank" rel="noopener noreferrer">
                          Upcoming Virtual College Admission Events
                        </a>
                      </h3>

                      {/* Text */}
                      <p className="text-gray-700">
                        This is a list of virtual tour resources and upcoming virtual events put on by colleges.
                      </p>
                    </div>
                  </div>

                  {/* Card */}
                  <div className="card mb-4">
                    <div className="card-body">
                      {/* Link */}
                      <h3>
                        <a href="https://docs.google.com/spreadsheets/d/13yRLukZxg8EotJWaz9YnH_S-iPEM8QNQY3Xxdv3Kg_E/edit#gid=1908149057" target="_blank" rel="noopener noreferrer">
                          College/University CyberGuidance for Illinois Students
                        </a>
                      </h3>

                      {/* Text */}
                      <p className="text-gray-700">
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
