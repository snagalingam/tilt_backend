import { gql } from "@apollo/client";

export const SCHOLARSHIPS_QUERY = gql`
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
