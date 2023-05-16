from panduza import Client, Dio
import time, logging


# CONFIGURATION
BROKER_ADDR="localhost"
BROKER_PORT=1883


    
# one topic per io
pzaTOPIC=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{6}"
pzaTOPIC1=f"pza/lab_paul/io_pza_controling/testing_of_io_controling{7}"



pzaClient = Client(port=BROKER_PORT, url=BROKER_ADDR)
pzaClient.connect()

    # scan the interface
inter = pzaClient.scan_interfaces()

    # list all the topics
print("scanning the interfaces..")
for topic in inter:
    print(f"- {topic} => {inter[topic]['type']}")

    # declare instances of dio. One per io control
d = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC, client=pzaClient)
d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=pzaTOPIC1, client=pzaClient)


print(f"setting the values for GPIO {0}, must see led {1} toggle..")

while True:
   
    d.direction.value.set("out")
    time.sleep(1)
    d.direction.pull.set("up")
    time.sleep(1)
    d.direction.polling_cycle.set(1)
    time.sleep(1)

    d.state.active_low.set(False)
    time.sleep(1)
    d.state.active.set(True)
    time.sleep(1)
    print(f" value of the input {d1.state.active.get()}")
    time.sleep(2)
    d.state.active.set(False)
    time.sleep(1)
    d.state.polling_cycle.set(1)
    time.sleep(1)

    print(f" value of the input {d1.state.active.get()}")
