import React, { useState } from "react";
import { Link } from "react-router-dom";

import ResetPasswordCaptcha from "./resetPasswordCaptcha/ResetPasswordCaptcha";
import ResetPasswordConfirmation from "./resetPasswordConfirmation/ResetPasswordConfirmation";
import ResetPasswordForm from "./resetPasswordForm/ResetPasswordForm";
import SideCarousel from "../../components/sideCarousel/SideCarousel";

import "./reset-password.scss";

const RESET_PASSWORD_VIEWS = {
  FORM: "FORM",
  CAPTCHA: "CAPTCHA",
  CONFIRM: "CONFIRM",
};

const { FORM, CAPTCHA, CONFIRM } = RESET_PASSWORD_VIEWS;

const ResetPassword = () => {
  const [currentView, setCurrentView] = useState(FORM);
  function handleSubmit(values) {
    if (values.email) {
      setCurrentView(CAPTCHA);
    }
  }

  return (
    <div className="authentication-container reset-password-container">
      <div className="authentication-left">
        <div className="tilt-logo">
          <img
            src="https://www.tiltaccess.com/static/media/tilt_logo.e727179e.png"
            alt="tilt-logo"
          ></img>
        </div>

        <SideCarousel />
      </div>

      <div className="authentication-right">
        {currentView === FORM && (
          <div className="reset-password-form-view">
            <div className="form-container">
              <div className="form-header">
                <h1>Reset Password</h1>
                <p>
                  Enter the email address associated with your account and we'll
                  send you a link to reset your password.
                </p>
              </div>

              <ResetPasswordForm handleSubmit={handleSubmit} />

              <div className="form-footer">
                <p>
                  Don't have an account? <Link to="/signup">Get started</Link>
                </p>
              </div>
            </div>
          </div>
        )}

        {currentView === CAPTCHA && (
          <ResetPasswordCaptcha
            setCurrentView={setCurrentView}
            views={RESET_PASSWORD_VIEWS}
          />
        )}

        {currentView === CONFIRM && (
          <ResetPasswordConfirmation
            setCurrentView={setCurrentView}
            views={RESET_PASSWORD_VIEWS}
          />
        )}
      </div>
    </div>
  );
};

export default ResetPassword;
