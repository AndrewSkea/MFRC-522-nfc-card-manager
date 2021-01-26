# MFRC-522 Card Manager

## About
This project aims to provide a simple way to manage your rfid cards on a raspberry pi which is connected to your MFRC-522 reader.

For the setup of your reader, follow this [blog post](https://pimylifeup.com/raspberry-pi-rfid-rc522/), but install this project using the steps below:

## Setup
```
# Clone this project
git clone https://gitlab.com/AndrewSkea/mfrc-522-card-manager
cd mfrc-522-card-manager

# Install this project
pip install -r requirements
```

## Usage
```
import mfrc522-card-manager as cm

# Get all cards
saved_cards = cm.list_cards()
print(saved_cards)

# Get content of a card with example id
card_id = 984895797429
card = cm.get_text_from_card(card_id)
print(card)

# Timeout of 30 seconds for user to place card on reader
num_tries = 30

# Start the read thread
# Keep checking the read 
cm.start_read()
for try in num_tries:
    data = cm.get_read_status()
    time.sleep(0.2)
    if data:
        break
print(data)


# Start the write thread
# Keep checking the write 
cm.start_write("text_to_write")
for try in num_tries:
    data = cm.get_write_status()
    time.sleep(0.2)
    if data:
        break
print(data)
```


## Credit
Special thanks to this project which provided the connection to the MFRC-522 reader connected to your Pi:
* https://github.com/pimylifeup/MFRC522-python
