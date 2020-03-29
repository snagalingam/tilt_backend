import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';

import './scss/theme.scss';
import 'aos/dist/aos.css';

import Footer from './Footer';
import HomePage from './HomePage';
import NavBar from './NavBar';
import { initializeAOS, initializeTyped } from './helpers';


const App = () => {
    useEffect(() => {
      document.title = 'Financial aid help for high school students - Tilt';
      initializeAOS();
      initializeTyped();
    });

  return (
    <body>
      <noscript>You need to enable JavaScript to run this app.</noscript>
      <NavBar classList=" navbar-light bg-white" type="boxed"/>
      <HomePage style={{ flex: 1 }}/>
      <Footer />
    </body>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
