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
              <a href="https://www.chicagoengineersfoundation.org/awards/" target="_blank" rel="noopener noreferrer">
                <h4 className="font-weight-bold">Chicago Engineer Foundation Scholarship</h4>
              </a>
              <p className="text-gray-700">
                <span className="font-weight-bold">Deadline:</span> May 1, 2020<br />
                <span className="font-weight-bold">Amount:</span> $1,000<br />
                <span className="font-weight-bold">Eligibility:</span> Chicago high school student pursuing engineering program with at least a 2.5 GPA.
              </p>

              {/* Month */}
              <h2 className="font-weight-bold">April</h2>

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
