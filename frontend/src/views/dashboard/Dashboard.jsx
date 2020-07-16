import React, { useRef } from "react";
import GoogleOAuth from "../../components/oAuth/GoogleOAuth";

const Dashboard = () => {
  return (
    <div>
      Dashboard
      <button>Logout</button>
      <a href="/logout">Logout</a>
      <GoogleOAuth style={{ display: "none" }} logout ref={googleLogout} />
    </div>
  );
};

export default Dashboard;
