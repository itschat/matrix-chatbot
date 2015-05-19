from __future__ import print_function
import time
from slackclient import SlackClient
import mh_python as mh
import random


def main():
    token = ""
    sc = SlackClient(token)
    mh.initbrain()
    try:
        if sc.rtm_connect():
            while True:
                for event in sc.rtm_read():
                    if event['type'] == 'message':
                        message = event['text']
                        print("Handling message: %s" % message)
                        if random.random() < 0.1:
                            reply = mh.doreply(message)
                            print("Replying: %s" % reply)
                            sc.rtm_send_message(event['channel'], reply)
                        else:
                            mh.learn(message)
                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")
    finally:
        mh.cleanup()

if __name__ == '__main__':
    main()
