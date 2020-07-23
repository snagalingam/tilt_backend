import { gql } from "@apollo/client";

export const GET_ME = gql`
  query UserQuery {
    me {
      firstName
      lastName
      email
    }
  }
`;
