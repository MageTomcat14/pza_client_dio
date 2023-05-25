from panduza import Client, Core, Dio
import time

BROKER_ADDR="localhost"
BROKER_PORT=1883

num = []

topicBegin = "pza/lab_paul/io_pza_controling/testing_of_io_controling-"

Core.LoadAliases(json_filepath="clientConf.json")
    
pzaPaulClient = Client(broker_alias="local")
pzaPaulClient.connect()

inter = pzaPaulClient.scan_interfaces()


for topic in inter:
    if str(inter[topic]['type']).rjust(10) == str('       DIO'): # load the DIO topics from json

        print(f"list of the TOPICS => {topic}")
        getioNumber = topic.split(topicBegin)[1]
        toInt = int(getioNumber)
        num.append(toInt)

print(num)
print("\033[92msorting array of topics\033[0m")
sort = sorted(num)
print(sort)

d0 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[0]}", client=pzaPaulClient)
d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[1]}", client=pzaPaulClient)
d16 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[2]}", client=pzaPaulClient)

print(d0)

while True:
    try:
        d0.direction.value.set("out")
        d1.direction.value.set("in")
        # d16.direction.value.set("out")

        d0.direction.pull.set("up")

        d0.direction.polling_cycle.set(0.1)
        d0.state.polling_cycle.set(0.1)
        d1.direction.polling_cycle.set(0.1)
        d1.state.polling_cycle.set(0.1)
        d16.direction.polling_cycle.set(0.1)
        d16.state.polling_cycle.set(0.1)

        d0.state.active_low.set(False)
        d0.state.active.set(True)
        time.sleep(1)
        print(f" value of the input \033[92m{d1.state.active.get()}\033[0m")
        time.sleep(1)
        d0.state.active.set(False)
        time.sleep(1)
        print(f" value of the input \033[92m{d1.state.active.get()}\033[0m")
        time.sleep(1)

        print("reading value of the push button")
        print(f" value of the push button \033[92m{d16.state.active.get()}\033[0m")
        time.sleep(1)

    except: # reset all the state of io's
       print("going back to init configuration")
       d0.state.active.set(False)
       d1.state.active.set(False)
       d0.direction.polling_cycle.set(1)
       d0.state.polling_cycle.set(1)
       d1.direction.polling_cycle.set(1)
       d1.state.polling_cycle.set(1)
       d16.direction.polling_cycle.set(1)
       d16.state.polling_cycle.set(1)
       exit()