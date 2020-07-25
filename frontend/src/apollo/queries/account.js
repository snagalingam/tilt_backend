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

export const GET_IS_LOGGED_IN = gql`
  query GetIsLoggedIn {
    isLoggedIn @client
  }
`;
