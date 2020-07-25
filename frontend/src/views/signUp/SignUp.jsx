import React from "react";
import { Link, Redirect } from "react-router-dom";
import { useQuery } from "@apollo/client";

import GoogleOAuth from "../../components/googleOAuth/GoogleOAuth";
import SignUpForm from "./signUpForm/SignUpForm";

import { GET_IS_LOGGED_IN } from "../../apollo/queries/account";

import "./sign-up.scss";

const SignUp = () => {
  const { data: data_isLoggedIn } = useQuery(GET_IS_LOGGED_IN);

  if (data_isLoggedIn) return <Redirect push to="/dashboard" />;

  return (
    <div className="authentication-container sign-up-container">
      <div className="authentication-left">
        <div className="tilt-logo">
          <img
            src="https://www.tiltaccess.com/static/media/tilt_logo.e727179e.png"
            alt="tilt-logo"
          ></img>
        </div>

        <div className="tilt-message-container">
          <div className="tilt-message">
            <h2>Find affordable colleges</h2>
            <p>We estimate college prices based on your family income</p>
          </div>
          <div className="tilt-message">
            <h2>Meet your Financial Aid Advisor</h2>
            <p>They can answer any questions that come up along the way</p>
          </div>
          <div className="tilt-message">
            <h2>Budget for college</h2>
            <p>We'll walk you through your scholarship and loan options</p>
          </div>
        </div>

        <div className="tilt-footer">
          <p>Tilt 2020</p>
        </div>
      </div>

      <div className="authentication-right">
        <div className="form-container">
          <div className="form-header">
            <h1>Create your Tilt account</h1>
            <p>No credit card required. Cancel anytime.</p>
          </div>

          <GoogleOAuth signup />

          <div className="form-divider">
            <div />
            <span>OR</span>
            <div />
          </div>

          <SignUpForm />

          <div className="form-footer">
            <p>
              Have an account? <Link to="/login">Sign in</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
