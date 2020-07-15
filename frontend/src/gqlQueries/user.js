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

export const CREATE_USER = gql`
  mutation CreateUser(
    $firstName: String!
    $lastName: String!
    $email: String!
    $password: String
  ) {
    createUser(
      firstName: $firstName
      lastName: $lastName
      email: $email
      password: $password
    ) {
      user {
        firstName
        lastName
        email
      }
    }
  }
`;
