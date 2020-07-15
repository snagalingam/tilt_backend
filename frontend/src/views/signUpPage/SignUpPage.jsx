import React from "react";
import { useEffect } from "react";
import FacebookIcon from "@material-ui/icons/Facebook";

import SignUpForm from "../../components/form/SignUpForm";
import TiltButton from "../../components/button/TiltButton";
import { CREATE_USER } from "../../gqlQueries/user";
import GoogleOAuth from "../../components/oAuth/GoogleOAuth";

import "./sign-up-page.scss";

const SignUpPage = () => {
  useEffect(() => {}, []);

  return (
    <div className="sign-up-page">
      <SignUpForm />
      <div className="oauth-sign-up">
        <span>Sign up with</span>
        <div className="oauth-buttons">
          <GoogleOAuth />
          <GoogleOAuth logout />
        </div>
      </div>
    </div>
  );
};

export default SignUpPage;
