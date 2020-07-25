import React from "react";
import { useQuery } from "@apollo/client";
import { Redirect } from "react-router-dom";

import { GET_IS_LOGGED_IN } from "../../apollo/queries/account";

const ProtectedRoute = ({ component: Component }) => {
  const {
    data: data_isLoggedIn,
    loading: loading_isLoggedIn,
    error: error_isLoggedIn,
  } = useQuery(GET_IS_LOGGED_IN);

  if (data_isLoggedIn) return <Component />;
  if (!data_isLoggedIn) return <Redirect push to="/" />;
};

export default ProtectedRoute;
