import React from "react";
import { Link } from "react-router-dom";

import tiltLogo from "../../img/tilt_logo.png";
import "./nav-bar.scss";

const NavBar = () => {
  return (
    <div className="tilt-nav-bar-container">
      <img src={tiltLogo} alt="tilt logo" />
      <nav>
        <Link className="tilt-button" to="/blog">
          Blog
        </Link>
        <Link className="tilt-button" to="/faq">
          FAQ
        </Link>
        <Link className="tilt-button" to="/contacts">
          Contacts
        </Link>
      </nav>
      <div className="login-and-get-started">
        <button className="tilt-button">Login</button>
        <button className="tilt-button light">Get Started</button>
      </div>
    </div>
  );
};

export default NavBar;
