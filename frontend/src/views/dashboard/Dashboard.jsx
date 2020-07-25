import React from "react";
import { useQuery } from "@apollo/client";

import { GET_ME } from "../../apollo/queries/account";

import "./dashboard.scss";

const Dashboard = () => {
  const { data, error, loading } = useQuery(GET_ME);

  return (
    <div className="dashboard-container">
      <h1>{`Welcome ${data?.me?.firstName}!`}</h1>
    </div>
  );
};

export default Dashboard;
