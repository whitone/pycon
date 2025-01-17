import {
  Heading,
  StyledHTMLText,
  Spacer,
  Section,
  Container,
  MultiplePartsCard,
  CardPart,
  Button,
} from "@python-italia/pycon-styleguide";

import { BodyTextSize, TextSection as TextSectionType } from "~/types";

export const TextSection = ({
  title,
  isMainTitle,
  subtitle,
  body,
  bodyTextSize,
  illustration,
  accordions,
  cta,
}: TextSectionType) => {
  const onlyAccordions = !title && !subtitle && !body && !cta;
  return (
    <Section
      spacingSize={isMainTitle ? "2xl" : "xl"}
      illustration={(illustration as any) || undefined}
    >
      <Container noPadding center={false} size="medium">
        {title && (
          <>
            <Heading size={isMainTitle ? "display1" : "display2"}>
              {title}
            </Heading>
            {(subtitle || body || cta) && <Spacer size="xl" />}
          </>
        )}

        {subtitle && (
          <>
            <Heading size={2}>{subtitle}</Heading>
            {(body || cta) && <Spacer size="medium" />}
          </>
        )}
        {body && (
          <>
            <StyledHTMLText
              text={body}
              baseTextSize={bodyTextSize === BodyTextSize.Text_1 ? 1 : 2}
            />
            {cta && <Spacer size="large" />}
          </>
        )}
        {cta && (
          <>
            <Button href={cta.link} role="secondary" fullWidth="mobile">
              {cta.label}
            </Button>
          </>
        )}
      </Container>
      <Container noPadding size="2md">
        {accordions.length > 0 && (
          <>
            {!onlyAccordions && <Spacer size="xl" />}
            {accordions?.map((accordion, index) => (
              <>
                <MultiplePartsCard
                  key={index}
                  clickablePart="heading"
                  expandTarget="content"
                  openByDefault={accordion.isOpen}
                >
                  <CardPart contentAlign="left" id="heading">
                    <Heading size={3}>{accordion.title}</Heading>
                  </CardPart>
                  <CardPart id="content" contentAlign="left" background="milk">
                    <StyledHTMLText text={accordion.body} baseTextSize={2} />
                  </CardPart>
                </MultiplePartsCard>
                {/* todo replace with MultiplePartsCardCollection */}
                {index !== accordions.length - 1 && <Spacer size="small" />}
              </>
            ))}
          </>
        )}
      </Container>
    </Section>
  );
};
