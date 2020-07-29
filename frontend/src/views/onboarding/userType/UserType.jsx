import React from "react";
import { useQuery } from "@apollo/client";

import { GET_ONBOARDING_ANSWERS } from "../../../apollo/queries/account";
import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";
import { USER_TYPE } from "../../../helper/databaseVariables";

import "./user-type.scss";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

const { K12, TRANSFER, PARENT, STAFF, OTHER } = USER_TYPE;

const UserType = ({ previous, next, flows }) => {
  const { data: onboardingData } = useQuery(GET_ONBOARDING_ANSWERS);
  const { onboardingAnswers } = onboardingData;
  const { preferredName } = onboardingAnswers;

  const {
    highSchoolFlow,
    transferFlow,
    parentFlow,
    staffFlow,
    otherFlow,
  } = flows;

  function handleClick(value) {
    onboardingAnswersVar({ ...onboardingAnswers, userType: value });

    switch (value) {
      case K12.value:
        next(highSchoolFlow);
        break;
      case TRANSFER.value:
        next(transferFlow);
        break;
      case PARENT.value:
        next(parentFlow);
        break;
      case STAFF.value:
        next(staffFlow);
        break;
      case OTHER.value:
        next(otherFlow);
        break;
      default:
    }
  }

  function handlePrevious() {
    const copy = { ...onboardingAnswers };
    if (copy.userType) delete copy.userType;
    onboardingAnswersVar(copy);
    previous();
  }

  const userTypeButton = ({ display, value }) => (
    <button
      key={value}
      className="block-button"
      onClick={() => handleClick(value)}
    >
      {display}
    </button>
  );

  return (
    <OnboardingTemplate
      name="user-type"
      h1Array={[`Thanks ${preferredName}!`, "So, are you a...?"]}
      previousFunc={handlePrevious}
    >
      <div>
        <div className="first-row">
          {[K12, TRANSFER, PARENT].map((object) => userTypeButton(object))}
        </div>
        <div className="second-row">
          {[STAFF, OTHER].map((object) => userTypeButton(object))}
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default UserType;
