# Hedera Transactions Per Second (TPS) Calculation
This Python script (also provided in JavaScript) calculates the Transactions Per Second (TPS) for Hedera by analyzing data from the last few blocks.

## 1. Fetch Block Data
Every block on Hedera takes approximately 2 seconds. In our script, we're focusing on the last 5 blocks:
Data for the last 5 blocks is retrieved using Hedera's mirror node REST API:
```python
# Each block on Hedera is approximately 2 seconds
numBlocks = 5
blocks_url = f"https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?limit={numBlocks}"
response = requests.get(blocks_url)
```

## 2. Add Up Transactions
For these 5 blocks, the total number of transactions is calculated by summing up the transaction counts of each block:
```python
blocks = response.json()['blocks']
sum_of_transactions = sum(block['count'] for block in blocks)
```

## 3. Calculate Duration
We determine the total duration of these 5 blocks by calculating the difference between the timestamps of the newest and the oldest block:
```python
newest_block_to_timestamp = float(blocks[0]['timestamp']['to'])
oldest_block_from_timestamp = float(blocks[-1]['timestamp']['from'])
duration = newest_block_to_timestamp - oldest_block_from_timestamp
```

## 4. Calculate TPS 🎉🎉
The TPS is simply the **total number of transactions** in the last 5 blocks (approximately 10 seconds) divided by the **actual duration of those blocks**. 

```python
transactions_per_second = sum_of_transactions / duration
```

# See the Results!
Simply run the script:
```python
TPS = get_transactions_per_second()
print(f"Hedera TPS:", TPS)
```
<img width="435" alt="image" src="https://github.com/ed-marquez/hedera-tps-calculator/assets/72571340/615e51d7-8ec5-48d7-8ee7-38828b9453ff">
