from TTS.api import TTS
import os

def synthesize_speech(text, speaker_wav="voice_samples/aliya.wav", output_file="output/output.wav"):
    try:
        print("Инициализация модели...")
        tts = TTS(model_name="fish-speech/xtts", progress_bar=False)
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        print("Генерация речи...")
        tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language="ru",
            file_path=output_file
        )
        
        print(f"Речь успешно сгенерирована и сохранена в {output_file}")
        
    except Exception as e:
        print(f"Ошибка при синтезе речи: {str(e)}")



text = "Привет Марсель, хочу поздравить тебя с новым годом, я тебя люблю."
synthesize_speech(text) # speaker_wav="voice_samples/aliya.wav"
