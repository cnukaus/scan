# scan
##To validate
1. path is chinese (事unicode)

2 if fileitem in D[in]: 如何克服重名（用dict). in D也是错的

WARNING:root:[Errno 2] No such file or directory: 'd:\\\\\\xbc\\xd2\\xca\\xc2\\\\5.pdf'

3. Linux partitions

saved:d:\5.pdf to
d:\\tmp\\5.pdfEND

##To combine
搜索逻辑：精确匹配，模糊匹配，新规则建立

hawkeye的 https://github.com/0xbug/Hawkeye 爬虫 报警功能
https://github.com/UKHomeOffice/repo-security-scanner\rules\gitrob.json
: [
  {
    "part": "filename",
    "type": "regex",
    "pattern": "\\A.*_rsa\\z",
    "caption": "Private SSH key",
    "description": null
  },
