from panduza import Client, Core, Dio
import time, array

BROKER_ADDR="localhost"
BROKER_PORT=1883

num = []

topicBegin = "pza/lab_paul/io_pza_controling/testing_of_io_controling-"
Core.LoadAliases(json_filepath="clientConf.json")
    
pzaPaulClient = Client(broker_alias="local")
pzaPaulClient.connect()

inter = pzaPaulClient.scan_interfaces()


for topic in inter:
    # print(f"- printing topics {topic} => {inter[topic]['type']}")
    # if str(inter[topic]['type']) == str("Dio"):
    # print(f"before loop [{str(inter[topic]['type']).rjust(10)}] - {topic}")

    if str(inter[topic]['type']).rjust(10) == str('       DIO'): # load the DIO topics from json

        print(f"list of the TOPICS => {topic}")
        getioNumber = topic.split(topicBegin)[1]
        toInt = int(getioNumber)
        print("test", toInt)
        num.append(toInt)

print(num)
print("\033[92msorting array of topics\033[0m")
sort = sorted(num)
print(sort)

d0 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[0]}", client=pzaPaulClient)
d1 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[1]}", client=pzaPaulClient)
d2 = Dio (addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[2]}", client=pzaPaulClient)
d3 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[3]}", client=pzaPaulClient)
d4 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[4]}", client=pzaPaulClient)
d5 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[5]}", client=pzaPaulClient)
d6 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[6]}", client=pzaPaulClient)
d7 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[7]}", client=pzaPaulClient)
d8 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[8]}", client=pzaPaulClient)
d9 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[9]}", client=pzaPaulClient)
d10 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[10]}", client=pzaPaulClient)
d11 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[11]}", client=pzaPaulClient)
d12 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[12]}", client=pzaPaulClient)
d13 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[13]}", client=pzaPaulClient)
d14 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[14]}", client=pzaPaulClient)
d15 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[15]}", client=pzaPaulClient)
d16 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[16]}", client=pzaPaulClient)
d17 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[17]}", client=pzaPaulClient)
d18 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[18]}", client=pzaPaulClient)
d19 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[19]}", client=pzaPaulClient)
d20 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[20]}", client=pzaPaulClient)
d21 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[21]}", client=pzaPaulClient)
d22 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[22]}", client=pzaPaulClient)
d26 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[23]}", client=pzaPaulClient)
d27 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[24]}", client=pzaPaulClient)
d28 = Dio(addr=BROKER_ADDR, port=BROKER_PORT, topic=f"pza/lab_paul/io_pza_controling/testing_of_io_controling-{sort[25]}", client=pzaPaulClient)


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