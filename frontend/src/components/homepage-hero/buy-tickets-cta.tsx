/** @jsxRuntime classic */

/** @jsx jsx */
import React from "react";
import { jsx, ThemeUIStyleObject, useThemeUI } from "theme-ui";

export const BuyTicketsCTA = (props: { sx?: ThemeUIStyleObject }) => {
  const { theme } = useThemeUI();

  return (
    <svg
      viewBox="0 0 151 151"
      width={151}
      height={151}
      fill="none"
      {...props}
      sx={
        {
          "--fill": "white",
          "&:hover": {
            "--fill": theme.colors?.yellow,
          },
        } as any
      }
    >
      <path
        d="M75.4996 148.271C115.69 148.271 148.271 115.69 148.271 75.5C148.271 35.3096 115.69 2.72891 75.4996 2.72891C35.3092 2.72891 2.72852 35.3096 2.72852 75.5C2.72852 115.69 35.3092 148.271 75.4996 148.271Z"
        fill="white"
        stroke="#1D1D1B"
        strokeWidth="4"
        strokeMiterlimit="10"
      />
      <path
        d="M75.4998 111.886C95.595 111.886 111.885 95.5952 111.885 75.5C111.885 55.4048 95.595 39.1145 75.4998 39.1145C55.4046 39.1145 39.1143 55.4048 39.1143 75.5C39.1143 95.5952 55.4046 111.886 75.4998 111.886Z"
        fill="#F17A5D"
        stroke="#1D1D1B"
        strokeWidth="4"
        strokeMiterlimit="10"
      />
      <path
        d="M55.984 88V84.497C57.1 83.7117 58.0817 83.0193 58.929 82.42C59.797 81.8207 60.572 81.273 61.254 80.777C61.9567 80.281 62.618 79.8057 63.238 79.351C64.7673 78.235 65.9143 77.3257 66.679 76.623C67.4437 75.8997 67.9707 75.2693 68.26 74.732C68.57 74.174 68.725 73.5747 68.725 72.934C68.725 71.9007 68.384 71.1153 67.702 70.578C67.0407 70.0407 66.059 69.772 64.757 69.772C63.4963 69.772 62.5147 70.0303 61.812 70.547C61.1093 71.0637 60.5927 71.911 60.262 73.089L55.767 72.593C56.1803 70.423 57.162 68.78 58.712 67.664C60.2827 66.548 62.37 65.99 64.974 65.99C67.6813 65.99 69.7893 66.5687 71.298 67.726C72.8067 68.8833 73.561 70.485 73.561 72.531C73.561 73.585 73.3647 74.5357 72.972 75.383C72.6 76.2097 71.9903 77.0467 71.143 77.894C70.2957 78.7207 69.1383 79.6507 67.671 80.684C66.1623 81.7587 64.4677 82.916 62.587 84.156H73.995L73.406 88H55.984ZM77.6901 88V84.497C78.8061 83.7117 79.7877 83.0193 80.6351 82.42C81.5031 81.8207 82.2781 81.273 82.9601 80.777C83.6627 80.281 84.3241 79.8057 84.9441 79.351C86.4734 78.235 87.6204 77.3257 88.3851 76.623C89.1497 75.8997 89.6767 75.2693 89.9661 74.732C90.2761 74.174 90.4311 73.5747 90.4311 72.934C90.4311 71.9007 90.0901 71.1153 89.4081 70.578C88.7467 70.0407 87.7651 69.772 86.4631 69.772C85.2024 69.772 84.2207 70.0303 83.5181 70.547C82.8154 71.0637 82.2987 71.911 81.9681 73.089L77.4731 72.593C77.8864 70.423 78.8681 68.78 80.4181 67.664C81.9887 66.548 84.0761 65.99 86.6801 65.99C89.3874 65.99 91.4954 66.5687 93.0041 67.726C94.5127 68.8833 95.2671 70.485 95.2671 72.531C95.2671 73.585 95.0707 74.5357 94.6781 75.383C94.3061 76.2097 93.6964 77.0467 92.8491 77.894C92.0017 78.7207 90.8444 79.6507 89.3771 80.684C87.8684 81.7587 86.1737 82.916 84.2931 84.156H95.7011L95.1121 88H77.6901Z"
        fill="#1D1D1B"
      />
      <path
        d="M76.7734 25.1606L78.5927 12.1892L84.9056 13.0624C88.4532 13.5536 90.0724 14.9181 89.7631 17.1558C89.5812 18.502 88.7443 19.3207 87.2707 19.63C88.9262 20.4487 89.6539 21.5948 89.4356 23.0866C89.2537 24.3237 88.6533 25.197 87.6345 25.7064C86.6157 26.2158 85.1967 26.3431 83.3774 26.0884L76.7734 25.1606ZM83.4684 23.8689C84.469 24.0145 85.2331 23.9781 85.7243 23.7598C86.2155 23.5414 86.5066 23.1412 86.5975 22.5408C86.6885 21.9405 86.5066 21.4493 86.0881 21.1036C85.6697 20.7398 84.9602 20.5033 83.9778 20.3577L80.3028 19.8483L79.8116 23.3595L83.4684 23.8689ZM84.1961 18.2473C85.0512 18.3747 85.7061 18.3201 86.1427 18.1382C86.5793 17.9381 86.834 17.5742 86.9068 17.0466C86.9796 16.5372 86.8159 16.137 86.452 15.8641C86.07 15.573 85.415 15.3729 84.4872 15.2455L81.0487 14.7725L80.6303 17.7743L84.1961 18.2473Z"
        fill="black"
      />
      <path
        d="M104.79 19.4663L107.465 20.6852L104.317 27.5984C103.499 29.3813 102.425 30.4911 101.061 30.9277C99.6963 31.3643 98.0226 31.146 96.0578 30.2364C94.093 29.3449 92.8195 28.2352 92.2555 26.9071C91.6915 25.5972 91.8189 24.0327 92.6193 22.268L95.7667 15.3547L98.441 16.5736L95.2209 23.6324C94.7479 24.6512 94.6751 25.5245 94.9662 26.234C95.2573 26.9435 95.9486 27.5439 97.0402 28.0533C98.1318 28.5445 99.0414 28.6718 99.7691 28.4353C100.497 28.1988 101.097 27.5621 101.57 26.5251L104.79 19.4663Z"
        fill="black"
      />
      <path
        d="M107.01 36.622L110.43 32.656L111.358 23.0866L113.85 25.2334L113.104 31.8555L119.581 30.1636L121.982 32.2376L112.65 34.5663L109.229 38.5323L107.01 36.622Z"
        fill="black"
      />
      <path
        d="M120.873 54.3236L130.661 50.1029L128.623 45.3909L130.861 44.4267L136.1 56.5613L133.863 57.5255L131.825 52.8136L122.037 57.0343L120.873 54.3236Z"
        fill="black"
      />
      <path
        d="M124.002 63.0743L136.773 60.1999L137.41 63.0562L124.639 65.9306L124.002 63.0743Z"
        fill="black"
      />
      <path
        d="M130.187 81.6674C128.622 81.4854 127.422 80.8123 126.548 79.6298C125.675 78.4472 125.239 76.8826 125.202 74.936C125.184 73.4624 125.42 72.1707 125.948 71.061C126.476 69.9512 127.24 69.0961 128.259 68.4776C129.277 67.859 130.514 67.5316 131.952 67.5134C133.316 67.4952 134.517 67.7499 135.554 68.3139C136.591 68.8778 137.428 69.6965 138.028 70.7881C138.628 71.8796 138.938 73.1713 138.974 74.6631C139.047 78.3017 137.591 80.5212 134.608 81.3581L134.208 78.4472C135.063 78.1198 135.681 77.6649 136.063 77.0828C136.427 76.5006 136.609 75.7001 136.591 74.6995C136.573 73.3896 136.154 72.3708 135.336 71.6249C134.535 70.879 133.425 70.5152 132.024 70.5516C130.624 70.5698 129.532 70.97 128.75 71.7523C127.967 72.5346 127.604 73.5898 127.622 74.936C127.64 76.0276 127.858 76.8826 128.277 77.5012C128.695 78.1198 129.314 78.52 130.151 78.7201L130.187 81.6674Z"
        fill="black"
      />
      <path
        d="M122.565 93.0014L130.242 90.0906L129.005 87.3617L124.512 86.0882L125.312 83.2683L137.92 86.8341L137.119 89.654L131.898 88.1804L135.373 95.8759L134.408 99.2961L131.352 92.5648L121.655 96.2761L122.565 93.0014Z"
        fill="black"
      />
      <path
        d="M120.945 97.1312L132.115 103.99L126.384 113.341L124.329 112.086L128.531 105.245L126.184 103.808L122.182 110.321L120.126 109.066L124.129 102.553L121.454 100.915L117.033 108.101L115.178 106.537L120.945 97.1312Z"
        fill="black"
      />
      <path
        d="M111.157 110.63L118.525 118.326L122.237 114.778L123.929 116.543L114.396 125.676L112.704 123.911L116.415 120.363L109.047 112.668L111.157 110.63Z"
        fill="black"
      />
      <path
        d="M101.116 129.26C101.643 129.678 102.189 129.896 102.771 129.896C103.353 129.896 104.045 129.678 104.845 129.223C105.755 128.732 106.392 128.223 106.755 127.75C107.119 127.277 107.174 126.804 106.937 126.367C106.719 125.967 106.41 125.73 106.009 125.712C105.609 125.694 104.991 125.821 104.136 126.13L101.57 127.058C100.042 127.604 98.8052 127.768 97.8409 127.568C96.8767 127.368 96.1308 126.767 95.585 125.785C94.9847 124.675 94.9847 123.547 95.585 122.401C96.2036 121.273 97.3861 120.218 99.1508 119.254C100.424 118.562 101.57 118.126 102.571 117.962C103.572 117.798 104.463 117.907 105.245 118.271C106.028 118.635 106.719 119.272 107.319 120.163L104.736 121.582C104.227 120.891 103.608 120.509 102.88 120.454C102.171 120.4 101.279 120.654 100.224 121.218C99.2782 121.728 98.6414 122.255 98.2958 122.765C97.9501 123.274 97.9137 123.784 98.1866 124.275C98.4049 124.675 98.7324 124.893 99.169 124.948C99.6056 125.003 100.206 124.893 100.934 124.602L103.008 123.82C104.7 123.183 106.046 122.947 107.083 123.11C108.12 123.274 108.902 123.875 109.466 124.893C109.848 125.585 109.957 126.294 109.794 127.04C109.648 127.786 109.23 128.514 108.556 129.241C107.883 129.969 106.974 130.642 105.846 131.261C104.281 132.116 102.917 132.516 101.789 132.462C100.643 132.407 99.642 131.898 98.7506 130.933L101.116 129.26Z"
        fill="black"
      />
      <path
        d="M90.0176 129.314L90.4179 131.716L79.3749 133.517L78.9746 131.115L90.0176 129.314Z"
        fill="black"
      />
      <path
        d="M77.2459 125.821L76.2089 138.884L69.8597 138.374C66.2939 138.083 64.5838 136.828 64.7657 134.59C64.8748 133.244 65.6571 132.371 67.1126 131.97C65.4206 131.261 64.6201 130.151 64.7475 128.659C64.8385 127.422 65.3842 126.513 66.3848 125.93C67.3855 125.366 68.7863 125.148 70.6056 125.294L77.2459 125.821ZM70.642 127.513C69.6232 127.44 68.8773 127.513 68.4042 127.75C67.913 127.986 67.6583 128.405 67.6038 129.023C67.5492 129.623 67.7493 130.097 68.1859 130.424C68.6226 130.751 69.3503 130.952 70.3509 131.043L74.044 131.334L74.3169 127.804L70.642 127.513ZM70.2599 133.171C69.3867 133.098 68.7499 133.171 68.3315 133.408C67.913 133.626 67.6765 134.008 67.6401 134.554C67.6038 135.063 67.7857 135.445 68.1677 135.718C68.568 135.973 69.2411 136.137 70.1689 136.209L73.6256 136.482L73.8621 133.462L70.2599 133.171Z"
        fill="black"
      />
      <path
        d="M49.5928 133.189L46.8457 132.134L49.5746 125.039C50.2841 123.22 51.3029 122.037 52.631 121.51C53.9591 120.982 55.651 121.109 57.6704 121.892C59.6898 122.674 61.0179 123.693 61.6546 124.984C62.2914 126.258 62.255 127.822 61.5637 129.642L58.8347 136.737L56.0876 135.682L58.8711 128.441C59.2714 127.386 59.3077 126.513 58.9803 125.821C58.6528 125.13 57.9251 124.566 56.7971 124.129C55.6874 123.693 54.7596 123.62 54.05 123.911C53.3405 124.202 52.7765 124.875 52.3763 125.912L49.5928 133.189Z"
        fill="black"
      />
      <path
        d="M46.373 116.215L43.2074 120.382L42.8436 130.006L40.2238 128.023L40.5695 121.364L34.2202 123.438L31.6914 121.51L40.8606 118.617L44.0261 114.451L46.373 116.215Z"
        fill="black"
      />
      <path
        d="M31.4732 99.3143L21.9584 104.117L24.2689 108.702L22.0858 109.793L16.1367 98.0045L18.3199 96.9129L20.6303 101.497L30.1452 96.6946L31.4732 99.3143Z"
        fill="black"
      />
      <path
        d="M27.8163 90.7637L15.2269 94.3841L14.4082 91.5642L26.9976 87.9438L27.8163 90.7637Z"
        fill="black"
      />
      <path
        d="M20.5576 72.5346C22.1222 72.6255 23.3775 73.2259 24.3053 74.3539C25.2332 75.4818 25.7789 77.01 25.9245 78.9748C26.0336 80.4302 25.8699 81.7401 25.4151 82.8863C24.9603 84.0324 24.2326 84.9239 23.2502 85.6152C22.2677 86.2883 21.0488 86.6886 19.6298 86.7977C18.2835 86.9069 17.0646 86.7068 15.9912 86.1974C14.9179 85.688 14.0446 84.9239 13.3897 83.8687C12.7347 82.8135 12.3163 81.5218 12.2071 80.0482C11.9342 76.4096 13.2441 74.0992 16.1732 73.0986L16.7371 75.973C15.9003 76.3369 15.2999 76.8281 14.9724 77.4466C14.645 78.047 14.5176 78.8657 14.5904 79.8663C14.6814 81.1761 15.1726 82.1767 16.0094 82.8681C16.8645 83.5594 17.9742 83.8505 19.3751 83.7595C20.7759 83.6504 21.8493 83.1955 22.577 82.3769C23.3047 81.5582 23.614 80.4848 23.523 79.1386C23.4321 78.047 23.1774 77.2101 22.7226 76.628C22.2677 76.0276 21.631 75.6637 20.7759 75.5182L20.5576 72.5346Z"
        fill="black"
      />
      <path
        d="M27.489 60.8366L19.9936 64.2023L21.3944 66.8584L25.9608 67.859L25.3423 70.7335L12.5527 67.9318L13.1713 65.0573L18.4836 66.2217L14.5539 58.7626L15.318 55.2878L18.7747 61.819L28.2349 57.5437L27.489 60.8366Z"
        fill="black"
      />
      <path
        d="M28.8532 56.6159L17.3008 50.4486L22.4675 40.77L24.5961 41.898L20.812 48.9749L23.2316 50.2666L26.8338 43.5171L28.9623 44.6451L25.3602 51.3946L28.1255 52.8682L32.1097 45.4274L34.0563 46.8828L28.8532 56.6159Z"
        fill="black"
      />
      <path
        d="M37.8228 42.5529L30.0181 35.294L26.5251 39.0599L24.7422 37.4043L33.7294 27.7258L35.5123 29.3813L32.0193 33.1472L39.824 40.4061L37.8228 42.5529Z"
        fill="black"
      />
      <path
        d="M46.7371 23.3777C46.1913 22.9957 45.6274 22.8137 45.0452 22.8501C44.463 22.8865 43.7899 23.1594 43.0076 23.6324C42.1344 24.1782 41.5158 24.7058 41.1883 25.2334C40.8609 25.761 40.8245 26.1976 41.0792 26.616C41.3339 27.0163 41.6432 27.2164 42.0434 27.2164C42.4436 27.2164 43.0622 27.0527 43.8809 26.6888L46.3915 25.6154C47.8833 24.9787 49.1204 24.7422 50.0846 24.8877C51.0488 25.0333 51.8493 25.579 52.4315 26.5433C53.1046 27.6166 53.1774 28.7446 52.6316 29.9089C52.0858 31.0733 50.9579 32.2012 49.2659 33.2564C48.0288 34.0205 46.9191 34.5299 45.9185 34.7482C44.9179 34.9665 44.0264 34.9119 43.2259 34.6027C42.4254 34.2934 41.6977 33.693 41.0428 32.838L43.5534 31.2734C44.1174 31.9283 44.7541 32.274 45.4636 32.2922C46.1913 32.3104 47.0464 32.0011 48.0652 31.3643C48.9748 30.8004 49.5934 30.2364 49.9027 29.7088C50.212 29.1812 50.212 28.6718 49.9209 28.1988C49.6844 27.8167 49.3387 27.6166 48.9021 27.5802C48.4654 27.562 47.8833 27.7076 47.1556 28.0169L45.118 28.9265C43.4806 29.6724 42.1344 29.9817 41.0974 29.8725C40.0604 29.7634 39.2235 29.2176 38.605 28.2352C38.1865 27.562 38.041 26.8707 38.1501 26.1248C38.2593 25.3789 38.6232 24.6148 39.2599 23.8689C39.8967 23.123 40.7517 22.3771 41.8433 21.704C43.3533 20.758 44.6813 20.2667 45.8275 20.2486C46.9736 20.2304 48.0106 20.6852 48.9385 21.5948L46.7371 23.3777Z"
        fill="black"
      />
      <path
        d="M57.8167 22.6318L57.2891 20.2486L68.2047 17.7925L68.7323 20.1758L57.8167 22.6318Z"
        fill="black"
      />
    </svg>
  );
};
