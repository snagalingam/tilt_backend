import { gql } from "@apollo/client";

export const LOGIN = gql`
  mutation LoginUser($email: String!, $password: String!) {
    loginUser(email: $email, password: $password) {
      user {
        email
      }
    }
  }
`;

export const SIGN_UP = gql`
  mutation CreateUser(
    $email: String!
    $firstName: String
    $lastName: String
    $password: String!
  ) {
    createUser(
      email: $email
      firstName: $firstName
      lastName: $lastName
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
