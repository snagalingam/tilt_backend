import React from "react";
import { ApolloClient, ApolloProvider, createHttpLink } from "@apollo/client";

import { cache } from "./cache";

const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql",
  credentials: "same-origin",
});

const client = new ApolloClient({
  link: httpLink,
  cache,
});

export default function Apollo({ children }) {
  return <ApolloProvider client={client}>{children}</ApolloProvider>;
}
