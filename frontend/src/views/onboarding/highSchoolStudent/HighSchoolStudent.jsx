import React, { useState } from "react";

import CustomGradYear from "../customGradYear/CustomGradYear";
import GraduationYear from "../graduationYear/GraduationYear";
import HighSchoolName from "../highSchoolName/HighSchoolName";

const HighSchoolStudent = ({ flowIndex, next, previous, setAnswers }) => {
  const [isCustomGradYear, setIsCustomGradYear] = useState(false);

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
      {flowIndex === 2 &&
        (isCustomGradYear ? (
          <CustomGradYear
            next={next}
            previous={previous}
            answer={(graduationYear) =>
              setAnswers((prev) => ({ ...prev, graduationYear }))
            }
          />
        ) : (
          <GraduationYear
            highSchool
            next={next}
            previous={previous}
            answer={(graduationYear) =>
              setAnswers((prev) => ({ ...prev, graduationYear }))
            }
            setIsCustomGradYear={() => setIsCustomGradYear(true)}
          />
        ))}
    </div>
  );
};

export default HighSchoolStudent;
