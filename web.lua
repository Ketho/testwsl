local https = require "ssl.https"

local url = "https://www.google.com/"
local body = https.request(url)
print(body)
