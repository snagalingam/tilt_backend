import React from 'react';
import ReactDOM from 'react-dom';
import ScholarshipDetail from './ScholarshipDetail';
import './scss/theme.scss';

const App = () => {
  return (
    <div>
      <ScholarshipDetail />
    </div>
  );
};

ReactDOM.render(
  <App />,
  document.querySelector('#root')
);
