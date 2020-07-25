import React, { useState } from "react";

import Act from "../act/Act";
import CustomGradYear from "../customGradYear/CustomGradYear";
import Gpa from "../gpa/Gpa";
import GraduationYear from "../graduationYear/GraduationYear";
import HighSchoolName from "../highSchoolName/HighSchoolName";
import Sat from "../sat/Sat";

const HighSchoolStudent = ({ flowIndex, next, previous, setAnswers }) => {
  const [isCustomGradYear, setIsCustomGradYear] = useState(false);

  return (
    <div className="high-school-student-container">
      {flowIndex === 1 && (
        <HighSchoolName
          next={next}
          previous={previous}
          setAnswers={setAnswers}
        />
      )}
      {flowIndex === 2 &&
        (isCustomGradYear ? (
          <CustomGradYear
            next={next}
            previous={previous}
            setAnswers={setAnswers}
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
      {flowIndex === 3 && (
        <Act next={next} previous={previous} setAnswers={setAnswers} />
      )}
      {flowIndex === 4 && (
        <Sat next={next} previous={previous} setAnswers={setAnswers} />
      )}
      {flowIndex === 5 && (
        <Gpa next={next} previous={previous} setAnswers={setAnswers} />
      )}
    </div>
  );
};

export default HighSchoolStudent;
