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
              <h2 className="font-weight-bold">July</h2>

              {/* Scholarship */}
              <a href="https://www.lambdapichi.org/page/2020_BookScholarship" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">A2020 College Book Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 10, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must identify as women or non-binary and committed to community service, leadership, and academic excellence. 
              </p>

              {/* Scholarship */}
              <a href="https://www.afghanamericanconference.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Afghan-American Scholarship Program </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 7, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be Afghan-American, have at least a 3.0 GPA, be a U.S. citizen, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.txadc.org/Scholarships.php" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Texas Urban Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 6, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Texas and be a U.S. citizen.
              </p>

              {/* Scholarship */}
              <a href="https://www.blmsquaredscholarship.org/apply" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">BLM² Scholarship Foundation College Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 3, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Illinois, be a minority, and have at least a 3.0 GPA.
              </p>

              {/* Scholarship */}
              <a href="https://laoamericanscholarship.org/apply" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">LASF Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 3, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in western NY and be of Laotian descent.
              </p>

              {/* Scholarship */}
              <a href="https://www.sccavs.org/CarveyScholarshipApplication.pdf" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Elmer Carvey Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue physics, chemistry, materials science and engineering and reside in California.
              </p>

              {/* Scholarship */}
              <a href="http://www.ohe.state.mn.us/mPg.cfm?pageID=149" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Minnesota Indian Scholarship Program </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $4,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to attend school in Minnesota, reside in Minnesota, be 1/4 or more American Indian, and have financial need.
              </p>

              {/* Scholarship */}
              <a href="https://www.nadona.org/stephanie-carroll-scholarship-2020/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Stephanie Carroll Scholarship </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> July 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> Varies<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must plan to pursue nursing.
              </p>

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
              <a href="http://blackskepticsla.org/scholarship-application/"_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">First in the Family Humanist Scholarship: Freedom from Religion Foundation Forward Freethought Scholarship 2020 </h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> June 26, 2020<br />
                <span className="font-weight-bold">Amount:</span> $5,000<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must be a person of color who identifies as agnostic, atheist, humanist, and/or secular.
              </p>

              {/* Scholarship */}
              <a href="https://breakthroughjuniorchallenge.org"_blank" rel="noopener noreferrer">
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
              <a href="https://awafoundation.org/Scholarships target="_blank" rel="noopener noreferrer">
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

              {/* Scholarship */}
              <a href="https://scholarships.uncf.org/Program/Details/be57b2be-b03d-4dc3-bcee-78cf9f6b0ea2?_ga=2.30033471.1867487941.1586898157-80437064.1586898157" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">William L. & Mary Ann Brown Scholarships</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 22, 2020<br />
                <span className="font-weight-bold">Amount:</span> $2,500<br />
                <span className="font-weight-bold">Eligibility:</span> Candidates must reside in Meckleburg Co, NC, plan to attend a HBCU, plan to pursue STEM, have a 3.0 GPA, have financial need, and be a U.S. Citizen
              </p>

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
