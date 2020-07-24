import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import GraduationYear from "../graduationYear/GraduationYear";
import HighSchoolInput from "../highSchoolInput/HighSchoolInput";

const HighSchoolStudent = ({ flowIndex, next, setAnswers }) => {
  return (
    <div className="high-school-student-container form-container">
      {flowIndex === 1 && (
        <HighSchoolInput
          next={next}
          answer={(highSchoolName) =>
            setAnswers((prev) => ({ ...prev, highSchoolName }))
          }
        />
      )}
      {flowIndex === 2 && (
        <GraduationYear
          highSchool
          next={next}
          answer={(graduationYear) =>
            setAnswers((prev) => ({ ...prev, graduationYear }))
          }
        />
      )}
    </div>
  );
};

export default HighSchoolStudent;
