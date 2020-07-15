import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import GoogleOAuth from "../../components/oAuth/GoogleOAuth";
import SignUpForm from "../../components/form/SignUpForm";

import { APP_URLS } from "../../constants/urlConstants";

import "./sign-up-page.scss";

const { DASHBOARD } = APP_URLS;

const SignUpPage = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <>
      {isAuthenticated ? (
        <Redirect to={DASHBOARD} />
      ) : (
        <div className="sign-up-page">
          <SignUpForm setIsAuthenticated={setIsAuthenticated} />
          <div className="oauth-sign-up">
            <span>Sign up with</span>
            <div className="oauth-buttons">
              <GoogleOAuth setIsAuthenticated={setIsAuthenticated} />
              {/* <GoogleOAuth logout /> */}
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default SignUpPage;
