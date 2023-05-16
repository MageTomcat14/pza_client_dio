from panduza import Client, Core, Dio
import time



Core.LoadAliases({
        "local":{
                "url": "localhost",
                "port": 1883,
                "interfaces": {}
        }
})
    
pzaPaulClient = Client(broker_alias="local")
pzaPaulClient.connect()


inter = pzaPaulClient.scan_interfaces()

for topic in inter:
    print(f"- {topic} => {inter[topic]['type']}")

d = Dio(addr="url", port=1883, topic=topic, client=pzaPaulClient)

while True:
    d.direction.value.set("out")
    time.sleep(1)
    d.direction.pull.set("up")
    time.sleep(1)
    d.direction.polling_cycle.set(2)
    time.sleep(1)

    d.state.active.set(False)
    time.sleep(1)
    d.state.active_low.set(True)
    time.sleep(1)
    d.state.polling_cycle.set(2)
    time.sleep(1)
