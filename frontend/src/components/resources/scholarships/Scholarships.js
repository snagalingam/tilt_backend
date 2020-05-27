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
              <h2 className="font-weight-bold">June</h2>

              {/* Scholarship */}
              <a href="https://programs.applyists.com/walmartassociate/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Walmart Associate Scholarship  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have financial need, be a U.S. citizen, and be employed part-time or full-time by Walmart.
              </p>

              {/* Scholarship */}
              <a href="http://www.cbsmf.org/scholarship.html" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Charles B. Staats Memorial Foundation Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must serve as a swim coach in their community and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://nyramblers.com/scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">New York Ramblers Scholarships  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be an athlete, identify as lesbian, gay, bisexual, transgender, queer, or intersex person; or a demonstrated and committed ally, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.platinumed.com/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Platinum Educational Group Scholarship Program  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue EMS, Nursing, Allied Health Fields.
              </p>

              {/* Scholarship */}
              <a href="https://ffrf.org/outreach/ffrf-student-scholarship-essay-contests" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 William J Schulz Memorial Essay Contest for College-Bound High School Seniors </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $3,500<br />
                <span className="font-weight-bold">Eligibility:</span> Open to all.
              </p>

              {/* Scholarship */}
              <a href="https://www.joefrancis.com/apply" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Joe Francais Haircare Scholarship  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,200<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be currently applying for entrance into Cosmetology/Barber School, OR actively enrolled in a Cosmetology/Barber program.
              </p>

              {/* Scholarship */}
              <a href="http://www.jasna.org/programs/essay-contest?" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Jane Austen Society of North America Essay Contest </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Open to all.
              </p>

              {/* Scholarship */}
              <a href="https://www.iaee.com/helen-brett-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Helen Brett Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a U.S. citizen and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://arborjet.com/taking-root-scholarship-program/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Taking Root College Scholarship Program </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $10,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan on pursuing Plant Sciences, Horticulture, Entomology, Plant Pathology, Environmental Science and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="http://www.ipcdf.org/cms/wp-content/uploads/2020/04/Microsoft-Word-2020-IPCDF-HBCU-Scholarship-Application-COVID-19-approved.pdf" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 HBCU Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan on attending a HBCU, reside in Chicago, IL, and have at least a 2.85 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://www.ipcdf.org/cms/wp-content/uploads/2020/04/Microsoft-Word-2020-IPCDF-General-Scholarship-Application-COVID-19-approved.pdf" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 General Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Chicago, Illinois and have at least a 2.85 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://www.ipcdf.org/cms/wp-content/uploads/2020/04/2020-IPCDF-Dana-G.-Woodley-Scholarship-Application-COVID-19-approved.pdf" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Dana G. Woodley Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue STEM, identify as African American, reside in Illinois, Michigan, or Indiana, have at least a 3.5 GPA, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="http://www.ipcdf.org/cms/wp-content/uploads/2020/04/Microsoft-Word-IPCDF-2020-2-Year-College-Scholarship-Application-COVID-19-approved.pdf" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Two‐Year College and Vocation Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue two‐year colleges, vocational, trade or apprenticeship programs, reside in Chicago, IL and have at least a 2.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://www.ipcdf.org/cms/wp-content/uploads/2020/04/Microsoft-Word-2020-IPCDF-Helen-R.-Jackson-Scholarship-Application-COVID-19-approved.pdf" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Helen R. Jackson Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Chicago, IL and have at least a 2.0 GPA.
              </p>

              {/* Month */}
              <h2 className="font-weight-bold">May</h2>

              {/* Scholarship */}
              <a href="https://www.federalresources.com/scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Warrior's Legacy Scholarship Fund</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a child of police, EMT, paramedic, fire fighter, or military parent, have at least a 3.0 GPA, and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="http://againstthegrainproductions.com/atg-artistic-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Against the Grain Artistic Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue erforming arts, visual arts, journalism, or communications, identify as Asian American/Pacific Islander, have at least a 3.0 GPA, and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="http://againstthegrainproductions.com/lily-pabilona-emerging-entrepreneur-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Lily Pabilona</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as Asian American/Pacific Islander, have at least a 3.0 GPA, and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://app.smartsheet.com/b/form/bc3d8106e24042ef9c888afe6c8c40f8" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Exelon African-American Resource Alliance (EAARA) Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates reside in Illinois, identify as African American, and have at least a 2.75 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://againstthegrainproductions.com/groundbreaker-leadership-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Against The Grain Groundbreaker Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as Asian American/Pacific Islander, have at least a 3.5 GPA, and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://www.earnest.com/student-loans/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Earnest Scholarship Fund</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a U.S. citizen or have DACA status.
              </p>

              {/* Scholarship */}
              <a href="http://againstthegrainproductions.com/livelikelyly-memorial-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Lyly Koenig Mendez Memorial Artistic Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to puruse fashion or graphic design, identify as Asian American/Pacific Islander, have at least a 3.0 GPA, and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://www.naaiachicago.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Ron Allen Award Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Chicago, IL and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.naaiachicago.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">NAAIA Chicago 2020 Insuring Excellence Awards</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 31, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Chicago, IL and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://cuidadocaserofoundation.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Nursing Student Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must puruse nursing, reside in Dallas, TX, identify as Hispanic/Latinx, have at least a 3.0 GPA, be a U.S. citizen, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://aynrand.org/students/essay-contests#tab-3-anthem" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Anthem Contest</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 28, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be in 11th or 12th grade.
              </p>

              {/* Scholarship */}
              <a href="https://aynrand.org/students/essay-contests#tab-3-the-fountainhead" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">The Fountainhead Contest</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 28, 2020<br />
                <span className="font-weight-bold">Amount:</span> $10,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be in 11th or 12th grade.
              </p>

            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Scholarships;
