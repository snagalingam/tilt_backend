import { InMemoryCache } from "@apollo/client";

import {
  isLoggedInVar,
  onboardingAnswersVar,
} from "../reactiveVariables/account";

export const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        isLoggedIn: {
          read() {
            return isLoggedInVar();
          },
        },
        onboardingAnswers: {
          read() {
            return onboardingAnswersVar();
          },
        },
      },
    },
  },
});
