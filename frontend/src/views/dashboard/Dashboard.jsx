import React, { useRef } from "react";
import GoogleOAuth from "../../components/oAuth/GoogleOAuth";

const Dashboard = () => {
  return (
    <div>
      Dashboard
      <a href="/logout">Logout</a>
      <GoogleOAuth style={{ display: "none" }} logout />
    </div>
  );
};

export default Dashboard;
