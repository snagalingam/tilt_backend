import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import GraduationYear from "../graduationYear/GraduationYear";
import HighSchoolName from "../highSchoolName/HighSchoolName";

const HighSchoolStudent = ({ flowIndex, next, previous, setAnswers }) => {
  return (
    <div className="high-school-student-container form-container">
      {flowIndex === 1 && (
        <HighSchoolName
          next={next}
          previous={previous}
          answer={(highSchoolName) =>
            setAnswers((prev) => ({ ...prev, highSchoolName }))
          }
        />
      )}
      {flowIndex === 2 && (
        <GraduationYear
          highSchool
          next={next}
          previous={previous}
          answer={(graduationYear) =>
            setAnswers((prev) => ({ ...prev, graduationYear }))
          }
        />
      )}
    </div>
  );
};

export default HighSchoolStudent;
