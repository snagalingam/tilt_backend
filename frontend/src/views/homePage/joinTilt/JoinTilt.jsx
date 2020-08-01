import React from "react";
import CheckCircleIcon from "@material-ui/icons/CheckCircle";
import CancelIcon from "@material-ui/icons/Cancel";

import BrushedText from "../../../components/brushedText/BrushedText";
import CommunityCard from "./communityCard/CommunityCard";

import esIcon from "../../../img/clients/esIcon.png";
import gwIcon from "../../../img/clients/gwIcon.png";
import sin from "../../../img/sin.jpeg";
import "./join-tilt.scss";

const cardOne = (
  <div className="card-one">
    <h3>WELCOME TO TILT</h3>
    <div>
      <label>First Last Name</label>
      <p>Kathryn Murphy</p>
    </div>
    <div>
      <label>So, are you a... ?</label>
      <p>High School Student</p>
    </div>
  </div>
);

const cardTwo = (
  <div className="card-two">
    <div>
      <img src={gwIcon} />
      <p>George Westinghouse College Prep</p>
    </div>
    <div>
      <img src={esIcon} />
      <p>Eric Solorio High School</p>
    </div>
  </div>
);

const cardThree = (
  <div className="card-three">
    <div className="card-three-message">
      <img src={sin} />
      <div>
        <p>Congratulations!</p>
        <p>Your application has been approved.</p>
      </div>
    </div>
    <div className="card-three-approve">
      <CancelIcon className="cancel" />
      <CheckCircleIcon className="approve" />
    </div>
  </div>
);

const JoinTilt = () => {
  return (
    <div className="JoinTilt">
      <div className="JoinTilt__header">
        <h2>
          Join the <BrushedText text="Tilt" /> community
        </h2>
      </div>
      <div className="JoinTilt__community-cards">
        <CommunityCard
          step="1"
          stepColor="purple"
          card={cardOne}
          header="Sign up for free"
          text="We will always provide our services free of charge to students and families."
        />
        <CommunityCard
          step="2"
          stepColor="orange"
          card={cardTwo}
          header="Apply to affordable colleges"
          text="We will find you colleges that are likely to offer you the most money."
        />
        <CommunityCard
          step="3"
          stepColor="purple"
          card={cardThree}
          header="Get the most amount of aid"
          text="Our advisors will help you apply to financial aid and scholarships."
        />
      </div>
    </div>
  );
};

export default JoinTilt;
