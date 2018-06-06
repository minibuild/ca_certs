#import "."

module_type = 'download'
module_name = 'cacerts-download'

download_list = [
  ['https://mkcert.org/generate/', 'certdata-original.pem']
]

post_build = ['cadata-reparse']
