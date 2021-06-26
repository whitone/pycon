require("dotenv").config();
const path = require("path");
// const withSourceMaps = require("@zeit/next-source-maps");
const { withSentryConfig } = require("@sentry/nextjs");

const {
  SENTRY_ORG,
  SENTRY_PROJECT,
  SENTRY_AUTH_TOKEN,
  VERCEL_GITHUB_COMMIT_SHA,
  CONFERENCE_CODE,
  API_URL,
  API_TOKEN,
  VERCEL_ENV,
} = process.env;

const SentryWebpackPluginOptions = {
  silent: true,
  org: SENTRY_ORG,
  project: SENTRY_PROJECT,
  authToken: SENTRY_AUTH_TOKEN,
  release: VERCEL_GITHUB_COMMIT_SHA,
  dryRun: VERCEL_ENV !== "production",
};

module.exports = withSentryConfig(
  {
    serverRuntimeConfig: {
      API_TOKEN: API_TOKEN,
    },
    env: {
      API_URL: API_URL,
      conferenceCode: CONFERENCE_CODE || "pycon-demo",
    },
    images: {
      domains: ["production-pycon-backend-media.s3.amazonaws.com"],
    },
    webpack: (config) => {
      config.resolve.alias["~"] = path.resolve(__dirname) + "/src";
      return config;
    },
    eslint: {
      ignoreDuringBuilds: true,
    },
  },
  SentryWebpackPluginOptions,
);
