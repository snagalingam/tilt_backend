import React from 'react';
import gql from 'graphql-tag';
import { Query } from 'react-apollo';
import ScholarshipDetail from './ScholarshipDetail';


const SCHOLARSHIPS_QUERY = gql`
  {
    scholarships {
      id
      name
      amount
      deadline
      url
    }
  }
`;

const ScholarshipList = () => {
  return(
    <Query query={SCHOLARSHIPS_QUERY}>
      {({ loading, error, data }) => {
        if (loading) return <div>Loading ...</div>
        if (error) return <div>Error</div>

        const scholarshipsToRender = data.scholarships;

        console.log(scholarshipsToRender);

        return (
          <div>
            {scholarshipsToRender.map(scholarship =>
              <ScholarshipDetail
                key={scholarship.id}
                name={scholarship.name}
                amount={scholarship.amount}
                deadline={scholarship.deadline}
                url={scholarship.url}
              />
            )}
          </div>
        )
      }}
    </Query>
  );
};

export default ScholarshipList;
