Other candidates: 交易所差价index; 跑路指数( lCO contract In/out token,time domain purchased/expiry)bitdb.network; coinbase bulletin; https://dappradar.com; Bitcointalk之后是谁- 用correlation来检测
## Scanner of important information
### bug to fix:
fileitem in Dic[in]: 如何克服重名（用dict). in D也是错的
### 现在需添加功能
MD5存下来？
Python应该启用Logger方便调错

模糊匹配，

规则存储改为https://github.com/UKHomeOffice/repo-security-scanner\rules\gitrob.json 格式
https://github.com/MiSecurity/x-patrol
### 中期所缺功能：
1. online API to store result
2. 新文件源：iCrawler(QR-pirate)+ OCR to detect new sources
3. Linux partitions
4. 如都是机械硬盘或混有Flash Disk,何时适合Multithreading(读机械盘不适合4+线程并行）
### 远期功能：
1. Push rules that based on blockchain file price trend/ indicated by future hot topic?

### Done and To Test
TO check other Forensic BItbucket and found 2 Git proj (QRcod)

WARNING:root:[Errno 2] No such file or directory: 'd:\\\\\\xbc\\xd2\\xca\\xc2\\\\5.pdf'



### To combine
搜索逻辑：精确匹配，

hawkeye的 https://github.com/0xbug/Hawkeye 爬虫 报警功能
https://github.com/FeeiCN/GSIL/blob/master/gsil/engine.py 扫描邮件地址并保存-考虑并行，磁盘，冲突及无趣公用邮件库：
public_mail_services = [
    'msg.com',
    '126.com',
    '139.com',
    '163.com',
    'qq.com',

Token recommendation using BigQuery 
https://medium.com/google-cloud/building-token-recommender-in-google-cloud-platform-1be5a54698eb
#standardSQL by Evgenny
with top_tokens as (
  select token_address, count(1) as transfer_count
  from `bigquery-public-data.ethereum_blockchain.token_transfers` as token_transfers
  group by token_address
  order by transfer_count desc
  limit 1000
),
token_balances as (
    with double_entry_book as (
        select token_address, to_address as address, cast(value as float64) as value, block_timestamp
        from `bigquery-public-data.ethereum_blockchain.token_transfers`
        union all
        select token_address, from_address as address, -cast(value as float64) as value, block_timestamp
        from `bigquery-public-data.ethereum_blockchain.token_transfers`
    )
    select double_entry_book.token_address, address, sum(value) as balance
    from double_entry_book
    join top_tokens on top_tokens.token_address = double_entry_book.token_address
    where address != '0x0000000000000000000000000000000000000000'
    group by token_address, address
    having balance > 0
),
token_supplies as (
    select token_address, sum(balance) as supply
    from token_balances
    group by token_address
)
select 
    token_balances.token_address, 
    token_balances.address as user_address, 
    balance/supply * 100 as rating
from token_balances
join token_supplies on token_supplies.token_address = token_balances.token_address
where balance/supply * 100 > 0.001
