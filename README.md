# MINFT1
###### A minting toolkit for the Chia Blockchain.

## Requirements
- The finished artwork of your NFTs
- The metadata in JSON format for all of your NFTs
- A fully synced Chia Node / Wallet
- A Chia NFT wallet and a DID
- A PostgreSQL server

## Setup Instructions

#### 1. Clone or copy this repository into the `chia-blockchain` directory.
#### 2. Change to the new directory and install additional dependencies 
```
$ pip install -r requirements.txt
```

#### 3. Copy `config.default.yml` to `config.yml` and set all configuration parameters in it.

#### 4. Copy all images into the designated images folder and all the JSON metadata into the designated metadata folder. If you're using the default settings these are `assets/images/` and `assets/metadata/`.

#### 5. Make sure you have a fully synced wallet running on the machine you want to use for minting.

#### 6. Run the minter
```python
python minft1.py
```

---

#### Adapted by codephunk. Based on the Marmot Minter by Yostra.

#### Original License:

MIT License

Copyright (c) Yostra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
