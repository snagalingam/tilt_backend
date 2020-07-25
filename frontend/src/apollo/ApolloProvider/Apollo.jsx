import React from "react";
import { ApolloClient, ApolloProvider, createHttpLink } from "@apollo/client";

import { cache } from "./cache";

const httpLink = createHttpLink({
  uri: "https://tilt-website-staging.herokuapp.com//graphql",
  credentials: "same-origin",
});

const client = new ApolloClient({
  link: httpLink,
  cache,
});

export default function Apollo({ children }) {
  return <ApolloProvider client={client}>{children}</ApolloProvider>;
}
