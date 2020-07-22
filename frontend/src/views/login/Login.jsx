import React from "react";

import GoogleOAuth from "../../components/googleOAuth/GoogleOAuth";
import LoginCarousel from "./loginCarousel/LoginCarousel";
import LoginForm from "./loginForm/LoginForm";

import "./login.scss";

const Login = () => {
  return (
    <div className="authentication-container login-container">
      <div className="authentication-left">
        <div className="tilt-logo">
          <img src="https://www.tiltaccess.com/static/media/tilt_logo.e727179e.png"></img>
        </div>

        <LoginCarousel />
      </div>

      <div className="authentication-right">
        <div className="form">
          <div className="form-header">
            <h1>Welcome to Tilt</h1>
            <p>
              We provide friendly reports simplifying your financial aid
              packages and helping you compare across colleges
            </p>
          </div>
          <GoogleOAuth login />

          <div className="form-divider">
            <div />
            <span>OR</span>
            <div />
          </div>

          <LoginForm />

          <div className="form-footer">
            <p>Don't have an account? Get started</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
