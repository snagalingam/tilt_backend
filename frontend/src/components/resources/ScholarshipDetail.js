import React from 'react';

const ScholarshipDetail = props => {
  return (
    <div>
      <a href={this.props.scholarhip.url} target="_blank" rel="noopener noreferrer">
        <h4 className="font-weight-bold">{this.props.scholarhip.description}</h4>
      </a>

      <p className="text-gray-700">
        <span className="font-weight-bold">Deadline:</span> {this.props.scholarhip.description}
        <br />
        <span className="font-weight-bold">Amount:</span> {this.props.scholarhip.description}
      </p>
    </div>
  );
};

export default ScholarshipDetail;
