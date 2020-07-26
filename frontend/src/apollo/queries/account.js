import { gql } from "@apollo/client";

export const GET_ME = gql`
  query UserQuery {
    me {
      id
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

export const GET_ONBOARDING_ANSWERS = gql`
  query GetOnboardingAnswers {
    onboardingAnswers @client
  }
`;
