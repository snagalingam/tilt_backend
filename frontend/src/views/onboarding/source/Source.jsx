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

import "./source.scss";

const Source = ({ previous, next, userTypes, flows }) => {
  const [onboardUser, response] = useMutation(ONBOARD_USER);
  const { data: onboardingData } = useQuery(GET_ONBOARDING_ANSWERS);
  const { data: meData } = useQuery(GET_ME);
  const { onboardingAnswers } = onboardingData;

  const [isCustomSource, toggleIsCustomSource] = useState(false);
  const [otherSource, setOther] = useState(null);
  const [sources, selectSources] = useState([]);

  const { HIGH_SCHOOL, COLLEGE, PARENT, COUNSELOR, OTHER } = userTypes;
  const {
    highSchoolFlow,
    collegeFlow,
    parentFlow,
    counselorFlow,
    otherFlow,
  } = flows;
  const { userType } = onboardingAnswers;

  function handlePrevious() {
    if (userType === HIGH_SCHOOL) {
      previous(highSchoolFlow);
    }
    if (userType === COLLEGE) {
      previous(collegeFlow);
    }
    if (userType === PARENT) {
      previous(parentFlow);
    }
    if (userType === COUNSELOR) {
      previous(counselorFlow);
    }
    if (userType === OTHER) {
      if (onboardingAnswers?.organizationName)
        delete onboardingAnswers.organizationName;
      if (onboardingAnswers?.graduationYear)
        delete onboardingAnswers.graduationYear;
      onboardingAnswersVar(onboardingAnswers);
      previous(otherFlow);
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

  const sourceButton = (option) => {
    const index = sources.indexOf(option);
    return (
      <button
        key={option}
        onClick={() => handleClick(option)}
        className={`block-button${index >= 0 ? " selected" : ""}`}
      >
        {option}
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
          {["Instagram", "Facebook", "Parent"].map((source) =>
            sourceButton(source)
          )}
        </div>
        <div className="second-row">
          {["School or District Staff", "Friend"].map((source) =>
            sourceButton(source)
          )}
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
