import React, { useEffect, useRef } from "react";
import { ReCaptcha } from "react-recaptcha-google";
import { Link } from "react-router-dom";

import "./reset-password-recaptcha.scss";

const ResetPasswordCaptcha = ({ setCurrentView, views }) => {
  const captchaRef = useRef(null);

  const { CONFIRM } = views;

  function onLoadRecaptcha() {
    if (captchaRef.current) {
      captchaRef.current.reset();
    }
  }

  useEffect(() => {
    onLoadRecaptcha();
  }, []);

  function verifyCallback(recaptchaToken) {
    // API for verifying token with server
    // https://www.google.com/recaptcha/api/siteverify
    if (recaptchaToken) {
      setCurrentView(CONFIRM);
      // TODO: send reset password email
    } else {
      captchaRef.current.reset();
    }
  }

  return (
    <div className="reset-password-captcha-view">
      <div className="form-container">
        <div className="form-header">
          <h1>You're not a robot, are you?...</h1>
          <p>
            This helps prevent robots (and other nefarious machines) from
            accessing your Tilt account.
          </p>
        </div>

        <div className="recaptcha-container">
          <ReCaptcha
            ref={(el) => {
              captchaRef.current = el;
            }}
            size="normal"
            data-theme="dark"
            render="explicit"
            sitekey="6Ley1bQZAAAAAAfbuBKAeVO1NM6fNhRUMm1eCPDH"
            onloadCallback={onLoadRecaptcha}
            verifyCallback={verifyCallback}
          ></ReCaptcha>
        </div>

        <div className="form-footer">
          <p>
            Don't have an account? <Link to="/signup">Get started</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default ResetPasswordCaptcha;
