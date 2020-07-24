import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";
import { useQuery } from "@apollo/client";
import { useHistory, useLocation } from "react-router-dom";

import CollegeStudent from "./collegeStudent/CollegeStudent";
import Completion from "./completion/Completion";
import Counselor from "./counselor/Counselor";
import Ethnicity from "./ethnicity/Ethnicity";
import HighSchoolStudent from "./highSchoolStudent/HighSchoolStudent";
import Parent from "./parent/Parent";
import PreferredName from "./preferredName/PreferredName";
import PreferredPronoun from "./preferredPronoun/PreferredPronoun";
import SkipOnboarding from "./skipOnboarding/SkipOnboarding";
import Source from "./source/Source";
import UserType from "./userType/UserType";

import { GET_ME } from "../../apollo/queries/account";

const highSchoolFlow = {
  1: "SCHOOL_NAME",
  2: "GRADUATION_YEAR",
};

const collegeFlow = {
  1: "GRADUATION_YEAR",
};

const parentFlow = {
  1: "GRADUATING",
};

const counselorFlow = {
  1: "HELPING",
};

const flow = {
  1: "SKIP_ONBOARDING",
  2: "PREFERRED_NAME",
  3: "USER_TYPE",
  4: { highSchoolFlow, collegeFlow, parentFlow, counselorFlow },
  5: "PREFERRED_PRONOUN",
  6: "ETHNICITIES",
  7: "SOURCE",
  8: "COMPLETE",
};

const Onboarding = () => {
  const { data, error, loading } = useQuery(GET_ME);

  // store this in apollo just in case user presses back button and they can continue where they left off
  const [flowType, setFlowType] = useState(flow);
  const [flowIndex, setFlowIndex] = useState(1);

  const [answers, setAnswers] = useState({});
  // const [questionNumber, setQuestionNumber] = useState(0);

  // if user already answered these questions, this page should not be accessible so redirect to dashboard
  // return <Redirect to='/dashboard' />

  // this should only be visible to people who are logged in
  function next(newFlow) {
    const numberOfItemsBeforeFork = 3;
    if (flowType === flow && flowIndex < numberOfItemsBeforeFork) {
      setFlowIndex((prev) => (prev += 1));
    }
    if (flowType === flow && flowIndex === numberOfItemsBeforeFork) {
      setFlowType(newFlow);
      setFlowIndex(1);
    }
    if (flowType !== flow && flowIndex < Object.keys(flowType).length) {
      setFlowIndex((prev) => (prev += 1));
    }
    if (flowType !== flow && flowIndex === Object.keys(flowType).length) {
      setFlowType(flow);
      setFlowIndex(5);
    }
  }

  useEffect(() => {
    console.log(flowType, flowIndex);
  }, [flowType, flowIndex]);

  function previous() {
    if (flowType === flow && flowIndex > 0) {
      setFlowIndex((prev) => (prev -= 1));
    }
  }

  useEffect(() => {
    console.log(answers);
  }, [answers]);

  const props = {
    me: data?.me || {},
    answers,
    setAnswers,
    next,
    previous,
    flowIndex,
  };

  const flows = {
    highSchool: highSchoolFlow,
    college: collegeFlow,
    parent: parentFlow,
    counselor: counselorFlow,
  };

  return (
    <div className="authentication-container onboarding-container">
      <div className="authentication-left"></div>
      <div className="authentication-right">
        {flowType[flowIndex] === flow[1] && <SkipOnboarding {...props} />}
        {flowType[flowIndex] === flow[2] && <PreferredName {...props} />}
        {flowType[flowIndex] === flow[3] && <UserType {...props} {...flows} />}
        {flowType[flowIndex] === flow[5] && <PreferredPronoun {...props} />}
        {flowType[flowIndex] === flow[6] && <Ethnicity {...props} />}
        {flowType[flowIndex] === flow[7] && <Source {...props} />}
        {flowType[flowIndex] === flow[8] && <Completion {...props} />}
        {flowType === highSchoolFlow && <HighSchoolStudent {...props} />}
        {flowType === collegeFlow && <CollegeStudent {...props} />}
        {flowType === parentFlow && <Parent {...props} />}
        {flowType === counselorFlow && <Counselor {...props} />}
      </div>
    </div>
  );
};

export default Onboarding;
