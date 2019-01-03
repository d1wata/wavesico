import pywaves as pw
from coinbase.wallet.client import Client
import configparser

```
Grabbing keys from 'config.ini'

```

config = configparser.ConfigParser()
config.read('config.ini')

apiKey = config['COINBASE']['api']
secretKey = config['COINBASE']['secret']
privKey = config['WAVES']['privkey']

```
Pseudocode/Semicode
Piecing Ideas

```

myAddress = pw.Address(privateKey=privKey)

otherAddress = pw.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM')
myAddress.sendWaves(otherAddress, 10000000)
myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
while not myToken.status():
	pass
myAddress.sendAsset(otherAddress, myToken, 50)
