import { Theme } from "theme-ui";

export const theme: Theme = {
  initialColorModeName: "light",
  useColorSchemeMediaQuery: true,
  space: [0, 4, 8, 16, 32, 64, 128, 256, 512],
  fonts: {
    body: "aktiv-grotesk-extended, sans-serif",
    heading: "inherit",
    monospace: "Menlo, monospace",
  },
  fontSizes: [12, 14, 16, 20, 24, 32, 48, 64, 96],
  fontWeights: {
    body: 400,
    heading: 500,
    medium: 500,
    bold: 700,
  },
  lineHeights: {
    body: 1.5,
    heading: 1.125,
  },
  sizes: {
    largeContainer: 1320,
    container: 1200,
  },
  colors: {
    text: "#000",
    background: "#fff",
    primary: "#07c",
    secondary: "#30c",
    muted: "#f6f6f6",
    green: "#219653",
    purple: "#FA00FF",
    yellow: "#F8B03D",
    orange: "#F17A5D",
    red: "#DB0000",
    violet: "#9473B0",
    lightViolet: "#dbcfe4",
    blue: "#79CDE0",
    lightBlue: "#DEF3F7",
    cinderella: "#FCE8DE",
    keppel: "#34B4A1",
  },
  borders: {
    primary: "4px solid #000000",
    socialCard: "14px solid #000000",
  },
  forms: {
    input: {
      fontFamily: "body",
      bg: "blue",
      color: "text",
      border: "primary",
      borderRadius: 0,
    },
    textarea: {
      fontFamily: "body",
      bg: "blue",
      border: "primary",
      borderRadius: 0,
    },
    select: {
      fontFamily: "body",
      bg: "blue",
      border: "primary",
      borderRadius: 0,
      option: {
        fontSize: 3,
        padding: 3,
        backgroundColor: "white",
      },
    },
  },
  buttons: {
    primary: {
      position: "relative",
      padding: 3,
      fontSize: 2,
      fontFamily: "body",
      fontWeight: "heading",

      color: "#000",
      border: "primary",
      backgroundColor: "yellow",

      borderRadius: 0,

      "&:hover": {
        backgroundColor: "orange",
        cursor: "pointer",
      },
    },
    plus: {
      variant: "buttons.primary",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      textAlign: "center",
      width: 50,
      height: 50,
      p: [0, 0],
    },
    minus: {
      variant: "buttons.plus",
    },
    small: {
      position: "relative",
      padding: 2,

      fontSize: 0,
      fontFamily: "body",
      fontWeight: "heading",

      color: "#000",
      border: "primary",
      backgroundColor: "yellow",
      "&:hover": {
        backgroundColor: "orange",
      },
    },
    white: {
      variant: "buttons.primary",
      background: "#fff",

      "&:hover": {
        background: "#fff",
      },
    },
  },
  links: {
    heading: {
      color: "text",
      fontSize: 5,
    },
    header: {
      color: "white",
      fontSize: 4,
      textDecoration: "none",
      display: "block",
      "&:hover": {
        textDecoration: "underline",
        textDecorationSkip: "edges",
        textDecorationThickness: "2px",
        textUnderlineOffset: "0.2em",
      },
    },
    google: {
      border: "primary",
      display: "inline-flex",
      alignItems: "center",
      pr: 3,
      textDecoration: "none",
      color: "black",
      "&:hover": {
        backgroundColor: "muted",
      },
    },
    button: {
      position: "relative",
      px: 3,
      fontSize: 2,
      lineHeight: "43px",
      display: "inline-block",
      fontFamily: "body",
      fontWeight: "heading",
      color: "#000",
      textDecoration: "none",
      textTransform: "uppercase",
      border: "primary",
      "&:hover": {
        backgroundColor: "orange",
      },
    },
    "arrow-button": {
      variant: "links.button",
      height: 50,
      borderColor: "transparent",
      "&:hover": {
        backgroundColor: "none",
      },
    },
    buttonFullWidth: {
      variant: "links.arrow-button",
      border: "primary",
      borderColor: "black",
      backgroundColor: "yellow",
      width: "100%",
      textAlign: "center",
      "&:hover": {
        backgroundColor: "orange",
      },
    },
  },
  badges: {
    tag: {
      color: "text",
      backgroundColor: "orange",
      border: "primary",
      fontSize: 2,
      p: 2,
      my: 3,
      mr: 3,
      userSelect: "none",
    },
    selectedTag: {
      variant: "badges.tag",
      position: "relative",
      backgroundColor: "blue",
      mr: 4,
      "&::after": {
        content: "'⨉'",
        position: "absolute",
        borderRadius: "100%",
        width: 20,
        height: 20,
        fontSize: 1,
        display: "flex",
        justifyContent: "center",
        lineHeight: "18px",
        top: -12,
        right: -12,
        p: 0,
        background: "orange",
        border: "primary",
      },
    },
    placeholderTag: {
      variant: "badges.tag",
      backgroundColor: "muted",
      cursor: "normal",
      opacity: 0.7,
    },
    remove: {
      my: 1,
      ml: -3,
      height: 20,
    },
  },
  text: {
    caps: {
      textTransform: "uppercase",
    },
    header: {
      variant: "text.caps",
      fontSize: 2,
      fontWeight: "bold",
      mb: 3,
    },
    prefooter: {
      fontWeight: "bold",
      color: "violet",
      display: "block",
    },
    heading: {
      fontSize: 5,
      fontFamily: "heading",
      fontWeight: "heading",
      lineHeight: "heading",
    },
    marquee: {
      variant: "text.caps",
      fontSize: 5,
      whiteSpace: "nowrap",
    },
    label: {
      textTransform: "uppercase",
      fontWeight: "bold",
      fontSize: 3,
      color: "orange",
      mb: 2,
    },
    labelDescription: {
      mb: 3,
      color: "text",
      fontWeight: "normal",
      fontSize: 2,
      textTransform: "none",
    },
  },
  styles: {
    root: {
      fontFamily: "body",
      lineHeight: "body",
      fontWeight: "body",
    },
    h1: {
      color: "text",
      fontFamily: "heading",
      lineHeight: "heading",
      fontWeight: "heading",
      mb: "1em",
      fontSize: 5,
    },
    h2: {
      color: "text",
      fontFamily: "heading",
      lineHeight: "heading",
      fontWeight: "heading",
      mb: "1em",
      fontSize: 4,
    },
    h3: {
      color: "text",
      fontFamily: "heading",
      lineHeight: "heading",
      fontWeight: "heading",
      mb: "1em",
      fontSize: 3,
    },
    h4: {
      color: "text",
      fontFamily: "heading",
      lineHeight: "heading",
      fontWeight: "heading",
      mb: "1em",
      fontSize: 2,
    },
    h5: {
      color: "text",
      fontFamily: "heading",
      lineHeight: "heading",
      fontWeight: "heading",
      mb: "1em",
      fontSize: 1,
    },
    h6: {
      color: "text",
      fontFamily: "heading",
      lineHeight: "heading",
      fontWeight: "heading",
      mb: "1em",
      fontSize: 0,
    },
    p: {
      color: "text",
      fontFamily: "body",
      fontWeight: "body",
      lineHeight: "body",
      mb: "1em",
    },
    a: {
      color: "primary",
    },
    pre: {
      fontFamily: "monospace",
      overflowX: "auto",
      code: {
        color: "inherit",
      },
    },
    code: {
      fontFamily: "monospace",
      fontSize: "inherit",
    },
    table: {
      width: "100%",
      borderCollapse: "separate",
      borderSpacing: 0,
    },
    th: {
      textAlign: "left",
      borderBottomStyle: "solid",
    },
    td: {
      textAlign: "left",
      borderBottomStyle: "solid",
    },
    img: {
      maxWidth: "100%",
    },
  },
  zIndices: {
    header: 11,
    scheduleItemPanel: 19,
    scheduleLoading: 20,
    scheduleHeader: 10,
    scheduleDraggable: 9,
    footer: 0,
  },
};
