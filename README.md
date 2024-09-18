# Telegram Group Counter

[![👮‍♂️ Sanity checks](https://github.com/pcaversaccio/telegram-group-counter/actions/workflows/checks.yml/badge.svg)](https://github.com/pcaversaccio/telegram-group-counter/actions/workflows/checks.yml)
[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-blue.svg)](http://www.wtfpl.net/about/)

The Python script [`telegram_group_counter.py`](./scripts/telegram_group_counter.py) allows you to programmatically count the number of Telegram groups you're a member of using the [Telegram API](https://core.telegram.org) and the [Telethon](https://github.com/LonamiWebs/Telethon) library.

![image](https://github.com/user-attachments/assets/0c666862-674d-4709-af33-66d43cb02d39)

## Prerequisites

- Python `>=3.6`
- Telegram API credentials (`api_id` and `api_hash`)

1. Clone this repository:

```console
git clone https://github.com/pcaversaccio/telegram-group-counter.git
cd telegram-group-counter
```

2. Create a virtual environment (optional but recommended):

```console
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`.
```

3. Install the required packages:

```console
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Telegram API credentials[^1]:

```txt
API_ID="your_api_id"
API_HASH="your_api_hash"
PHONE_NUMBER="your_phone_number"
```

> [!CAUTION]
> Make sure to keep your `.env` file secure and _never_ commit it to version control!

## Usage

Run the script using Python:

```console
python scripts/telegram_group_counter.py
```

The script will output the number of Telegram groups you're a member of 🫡.

```console
You are in 123 Telegram groups.
```

[^1]: To get the Telegram API credentials go to [`my.telegram.org`](https://my.telegram.org) and log in with your phone number. Now click on `API development tools` and create a new application by filling in the required fields. Once created, you'll see your `api_id` (a number) and `api_hash` (a string).
