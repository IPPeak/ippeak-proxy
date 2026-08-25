const axios = require("axios");
const { HttpsProxyAgent } = require("https-proxy-agent");

const PROXY_HOST = "YOUR_PROXY_HOST";
const PROXY_PORT = "YOUR_PROXY_PORT";
const PROXY_USERNAME = "YOUR_PROXY_USERNAME";
const PROXY_PASSWORD = "YOUR_PROXY_PASSWORD";

const proxyURL =
  `http://${encodeURIComponent(PROXY_USERNAME)}:` +
  `${encodeURIComponent(PROXY_PASSWORD)}@` +
  `${PROXY_HOST}:${PROXY_PORT}`;

const agent = new HttpsProxyAgent(proxyURL);

async function main() {
  try {
    const response = await axios.get(
      "https://httpbin.org/ip",
      {
        httpsAgent: agent,
        proxy: false,
        timeout: 30000,
      }
    );

    console.log("Proxy IP:");
    console.log(response.data);
  } catch (error) {
    console.error("Proxy request failed:");

    if (error.response) {
      console.error(
        `HTTP ${error.response.status}: ${error.response.statusText}`
      );
    } else {
      console.error(error.message);
    }
  }
}

main();
