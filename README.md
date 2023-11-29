# Try It with GitPod

💻 [Quickly run this example in your browser](https://gitpod.io/#https://github.com/ed-marquez/hedera-tps-calculator-js)

# Hedera Transactions Per Second (TPS) Calculation

This JavaScript script (also provided in Python - [see repo](https://github.com/ed-marquez/hedera-tps-calculator-python/tree/main)) calculates the Transactions Per Second (TPS) for Hedera by analyzing data from the last few blocks.

## 1. Fetch Block Data

Every block on Hedera takes approximately 2 seconds. In the script, we're focusing on the last 5 blocks:
Data for the last 5 blocks is retrieved using Hedera's mirror node REST API:

```js
const axios = require("axios");

async function getTransactionsPerSecond() {

    const numBlocks = 5;
    const blocksUrl = `https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?limit=${numBlocks}`;
    const response = await axios.get(blocksUrl);
```

## 2. Add Up Transactions

For these 5 blocks, the total number of transactions is calculated by summing up the transaction counts of each block:

```js
const blocks = response.data["blocks"];
const sumOfTransactions = blocks.reduce((acc, block) => acc + block["count"], 0);
```

## 3. Calculate Duration

We determine the total duration of these 5 blocks by calculating the difference between the timestamps of the newest and the oldest block:

```js
const newestBlockToTimestamp = parseFloat(blocks[0]["timestamp"]["to"]);
const oldestBlockFromTimestamp = parseFloat(blocks[blocks.length - 1]["timestamp"]["from"]);
const duration = newestBlockToTimestamp - oldestBlockFromTimestamp;
```

## 4. Calculate TPS 🎉🎉

The TPS is simply the **total number of transactions** in the last 5 blocks (approximately 10 seconds) divided by the **actual duration of those blocks**.

```js
    const transactionsPerSecond = sumOfTransactions / duration;
    return transactionsPerSecond;
}
```

# See the Results!

Simply run the script:

```js
(async () => {
	const TPS = await getTransactionsPerSecond();
	console.log(`Hedera TPS: ${TPS}`);
})();
```

<img width="435" alt="image" src="https://github.com/ed-marquez/hedera-tps-calculator/assets/72571340/615e51d7-8ec5-48d7-8ee7-38828b9453ff">
