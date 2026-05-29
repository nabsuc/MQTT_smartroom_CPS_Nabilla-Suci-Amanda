# MQTT Smart Room Monitoring

## Deskripsi
Project ini merupakan implementasi komunikasi MQTT menggunakan Python dan Mosquitto Broker pada studi kasus Smart Room Monitoring. Sistem menggunakan pola komunikasi publish-subscribe, di mana publisher mengirimkan data sensor virtual dan subscriber menerima data melalui broker MQTT.

## Tools dan Teknologi
- Python 3.14
- Mosquitto Broker
- Library paho-mqtt
- MQTT Protocol

## Struktur Folder

```text
mqtt-smartroom-nabilla/
├── code/
├── screenshot/
├── gambar/
└── README.md
```

## Instalasi

Install library MQTT:

```bash
pip install paho-mqtt
```

Pastikan Mosquitto Broker sudah terinstall.

## Menjalankan Program

### Skenario 1 – Basic Publisher Subscriber

Subscriber:

```bash
python code/subscriber_basic.py
```

Publisher:

```bash
python code/publisher_basic.py
```

### Skenario 2 – QoS

Subscriber:

```bash
python code/subscriber_qos.py
```

Publisher:

```bash
python code/publisher_qos.py
```

### Skenario 3 – Multi Topic

Subscriber:

```bash
python code/subscriber_multitopic.py
```

Publisher:

```bash
python code/publisher_multitopic.py
```

### Skenario 4 – Wildcard +

Subscriber:

```bash
python code/subscriber_wildcard_plus.py
```

Publisher:

```bash
python code/publisher_wildcard_plus.py
```

### Skenario 5 – Wildcard #

Subscriber:

```bash
python code/subscriber_wildcard_hash.py
```

Publisher:

```bash
python code/publisher_wildcard_hash.py
```

## Author

Nabilla Suci Amanda - 235150301111044