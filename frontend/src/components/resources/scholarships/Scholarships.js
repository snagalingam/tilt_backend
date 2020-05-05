import React, { useEffect, useState } from 'react';

import NavBar from '../../NavBar';
import ResourcesSideNav from '../ResourcesSideNav';


const BG_LIGHT = "bg-light";
const BODY_PADDING = "body-padding";

const Scholarships = () => {
  const [sideNavCollapsed, setSideNavCollapsed] = useState(true);
  const toggleSideNav = () => setSideNavCollapsed(!sideNavCollapsed);
  const classSideNavCollapsed = sideNavCollapsed ? 'collapse d-lg-block' : 'collapse d-lg-block show';
  const classSideNavToggler = sideNavCollapsed ? 'navbar-toggler collapsed' : 'navbar-toggler';

  useEffect(() => {
    document.title = 'Tilt: Scholarships';
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
                    Scholarships
                  </span>
                </li>
                <li className="breadcrumb-item active" aria-current="page">
                  <span className="text-white">
                    Links
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
              <h1 className="mb-1">Scholarship Links</h1>
              <br />

              {/* Month */}
              <h2 className="font-weight-bold">May</h2>

              {/* Scholarship */}
              <a href="https://www.angelswingsfoundation.org/angels-wings-thai-scholarship-2020" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Angels Wings Thai Scholarships</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 18, 2020<br />
                <span className="font-weight-bold">Amount:</span> $10,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have at least a 3.0 GPA and identify as Thai.
              </p>

              {/* Scholarship */}
              <a href="http://www.upakar.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Upakar Indian-American Scholarship Foundation Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as Indian, be US citizens with financial need, and have at least a 3.60 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://lmofoundation.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Gladys Lewis HBCU Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have demonstrated commitment to community service, identify as women, have at least a 2.75 GPA, and attend an HBCU.
              </p>

              {/* Scholarship */}
              <a href="http://lmofoundation.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Jessie M. Shaw Merit Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Students must have demonstrated commitment to community service, identify as women, and have at least a 3.30 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://lmofoundation.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Claudette McFarland Winstead Need Based Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have a demonstrated interest in community service, identify as women, have at least a 2.75 GPA, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="http://www.revgruffoloscholarship.com" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Rev. George Ruffolo Memorial Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from Cook County, IL with at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://www.vaneseagape.org/apply" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Keisha Bodden Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be US Citizens with financial need, have at least a 2.75 GPA, and be from Florida.
              </p>

              {/* Scholarship */}
              <a href="https://www.maxwell.org/guidelines" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">The Edmund F. Maxwell Foundation</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from Washington and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.thecha.org/residents/chicago-housing-authority-scholarship-program" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Chicago Housing Authority Scholarship Program</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 14, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be listed on a Chicago Housing Authoritty lease and have at least a 2.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://www.illinoishotels.org/Scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">IHLAEF Scholarships</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 14, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000 - $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be US citizens from Illinois and pursuing a degree in hospitality.
              </p>

              {/* Scholarship */}
              <a href="https://azdchipsi.org/buell/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Temple Hoyne Buell Memorial Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 9, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be entering freshmen at UIUC and identify as men.
              </p>

              {/* Scholarship */}
              <a href="https://www.fiestadelsol.org/scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Fiesta del Sol Guadalupe A. Reyes Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as Latinx.
              </p>

              {/* Scholarship */}
              <a href="https://cps.academicworks.com/opportunities/3354" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Lakeside Bank "Write On!" Creative Writing Challenge</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be students at Chicago Public Schools with financial need.
              </p>

              {/* Scholarship */}
              <a href="https://bhw.hrsa.gov/loans-scholarships/nurse-corps/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">NURSE Corps Scholarship Program</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be pursuing a nursing degree and be US citizens with financial need.
              </p>

              {/* Scholarship */}
              <a href="https://allwomeninmedia.org/ford-emerging-voices-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Ford Emerging Voices Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000 or $3,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as women and be interested in journalism.
              </p>

              {/* Scholarship */}
              <a href="https://www.beccascloset.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Becca's Closet Scholarships</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have demonstrated commitment to community service with at least a 2.0 GPA. Both US citizens and DACA students can apply.
              </p>

              {/* Scholarship */}
              <a href="https://www.isee.org/students" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">SEE Education Foundation Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500 - $7,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have financial need and be pursuing a degree related to the explosives industry.
              </p>

              {/* Scholarship */}
              <a href="https://whitakerwatercolors.org/the-foundation/the-foundation-scholarship-fund-and-application/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">The Foundation Scholarship Fund</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 5, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be interested in art and be US citizens with at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.thermofisher.com/us/en/home/life-science/antibodies/thermo-fisher-scientific-antibody-scholarship-program.html" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Thermo Fischer Antibody Scholarship Program</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 5, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000 - $10,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be pursuing a degree in life sciences and be US citizens with at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.cgcs.org/Scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">CGCS - Bernard Harris Scholars </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 4, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be pursuing a degree in STEM with a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.calculatedgenius.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Steminist Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 3, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from Chicago, IL and pursuing a degree in STEM, and identify as women with at least a 3.0 GPA. Both US citizens and DACA students can apply.
              </p>

              {/* Scholarship */}
              <a href="https://www.chicagoengineersfoundation.org/awards/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Chicago Engineer Foundation Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from Chicago with at least a 2.5 GPA and be pursuing an engineering degree.
              </p>

              {/* Scholarship */}
              <a href="https://www.jssa.org/get-help/scholarships/scholarships-for-undergraduate-students/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Morton A. Gibson Memorial Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from the Metro DC area, identify as Jewish, be a US citizen, and have demonstrated community service.
              </p>

              {/* Scholarship */}
              <a href="https://www.jssa.org/get-help/scholarships/scholarships-for-undergraduate-students/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Max and Emmy Dreyfuss Jewish Undergrad Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $4,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from the Metro DC area, identify as Jewish, and be a US citizen.
              </p>

              {/* Scholarship */}
              <a href="https://www.jssa.org/get-help/scholarships/scholarships-for-undergraduate-students/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">JSSA Educational Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $6,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from the Montgomery County in Maryland, identify as Jewish, be a US citizen, and have demonstrated need.
              </p>

              {/* Month */}
              <h2 className="font-weight-bold">April</h2>

              {/* Scholarship */}
              <a href="http://globalsportsdevelopment.org/exceptional-youth-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Global Sports Development: Exceptional Youth Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $10,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be US citizen with at least a 3.0 GPA and have participated in community service.
              </p>

              {/* Scholarship */}
              <a href="https://www.jccia.com/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">John Fischetti Scholarship Award 2020</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as Italian, be from Chicago, and interested in pursuing journalism.
              </p>

              {/* Scholarship */}
              <a href="https://www.edisonparkcc.com/jill-doherty-memorial-scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Jill Doherty Memorial Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from Edison Park in Chicago and have participted in community service.
              </p>

              {/* Scholarship */}
              <a href="http://www.joshgardnerendowment.org/application/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Joshua David Gardner Memorial Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a US citizen with at least a 2.8 GPA and attending an HBCU.
              </p>

              {/* Scholarship */}
              <a href="https://www.maeandmarylegacyfoundation.org/apply" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Mae & Mary Scholarship Fund </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be African American and interested in the health care field.
              </p>

              {/* Scholarship */}
              <a href="https://www.niche.com/about/scholarship-rules/no-essay-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Niche "No Essay" Scholarship Fund</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be US citizens.
              </p>

              {/* Scholarship */}
              <a href="http://brownmae.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Norman Brown Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as Black/African American, Native American/American Indian, Hispanic/Latin American, or Asian/Pacific Islander and have at least a 2.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.trea.org/TREA/Resources/Scholarship/TREA/Scholarships.aspx" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">TREA Scholarship Program</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be US citizens.
              </p>

              {/* Scholarship */}
              <a href="https://www.shawncartersf.com/scholarship-fund/#app" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Shawn Carter Scholarship Fund</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be US citizens with at least a 2.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.tedrollinsecoscholars.com/ted-rollins-eco-scholarship-application-details/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Ted Rollins Eco Schlarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have demonstrated interest in sustainability.
              </p>

              {/* Scholarship */}
              <a href="http://www.sarascholarship.org" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">The Sara Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be interested in golf, identify as a woman, have at least a 3.30 GPA, and have demonstrated financial need.
              </p>

              {/* Scholarship */}
              <a href="https://ncgc.org/scholarship-program/criteria/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">The Virginia W. Smith Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be from Long Island, NY and interested in horticulture.
              </p>

              {/* Scholarship */}
              <a href="https://scholarships.uncf.org/Program/Details/1dc8ade7-aa7f-4187-a7a6-6d3a8ede2758" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">UNCF/Best Buy Scholars Program</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $20,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be African American with demonstrated financial need and intent to enroll in an HBCU.
              </p>

              {/* Scholarship */}
              <a href="https://scholarships.uncf.org/Program/Details/0b1c9f9b-ddea-468f-ac77-2b952ed0c48f" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Nevada Scholarship Program</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> You must be a permanent resident of the Las Vegas region and attending an HBCU next fall. You must also have demonstrated financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.devantestokesscholarship.com/apply" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Devante Stokes Scholarship Fund</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Unknown<br />
                <span className="font-weight-bold">Eligibility:</span> You must reside in South Carolina and be attending an institution in the area.
              </p>

              {/* Scholarship */}
              <a href="https://www.monarchawardsfoundation.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Chicago Metropolitan High School Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $3,000<br />
                <span className="font-weight-bold">Eligibility:</span> Chicago high school students.
              </p>

              {/* Scholarship */}
              <a href="http://avasgrace.org/scholarship/scholarship-details/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Fiesta del Sol Guadalupe A. Reyes Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 24, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Students who identify as Hispnic / Latino.
              </p>

              {/* Scholarship */}
              <a href="https://www.nshss.org/scholarships/s/nshss-steam-scholarships-2020/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">NSHSS STEM Scholarships</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span>
              </p>

              {/* Scholarship */}
              <a href="https://www.corinnelicostiefamilyfoundation.com/apply.html" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Corinne Licostie Family Foundation Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $500<br />
                <span className="font-weight-bold">Eligibility:</span>
              </p>

              {/* Scholarship */}
              <a href="https://thebhwgroup.com/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">BHW Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $3,000<br />
                <span className="font-weight-bold">Eligibility:</span> Students who have parents who are currently or have been incarcerated and live in Missouri or Illinois counties that are part of the St. Louis Metro area.
              </p>

              {/* Scholarship */}
              <a href="https://balkhifoundation.com/making-education-more-affordable/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Balkhi Foundation Higher Education Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1000<br />
                <span className="font-weight-bold">Eligibility:</span>
              </p>

              {/* Scholarship Title */}
              <a href="http://avasgrace.org/scholarship/scholarship-details/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Ava's Grace Scholarship</h4>
              </a>

              {/* Scholarship Details */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> Up to $5,000 renewable for 4 years<br />
                <span className="font-weight-bold">Eligibility:</span> Students who have parents who are currently or have been incarcerated and live in Missouri or Illinois counties that are part of the St. Louis Metro area.
              </p>

              {/* Scholarship Title */}
              <a href="https://www.chicagohomeless.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Chicago Coalition for the Homeless</h4>
              </a>

              {/* Scholarship Details */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 13, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Students from Chicago and suburban schools are eligible to apply in 2020, as well as Chicago Coalition for the Homeless youth leaders and former youth clients.
              </p>

              {/* Scholarship Title */}
              <a href="https://www.ccclatinocaucus.org/clcf-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Chi Latino Caucus</h4>
              </a>

              {/* Scholarship Details */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 10, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Studnets must currently reside in Chicago, Illinois and be at least one-half Hispanic/Latino.
              </p>

              {/* Scholarship Title */}
              <a href="https://www.microsoft.com/en-us/diversity/programs/blacks-scholarships.aspx" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Blacks at Microsoft Scholarship</h4>
              </a>

              {/* Scholarship Details */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000 for up to four (4) consecutive years <br />
                <span className="font-weight-bold">Eligibility:</span> Students must be a high-school senior of African descent (African American or African).
              </p>

              {/* Scholarship Title */}
              <a href="https://www.microsoft.com/en-us/diversity/programs/blacks-scholarships.aspx" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">AKA Imani Pearls Community Development Foundation Scholarship</h4>
              </a>

              {/* Scholarship Details */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> April 3, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> The applicant must have permanent residency or attend school in the Bronzeville, Douglas, Englewood, Grand Boulevard, Hyde Park, Kenwood, Oakland, or Washington Park community in Chicago, Illinois.
              </p>

              {/* Month */}
              <h2 className="font-weight-bold">March</h2>

              {/* Heading */}
              <a href="https://www.friendsofvolobog.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Environmental Studies/Natural Science Scholarship</h4>
              </a>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> March 31, 2020 <br />
                <span className="font-weight-bold">Amount:</span> Up to $1,000
              </p>

              {/* Heading */}
              <a href="https://doodles.google.com/d4g/how-it-works/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Palumbo Family Foundation</h4>
              </a>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> March 31, 2020 <br />
                <span className="font-weight-bold">Requirements:</span> Only for Illinois residents
              </p>

              {/* Heading */}
              <a href="https://doodles.google.com/d4g/how-it-works/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Doodle for Google</h4>
              </a>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> March 13, 2020 <br />
                <span className="font-weight-bold">Amount:</span> Up to $30,000
              </p>

              {/* Heading */}
              <a href="https://coagonline.org/coag-scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Constitutional Officers Association of Georgia Scholarship</h4>
              </a>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> March 13, 2020 <br />
                <span className="font-weight-bold">Amount:</span> $1,000
              </p>

              {/* Heading */}
              <a href="https://ilache.org/Scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Illinois Latino Council on Higher Education (ILACHE)</h4>
              </a>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> March 6, 2020 <br />
                <span className="font-weight-bold">Amount:</span> $1,000
              </p>

              {/* Heading */}
              <a href="https://www.intertech.com/about/foundation/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Intertech Foundation STEM Scholarship</h4>
              </a>

              {/* Text */}
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> March 10, 2020 <br />
                <span className="font-weight-bold">Amount:</span> Up to $2,500
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Scholarships;
