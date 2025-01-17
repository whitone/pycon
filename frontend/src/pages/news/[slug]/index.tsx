import {
  Container,
  StyledHTMLText,
  Heading,
  Page,
  Section,
  Spacer,
  Text,
} from "@python-italia/pycon-styleguide";
import { parseISO } from "date-fns";
import { FormattedMessage } from "react-intl";

import { GetStaticPaths, GetStaticProps } from "next";
import { useRouter } from "next/router";

import { addApolloState, getApolloClient } from "~/apollo/client";
import { Article } from "~/components/article";
import { MetaTags } from "~/components/meta-tags";
import { compile } from "~/helpers/markdown";
import { prefetchSharedQueries } from "~/helpers/prefetch";
import { useCurrentLanguage } from "~/locale/context";
import {
  queryAllNewsArticles,
  queryNewsArticle,
  useNewsArticleQuery,
} from "~/types";

export const NewsArticlePage = () => {
  const language = useCurrentLanguage();
  const router = useRouter();
  const slug = router.query.slug as string;
  const dateFormatter = new Intl.DateTimeFormat(language, {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });

  const { data } = useNewsArticleQuery({
    variables: {
      language,
      slug,
      code: process.env.conferenceCode,
    },
  });

  const newsArticle = data.newsArticle;
  const blogPost = data.blogPost;
  const post = newsArticle || {
    ...blogPost,
    publishedAt: blogPost.published,
    authorFullname: blogPost.author.fullName,
    body: blogPost.content,
  };

  return (
    <Page endSeparator={false}>
      <MetaTags
        title={post.title}
        description={post.excerpt || post.title}
        useDefaultSocialCard={false}
        useNewSocialCard={true}
      />

      <Section illustration="snakeHead">
        <Text size={2}>
          <FormattedMessage
            id="blog.publishedOn"
            values={{
              date: dateFormatter.format(parseISO(post.publishedAt)),
              author: post.authorFullname,
            }}
          />
        </Text>
        <Spacer size="medium" />
        <Heading size={1}>{post.title}</Heading>
      </Section>

      <Section illustration="snakeTail">
        <Container noPadding center={false} size="medium">
          {newsArticle && <StyledHTMLText text={post.body} baseTextSize={2} />}
          {blogPost && <Article>{compile(blogPost.content).tree}</Article>}
        </Container>
      </Section>
    </Page>
  );
};

export const getStaticProps: GetStaticProps = async ({ params, locale }) => {
  const slug = params.slug as string;
  const client = getApolloClient();

  const [_, newsArticle] = await Promise.all([
    prefetchSharedQueries(client, locale),
    queryNewsArticle(client, {
      slug,
      code: process.env.conferenceCode,
      language: locale,
    }),
  ]);

  if (
    !newsArticle.data ||
    (!newsArticle.data.newsArticle && !newsArticle.data.blogPost)
  ) {
    return {
      notFound: true,
    };
  }

  return addApolloState(client, {
    props: {},
  });
};

export const getStaticPaths: GetStaticPaths = async () => {
  const client = getApolloClient();

  const [
    {
      data: { newsArticles: italianNewsArticles },
    },
    {
      data: { newsArticles: englishNewsArticles },
    },
  ] = await Promise.all([
    queryAllNewsArticles(client, {
      language: "it",
      code: process.env.conferenceCode,
    }),
    queryAllNewsArticles(client, {
      language: "en",
      code: process.env.conferenceCode,
    }),
  ]);

  const paths = [
    ...italianNewsArticles.map((blogPost) => ({
      params: {
        slug: blogPost.slug,
      },
      locale: "it",
    })),
    ...englishNewsArticles.map((blogPost) => ({
      params: {
        slug: blogPost.slug,
      },
      locale: "en",
    })),
  ];

  return {
    paths,
    fallback: "blocking",
  };
};

export default NewsArticlePage;
