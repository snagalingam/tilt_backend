import { gql } from "@apollo/client";

export const CREATE_SCHOLARSHIP = gql`
  mutation CreateScholarship(
    $name: String!
    $amount: Int!
    $deadline: Date!
    $url: String!
  ) {
    createScholarship(
      name: $name
      amount: $amount
      deadline: $deadline
      url: $url
    ) {
      id
      name
      amount
      deadline
      url
    }
  }
`;
