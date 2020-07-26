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

export const ONBOARD_USER = gql`
  mutation OnboardUser(
    $id: ID
    $gpa: Float
    $actScore: Int
    $satScore: Int
    $termsAndConditions: Boolean
    $pronouns: String
    $ethnicity: String
    $userType: String
    $highschoolGraduationYear: Int
  ) {
    onboardUser(
      id: $id
      gpa: $gpa
      actScore: $actScore
      satScore: $satScore
      termsAndConditions: $termsAndConditions
      pronouns: $pronouns
      ethnicity: $ethnicity
      userType: $userType
      highschoolGraduationYear: $highschoolGraduationYear
    ) {
      user {
        email
        firstName
        lastName
        email
      }
    }
  }
`;
