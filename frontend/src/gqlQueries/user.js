import { gql } from "apollo-boost";

export const GET_ME = gql`
  {
    me {
      firstName
      lastName
      email
    }
  }
`;

export const GET_USERS = gql`
  {
    users {
      firstName
      lastName
      email
    }
  }
`;

