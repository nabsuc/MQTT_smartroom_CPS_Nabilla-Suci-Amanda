# 🏠 MQTT Smart Room Monitoring

> Implementasi sistem komunikasi MQTT untuk Smart Room Monitoring menggunakan Python dan Mosquitto Broker

## 📋 Deskripsi Singkat

Project ini merupakan implementasi komunikasi MQTT menggunakan **Python** dan **Mosquitto Broker** pada studi kasus Smart Room Monitoring. Sistem menggunakan pola komunikasi **publish-subscribe**, di mana publisher mengirimkan data dan subscriber menerima data secara real-time melalui broker MQTT.

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| **Bahasa Pemrograman** | Python 3.14 |
| **Message Broker** | Mosquitto Broker |
| **MQTT Library** | paho-mqtt |
| **Protocol** | MQTT (Message Queuing Telemetry Transport) |

---

## 📁 Struktur Proyek

```
MQTT_smartroom_CPS_Nabilla-Suci-Amanda/
├── code/                    # Folder utama untuk semua script Python
│   ├── subscriber_basic.py
│   ├── publisher_basic.py
│   ├── subscriber_qos.py
│   ├── publisher_qos.py
│   ├── subscriber_multitopic.py
│   ├── publisher_multitopic.py
│   ├── subscriber_wildcard_plus.py
│   ├── publisher_wildcard_plus.py
│   ├── subscriber_wildcard_hash.py
│   └── publisher_wildcard_hash.py
├── screenshot/              # Dokumentasi visual
├── gambar/                  # Asset gambar
├── README.md               # File ini
└── requirements.txt        # Dependency list
```

---

## 🚀 Quick Start

### 1️⃣ Instalasi Dependencies

```bash
# Install MQTT Library
pip install paho-mqtt

# Atau menggunakan requirements.txt (jika ada)
pip install -r requirements.txt
```

**Prasyarat:** Pastikan Mosquitto Broker sudah terinstall dan berjalan di sistem Anda.

---

## 📚 Skenario & Cara Menjalankan

### Skenario 1: Basic Publisher-Subscriber
Implementasi dasar komunikasi MQTT dengan satu publisher dan satu subscriber.

```bash
# Terminal 1 - Subscriber
python code/subscriber_basic.py

# Terminal 2 - Publisher
python code/publisher_basic.py
```

---

### Skenario 2: QoS (Quality of Service)
Pengujian berbagai level QoS untuk memastikan delivery pesan.

```bash
# Terminal 1 - Subscriber
python code/subscriber_qos.py

# Terminal 2 - Publisher
python code/publisher_qos.py
```

---

### Skenario 3: Multi Topic
Publisher dan subscriber berkomunikasi melalui multiple topics.

```bash
# Terminal 1 - Subscriber
python code/subscriber_multitopic.py

# Terminal 2 - Publisher
python code/publisher_multitopic.py
```

---

### Skenario 4: Wildcard (+)
Menggunakan wildcard `+` untuk subscribe ke single-level topics.

```bash
# Terminal 1 - Subscriber
python code/subscriber_wildcard_plus.py

# Terminal 2 - Publisher
python code/publisher_wildcard_plus.py
```

---

### Skenario 5: Wildcard (#)
Menggunakan wildcard `#` untuk subscribe ke multi-level topics.

```bash
# Terminal 1 - Subscriber
python code/subscriber_wildcard_hash.py

# Terminal 2 - Publisher
python code/publisher_wildcard_hash.py
```

---

## 💡 Tips Menjalankan

- **Buka minimal 2 terminal** untuk menjalankan subscriber dan publisher secara bersamaan
- **Jalankan subscriber terlebih dahulu** sebelum publisher agar tidak kehilangan pesan
- **Monitor output** untuk melihat proses publish-subscribe terjadi
- Gunakan `Ctrl+C` untuk menghentikan program

---

## 📊 Konsep MQTT yang Diimplementasikan

- ✅ **Publish-Subscribe Pattern** - Decoupled communication
- ✅ **QoS Levels** - Quality of Service (0, 1, 2)
- ✅ **Topic Hierarchies** - Organized message routing
- ✅ **Wildcards** - Flexible topic subscription
- ✅ **Real-time Communication** - Live data streaming

---

## 👤 Author

**Nabilla Suci Amanda**  
NIM: 235150301111044

---

## 📝 License

Proyekini dibuat untuk keperluan akademis - Cyber Physical System (CPS)

---

**Last Updated:** 2026  
*Smart Room Monitoring System via MQTT*
