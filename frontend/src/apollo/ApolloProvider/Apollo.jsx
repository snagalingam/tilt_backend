import React from "react";
import { ApolloClient, ApolloProvider, createHttpLink } from "@apollo/client";

import { cache } from "./cache";

const environment = process.env.NODE_ENV || "development";

const httpLink = createHttpLink({
  uri: "/graphql",
  credentials: "same-origin",
});

const client = new ApolloClient({
  link: httpLink,
  cache,
});

export default function Apollo({ children }) {
  return <ApolloProvider client={client}>{children}</ApolloProvider>;
}
