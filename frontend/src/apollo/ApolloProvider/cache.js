import { InMemoryCache } from "@apollo/client";

import { isLoggedInVar } from "../reactiveVariables/account";

export const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        isLoggedIn: {
          read() {
            return isLoggedInVar();
          },
        },
      },
    },
  },
});
