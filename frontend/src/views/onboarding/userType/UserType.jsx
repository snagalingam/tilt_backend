import React from "react";
import { useQuery } from "@apollo/client";

import { GET_ONBOARDING_ANSWERS } from "../../../apollo/queries/account";
import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";

import "./user-type.scss";

const UserType = ({
  previous,
  next,
  highSchoolFlow,
  collegeFlow,
  parentFlow,
  counselorFlow,
  otherFlow,
  userTypes,
}) => {
  const { data: onboardingData } = useQuery(GET_ONBOARDING_ANSWERS);
  const { onboardingAnswers } = onboardingData;
  const { preferredName } = onboardingAnswers;

  const { HIGH_SCHOOL, COLLEGE, PARENT, COUNSELOR, OTHER } = userTypes;

  function handleHighSchool() {
    onboardingAnswersVar({ ...onboardingAnswers, userType: HIGH_SCHOOL });
    next(highSchoolFlow);
  }

  function handleCollege() {
    onboardingAnswersVar({ ...onboardingAnswers, userType: COLLEGE });
    next(collegeFlow);
  }

  function handleParent() {
    onboardingAnswersVar({ ...onboardingAnswers, userType: PARENT });
    next(parentFlow);
  }

  function handleCounselor() {
    onboardingAnswersVar({ ...onboardingAnswers, userType: COUNSELOR });
    next(counselorFlow);
  }

  function handleOther() {
    onboardingAnswersVar({ ...onboardingAnswers, userType: OTHER });
    next(otherFlow);
  }

  function handlePrevious() {
    const copy = { ...onboardingAnswers };
    if (copy.userType) delete copy.userType;
    onboardingAnswersVar(copy);
    previous();
  }

  return (
    <div className="user-type-container form-container">
      <div className="form-header">
        <h1>{`Thanks ${preferredName}!`}</h1>
        <h1>So, are you a...?</h1>
      </div>
      <div className="form-body">
        <div>
          <div className="first-row">
            <button onClick={handleHighSchool} className="block-button ">
              High School Student
            </button>
            <button onClick={handleCollege} className="block-button ">
              College Student
            </button>
            <button onClick={handleParent} className="block-button ">
              Parent
            </button>
          </div>
          <div className="second-row">
            <button onClick={handleCounselor} className="block-button ">
              Counselor, Teacher or Administrator
            </button>
            <button className="block-button" onClick={handleOther}>
              Other
            </button>
          </div>
        </div>
      </div>
      <div className="onboarding-buttons">
        <button className="secondary-button" onClick={handlePrevious}>
          Back
        </button>
      </div>
    </div>
  );
};

export default UserType;
