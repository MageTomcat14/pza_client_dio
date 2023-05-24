from panduza import Client, Dio, Core
import time, logging


# CONFIGURATION
BROKER_ADDR="localhost"
BROKER_PORT=1883

# one topic per io
pzaTOPIC_OUT=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{0}"
pzaTOPIC_IN=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{1}"
pzaTOPIC_PUSHBUTTON=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{16}"
pzaClient = Client(port=BROKER_PORT, url=BROKER_ADDR)
pzaClient.connect()

# scan the interface
inter = pzaClient.scan_interfaces()

    # list all the topics
print("scanning the topics..")
for topic in inter:
    print(f"- {topic} => {inter[topic]['type']}")

    # declare instances of dio. One per io control
d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC_OUT, client=pzaClient)
d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC_IN, client=pzaClient)
d16 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC_PUSHBUTTON, client=pzaClient)

print(f"setting the values for GPIO {0}, must see led {1} toggle..")


while True:
    try:
        d.direction.value.set("out")
        d1.direction.value.set("in")
        # d16.direction.value.set("out")

        d.direction.pull.set("up")

        d.direction.polling_cycle.set(0.1)
        d.state.polling_cycle.set(0.1)
        d1.direction.polling_cycle.set(0.1)
        d1.state.polling_cycle.set(0.1)
        d16.direction.polling_cycle.set(0.1)
        d16.state.polling_cycle.set(0.1)

        d.state.active_low.set(False)
        d.state.active.set(True)
        time.sleep(1)
        print(f" value of the input \033[92m{d1.state.active.get()}\033[0m")
        time.sleep(1)
        d.state.active.set(False)
        time.sleep(1)
        print(f" value of the input \033[92m{d1.state.active.get()}\033[0m")
        time.sleep(1)

        print("reading value of the push button")
        print(f" value of the push button \033[92m{d16.state.active.get()}\033[0m")
        time.sleep(1)

    except: # reset all the state of io's
       print("going back to init configuration")
       d.state.active.set(False)
       d1.state.active.set(False)
       d.direction.polling_cycle.set(1)
       d.state.polling_cycle.set(1)
       d1.direction.polling_cycle.set(1)
       d1.state.polling_cycle.set(1)
       d16.direction.polling_cycle.set(1)
       d16.state.polling_cycle.set(1)
       exit()