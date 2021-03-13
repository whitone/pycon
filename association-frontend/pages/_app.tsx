import { authExchange } from "@urql/exchange-auth";
import {
  cacheExchange,
  dedupExchange,
  fetchExchange,
  makeOperation,
  ssrExchange,
} from "urql";

import { withUrqlClient } from "next-urql";
import { Router } from "next/router";

import Footer from "~/components/footer/footer";
import Header from "~/components/header/header";
import { UserProvider } from "~/components/user-provider";

import "styles/globals.css";
import "tailwindcss/tailwind.css";

type AuthState = {
  token?: string;
};

const MyApp = ({ Component, pageProps, resetUrqlClient }) => {
  return (
    <div>
      <UserProvider resetUrqlClient={resetUrqlClient}>
        <Header />
        <main>
          <Component {...pageProps} />
        </main>
        <Footer />
      </UserProvider>
    </div>
  );
};

export default withUrqlClient((_ssrExchange) => ({
  url: "/graphql",
  exchanges: [
    dedupExchange,
    cacheExchange,
    ssrExchange,
    authExchange({
      didAuthError({ error }) {
        return error.graphQLErrors.some(
          (e) => e.extensions.exception.message === "Unauthorized",
        );
      },
      async getAuth({ authState }: { authState?: AuthState }) {
        console.log(`getAuth!! ${authState}`);
        if (!authState) {
          return null;
        }

        if (typeof window !== "undefined") {
          Router.replace("/logout");
        }

        return null;
      },
      addAuthToOperation({
        authState,
        operation,
      }: {
        authState?: AuthState;
        operation: any;
      }) {
        return operation;
      },
    }),
    fetchExchange,
  ],
  fetchOptions: {
    credentials: "include",
  },
}))(MyApp);
