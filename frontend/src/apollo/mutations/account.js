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
    $lastName: String
    $preferredName: String
    $gpa: Float
    $actScore: Int
    $satScore: Int
    $efc: Int
    $termsAndConditions: Boolean
    $pronouns: String
    $ethnicity: String
    $userType: String
    $highSchoolGradYear: Int
    $incomeQuintile: String
    $foundFrom: [String]
  ) {
    onboardUser(
      id: $id
      lastName: $lastName
      preferredName: $preferredName
      gpa: $gpa
      actScore: $actScore
      satScore: $satScore
      efc: $efc
      termsAndConditions: $termsAndConditions
      pronouns: $pronouns
      ethnicity: $ethnicity
      userType: $userType
      highSchoolGradYear: $highSchoolGradYear
      incomeQuintile: $incomeQuintile
      foundFrom: $foundFrom
    ) {
      user {
        email
        firstName
        lastName
        email
        preferredName
        gpa
        actScore
        satScore
        efc
        termsAndConditions
        pronouns
        ethnicity
        userType
        highSchoolGradYear
        incomeQuintile
        foundFrom
      }
    }
  }
`;

export const LOGOUT_USER = gql`
  mutation LogoutUser {
    logoutUser {
      user {
        email
      }
    }
  }
`;
