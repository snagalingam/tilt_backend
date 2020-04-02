import ApolloClient, { gql } from 'apollo-boost';
import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom';

import './scss/theme.scss';
import 'aos/dist/aos.css';
import 'cross-fetch/polyfill';

import ContactUs from './components/ContactUs';
import HomePage from './components/HomePage';
import { initializeAOS, initializeSmoothScroll, initializeTyped } from './js/helpers';
import PrivacyPolicy from './components/PrivacyPolicy';
import ResourcesFAQs from './components/resources/ResourcesFAQs';
import ResourcesIntro from './components/resources/ResourcesIntro';
import Scholarships from './components/resources/Scholarships';
import ScrollToTop from './components/ScrollToTop';
import Terminology from './components/resources/Terminology';
import TermsOfService from './components/TermsOfService';

const client = new ApolloClient({
  uri: 'https://localhost:8000/graphql',
  request: operation => {
    operation.setContext({
      headers: {
        authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyMSIsImV4cCI6MTU4NTg0NTYzNiwib3JpZ19pYXQiOjE1ODU4NDUzMzZ9.M-tYqYuIcr0hVpuq-FswbWwoJsY0tvtcmuKa_UZbNJA'
      },
    });
  },
})

const GET_USER = gql`
  {
    me {
      username
      email
    }
  }
`;

client
  .query({
    query: GET_USER,
  })
  .then(console.log);

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
          <Route path='/resources' exact component={ResourcesIntro} />
          <Route path='/resources/faqs' exact component={ResourcesFAQs} />
          <Route path='/resources/scholarships' exact component={Scholarships} />
          <Route path='/resources/terminology' exact component={Terminology} />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
