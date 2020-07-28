import React from "react";
import { ApolloClient, ApolloProvider, createHttpLink } from "@apollo/client";

import { cache } from "./cache";

const environment = process.env.NODE_ENV || "development";

const httpLink = createHttpLink({
  uri:
    environment === "development"
      ? "http://localhost:8000/graphql"
      : "https://tilt-website-staging.herokuapp.com/graphql",
  credentials: "same-origin",
});

const client = new ApolloClient({
  link: httpLink,
  cache,
});

export default function Apollo({ children }) {
  return <ApolloProvider client={client}>{children}</ApolloProvider>;
}
