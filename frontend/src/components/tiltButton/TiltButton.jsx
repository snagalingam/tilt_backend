import { Button } from "@material-ui/core";
import React from "react";

import "./tilt-button.scss";

const TiltButton = ({ children, classes = [], type, onClick }) => {
  classes.push("TiltButton");
  const classString = classes.join(" ");
  return (
    <Button className={classString} type={type} onClick={onClick}>
      {children}
    </Button>
  );
};

export default TiltButton;
