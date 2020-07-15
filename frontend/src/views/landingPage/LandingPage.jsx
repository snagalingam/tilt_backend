import React from "react";
import { Link } from "react-router-dom";

const LandingPage = () => {
  return (
    <div>
      Landing Page
      <Link to="/signup" />
      <Link to="/login" />
    </div>
  );
};

export default LandingPage;
