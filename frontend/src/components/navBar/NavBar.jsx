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

  return (
    <div className="NavBar">
      <Link to="/">
        <img src={tiltLogo} alt="tilt logo" />
      </Link>
      <nav>
        <ul>
          {links.map((link) => {
            const selected = pathname === link.pathname;
            const classList = selected ? "selected" : "";
            return (
              <li key={link.pathname} className={classList}>
                <Link to={link.pathname}>{link.display}</Link>
                <div className="underline" />
              </li>
            );
          })}
        </ul>
      </nav>
      <div className="NavBar__buttons">
        <Link to="/login" className="TiltButton">
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
