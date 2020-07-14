import React, {useState } from 'react';
import { Link } from 'react-router-dom';
import { X } from 'react-feather';

import logo from '../img/tilt_logo.png';


const containerFluid = type => {
  if (type === 'boxed') {
    return 'container';
  }
  return 'container-fluid';
};

const navStyle = classList => {
  var base = "navbar navbar-expand-lg"
  if (classList) {
    return base.concat(classList);
  }
  return base;
};

const NavBar = props => {
  const classList = props.classList;
  const type = props.type;
  const [collapsed, setCollapsed] = useState(true);
  const toggleNavbar = () => setCollapsed(!collapsed);
  const classNavBarCollapsed = collapsed ? 'collapse navbar-collapse' : 'collapse navbar-collapse show';
  const classNavBarToggler = collapsed ? 'navbar-toggler collapsed' : 'navbar-toggler';

  return (
    <nav className={navStyle(classList)}>
      <div className={containerFluid(type)}>

        {/* Brand */}
        <Link className="navbar-brand" to="/">
          <img src={logo} className="navbar-brand-img" alt="..." />
        </Link>

        {/* Toggler */}
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarGetStarted" aria-controls="navbarGetStarted" aria-expanded="false" aria-label="Toggle Get Started">
          <Link className="btn btn-sm btn-primary lift ml-auto" to="/signup-survey">
            Get Started
          </Link>
        </button>

        <button className={classNavBarToggler} type="button" onClick={toggleNavbar} data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Collapse */}
        <div className={classNavBarCollapsed} id="navbarCollapse">

          {/* Toggler */}
          <button className="navbar-toggler" type="button" onClick={toggleNavbar} data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <X className="fe" />
          </button>

          {/* Navigation */}
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <Link className="nav-link" id="navbarResources" to="/resources">
                Resources
              </Link>
            </li>

            <li className="nav-item">
              <Link className="nav-link" id="navbarContact" to="/contact">
                Contact
              </Link>
            </li>
          </ul>


          {/* Button */}
          <Link className="navbar-btn btn btn-sm btn-primary lift ml-auto" to="/signup-survey">
            Get Started
          </Link>

        </div>
      </div>
    </nav>
  );
};

export default NavBar;
