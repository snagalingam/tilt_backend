import React from 'react';
import { Link } from 'react-router-dom';


const ResourcesSideNav = () => {
  return (
    <div className="collapse d-lg-block" id="sidenavCollapse">
      <div className="py-7 py-lg-9 px-lg-7">

        {/* Links */}
        <ul className="list mb-6">
          <li className="list-item">
            <Link className="list-link" to="/resources">Introduction</Link>
          </li>
        </ul>

        {/* Heading */}
        <h6 className="text-uppercase font-weight-bold">
          Financial Aid
        </h6>

        {/* Links */}
        <ul className="list mb-6">
          <li className="list-item">
            <Link className="list-link" to="/resources/terminology">Terminology</Link>
          </li>
          <li className="list-item d-flex">
            <Link className="list-link" to="/resources/faqs">FAQs</Link>
          </li>
        </ul>

        {/* Heading */}
        <h6 className="text-uppercase font-weight-bold">
          Scholarships
        </h6>

        {/* Links */}
        <ul className="list mb-6">
          <li className="list-item">
            <Link className="list-link" to="/resources/scholarships">Links</Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default ResourcesSideNav;
