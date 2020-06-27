import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import { ApolloClient } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';
import { BrowserRouter, Route } from 'react-router-dom';
import { createHttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';

import 'aos/dist/aos.css';
import './fonts/Feather/feather.css';
import './scss/theme.scss';
import 'cross-fetch/polyfill';

import CreateScholarship from './components/resources/scholarships/CreateScholarship';
import ContactUs from './components/ContactUs';
import HomePage from './components/HomePage';
import Login from './components/account/Login';
import PrivacyPolicy from './components/PrivacyPolicy';
import ResourcesFAQs from './components/resources/ResourcesFAQs';
import ResourcesIntro from './components/resources/ResourcesIntro';
import Scholarships from './components/resources/scholarships/Scholarships';
import ScrollToTop from './components/ScrollToTop';
import Sitemap from './components/Sitemap';
import SignupSurvey from './components/signup/SignupSurvey';
import SignupThankYou from './components/signup/SignupThankYou';
import Terminology from './components/resources/Terminology';
import TermsOfService from './components/TermsOfService';
import { initializeAOS, initializeSmoothScroll, initializeTyped } from './js/helpers';


const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql',
  credentials: 'same-origin'
})

const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})

const App = () => {
    useEffect(() => {
      document.title = 'Financial aid help for high school students - Tilt';
      initializeAOS();
      initializeSmoothScroll();
      initializeTyped();
    });

  return (
    <BrowserRouter>
      <ApolloProvider client={client}>
        <ScrollToTop>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/contact" component={ContactUs} />
          <Route exact path="/privacy-policy" component={PrivacyPolicy} />
          <Route exact path="/terms-of-service" component={TermsOfService} />
          <Route exact path="/login" component={Login} />
          <Route exact path='/resources' component={ResourcesIntro} />
          <Route exact path='/resources/faqs' component={ResourcesFAQs} />
          <Route exact path='/resources/scholarships' component={Scholarships} />
          <Route exact path='/resources/scholarships/create' component={CreateScholarship} />
          <Route exact path='/resources/terminology' component={Terminology} />
          <Route exact path='/signup-survey' component={SignupSurvey} />
          <Route exact path='/signup-thank-you' component={SignupThankYou} />
          <Route exact path='/sitemap' component={Sitemap} />
        </ScrollToTop>
      </ApolloProvider>
    </BrowserRouter>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
