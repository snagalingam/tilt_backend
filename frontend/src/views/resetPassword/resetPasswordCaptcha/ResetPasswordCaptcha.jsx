import React from "react";

const ResetPasswordCaptcha = ({ setCurrentView, views }) => {
  const { CONFIRM } = views;
  function handleSuccess() {
    setCurrentView(CONFIRM);
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
        <button onClick={handleSuccess}>Pretend this is captcha</button>
        <div className="form-footer">
          <p>Don't have an account? Get started</p>
        </div>
      </div>
    </div>
  );
};

export default ResetPasswordCaptcha;
