import { gql } from "apollo-boost";

export const GET_TOKEN = gql`
  mutation TokenAuth($email: String!, $password: String!) {
    tokenAuth(email: $email, password: $password) {
      token
    }
  }
`;

export const GET_SOCIAL_TOKEN = gql`
  mutation SocialAuth($provider: String!, $accessToken: String!) {
    socialAuth(provider: $provider, accessToken: $accessToken) {
      social {
        uid
      }
      token
    }
  }
`;

export const GOOGLE_GET_TOKEN = gql`
  mutation TokenAuth($email: String!, $googleId: String!) {
    tokenAuth(email: $email, googleId: $googleId) {
      token
    }
  }
`;

export const FB_GET_TOKEN = gql`
  mutation TokenAuth($email: String!, $facebookId: String!) {
    tokenAuth(email: $email, facebookId: $facebookId) {
      token
    }
  }
`;

// { email, exp, orig-iat } = payload
export const VERIFY_TOKEN = gql`
  mutation VerifyToken($token: String!) {
    verifyToken(token: $token) {
      payload
    }
  }
`;
