import React, { useEffect } from 'react';

import NavBar from '../NavBar';
import ResourcesSideNav from './ResourcesSideNav';


const BG_LIGHT = "bg-light";
const BODY_PADDING = "body-padding";

const Terminology = () => {
  useEffect(() => {
    document.title = 'Tilt: Terminology';
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
                    Financial Aid
                  </span>
                </li>
                <li className="breadcrumb-item active" aria-current="page">
                  <span className="text-white">
                    Terminology
                  </span>
                </li>
              </ol>

            </div>
            <div className="col-auto">

              {/* Toggler */}
              <div className="navbar-dark">
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#sidenavCollapse" aria-controls="sidenavCollapse" aria-expanded="false" aria-label="Toggle navigation">
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

              <ResourcesSideNav />

            </div>
            <div className="col-12 col-lg-8 col-xl-8 offset-lg-3 offset-xl-2 py-7 py-lg-9 px-lg-7">

              {/* Heading */}
              <h1 className="mb-1" id="alerts">Financial Aid Terminology</h1>

              {/* Text */}
              <p className="font-size-lg text-gray-700">
                Financial aid can be confusing, especially with all the different words that they use. Here is a quick reference sheet if you get confused.
              </p>

              {/* Divider */}
              <hr className="border-gray-300 my-6" />

              {/* Heading */}
              <h3 className="font-weight-bold" id="whyFigma">Costs</h3>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Total Costs =</span> Direct Costs + Personal Expenses
              </p>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Direct Costs:</span> This is what the college will charge you. It includes tuition & fees and room & board (aka rent and a meal plan).
              </p>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Personal Expenses (also known as Indirect Costs):</span> This is for other living expenses that you don’t directly pay to the college. Usually, these are just estimated, and it depends on how much you spend. It generally includes textbooks, personal expenses, and transportation. We will use the same $5,000 amount for every college.
              </p>

              {/* Divider */}
              <hr className="border-gray-300 my-6" />

              {/* Heading */}
              <h3 className="font-weight-bold" id="whyFigma">Types of Money Offered</h3>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Gift Aid (also known as Grants and Scholarships):</span> A gift that college or taxpayers are giving you to pay for your school that does not need to be repaid! Keep in mind that this amount may vary every year.
              </p>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Loans:</span> This is money that you are borrowing and needs to be repaid with interest. Interest is basically a fee that you pay someone for borrowing their money. You have to pay back how much you borrowed plus interest.
              </p>


              {/* List */}
              <ul className="text-gray-700">
                <li className="p-2">
                  <span className="font-weight-bold text-primary">Federal Subsidized Loan::</span> For this loan, the federal government pays the interest while you are 	in school at least half-time.
                </li>
                <li className="p-2">
                  <span className="font-weight-bold text-primary">Federal Unsubsidized Loan:</span> For this loan, you have to pay the interest that accrues while you 	are attending school.
                </li>
                <li className="p-2">
                  <span className="font-weight-bold text-primary">Parent PLUS Loan:</span> This is another type of federal loan that your parent can apply for, but they 	can’t have bad credit history.
                </li>
                <li className="p-2">
                  <span className="font-weight-bold text-primary">Private Student Loan:</span> If you can’t get any more federal loans, you can then borrow money from 	private companies to help pay for your school.
                </li>
              </ul>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Work-Study:</span> This is the maximum amount of money you can get from a specific part-time job that the federal government subsidizes. However, you are still responsible to apply for and get a job.
              </p>

              {/* Heading */}
              <h3 className="font-weight-bold" id="whyFigma">Calculations</h3>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Your Cost (also known as Net Price):</span> This is how much you will have to pay to attend college. To calculate this, we take the total costs and subtract gift aid.
                <br />
                Your Cost = Total Costs - Gift Aid
              </p>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold text-primary">Tuition Bill:</span> This is the amount that you will have to pay directly to the college at the start of the semester.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Terminology;
