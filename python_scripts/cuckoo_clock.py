# import time

# play cuckoo clock an x amount of times
entity_id = data.get("entity_id")
hour = int(data.get("hour"))
minute = int(data.get("minute"))

amount = hour


if hour > 12:
    amount = hour - 12

if minute > 55:
    amount += 1

if minute < 55 and minute > 5:
    amount = 1

# Only allowed after work hours, otherwise the girlfriend gets angry
if entity_id is not None and hour >= 18:
    service_data = {
        "entity_id": entity_id,
        "media_content_id": "http://projects.kokokoding.nl/home-assistant/cuckoo.wav",
        "media_content_type": "audio/wav",
    }

    for i in range(amount):
        hass.services.call("media_player", "play_media", service_data, True)
        time.sleep(1.5)
