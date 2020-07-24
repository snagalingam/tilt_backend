import React from "react";
import { Query } from "@apollo/client/react/components";
import ScholarshipDetail from "./ScholarshipDetail";

import { SCHOLARSHIPS_QUERY } from "../../../apollo/queries/scholarship";

const ScholarshipList = () => {
  return (
    <Query query={SCHOLARSHIPS_QUERY}>
      {({ loading, error, data }) => {
        if (loading) return <div>Loading ...</div>;
        if (error) return <div>Error</div>;

        const scholarshipsToRender = data.scholarships;

        console.log(scholarshipsToRender);

        return (
          <div>
            {scholarshipsToRender.map((scholarship) => (
              <ScholarshipDetail
                key={scholarship.id}
                name={scholarship.name}
                amount={scholarship.amount}
                deadline={scholarship.deadline}
                url={scholarship.url}
              />
            ))}
          </div>
        );
      }}
    </Query>
  );
};

export default ScholarshipList;
