# voicebox-stackchan-api

voicebox を利用したスタックチャン用 api

## テスト方法

```
curl -X POST http://localhost:8000/synthesize_to_mp3/ -H "Content-Type: application/json" -d '{"text":"こんにちは、世界！", "speaker": 1}' --output response.mp3

```
