# 🎤 Voice Synthesis Project

Проект для синтеза речи с использованием модели fish-speech/xtts. Позволяет преобразовывать текст в речь с клонированием голоса.

## 🎧 Демонстрация

### Образец голоса
<audio src="./voice_samples/aliya.wav" controls></audio>

### Результат синтеза
<audio src="./output/output.wav" controls></audio>

## ✨ Особенности

- Клонирование голоса из WAV-файла
- Поддержка русского языка
- Высокое качество синтеза
- Простой API

## 🔧 Требования

- Ubuntu/Debian
- Python 3.11+
- Библиотека TTS
- Образец голоса (WAV, 16kHz, моно)
- Минимум 4GB RAM

## ⚙️ Установка

### Клонирование репозитория

1. Клонируйте проект:
    ```bash
    git clone git@github.com:marse11e/Voice-Synthesis.git
    cd Voice-Synthesis
    ```

### Обновление Python до версии 3.11

Если у вас установлена другая версия Python, выполните следующие шаги:

1. Деактивируйте текущее виртуальное окружение (если есть):
    ```bash
    deactivate
    ```

2. Добавьте репозиторий Python и обновите систему:
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    ```

3. Установите Python 3.11:
    ```bash
    sudo apt install python3.11 python3.11-venv
    ```

### Настройка проекта

1. Создайте новое виртуальное окружение:
    ```bash
    python3.11 -m venv new_venv
    ```

2. Активируйте окружение:
    ```bash
    source new_venv/bin/activate
    ```

3. Установите TTS:
    ```bash
    pip install TTS
    ```

## 📁 Структура проекта

```
Voice-Synthesis/
├── main.py              # Основной скрипт
├── voice_samples/       # Образцы голоса
│   └── aliya.wav       # Пример образца
└── output/             # Выходные файлы
    └── output.wav
```

## 🚀 Использование

1. Поместите WAV-файл с образцом голоса в `voice_samples/`

2. Запустите синтез:
    ```python
    text = "Ваш текст для синтеза"
    synthesize_speech(
        text=text,
        speaker_wav="voice_samples/your_sample.wav"
    )
    ```

3. Запустите скрипт:
    ```bash
    python main.py
    ```

## ❗ Устранение проблем

- **CUDA out of memory**: Уменьшите размер текста
- **Искажение голоса**: Проверьте частоту дискретизации (16kHz)
- **FileNotFoundError**: Проверьте пути к файлам

## 📞 Контакты

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/MarselleNaz)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/marselle.naz)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:marselle.naz@yandex.kz)

---
⭐️ Если проект оказался полезным, поставьте звездочку!