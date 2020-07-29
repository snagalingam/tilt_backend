import React from "react";
import { Link } from "react-router-dom";
import { useQuery, useMutation } from "@apollo/client";

import { GET_ME } from "../../apollo/queries/account";
import { LOGOUT_USER } from "../../apollo/mutations/account";

import "./dashboard.scss";

const Dashboard = () => {
  const { data: meData, error, loading } = useQuery(GET_ME);
  const [logoutUser, response] = useMutation(LOGOUT_USER);

  function handleLogout() {
    logoutUser();
  }

  return (
    <div className="dashboard-container">
      <h1>{`Welcome ${meData?.me?.firstName}!`}</h1>
      <Link to="/onboarding">Onboarding</Link>
      <button onClick={handleLogout}>Log out</button>
    </div>
  );
};

export default Dashboard;
