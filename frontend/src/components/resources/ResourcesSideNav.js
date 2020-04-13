import React from 'react';
import { Link } from 'react-router-dom';


const ResourcesSideNav = props => {
  return (
    <div class="py-7 py-lg-9 px-lg-7">

      {/* Links */}
      <ul class="list mb-6">
        <li class="list-item">
          <Link class="list-link" to="/resources">Introduction</Link>
        </li>
      </ul>

      {/* Heading */}
      <h6 class="text-uppercase font-weight-bold">
        Financial Aid
      </h6>

      {/* Links */}
      <ul class="list mb-6">
        <li class="list-item">
          <Link class="list-link" to="/resources/terminology">Terminology</Link>
        </li>
        <li class="list-item d-flex">
          <Link class="list-link" to="/resources/faqs">FAQs</Link>
        </li>
      </ul>

      {/* Heading */}
      <h6 class="text-uppercase font-weight-bold">
        Scholarships
      </h6>

      {/* Links */}
      <ul class="list mb-6">
        <li class="list-item">
          <Link class="list-link" to="/resources/scholarships">Links</Link>
        </li>
      </ul>
    </div>
  );
};

export default ResourcesSideNav;
