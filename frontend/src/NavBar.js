import React from 'react';
import { Link } from 'react-router-dom';

import logo from './img/tilt_logo.png';


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

  return (
    <nav className={navStyle(classList)}>
      <div className={containerFluid(type)}>

        {/* Brand */}
        <Link className="navbar-brand" to="/">
          <img src={logo} className="navbar-brand-img" alt="..." />
        </Link>

        {/* Toggler */}
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarButton" aria-controls="navbarButton" aria-expanded="false" aria-label="Toggle Button">
          <a className="btn btn-sm btn-primary lift ml-auto" href="https://kellogg.qualtrics.com/jfe/form/SV_578NDO4HdsYbd4h" target="_blank" rel="noopener noreferrer">
            Get Started
          </a>
        </button>

        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Collapse */}
        <div className="collapse navbar-collapse" id="navbarCollapse">

          {/* Toggler */}
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <i className="fe fe-x"></i>
          </button>

          {/* Navigation */}
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <a className="nav-link" id="navbarResources" href="@@webRoot/resources/index.html">
                Resources
              </a>
            </li>

            <li className="nav-item">
              <Link className="nav-link" id="navbarContact" to="/contact">
                Contact
              </Link>
            </li>
          </ul>


          {/* Button */}
          <a className="navbar-btn btn btn-sm btn-primary lift ml-auto" href="https://kellogg.qualtrics.com/jfe/form/SV_578NDO4HdsYbd4h" target="_blank" rel="noopener noreferrer">
            Get Started
          </a>

        </div>
      </div>
    </nav>
  );
};

export default NavBar;
