import React from 'react';

import NavBar from '../NavBar';
import ResourcesSideNav from './ResourcesSideNav';


const Terminology = () => {
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
                    Terminology
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
              <h1 class="mb-1" id="alerts">Financial Aid Terminology</h1>

              {/* Text */}
              <p class="font-size-lg text-gray-700">
                Financial aid can be confusing, especially with all the different words that they use. Here is a quick reference sheet if you get confused.
              </p>

              {/* Divider */}
              <hr class="border-gray-300 my-6" />

              {/* Heading */}
              <h3 class="font-weight-bold" id="whyFigma">Costs</h3>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Total Costs =</span> Direct Costs + Personal Expenses
              </p>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Direct Costs:</span> This is what the college will charge you. It includes tuition & fees and room & board (aka rent and a meal plan).
              </p>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Personal Expenses (also known as Indirect Costs):</span> This is for other living expenses that you don’t directly pay to the college. Usually, these are just estimated, and it depends on how much you spend. It generally includes textbooks, personal expenses, and transportation. We will use the same $5,000 amount for every college.
              </p>

              {/* Divider */}
              <hr class="border-gray-300 my-6" />

              {/* Heading */}
              <h3 class="font-weight-bold" id="whyFigma">Types of Money Offered</h3>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Gift Aid (also known as Grants and Scholarships):</span> A gift that college or taxpayers are giving you to pay for your school that does not need to be repaid! Keep in mind that this amount may vary every year.
              </p>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Loans:</span> This is money that you are borrowing and needs to be repaid with interest. Interest is basically a fee that you pay someone for borrowing their money. You have to pay back how much you borrowed plus interest.
              </p>


              {/* List */}
              <ul class="text-gray-700">
                <li class="p-2">
                  <span class="font-weight-bold text-primary">Federal Subsidized Loan::</span> For this loan, the federal government pays the interest while you are 	in school at least half-time.
                </li>
                <li class="p-2">
                  <span class="font-weight-bold text-primary">Federal Unsubsidized Loan:</span> For this loan, you have to pay the interest that accrues while you 	are attending school.
                </li>
                <li class="p-2">
                  <span class="font-weight-bold text-primary">Parent PLUS Loan:</span> This is another type of federal loan that your parent can apply for, but they 	can’t have bad credit history.
                </li>
                <li class="p-2">
                  <span class="font-weight-bold text-primary">Private Student Loan:</span> If you can’t get any more federal loans, you can then borrow money from 	private companies to help pay for your school.
                </li>
              </ul>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Work-Study:</span> This is the maximum amount of money you can get from a specific part-time job that the federal government subsidizes. However, you are still responsible to apply for and get a job.
              </p>

              {/* Heading */}
              <h3 class="font-weight-bold" id="whyFigma">Calculations</h3>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Your Cost (also known as Net Price):</span> This is how much you will have to pay to attend college. To calculate this, we take the total costs and subtract gift aid.
                <br />
                Your Cost = Total Costs - Gift Aid
              </p>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold text-primary">Tuition Bill:</span> This is the amount that you will have to pay directly to the college at the start of the semester.
              </p>
            </div>
          </div>
        </div>
      </section>
    </body>
  );
};

export default Terminology;