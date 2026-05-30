# 🏠 MQTT Smart Room Monitoring

> Implementasi sistem komunikasi MQTT untuk Smart Room Monitoring menggunakan Python dan Mosquitto Broker

## 📋 Deskripsi Singkat

Project ini merupakan implementasi komunikasi MQTT menggunakan **Python** dan **Mosquitto Broker** pada studi kasus Smart Room Monitoring. Sistem menggunakan pola komunikasi **publish-subscribe**, [...]

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

### 0️⃣ Install Mosquitto Broker

**Windows:**
1. Download dari: https://mosquitto.org/download/
2. Install dengan default settings
3. Mosquitto akan ter-install di `C:\Program Files\mosquitto\`

**macOS:**
```bash
brew install mosquitto
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install mosquitto
sudo systemctl start mosquitto
```

---

### 1️⃣ Instalasi Dependencies

```bash
# Install MQTT Library
pip install paho-mqtt

# Atau menggunakan requirements.txt
pip install -r requirements.txt
```

---

### 2️⃣ Jalankan Mosquitto Broker

**Windows (Command Prompt/PowerShell):**
```bash
mosquitto -v
```

Jika command tidak ditemukan, jalankan dari folder instalasi:
```bash
"C:\Program Files\mosquitto\mosquitto.exe"
```

**macOS/Linux:**
```bash
mosquitto -v
```

✅ Broker seharusnya running di port **1883** (localhost:1883)

---

## 📚 Skenario & Cara Menjalankan

> ⚠️ **PENTING:** Jalankan Mosquitto Broker terlebih dahulu (lihat step 2️⃣ di atas), kemudian buka **minimal 2 terminal baru** untuk subscriber dan publisher

### Skenario 1: Basic Publisher-Subscriber
Implementasi dasar komunikasi MQTT dengan satu publisher dan satu subscriber.

```bash
# Terminal 1 - Mosquitto Broker
mosquitto -v

# Terminal 2 - Subscriber
python code/subscriber_basic.py

# Terminal 3 - Publisher
python code/publisher_basic.py
```

---

### Skenario 2: QoS (Quality of Service)
Pengujian berbagai level QoS untuk memastikan delivery pesan.

```bash
# Terminal 1 - Mosquitto Broker
mosquitto -v

# Terminal 2 - Subscriber
python code/subscriber_qos.py

# Terminal 3 - Publisher
python code/publisher_qos.py
```

---

### Skenario 3: Multi Topic
Publisher dan subscriber berkomunikasi melalui multiple topics.

```bash
# Terminal 1 - Mosquitto Broker
mosquitto -v

# Terminal 2 - Subscriber
python code/subscriber_multitopic.py

# Terminal 3 - Publisher
python code/publisher_multitopic.py
```

---

### Skenario 4: Wildcard (+)
Menggunakan wildcard `+` untuk subscribe ke single-level topics.

```bash
# Terminal 1 - Mosquitto Broker
mosquitto -v

# Terminal 2 - Subscriber
python code/subscriber_wildcard_plus.py

# Terminal 3 - Publisher
python code/publisher_wildcard_plus.py
```

---

### Skenario 5: Wildcard (#)
Menggunakan wildcard `#` untuk subscribe ke multi-level topics.

```bash
# Terminal 1 - Mosquitto Broker
mosquitto -v

# Terminal 2 - Subscriber
python code/subscriber_wildcard_hash.py

# Terminal 3 - Publisher
python code/publisher_wildcard_hash.py
```

---

## 💡 Tips Menjalankan

- **Buka minimal 3 terminal** untuk menjalankan:
  1. Mosquitto Broker
  2. Subscriber
  3. Publisher
- **Jalankan Mosquitto Broker terlebih dahulu** 
- **Jalankan subscriber sebelum publisher** agar tidak kehilangan pesan
- **Monitor output** untuk melihat proses publish-subscribe terjadi
- Gunakan `Ctrl+C` untuk menghentikan program

---

## ⚠️ Troubleshooting

| Error | Penyebab | Solusi |
|-------|---------|--------|
| `Command 'mosquitto' not found` | Mosquitto belum di PATH | Tambah ke Environment Variables atau jalankan dari folder instalasi |
| `Connection refused [Errno 111]` | Mosquitto Broker tidak running | Buka terminal baru dan jalankan `mosquitto -v` |
| `ModuleNotFoundError: No module named 'paho'` | paho-mqtt belum diinstall | Jalankan `pip install paho-mqtt` |
| Subscriber tidak menerima pesan | Publisher berjalan sebelum subscriber | Jalankan subscriber dulu, tunggu sampai "Waiting for messages", baru jalankan publisher |

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

Project ini dibuat untuk keperluan akademis - Cyber Physical System (CPS)

---

**Last Updated:** 2026  
*Smart Room Monitoring System via MQTT*
