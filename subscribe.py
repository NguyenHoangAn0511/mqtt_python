from utils import *
def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to {BROKER_URL} with port {PORT} successfully!")
            subscribe(client)
        else:
            print(f"Failed to connect, return code %d\n", rc)
def run():
    client = connect_mqtt()
    client.on_connect = on_connect
    client.loop_forever()


if __name__ == '__main__':
    run()