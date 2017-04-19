# -*- coding: utf-8 -*-

# Scrapy settings for nobelprize project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'nobelprize'

SPIDER_MODULES = ['nobelprize.spiders']
NEWSPIDER_MODULE = 'nobelprize.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nobelprize (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'nobelprize.middlewares.NobelprizeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'nobelprize.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'nobelprize.pipelines.NobelprizePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

FEED_EXPORTERS = {
    'csv': 'nobelprize.nobelprize_csv_item_exporter.MyProjectCsvItemExporter',
}
# Fields are hard coded
FIELDS_TO_EXPORT = [
	'A0_year',
	'A1_number',
	'A2_url',
	'A3_comments',
	'B0_nominee1_name',
	'B1_nominee1_gender',
	'B2_nominee1_birth',
	'B3_nominee1_death',
	'B4_nominee1_profession',
	'B5_nominee1_city',
	'B6_nominee1_country',
	'B7_nominee1_motivation',
	'C0_nominee2_name',
	'C1_nominee2_gender',
	'C2_nominee2_birth',
	'C3_nominee2_death',
	'C4_nominee2_profession',
	'C5_nominee2_city',
	'C6_nominee2_country',
	'C7_nominee2_motivation',
	'D0_nominee3_name',
	'D1_nominee3_gender',
	'D2_nominee3_birth',
	'D3_nominee3_death',
	'D4_nominee3_profession',
	'D5_nominee3_city',
	'D6_nominee3_country',
	'D7_nominee3_motivation',
	'E0_nominator1_name',
	'E1_nominator1_gender',
	'E2_nominator1_birth',
	'E3_nominator1_death',
	'E4_nominator1_profession',
	'E5_nominator1_university',
	'E6_nominator1_city',
	'E7_nominator1_country',
	'F0_nominator2_name',
	'F1_nominator2_gender',
	'F2_nominator2_birth',
	'F3_nominator2_death',
	'F4_nominator2_profession',
	'F5_nominator2_university',
	'F6_nominator2_city',
	'F7_nominator2_country',
	'G0_nominator3_name',
	'G1_nominator3_gender',
	'G2_nominator3_birth',
	'G3_nominator3_death',
	'G4_nominator3_profession',
	'G5_nominator3_university',
	'G6_nominator3_city',
	'G7_nominator3_country',
	'H0_nominator4_name',
	'H1_nominator4_gender',
	'H2_nominator4_birth',
	'H3_nominator4_death',
	'H4_nominator4_profession',
	'H5_nominator4_university',
	'H6_nominator4_city',
	'H7_nominator4_country',
	'I0_nominator5_name',
	'I1_nominator5_gender',
	'I2_nominator5_birth',
	'I3_nominator5_death',
	'I4_nominator5_profession',
	'I5_nominator5_university',
	'I6_nominator5_city',
	'I7_nominator5_country',
	'J0_nominator6_name',
	'J1_nominator6_gender',
	'J2_nominator6_birth',
	'J3_nominator6_death',
	'J4_nominator6_profession',
	'J5_nominator6_university',
	'J6_nominator6_city',
	'J7_nominator6_country',
	'K0_nominator7_name',
	'K1_nominator7_gender',
	'K2_nominator7_birth',
	'K3_nominator7_death',
	'K4_nominator7_profession',
	'K5_nominator7_university',
	'K6_nominator7_city',
	'K7_nominator7_country',
	'L0_nominator8_name',
	'L1_nominator8_gender',
	'L2_nominator8_birth',
	'L3_nominator8_death',
	'L4_nominator8_profession',
	'L5_nominator8_university',
	'L6_nominator8_city',
	'L7_nominator8_country',
	'M0_nominator9_name',
	'M1_nominator9_gender',
	'M2_nominator9_birth',
	'M3_nominator9_death',
	'M4_nominator9_profession',
	'M5_nominator9_university',
	'M6_nominator9_city',
	'M7_nominator9_country',
	'N0_nominator10_name',
	'N1_nominator10_gender',
	'N2_nominator10_birth',
	'N3_nominator10_death',
	'N4_nominator10_profession',
	'N5_nominator10_university',
	'N6_nominator10_city',
	'N7_nominator10_country',
	'O0_nominator11_name',
	'O1_nominator11_gender',
	'O2_nominator11_birth',
	'O3_nominator11_death',
	'O4_nominator11_profession',
	'O5_nominator11_university',
	'O6_nominator11_city',
	'O7_nominator11_country',
	'P0_nominator12_name',
	'P1_nominator12_gender',
	'P2_nominator12_birth',
	'P3_nominator12_death',
	'P4_nominator12_profession',
	'P5_nominator12_university',
	'P6_nominator12_city',
	'P7_nominator12_country',
	'Q0_nominator13_name',
	'Q1_nominator13_gender',
	'Q2_nominator13_birth',
	'Q3_nominator13_death',
	'Q4_nominator13_profession',
	'Q5_nominator13_university',
	'Q6_nominator13_city',
	'Q7_nominator13_country',
	'R0_nominator14_name',
	'R1_nominator14_gender',
	'R2_nominator14_birth',
	'R3_nominator14_death',
	'R4_nominator14_profession',
	'R5_nominator14_university',
	'R6_nominator14_city',
	'R7_nominator14_country',
	'S0_nominator15_name',
	'S1_nominator15_gender',
	'S2_nominator15_birth',
	'S3_nominator15_death',
	'S4_nominator15_profession',
	'S5_nominator15_university',
	'S6_nominator15_city',
	'S7_nominator15_country',
	'T0_nominator16_name',
	'T1_nominator16_gender',
	'T2_nominator16_birth',
	'T3_nominator16_death',
	'T4_nominator16_profession',
	'T5_nominator16_university',
	'T6_nominator16_city',
	'T7_nominator16_country',
	'U0_nominator17_name',
	'U1_nominator17_gender',
	'U2_nominator17_birth',
	'U3_nominator17_death',
	'U4_nominator17_profession',
	'U5_nominator17_university',
	'U6_nominator17_city',
	'U7_nominator17_country',
	'V0_nominator18_name',
	'V1_nominator18_gender',
	'V2_nominator18_birth',
	'V3_nominator18_death',
	'V4_nominator18_profession',
	'V5_nominator18_university',
	'V6_nominator18_city',
	'V7_nominator18_country',
	'W0_nominator19_name',
	'W1_nominator19_gender',
	'W2_nominator19_birth',
	'W3_nominator19_death',
	'W4_nominator19_profession',
	'W5_nominator19_university',
	'W6_nominator19_city',
	'W7_nominator19_country',
	'X0_nominator20_name',
	'X1_nominator20_gender',
	'X2_nominator20_birth',
	'X3_nominator20_death',
	'X4_nominator20_profession',
	'X5_nominator20_university',
	'X6_nominator20_city',
	'X7_nominator20_country',
	'Y0_nominator21_name',
	'Y1_nominator21_gender',
	'Y2_nominator21_birth',
	'Y3_nominator21_death',
	'Y4_nominator21_profession',
	'Y5_nominator21_university',
	'Y6_nominator21_city',
	'Y7_nominator21_country'
]
CSV_DELIMITER = "\t" # For tab
