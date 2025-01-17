import {
  Heading,
  Text,
  Section,
  VerticalStack,
  Spacer,
  SocialLinks,
} from "@python-italia/pycon-styleguide";

import { Hills } from "./hills";

type Props = {
  label: string;
  hashtag: string;
};
export const SocialsSection = ({ hashtag, label }: Props) => {
  return (
    <div className="bg-[#151C28] -mb-[3px]">
      <Section spacingSize="3xl">
        <VerticalStack alignItems="center">
          <Text weight="strong" uppercase color="milk" size="label2">
            {label}
          </Text>
          <Spacer size="medium" />

          <SocialLinks
            color="cream"
            hoverColor="green"
            socials={[
              {
                icon: "twitter",
                link: "https://twitter.com/pyconit",
                rel: "me",
              },
              {
                icon: "facebook",
                link: "https://www.facebook.com/pythonitalia",
                rel: "me",
              },
              {
                icon: "instagram",
                link: "https://www.instagram.com/python.it",
                rel: "me",
              },
              {
                icon: "linkedin",
                link: "https://www.linkedin.com/company/pycon-italia",
                rel: "me",
              },
              {
                icon: "mastodon",
                link: "https://social.python.it/@pycon",
                rel: "me",
              },
            ]}
          />
          <Spacer size="xl" />

          <Heading align="center" color="white" size="display1" fluid>
            #{hashtag}
          </Heading>
        </VerticalStack>
      </Section>
      <Hills />
    </div>
  );
};
