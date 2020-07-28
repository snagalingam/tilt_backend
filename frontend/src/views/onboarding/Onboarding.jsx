import React, { useState } from "react";
import { useQuery } from "@apollo/client";

import Completion from "./completion/Completion";
import Staff from "./staff/Staff";
import OtherUser from "./otherUser/OtherUser";
import Parent from "./parent/Parent";
import PreferredName from "./preferredName/PreferredName";
import SkipOnboarding from "./skipOnboarding/SkipOnboarding";
import Source from "./source/Source";
import Student from "./student/Student";
import UserType from "./userType/UserType";

import { GET_ME, GET_ONBOARDING_ANSWERS } from "../../apollo/queries/account";

const highSchoolFlow = {
  1: "Which school are you currently enrolled at?",
  2: "What year will you be graduating high school?",
  3: "What is your unweighted GPA?",
  4: "What was your highest SAT score?",
  5: "What was your highest ACT score?",
  6: "What is your family income?",
  7: "What are your preferred pronouns",
  8: "How do you identify yourself?",
};

const transferFlow = {
  1: "Which high school did you graduate from?",
  2: "What year did you graduate high school?",
  3: "What is your unweighted GPA?",
  4: "What was your highest SAT score?",
  5: "What was your highest ACT score?",
  6: "What is your family income?",
  7: "What are your preferred pronouns",
  8: "How do you identify yourself?",
};

const parentFlow = {
  1: "What school does your child currently attend?",
  2: "When is your child graduating?",
};

const staffFlow = {
  1: "What school or district do you work at?",
  2: "What year will your students graduate high school in?",
};

const otherFlow = {
  1: "Do you work at an organization that suppors students?",
};

const flow = {
  1: "Would you like to proceed or skip onboarding?",
  2: "What is your preferred name?",
  3: "What type of user are you?",
  4: { highSchoolFlow, transferFlow, parentFlow, staffFlow },
  5: "How did you hear about Tilt?",
  6: "Thank you!",
};

const flows = {
  highSchoolFlow,
  transferFlow,
  parentFlow,
  staffFlow,
  otherFlow,
};

const userTypes = {
  HIGH_SCHOOL: "student",
  TRANSFER: "transfer",
  PARENT: "parent",
  STAFF: "staff",
  OTHER: "other",
};

const Onboarding = () => {
  const { data: meData, error: meError } = useQuery(GET_ME);
  const { data: onboardingData } = useQuery(GET_ONBOARDING_ANSWERS);
  const { onboardingAnswers } = onboardingData;

  const [flowType, setFlowType] = useState(flow);
  const [flowIndex, setFlowIndex] = useState(1);

  function next(newFlow) {
    const indexBeforeFork = 3;
    const indexWhenMerge = 5;

    if (
      flowType === flow &&
      (flowIndex < indexBeforeFork || flowIndex >= indexWhenMerge)
    ) {
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
      setFlowType(flow);
      setFlowIndex(indexBeforeFork);
    }
    if (flowType === flow && flowIndex === indexWhenMerge) {
      setFlowType(newFlow);
      setFlowIndex(Object.keys(newFlow).length);
    }
  }

  const props = {
    me: meData?.me,
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
          <UserType {...props} flows={flows} userTypes={userTypes} />
        )}
        {/* fork */}
        {flowType === highSchoolFlow && <Student highSchool {...props} />}
        {flowType === transferFlow && <Student transfer {...props} />}
        {flowType === parentFlow && <Parent {...props} />}
        {flowType === staffFlow && <Staff {...props} />}
        {flowType === otherFlow && <OtherUser {...props} />}
        {/* merge */}
        {flowType[flowIndex] === flow[5] && (
          <Source {...props} flows={flows} userTypes={userTypes} />
        )}
        {flowType[flowIndex] === flow[6] && <Completion {...props} />}
      </div>
      {/* <div style={{ position: "absolute" }}>
        <ul>
          {Object.entries(onboardingAnswers).length > 0 &&
            Object.entries(onboardingAnswers).map(([key, value]) => (
              <li key={`${key}:${value}`}>{`${key}:${value}`}</li>
            ))}
        </ul>
      </div> */}
    </div>
  );
};

export default Onboarding;
