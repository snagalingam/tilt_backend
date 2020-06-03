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
              <a href="http://www.edascal.org/pr06.htm" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Raising Awareness of Mental Illness in Service Members Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://www.kasf.org/apply-mwrc/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Korean American Scholarship Foundation - Midwestern Regional Chapter </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be of Korean heritage, pursuing education at a school in the Midwestern region, have at least a 3.0 GPA, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.cyberdriveillinois.com/departments/library/center_for_the_book/emerging-writers.html" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Gwendolyn Brooks Poetry Award </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Illinois.
              </p>

              {/* Scholarship */}
              <a href="http://endcyberbullying.net/scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Delete Cyberbullying Scholarship Award</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="http://infoguides.pepperdine.edu/AEL" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">AEL Collegiate Essay Contest  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://www.automotivehalloffame.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Automotive Hall of Fame Scholarships  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue a career in automotives, have at least a 3.0 GPA, and be a U.S. citizen with financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.ccapw.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Central California Asian Pacific Women (CCAPW) Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 30, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be an Asian or Pacific Islander woman residing in Fresno, Kern, Kings, Madera, Merced, San Joaquin, Stanislaus or Tulare County, California and have financial need.
              </p>

              {/* Scholarship */}
              <a href="http://blackskepticsla.org/scholarship-application/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">First in the Family Humanist Scholarship: Freedom from Religion Foundation Forward Freethought Scholarship 2020 </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 26, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a person of color who identifies as agnostic, atheist, humanist, and/or secular.
              </p>

              {/* Scholarship */}
              <a href="https://breakthroughjuniorchallenge.org" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Breakthrough Juniors Challenge  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 25, 2020<br />
                <span className="font-weight-bold">Amount:</span> $250,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates make a video explaining a big idea in physics, life sciences, mathematics, or the science of the COVID-19 pandemic.
              </p>

              {/* Scholarship */}
              <a href="https://uicapsi.wixsite.com/zeta/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">The Dream Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 19, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to attend University of Chicago Illinois, be latinx, and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="http://www.parekhfamilyfoundation.org/scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Gunvant & Bharati Parekh College Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be of Indian origin and reside in the U.S.
              </p>

              {/* Scholarship */}
              <a href="https://form.jotform.com/200275477072050" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Emerald Creek Capital Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 15, 2020<br />
                <span className="font-weight-bold">Amount:</span> $10,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be in National Honors Society and reside in New York City.
              </p>

              {/* Scholarship */}
              <a href="https://awafoundation.org/Scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">AWA Foundation Education Scholarship   </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 12, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must a woman planning to pursue a career in the automotive or related industries, a U.S. citizen, and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.bbbchicagofoundation.org/about-the-contest-2020#entry-guidelines" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">BBB Embody Integrity Video Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 12, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Boone, Carroll, Cook, DeKalb, DuPage, Grundy, JoDavies, Kane, Kankakee, Kendall, Lake, LaSalle, Lee, McHenry, Ogle, Stephenson, Whiteside, Will, or Winnebago County in ILlinois and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://festivaldaculturaportuguesa.com/2020-fdcp-scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Festival da Cultura Portuguesa </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must have Portuguese ancestry, have at least a 3.0 GPA, and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://scholarships.uncf.org/Program/Details/9898a633-b8da-42eb-af7a-d55025fb2706?_ga=2.7510450.1057392258.1590279032-2022323697.1590279032" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Jack & Jill of America Foundation </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 8, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be African American, have at least a 3.0 GPA, and be a U.S. citizen with financial need.
              </p>

              {/* Scholarship */}
              <a href="https://rchwf.org/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">RCH Wrestling Foundation Scholarship  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 7, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Illinois or Indiana, have at least a 2.5 GPA, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.icahnautomotive.com/scholarship.html" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Technical Education Scholarship  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 5, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue an automotive technician degree or certification, have at least a 3.0 GPA, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.chicagomoa.net/moa-scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Metropolitan Officials Association Scholarship  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 5, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Chicago, IL and have at least a 2.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://www.provfound.org/index.php/programs/scholarship-program" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Provident Foundation Scholarship  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 5, 2020<br />
                <span className="font-weight-bold">Amount:</span> $3,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue medicine, reside in Chicago, IL, and be a minority.
              </p>

              {/* Scholarship */}
              <a href="https://www.luciefoundation.org/programs/scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">2020 Lucie Foundation Scholarship Program  </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 3, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must pursue art, film, or photography.
              </p>

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
