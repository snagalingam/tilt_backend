import React, { useState } from "react";
import { Redirect } from "react-router-dom";

const Source = ({ previous }) => {
  return (
    <div className="source-container form-container">
      Source<button onClick={previous}>Back</button>
    </div>
  );
};

export default Source;
