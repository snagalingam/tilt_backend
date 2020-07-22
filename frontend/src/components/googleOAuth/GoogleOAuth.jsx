import React from "react";

import "./google-oauth.scss";

const GoogleOAuth = ({ signup, login }) => {
  return (
    <button className="google-oauth-button">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/1004px-Google_%22G%22_Logo.svg.png" />
      {signup && "Sign up with Google"}
      {login && "Login with Google"}
    </button>
  );
};

export default GoogleOAuth;
