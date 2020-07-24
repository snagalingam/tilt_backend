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
  1: "High school name",
  2: "Graduation year",
  3: "Have you taken the ACT yet?",
  4: "Highest ACT score?",
  5: "Have you taken the SAT yet?",
  6: "What was your highest score?",
  7: "What is your unweighted GPA?",
};

const collegeFlow = {
  1: "graduation year",
};

const parentFlow = {
  1: "when is your child graduating?",
};

const counselorFlow = {
  1: "are you helping a student?",
};

const flow = {
  1: "proceed or skip onboarding",
  2: "preferred name",
  3: "user type",
  4: { highSchoolFlow, collegeFlow, parentFlow, counselorFlow },
  5: "preferred pronounc",
  6: "ethnicity",
  7: "how did you hear about us?",
  8: "complete!",
};

const flows = {
  highSchool: highSchoolFlow,
  college: collegeFlow,
  parent: parentFlow,
  counselor: counselorFlow,
};

const userTypes = {
  HIGH_SCHOOL: "high school",
  COLLEGE: "college",
  PARENT: "parent",
  COUNSELOR: "counselor",
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
    const indexBeforeFork = 3;
    if (flowType === flow && flowIndex < indexBeforeFork) {
      setFlowIndex((prev) => (prev += 1));
    }
    if (flowType === flow && flowIndex === indexBeforeFork) {
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

  function previous(newFlow) {
    const indexBeforeFork = 3;
    const indexWhenMerge = 5;
    if (flowType === flow && flowIndex > 0) {
      setFlowIndex((prev) => (prev -= 1));
    }
    if (flowType !== flow && flowIndex > 0) {
      setFlowIndex((prev) => (prev -= 1));
    }
    if (flowType !== flow && flowIndex === 1) {
      console.log("hi");
      setFlowType(flow);
      setFlowIndex(indexBeforeFork);
    }
    if (flowType === flow && flowIndex === indexWhenMerge) {
      setFlowType(newFlow);
      setFlowIndex(Object.keys(newFlow).length);
    }
  }

  useEffect(() => {
    console.log(flowType, flowIndex);
  }, [flowType, flowIndex]);

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

  return (
    <div className="authentication-container onboarding-container">
      <div className="authentication-left"></div>
      <div className="authentication-right">
        {flowType[flowIndex] === flow[1] && <SkipOnboarding {...props} />}
        {flowType[flowIndex] === flow[2] && <PreferredName {...props} />}
        {flowType[flowIndex] === flow[3] && (
          <UserType {...props} {...flows} userTypes={userTypes} />
        )}
        {flowType[flowIndex] === flow[5] && (
          <PreferredPronoun {...props} {...flows} userTypes={userTypes} />
        )}
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
