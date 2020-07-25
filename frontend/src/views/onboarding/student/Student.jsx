import React from "react";

import Act from "../act/Act";
import Ethnicity from "../ethnicity/Ethnicity";
import FamilyIncome from "../familyIncome/FamilyIncome";
import Gpa from "../gpa/Gpa";
import GradYear from "../graduationYear/GradYear";
import HighSchoolName from "../highSchoolName/HighSchoolName";
import PreferredPronoun from "../preferredPronoun/PreferredPronoun";
import Sat from "../sat/Sat";

const Student = (props) => {
  const { flowIndex } = props;

  return (
    <div className="student-container">
      {flowIndex === 1 && <HighSchoolName {...props} />}
      {flowIndex === 2 && <GradYear {...props} />}
      {flowIndex === 3 && <Gpa {...props} />}
      {flowIndex === 4 && <Sat {...props} />}
      {flowIndex === 5 && <Act {...props} />}
      {flowIndex === 6 && <FamilyIncome {...props} />}
      {flowIndex === 7 && <PreferredPronoun {...props} />}
      {flowIndex === 8 && <Ethnicity {...props} />}
    </div>
  );
};

export default Student;
