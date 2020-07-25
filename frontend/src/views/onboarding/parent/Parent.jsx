import React from "react";

import HighSchoolName from "../highSchoolName/HighSchoolName";
import GradYear from "../graduationYear/GradYear";

const Parent = (props) => {
  const { flowIndex } = props;
  return (
    <div className="parent-container">
      {flowIndex === 1 && <HighSchoolName {...props} parent />}
      {flowIndex === 2 && <GradYear {...props} parent />}
    </div>
  );
};

export default Parent;
