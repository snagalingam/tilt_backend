import React from 'react';
import { Link } from 'react-router-dom';

import facebook from '../img/social/facebook.svg';
import instagram from '../img/social/instagram.svg';
import logo from '../img/tilt_logo.png';
import twitter from '../img/social/twitter.svg';


const navStyle = classList => {
  var base = "py-8 py-md-11"
  if (classList) {
    return base.concat(classList);
  }
  return base;
};

const Footer = props => {
  const classList = props.classList;

  return (
    <footer className={navStyle(classList)}>
      <div className="container">
        <div className="row">
          <div className="col-12 col-md-4 col-lg-3">

            {/* Brand */}
            <img src={logo} width="100" alt="..." className="footer-brand img-fluid mb-2" />

            {/* Text */}
            <p className="text-gray-700 mb-2">
              Your financial aid expert.
            </p>

            {/* Social */}
            <ul className="list-unstyled list-inline list-social mb-6 mb-md-0">
              <li className="list-inline-item list-social-item mr-3">
                <a href="https://www.instagram.com/tiltaccess/" className="text-decoration-none">
                  <img src={instagram} className="list-social-icon" alt="..." />
                </a>
              </li>
              <li className="list-inline-item list-social-item mr-3">
                <a href="https://www.facebook.com/tiltaccess/" className="text-decoration-none">
                  <img src={facebook} className="list-social-icon" alt="..." />
                </a>
              </li>
              <li className="list-inline-item list-social-item mr-3">
                <a href="https://twitter.com/TiltAccess" className="text-decoration-none">
                  <img src={twitter} className="list-social-icon" alt="..." />
                </a>
              </li>

            </ul>

          </div>

          <div className="col-12 col-md-8 col-lg-9">
              <h5 className="text-muted">
                © Tilt 2020
                <br />
                <Link className="text-reset" to="/privacy-policy">Privacy Policy</Link> & <Link className="text-reset" to="/terms-of-service">Terms of Service</Link>
              </h5>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
