import React from 'react';

const ScholarshipDetail = props => {
  return (
    <div>
      <a href={props.url} target="_blank" rel="noopener noreferrer">
        <h4 className="font-weight-bold">{props.name}</h4>
      </a>

      <p className="text-gray-700">
        <span className="font-weight-bold">Deadline:</span> {props.deadline}
        <br />
        <span className="font-weight-bold">Amount:</span> {props.amount}
      </p>
    </div>
  );
};

export default ScholarshipDetail;
