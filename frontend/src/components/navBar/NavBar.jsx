import React from "react";
import { Link, useHistory } from "react-router-dom";

import TiltButton from "../tiltButton/TiltButton";

import tiltLogo from "../../img/tilt_logo.png";
import "./nav-bar.scss";

const NavBar = () => {
  const history = useHistory();

  return (
    <div className="tilt-nav-bar-container">
      <img src={tiltLogo} alt="tilt logo" />
      <nav>
        <ul>
          <li>
            <Link className="tilt-button" to="/blog">
              Blog
            </Link>
          </li>
          <li>
            <Link className="tilt-button" to="/faq">
              FAQ
            </Link>
          </li>
          <li>
            <Link className="tilt-button" to="/contacts">
              Contacts
            </Link>
          </li>
        </ul>
      </nav>
      <div className="login-and-get-started">
        <Link to="/login" className="tilt-button">
          Login
        </Link>
        <TiltButton classes={["light"]} onClick={() => history.push("/signup")}>
          Get Started
        </TiltButton>
      </div>
    </div>
  );
};

export default NavBar;
