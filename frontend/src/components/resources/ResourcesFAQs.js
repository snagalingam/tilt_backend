import React from 'react';

import NavBar from '../NavBar';
import ResourcesSideNav from './ResourcesSideNav';

const ResourcesFAQs = () => {
  return (
    <body class="bg-light" style={{ paddingTop: "84px" }}>
      <noscript>You need to enable JavaScript to run this app.</noscript>
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
                    Financial Aid
                  </span>
                </li>
                <li class="breadcrumb-item active" aria-current="page">
                  <span class="text-white">
                    FAQs
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
              <h1 class="mb-1">Financial Aid FAQs</h1>
              <br />

              {/* Heading */}
              <h3 class="font-weight-bold">What is financial aid?</h3>

              {/* Text */}
              <p class="text-gray-700">
                Financial aid is any form of funding that helps you pay for college, including scholarships, grants, loans and work-study programs.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold">What’s the difference between loans, grants, and scholarships?</h3>

              {/* Text */}
              <p class="text-gray-700">
                A scholarship is a money-based award specifically designated for education-related expenses. Grants are gift aid awarded to students often based on financial need. They typically come from state government, federal government, non-profit organizations, and schools. A student loan is a type of loan designed to help students pay for post-secondary education. Students must pay back the loan.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold">My parents make “too much money: I won’t qualify.</h3>

              {/* Text */}
              <p class="text-gray-700">
                The reality is there’s no income cut-off to qualify for federal student aid. It doesn’t matter if you have a low or high income, you will still qualify for some type of financial aid, including low-interst student loans.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold">What can I get from financial aid?</h3>

              {/* Text */}
              <p class="text-gray-700">
                Financial aid helps students and their families pay for college by covering higher education expenses, such as tuition and fees, room and board, books and supplies, and transportation.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold">Do I qualify for financial aid?</h3>

              {/* Text */}
              <p class="text-gray-700">
                Requirements includ that you have financial need, are a U.S. citizen or eligible noncitizen, be enrolled in an eligible degree or certificate program at your college or career school, and more.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold">Subsidized vs. Unsubsidized loans?</h3>

              {/* Text */}
              <p class="text-gray-700">
                The U.S. Department of Education pays the interest on a direct subsidized loan whereas you are responsible for paying the interest on a direct unsubsidized loan during all periods.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold">Only students with good grades get financial aid.</h3>

              {/* Text */}
              <p class="text-gray-700">
                While a high grade point average will help a student get into a good school and may help with academic scholarships, most of the federal student aid programs do not take a student’s grades into consideration.
              </p>
            </div>
          </div>
        </div>
      </section>
    </body>
  );
};

export default ResourcesFAQs;
