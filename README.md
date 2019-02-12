# scan
##To Fix
1. path is chinese (事unicode)

2 if fileitem in D[in]: 如何克服重名（用dict). in D也是错的

WARNING:root:[Errno 2] No such file or directory: 'd:\\\\\\xbc\\xd2\\xca\\xc2\\\\5.pdf'

3. Linux partitions

saved:d:\5.pdf to
d:\\tmp\\5.pdfEND

##To combine

https://github.com/UKHomeOffice/repo-security-scanner\rules\gitrob.json
: [
  {
    "part": "filename",
    "type": "regex",
    "pattern": "\\A.*_rsa\\z",
    "caption": "Private SSH key",
    "description": null
  },
