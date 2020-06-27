import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

import logo from '../../img/tilt_logo.png';

const SignupSurvey = () => {
  const BG_LIGHT = "bg-light";

  useEffect(() => {
    document.title = 'Tilt: Sign Up Survey';
    document.body.classList.add(BG_LIGHT);

    return () => { document.body.classList.remove(BG_LIGHT) }
  });

  return (
    <div>
      <section>
        <div className="container d-flex flex-column">
          <div className="row align-items-center justify-content-center no-gutters min-vh-100">
            <div className="col-12 col-md-6 col-lg-5 py-8 py-md-11">

              {/* Brand */}
              <div className="row align-items-center justify-content-center mb-2">
                <Link className="mb-5" to="/">
                  <img src={logo} className="navbar-brand-img" alt="..." />
                </Link>
              </div>

              <div className="card card-row shadow-light">
                <div className="row no-gutters">
                  <div className="col-12">
                    <div className="card-body" style= {{ textAlign: "center" }}>
                      <h3 style= {{ textAlign: "center" }}>Thank You for Signing Up!</h3>
                      <h3>We will let you know as soon as we launch!</h3>
                      <br />

                      <Link className="btn btn-block btn-primary" to="/">
                        Return to Our Home Page
                      </Link>
                    </div>
                  </div>
                </div>
              </div>


              {/* Text */}
              <div className="col-10 offset-1">
                <div className="container d-flex flex-column">
                  <div className="row align-items-center justify-content-between no-gutters mt-3">
                    <div className="col-4 text-center">
                      <p>
                        <Link className="font-size-sm text-center text-muted" to="/">
                          © Tilt
                        </Link>
                      </p>
                    </div>
                    <div className="col-4 text-center">
                      <p>
                        <Link className="font-size-sm text-center text-muted" to="/contact">
                          Contact
                        </Link>
                      </p>
                    </div>
                    <div className="col-4 text-center">
                      <p className="font-size-sm text-center text-muted">
                        <Link className="font-size-sm text-center text-muted" to="/privacy-policy">
                          Privacy
                        </Link>
                      </p>
                    </div>
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

export default SignupSurvey;
