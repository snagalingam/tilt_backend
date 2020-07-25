import React from "react";

import Organization from "../organization/Organization";

const OtherUser = (props) => {
  const { flowIndex } = props;

  return (
    <div className="other-user-container">
      {flowIndex === 1 && <Organization {...props} />}
    </div>
  );
};

export default OtherUser;
