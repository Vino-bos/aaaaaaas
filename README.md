
# Telegram Group Seller Bot

Otomatiskan penjualan akses grup Telegram dengan pembayaran manual via Lynk.id.  
Cukup atur token konfirmasi, bagikan setelah pembayaran, dan bot akan mengirim link grup.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/placeholder/template)

## Konfigurasi ENV
- `BOT_TOKEN` : Token bot dari @BotFather  
- `OWNER_ID`  : ID Telegram pemilik (7938342969)

## Cara Tambah Token
```
/add vip99 https://t.me/joinchat/abcdef
```
Bot akan membalas link konfirmasi:
```
https://t.me/YourBot?start=vip99
```
