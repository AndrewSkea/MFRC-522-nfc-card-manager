from mfrc522 import SimpleMFRC522

from thread_classes import ReadThread, WriteThread
from db import setup_connection, update_card, get_card, get_all_cards

reader = SimpleMFRC522()
setup_connection()

global read_thread
read_thread = None

global write_thread
write_thread = None


def check_write_progress():
    global write_thread
    print("check write, cid: {}, text: {}, status: {}".format(write_thread.cid, write_thread.text, write_thread.status))
    if write_thread.cid:
        data = {
            "status": "complete",
            "cid": write_thread.cid,
            "uri": write_thread.text
        }
        update_card(write_thread.cid, write_thread.text)
        return data
    else:
        return {"status": write_thread.status, "id": "", "uri": ""}


def write_text(text):
    print("Writing endpoint called with text: {}".format(text))
    text += max(8-len(text), 0) * " "
    global write_thread
    write_thread = WriteThread(reader, text)
    write_thread.start()
    return check_write_progress()
    
    
def check_read_progress():
    global read_thread
    print("check read, cid: {}, text: {}, status: {}".format(read_thread.cid, read_thread.text, read_thread.status))
    if read_thread.cid:
        data = {
            "status": "complete",
            "cid": read_thread.cid,
            "uri": read_thread.text
        }
        update_card(write_thread.cid, write_thread.text)
        return data
    else:
        print("check read, no cid, status: {}".format(read_thread.status))
        return {"status": read_thread.status, "id": "", "uri": ""}


def read_text():
    print("Reading endpoint called")
    global read_thread
    read_thread = ReadThread(reader)
    read_thread.start()
    return check_read_progress()


def get_text_from_card(card_id):
    return get_card(card_id)


def list_cards():
    cards = get_all_cards()
    return list(cards)