import { gql } from "apollo-boost";

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

export const SOCIAL_AUTH = gql`
  mutation SocialAuth($provider: String!, $accessToken: String!) {
    socialAuth(provider: $provider, accessToken: $accessToken) {
      social {
        uid
        extraData
      }
    }
  }
`;

// export const GET_TOKEN = gql`
//   mutation TokenAuth($email: String!, $password: String!) {
//     tokenAuth(email: $email, password: $password) {
//       token
//     }
//   }
// `;

// // { email, exp, orig-iat } = payload
// export const VERIFY_TOKEN = gql`
//   mutation VerifyToken($token: String!) {
//     verifyToken(token: $token) {
//       payload
//     }
//   }
// `;
