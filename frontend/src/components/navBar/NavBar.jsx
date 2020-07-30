import React from "react";
import { Link, useHistory, useLocation } from "react-router-dom";

import TiltButton from "../tiltButton/TiltButton";

import tiltLogo from "../../img/tilt_logo.png";
import "./nav-bar.scss";

const links = [
  {
    display: "Blog",
    pathname: "/blog",
  },
  {
    display: "FAQ",
    pathname: "/faq",
  },
  {
    display: "Contacts",
    pathname: "/contacts",
  },
];

const NavBar = () => {
  const history = useHistory();
  const location = useLocation();
  const { pathname } = location;
  console.log(pathname);

  return (
    <div className="tilt-nav-bar">
      <Link to="/">
        <img src={tiltLogo} alt="tilt logo" />
      </Link>
      <nav>
        <ul>
          {links.map((link) => {
            const selected = pathname === link.pathname;
            return (
              <li
                key={link.pathname}
                className={`${selected ? "selected" : ""}`}
              >
                <Link to={link.pathname}>{link.display}</Link>
                <div className="underline" />
              </li>
            );
          })}
        </ul>
      </nav>
      <div className="login-and-get-started">
        <Link to="/login" className="tilt-button">
          Login
        </Link>
        <TiltButton
          classes={["purple", "primary"]}
          onClick={() => history.push("/signup")}
        >
          Try Free
        </TiltButton>
      </div>
    </div>
  );
};

export default NavBar;
