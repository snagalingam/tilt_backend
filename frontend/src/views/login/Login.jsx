import React from "react";
import { Link, Redirect } from "react-router-dom";
import { useQuery } from "@apollo/client";

import GoogleOAuth from "../../components/googleOAuth/GoogleOAuth";
import LoginForm from "./loginForm/LoginForm";
import SideCarousel from "../../components/sideCarousel/SideCarousel";

import { GET_IS_LOGGED_IN } from "../../apollo/queries/account";

import "./login.scss";

const Login = () => {
  const { data: data_isLoggedIn } = useQuery(GET_IS_LOGGED_IN);
  const { isLoggedIn } = data_isLoggedIn;

  if (isLoggedIn) return <Redirect push to="/dashboard" />;

  return (
    <div className="authentication-container login-container">
      <div className="authentication-left">
        <div className="tilt-logo">
          <a href="/">
            <img
              src="https://www.tiltaccess.com/static/media/tilt_logo.e727179e.png"
              alt="tilt-logo"
            />
          </a>
        </div>

        <SideCarousel />
      </div>

      <div className="authentication-right">
        <div className="form-container">
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
            <p>
              Don't have an account? <Link to="/signup">Get started</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
