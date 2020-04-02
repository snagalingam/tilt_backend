import React from 'react';
import ScholarshipDetail from './ScholarshipDetail';


const ScholarshipList = props => {
  const linksToRender = [
    {
      id: '1',
      description: 'Prisma turns your database into a GraphQL API 😎',
      url: 'https://www.prismagraphql.com',
    },
    {
      id: '2',
      description: 'The best GraphQL client',
      url: 'https://www.apollographql.com/docs/react/',
    },
  ]

  return(
    <div>
    {linksToRender.map(scholarship =>
        <ScholarshipDetail
          key={scholarship.id}
          description={scholarship.description}
          url={scholarship.url}
        />
      )
    };
    </div>
  );
};

export default ScholarshipList;
