import React, { useEffect, useState } from "react";
import { useMutation, useQuery } from "@apollo/client";

import CustomSource from "./CustomSource";
import OnboardingTemplate from "../onboardingTemplate/OnboardingTemplate";

import { ONBOARD_USER } from "../../../apollo/mutations/account";
import {
  GET_ONBOARDING_ANSWERS,
  GET_ME,
} from "../../../apollo/queries/account";
import { onboardingAnswersVar } from "../../../apollo/reactiveVariables/account";
import { USER_TYPE, FOUND_FROM } from "../../../helper/databaseVariables";

import "./source.scss";

const { K12, TRANSFER, PARENT, STAFF, OTHER } = USER_TYPE;
const { IG, FB, PARENT_SOURCE, STAFF_SOURCE, FRIEND } = FOUND_FROM;

const Source = ({ previous, next, flows }) => {
  const [onboardUser, response] = useMutation(ONBOARD_USER);
  const { data: onboardingData } = useQuery(GET_ONBOARDING_ANSWERS);
  const { data: meData } = useQuery(GET_ME);
  const { onboardingAnswers } = onboardingData;
  const { userType } = onboardingAnswers;

  const [isCustomSource, toggleIsCustomSource] = useState(false);
  const [otherSource, setOther] = useState(null);
  const [sources, selectSources] = useState([]);

  const {
    highSchoolFlow,
    transferFlow,
    parentFlow,
    staffFlow,
    otherFlow,
  } = flows;

  function handlePrevious() {
  switch (userType) {
      case K12.value:
        previous(highSchoolFlow);
        break;
      case TRANSFER.value:
        previous(transferFlow);
        break;
      case PARENT.value:
        previous(parentFlow);
        break;
      case STAFF.value:
        previous(staffFlow);
        break;
      case OTHER.value:
        const copy = { ...onboardingAnswers };
        if (copy?.organizationName) delete copy.organizationName;
        if (copy?.highSchoolGradYear) delete copy.highSchoolGradYear;
        onboardingAnswersVar(copy);
        previous(otherFlow);
        break;
      default:
    }
  }

  function handleClick(option) {
    const copy = [...sources];
    const index = copy.indexOf(option);
    if (index >= 0) {
      copy.splice(index, 1);
    } else {
      copy.push(option);
    }
    selectSources(copy);
  }

  const sourceButton = ({ display, value }) => {
    const index = sources.indexOf(value);
    return (
      <button
        key={value}
        onClick={() => handleClick(value)}
        className={`block-button${index >= 0 ? " selected" : ""}`}
      >
        {display}
      </button>
    );
  };

  function handleSave() {
    const copy = [...sources];
    const index = copy.indexOf(otherSource);
    if (index < 0 && otherSource) {
      copy.push(otherSource);
    }
    selectSources(copy);
    const updatedOnboardingAnswers = { ...onboardingAnswers, sources: copy };
    onboardingAnswersVar(updatedOnboardingAnswers);
    onboardUser({
      variables: { ...updatedOnboardingAnswers, id: meData?.me?.id },
    });
    next();
  }

  if (isCustomSource)
    return (
      <CustomSource
        previous={() => toggleIsCustomSource(false)}
        addCustomSource={setOther}
      />
    );

  return (
    <OnboardingTemplate
      name="source"
      h1="How did you hear about Tilt?"
      nextFunc={handleSave}
      previousFunc={handlePrevious}
    >
      <div>
        <div className="first-row">
          {[IG, FB, PARENT_SOURCE].map((object) => sourceButton(object))}
        </div>
        <div className="second-row">
          {[STAFF_SOURCE, FRIEND].map((source) => sourceButton(source))}
          <button
            className={`block-button${otherSource ? " selected" : ""}`}
            onClick={() => toggleIsCustomSource(true)}
          >
            {otherSource || "Other"}
          </button>
        </div>
      </div>
    </OnboardingTemplate>
  );
};

export default Source;
