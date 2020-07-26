import React from "react";

import GradYear from "../graduationYear/GradYear";
import SchoolDistrict from "../schoolDistrict/SchoolDistrict";

const Staff = (props) => {
  const { flowIndex } = props;
  return (
    <div className="staff-container">
      {flowIndex === 1 && <SchoolDistrict {...props} />}
      {flowIndex === 2 && <GradYear staff {...props} />}
    </div>
  );
};

export default Staff;
