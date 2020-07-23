import React, { useEffect, useState } from "react";

import { useQuery, gql } from "@apollo/client";
import { Redirect } from "react-router-dom";

const ME_QUERY = gql`
  {
    me {
      firstName
      lastName
      email
    }
  }
`;

const Dashboard = () => {
  const { loading, error, data } = useQuery(ME_QUERY);

  useEffect(() => {
    console.log(data, error, loading);
  }, [data]);

  return (
    <div>{`${data?.me?.firstName} ${data?.me?.lastName} ${data?.me?.email}`}</div>
  );

  return;
};

export default Dashboard;
