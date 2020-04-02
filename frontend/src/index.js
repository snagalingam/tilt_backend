import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import { ApolloClient } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';
import { BrowserRouter, Route } from 'react-router-dom';
import { createHttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';

import './scss/theme.scss';
import 'aos/dist/aos.css';
import 'cross-fetch/polyfill';

import ContactUs from './components/ContactUs';
import HomePage from './components/HomePage';
import PrivacyPolicy from './components/PrivacyPolicy';
import ResourcesFAQs from './components/resources/ResourcesFAQs';
import ResourcesIntro from './components/resources/ResourcesIntro';
import Scholarships from './components/resources/Scholarships';
import ScrollToTop from './components/ScrollToTop';
import Terminology from './components/resources/Terminology';
import TermsOfService from './components/TermsOfService';
import { initializeAOS, initializeSmoothScroll, initializeTyped } from './js/helpers';


const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql',
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
    <ApolloProvider client={client}>
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
    </ApolloProvider>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
