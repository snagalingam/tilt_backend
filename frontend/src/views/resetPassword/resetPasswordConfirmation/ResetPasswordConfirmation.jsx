import React, { useState } from "react";
import { Redirect } from "react-router-dom";

import "./reset-password-confirmation.scss";

const ResetPasswordConfirmation = ({ setCurrentView, views }) => {
  const { FORM } = views;

  const [goBackToLogin, setGoBackToLogin] = useState(false);

  function handleResend() {
    setCurrentView(FORM);
  }

  function handleBack() {
    setGoBackToLogin(true);
  }

  return (
    <div className="reset-password-confirmation-view">
      <div className="form-container">
        <div className="form-header">
          <h1>Thanks, please check your email</h1>
          <p>Didn't get the email? Check your spam folder or resend.</p>
        </div>
        <button onClick={handleResend}>Resend</button>
        <button className="secondary-button" onClick={handleBack}>
          Back
        </button>
      </div>
      {goBackToLogin && <Redirect to="/login" />}
    </div>
  );
};

export default ResetPasswordConfirmation;
