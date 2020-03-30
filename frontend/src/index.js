import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom';

import './scss/theme.scss';
import 'aos/dist/aos.css';

import ContactUs from './components/ContactUs';
import HomePage from './components/HomePage';
import { initializeAOS, initializeSmoothScroll, initializeTyped } from './js/helpers';
import PrivacyPolicy from './components/PrivacyPolicy';
import ScrollToTop from './components/ScrollToTop';
import TermsOfService from './components/TermsOfService';


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
        <ScrollToTop>
          <Route path="/" exact component={HomePage} />
          <Route path="/contact" exact component={ContactUs} />
          <Route path="/privacy-policy" exact component={PrivacyPolicy} />
          <Route path="/terms-of-service" exact component={TermsOfService} />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
