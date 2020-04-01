import React from 'react';

import NavBar from '../NavBar';
import ResourcesSideNav from './ResourcesSideNav';


const Scholarships = () => {
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
                    Scholarships
                  </span>
                </li>
                <li class="breadcrumb-item active" aria-current="page">
                  <span class="text-white">
                    Upcoming Deadlines
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
              <h1 class="mb-1">Scholarship Links</h1>
              <br />

              {/* Month */}
              <h2 class="font-weight-bold">April</h2>

              {/* Scholarship Title */}
              <a href="http://avasgrace.org/scholarship/scholarship-details/" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Ava's Grace Scholarship</h4>
              </a>

              {/* Scholarship Details */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span class="font-weight-bold">Amount:</span> Up to $5,000 renewable for 4 years<br />
                <span class="font-weight-bold">Eligibility:</span> Students who have parents who are currently or have been incarcerated and live in Missouri or Illinois counties that are part of the St. Louis Metro area.
              </p>

              {/* Scholarship Title */}
              <a href="https://www.chicagohomeless.org/scholarships/" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Chicago Coalition for the Homeless</h4>
              </a>

              {/* Scholarship Details */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> April 13, 2020<br />
                <span class="font-weight-bold">Amount:</span> $2,500<br />
                <span class="font-weight-bold">Eligibility:</span> Students from Chicago and suburban schools are eligible to apply in 2020, as well as Chicago Coalition for the Homeless youth leaders and former youth clients.
              </p>

              {/* Scholarship Title */}
              <a href="https://www.ccclatinocaucus.org/clcf-scholarship/" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Chi Latino Caucus</h4>
              </a>

              {/* Scholarship Details */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> April 10, 2020<br />
                <span class="font-weight-bold">Amount:</span> $5,000<br />
                <span class="font-weight-bold">Eligibility:</span> Studnets must currently reside in Chicago, Illinois and be at least one-half Hispanic/Latino.
              </p>

              {/* Scholarship Title */}
              <a href="https://www.microsoft.com/en-us/diversity/programs/blacks-scholarships.aspx" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Blacks at Microsoft Scholarship</h4>
              </a>

              {/* Scholarship Details */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> April 15, 2020<br />
                <span class="font-weight-bold">Amount:</span> $5,000 for up to four (4) consecutive years <br />
                <span class="font-weight-bold">Eligibility:</span> Students must be a high-school senior of African descent (African American or African).
              </p>

              {/* Scholarship Title */}
              <a href="https://www.microsoft.com/en-us/diversity/programs/blacks-scholarships.aspx" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">AKA Imani Pearls Community Development Foundation Scholarship</h4>
              </a>

              {/* Scholarship Details */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> April 3, 2020<br />
                <span class="font-weight-bold">Amount:</span> $5,000<br />
                <span class="font-weight-bold">Eligibility:</span> The applicant must have permanent residency or attend school in the Bronzeville, Douglas, Englewood, Grand Boulevard, Hyde Park, Kenwood, Oakland, or Washington Park community in Chicago, Illinois.
              </p>

              {/* Month */}
              <h2 class="font-weight-bold">March</h2>

              {/* Heading */}
              <a href="https://www.friendsofvolobog.org/scholarships" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Environmental Studies/Natural Science Scholarship</h4>
              </a>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> March 31, 2020 <br />
                <span class="font-weight-bold">Amount:</span> Up to $1,000
              </p>

              {/* Heading */}
              <a href="https://doodles.google.com/d4g/how-it-works/" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Palumbo Family Foundation</h4>
              </a>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> March 31, 2020 <br />
                <span class="font-weight-bold">Requirements:</span> Only for Illinois residents
              </p>

              {/* Heading */}
              <a href="https://doodles.google.com/d4g/how-it-works/" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Doodle for Google</h4>
              </a>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> March 13, 2020 <br />
                <span class="font-weight-bold">Amount:</span> Up to $30,000
              </p>

              {/* Heading */}
              <a href="https://coagonline.org/coag-scholarship" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Constitutional Officers Association of Georgia Scholarship</h4>
              </a>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> March 13, 2020 <br />
                <span class="font-weight-bold">Amount:</span> $1,000
              </p>

              {/* Heading */}
              <a href="https://ilache.org/Scholarship" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Illinois Latino Council on Higher Education (ILACHE)</h4>
              </a>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> March 6, 2020 <br />
                <span class="font-weight-bold">Amount:</span> $1,000
              </p>

              {/* Heading */}
              <a href="https://www.intertech.com/about/foundation/scholarship" target="_blank" rel="noopener noreferrer">
                <h4 class="font-weight-bold">Intertech Foundation STEM Scholarship</h4>
              </a>

              {/* Text */}
              <p class="text-gray-700">
                <span class="font-weight-bold">Deadline:</span> March 10, 2020 <br />
                <span class="font-weight-bold">Amount:</span> Up to $2,500
              </p>
            </div>
          </div>
        </div>
      </section>
    </body>
  );
};

export default Scholarships;
