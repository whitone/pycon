/** @jsxRuntime classic */

/** @jsx jsx */
import { useState, useEffect } from 'react'
import { Box, Grid, Heading, jsx, Text, Flex } from "theme-ui";
import { useRouter } from 'next/router'
import { Logo } from "~/components/logo";

const Separator = (props) => (
  <svg
    width="55"
    height="425"
    viewBox="0 0 55 425"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M30.8568 -114.243C30.4602 -114.707 29.9537 -115.245 29.7931 -115.416C29.7664 -115.444 29.7493 -115.462 29.7438 -115.468L18.8658 -105.56C19.2171 -105.174 19.3656 -105.02 19.4529 -104.929C19.5313 -104.848 19.5605 -104.817 19.6428 -104.717L19.7672 -104.566L19.8994 -104.422C31.1115 -92.179 37.6933 -73.752 38.3051 -55.0022C38.9175 -36.2312 33.5239 -18.359 22.3588 -6.78573C7.61795 8.53066 0.644653 30.9613 0.644653 52.7514C0.644653 74.5411 7.61169 96.9592 22.3559 112.26C33.816 124.169 39.9491 142.565 39.9491 161.587C39.9491 180.61 33.8147 198.996 22.3559 210.887C7.61508 226.204 0.644653 248.631 0.644653 270.422C0.644653 292.211 7.61169 314.629 22.3559 329.93C33.77 341.776 39.9033 360.058 39.9578 378.992C40.0123 397.926 33.9839 416.267 22.6674 428.214L22.4006 428.495L22.3835 428.518C22.3736 428.528 22.3638 428.539 22.3538 428.549C22.2091 428.705 21.9977 428.942 21.7685 429.248L31.3375 436.422L33.345 438.323C33.2525 438.434 33.175 438.52 33.1228 438.576C33.0791 438.623 33.0459 438.657 33.0318 438.671C33.0125 438.69 33.0204 438.683 33.0318 438.671C33.0459 438.657 33.0791 438.623 33.1228 438.576C33.1669 438.531 33.2289 438.471 33.2998 438.395C33.3587 438.332 33.4273 438.257 33.5029 438.17C47.9397 422.826 54.7358 400.568 54.6737 378.95C54.6113 357.257 47.6389 334.964 32.9541 319.723C21.4954 307.832 15.3606 289.445 15.3606 270.422C15.3606 251.4 21.4937 233.005 32.9538 221.095C47.698 205.794 54.665 183.376 54.665 161.587C54.665 139.796 47.6978 117.372 32.957 102.056C21.4983 90.1647 15.3606 71.7749 15.3606 52.7514C15.3606 33.7292 21.4943 15.3326 32.9554 3.42288C47.6438 -11.8057 53.7142 -33.9958 53.0132 -55.4818C52.3131 -76.9384 44.8374 -98.9098 30.8568 -114.243Z"
      fill="black"
    />
  </svg>
);

const RightBackground = ({ textColor, ...props }) => (
  <svg
    width="74"
    height="425"
    viewBox="0 0 74 425"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      d="M91 12.808V433.177C91 433.246 90.9303 433.28 90.8607 433.28H20.9755C46.9779 405.985 46.8647 351.922 20.6185 324.835C-5.73206 297.643 -5.73206 243.226 20.6185 216C46.9691 188.808 46.9691 134.391 20.6185 107.165C-5.73206 79.9732 -5.73206 25.5557 20.6185 -1.67042C46.6209 -28.4724 43.6786 -81.7995 18.2768 -109.38C61.5329 -85.8497 91 -39.4286 91 12.808Z"
      fill={textColor}
    />
  </svg>
);

const Badge = () => {
  const router = useRouter()

  const [name, setName] = useState("unset")
  const [tagline, setTagline] = useState("unset")
  const [variant, setVariant] = useState("participant")

  useEffect(() => {
    // @ts-ignore
    window.changeBadgeData = ({name, tagline, variant}) => {
      setName(name)
      setTagline(tagline)
      setVariant(variant)
    }
  }, []);

  // const name = router.query.name;
  // const tagline = router.query.tagline;
  // const variant = router.query.variant;

  const isSpeaker = variant === 'speaker';
  const isParticipant = variant === 'participant';
  const isKeynoter = variant === 'keynoter';
  const isStaff = variant === 'staff';

  let textColor = '#F17A5D'

  if (isSpeaker) {
    textColor = '#F17A5D'
  } else if (isKeynoter) {
    textColor = '#9373B0'
  } else if (isParticipant) {
    textColor = '#36B39F'
  } else if (isStaff) {
    textColor = '#DC9BC4'
  }

  console.log("router", router.query)

  return (
    <Box
      sx={{
        // width: '550px',
        // height: '850px',
        // width: "275px",
        // height: "425px",
        width: "10cm",
        height: "10cm",
        backgroundColor: "#FCE8DE",
        position: "relative",
        overflow: "hidden",
      }}
    >
      <Box
        sx={{
          mt: "17px",

          ml: "13px",
          mr: "70px",
        }}
      >
        <Logo
          sx={{
            width: "100px",
          }}
        />

        <Text
          sx={{
            fontSize: "36px",
            fontWeight: "800",
            lineHeight: "38px",
            mt: "40px",
            mb: "8px",
          }}
        >
          {name}
        </Text>

        <Text>
          {tagline}
        </Text>
      </Box>

      <Text
        sx={{
          position: "absolute",
          left: "13px",
          bottom: "11px",
          fontSize: "20px",
          lineHeight: "26px",
          fontWeight: "800",
          color: textColor,
        }}
      >
        {isSpeaker && `Speaker`}
        {isParticipant && `Participant`}
        {isKeynoter && `Keynoter`}
        {isStaff && `Staff`}
      </Text>

      <RightBackground
        textColor={textColor}
        sx={{
          position: "absolute",
          top: 0,
          right: 0,
          overflow: "hidden",
        }}
      />

      <Separator
        sx={{
          position: "absolute",
          top: 0,
          right: 20,
          overflow: "hidden",
        }}
      />
    </Box>
  );
};

export default Badge;
