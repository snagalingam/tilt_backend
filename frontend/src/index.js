import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom';

import './scss/theme.scss';
import 'aos/dist/aos.css';

import ContactUs from './ContactUs';
import HomePage from './HomePage';
import { initializeAOS, initializeSmoothScroll, initializeTyped } from './helpers';


const App = () => {
    useEffect(() => {
      document.title = 'Financial aid help for high school students - Tilt';
      initializeAOS();
      initializeSmoothScroll();
      initializeTyped();
    });

  return (
    <div>
      <BrowserRouter>
        <Route path="/" exact component={HomePage} />
        <Route path="/contact" exact component={ContactUs} />
      </BrowserRouter>
    </div>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
