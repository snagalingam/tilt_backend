import React, { useEffect } from "react";
import { GoogleLogin, GoogleLogout } from "react-google-login";
import { useMutation } from "@apollo/react-hooks";
import Cookies from "js-cookie";

import { SOCIAL_AUTH } from "../../gqlQueries/authentication";

const GoogleOAuth = ({ logout, setIsAuthenticated }) => {
  const handleError = (error) => {
    console.log(error);
  };

  const [socialAuth, { data, error, loading }] = useMutation(SOCIAL_AUTH, {
    onError: handleError,
  });

  const handleSignUpLogin = (response) => {
    const { accessToken } = response;

    socialAuth({
      variables: {
        provider: "google-oauth2",
        accessToken,
      },
    });
  };

  useEffect(() => {
    if (data && !error && !loading) {
      setIsAuthenticated(true);
    }
  }, [data]);

  const handleLogout = (response) => {
    console.log(response);
  };

  return (
    <>
      {logout ? (
        <GoogleLogout
          clientId="202817388070-in7f4g0896eg0c393odpeig3ein3ebs5.apps.googleusercontent.com"
          buttonText="logout"
          onLogoutSuccess={handleLogout}
        />
      ) : (
        <GoogleLogin
          clientId="202817388070-in7f4g0896eg0c393odpeig3ein3ebs5.apps.googleusercontent.com"
          buttonText="Login"
          onSuccess={handleSignUpLogin}
          onFailure={handleError}
          cookiePolicy={"single_host_origin"}
        />
      )}
    </>
  );
};

export default GoogleOAuth;
