TIMEOUT = 10

HOST = 'https://wallet.shiftnrg.org'
START = ''.join([HOST, '/api'])

ACCOUNTS = ''.join([START, '/accounts'])
ACCOUNTS_OPEN = ''.join([ACCOUNTS, '/open'])
ACCOUNTS_GET_BALANCE = ''.join([ACCOUNTS, '/getBalance'])
ACCOUNTS_GET_PUBLICKEY = ''.join([ACCOUNTS, '/getPublicKey'])
ACCOUNTS_GEN_PUBLICKEY = ''.join([ACCOUNTS, '/generatePublicKey'])
ACCOUNTS_GET = ACCOUNTS
ACCOUNTS_GET_DELEGATES = ''.join([ACCOUNTS, '/delegates'])
ACCOUNTS_PUT_DELEGATES = ''.join([ACCOUNTS, '/delegates'])

LOADER = ''.join([START, '/loader'])
LOADER_GET_STATUS = ''.join([LOADER, '/status'])
LOADER_GET_SYNC = ''.join([LOADER, '/status/sync'])

TRANSACTIONS = ''.join([START, '/transactions'])
TRANSACTIONS_LIST = TRANSACTIONS
TRANSACTIONS_SEND = TRANSACTIONS
TRANSACTIONS_GET = ''.join([TRANSACTIONS, '/get'])
TRANSACTIONS_UNCONFIRMED_GET = ''.join([TRANSACTIONS, '/unconfirmed/get'])
TRANSACTIONS_UNCONFIRMED_LIST = ''.join([TRANSACTIONS, '/unconfirmed'])

PEERS = ''.join([START, '/peers'])
PEERS_LIST = PEERS
PEERS_GET = ''.join([PEERS, '/get'])
PEERS_GET_VERSION = ''.join([PEERS, '/version'])

BLOCKS = ''.join([START, '/blocks'])
BLOCKS_GET_ONE = ''.join([BLOCKS, '/get'])
BLOCKS_GET_FILTER = BLOCKS
BLOCKS_GET_FEE = ''.join([BLOCKS, '/getFee'])
BLOCKS_GET_FEES = ''.join([BLOCKS, '/getFees'])
BLOCKS_GET_REWARD = ''.join([BLOCKS, '/getReward'])
BLOCKS_GET_SUPPLY = ''.join([BLOCKS, '/getSupply'])
BLOCKS_GET_HEIGHT = ''.join([BLOCKS, '/getHeight'])
BLOCKS_GET_STATUS = ''.join([BLOCKS, '/getStatus'])
BLOCKS_GET_NETHASH = ''.join([BLOCKS, '/getNethash'])
BLOCKS_GET_MILESTONE = ''.join([BLOCKS, '/getMilestone'])

SIGNATURES = ''.join([START, '/signatures'])
SIGNATURES_GET = ''.join([SIGNATURES, '/get'])
SIGNATURES_ADD_SECOND = SIGNATURES

DELEGATES = ''.join([START, '/delegates'])
DELEGATES_CREATE = DELEGATES
DELEGATES_LIST = DELEGATES
DELEGATES_GET = ''.join([DELEGATES, '/get'])
DELEGATES_COUNT = ''.join([DELEGATES, '/count'])
DELEGATES_GET_VOTES = ACCOUNTS_GET_DELEGATES
DELEGATES_GET_VOTERS = ''.join([DELEGATES, '/voters'])
DELEGATES_ENABLE_FORGING = ''.join([DELEGATES, '/forging/enable'])
DELEGATES_DISABLE_FORGING = ''.join([DELEGATES, '/forging/disable'])
DELEGATES_GET_FORGED = ''.join([DELEGATES, '/forging/getForgedByAccount'])

APPS = ''.join([START, '/dapps'])
APPS_REGISTER = APPS
APPS_GET_REGISTERED = APPS
APPS_GET = APPS
APPS_SEARCH = ''.join([APPS, '/search'])
APPS_INSTALL = ''.join([APPS, '/install'])
APPS_INSTALLED = ''.join([APPS, '/installed'])
APPS_INSTALLED_IDS = ''.join([APPS, '/installedIds'])
APPS_UNINSTALL = ''.join([APPS, '/uninstall'])
APPS_LAUNCH = ''.join([APPS, '/launch'])
APPS_INSTALLING = ''.join([APPS, '/installing'])
APPS_UNINSTALLING = ''.join([APPS, '/uninstalling'])
APPS_LAUNCHED = ''.join([APPS, '/launched'])
APPS_CATEGORIES = ''.join([APPS, '/categories'])
APPS_STOP = ''.join([APPS, '/stop'])

MULTI_SIGNATURE = ''.join([START, '/multisignatures'])
MULTI_SIGNATURE_PENDING = ''.join([MULTI_SIGNATURE, '/pending'])
MULTI_SIGNATURE_CREATE_ACCOUNT = MULTI_SIGNATURE
MULTI_SIGNATURE_SIGN = ''.join([MULTI_SIGNATURE, '/sign'])
MULTI_SIGNATURE_ACCOUNTS = ''.join([MULTI_SIGNATURE, '/accounts'])
