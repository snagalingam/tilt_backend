import React from "react";

import GradYear from "../graduationYear/GradYear";
import SchoolDistrict from "../schoolDistrict/SchoolDistrict";

const Counselor = (props) => {
  const { flowIndex } = props;
  return (
    <div className="counselor-container">
      {flowIndex === 1 && <SchoolDistrict {...props} />}
      {flowIndex === 2 && <GradYear counselor {...props} />}
    </div>
  );
};

export default Counselor;
