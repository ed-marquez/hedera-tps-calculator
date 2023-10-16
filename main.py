import requests

def get_transactions_per_second():
  # Each block on Hedera is approximately 2 seconds
  numBlocks = 5
  # Use the mirror node REST API to get info from the last 5 blocks
  blocks_url = f"https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?limit={numBlocks}"
  response = requests.get(blocks_url)
  
  # Add up the transactions from each block
  blocks = response.json()['blocks']
  sum_of_transactions = sum(block['count'] for block in blocks)

  # Calculate the duration of the 5 blocks from the timestamps of the first and last blocks
  newest_block_to_timestamp = float(blocks[0]['timestamp']['to'])
  oldest_block_from_timestamp = float(blocks[-1]['timestamp']['from'])
  duration = newest_block_to_timestamp - oldest_block_from_timestamp

  # Calculate the transactions per second
  transactions_per_second = sum_of_transactions / duration
  return transactions_per_second

TPS = get_transactions_per_second()
print(f"Hedera TPS:", TPS)
