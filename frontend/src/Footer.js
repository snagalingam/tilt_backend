import React from 'react';

import facebook from './img/social/facebook.svg';
import instagram from './img/social/instagram.svg';
import logo from './img/tilt_logo.png';
import twitter from './img/social/twitter.svg';


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
    <footer class={navStyle(classList)}>
      <div class="container">
        <div class="row">
          <div class="col-12 col-md-4 col-lg-3">

            {/* Brand */}
            <img src={logo} width="100" alt="..." class="footer-brand img-fluid mb-2" />

            {/* Text */}
            <p class="text-gray-700 mb-2">
              Your financial aid expert.
            </p>

            {/* Social */}
            <ul class="list-unstyled list-inline list-social mb-6 mb-md-0">
              <li class="list-inline-item list-social-item mr-3">
                <a href="https://www.instagram.com/tiltaccess/" class="text-decoration-none">
                  <img src={instagram} class="list-social-icon" alt="..." />
                </a>
              </li>
              <li class="list-inline-item list-social-item mr-3">
                <a href="https://www.facebook.com/tiltaccess/" class="text-decoration-none">
                  <img src={facebook} class="list-social-icon" alt="..." />
                </a>
              </li>
              <li class="list-inline-item list-social-item mr-3">
                <a href="https://twitter.com/TiltAccess" class="text-decoration-none">
                  <img src={twitter} class="list-social-icon" alt="..." />
                </a>
              </li>

            </ul>

          </div>

          <div class="col-12 col-md-8 col-lg-9">
              <h5 class="text-muted">
                © Tilt 2020
                <br />
                <a class="text-reset" href="@@webRoot/privacy-policy.html">Privacy Policy</a> & <a class="text-reset" href="@@webRoot/terms-of-service.html">Terms of Service</a>
              </h5>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
