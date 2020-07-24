import { gql } from "@apollo/client";

export const LOGIN_MUTATION = gql`
  mutation LOGIN_USER($email: String!, $password: String!) {
    loginUser(email: $email, password: $password) {
      user {
        email
      }
    }
  }
`;

export const SIGNUP_MUTATION = gql`
  mutation CREATE_USER(
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