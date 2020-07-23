import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";
import { useQuery } from "@apollo/client";

import { GET_ME } from "../../apollo/queries/account";

import "./dashboard.scss";

const Dashboard = () => {
  const { data, error, loading } = useQuery(GET_ME);

  if (loading) return <div>Loading...</div>;
  if (error) return <Redirect to="/login" />;

  return (
    <div className="dashboard-container">
      <h1>{`Welcome ${data?.me?.firstName}!`}</h1>
    </div>
  );

  return;
};

export default Dashboard;
