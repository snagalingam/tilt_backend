import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import GraduationYear from "../graduationYear/GraduationYear";

const CollegeStudent = ({ next, previous, flowIndex, setAnswers }) => {
  return (
    <div className="college-student-container form-container">
      {flowIndex === 1 && (
        <GraduationYear
          college
          previous={previous}
          next={next}
          answer={(graduationYear) =>
            setAnswers((prev) => ({ ...prev, graduationYear }))
          }
        />
      )}
    </div>
  );
};

export default CollegeStudent;
