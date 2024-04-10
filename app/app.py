from fastapi import FastAPI, HTTPException
from fastapi.responses import Response  # Responseクラスをインポート
from models.request_models import SynthesizeRequest  # モデルのインポート
from fastapi.responses import StreamingResponse
from pydub import AudioSegment
import io
import httpx

app = FastAPI()

VOICEVOX_ENGINE_URL = "http://vsa-voicevox-engine:50021"

@app.post("/synthesize_to_mp3/")
async def synthesize_to_mp3(request: SynthesizeRequest):
    # VOICEVOXから音声データを取得
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{VOICEVOX_ENGINE_URL}/audio_query?text={request.text}&speaker={request.speaker}", json={})
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error from VOICEVOX Engine")
        query = response.json()
        synthesis_response = await client.post(f"{VOICEVOX_ENGINE_URL}/synthesis?speaker={request.speaker}", json=query)
        if synthesis_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error from VOICEVOX Engine")

    # 取得した音声データ（WAV）をMP3に変換
    audio_data = AudioSegment.from_file(io.BytesIO(synthesis_response.content), format="wav")
    mp3_buffer = io.BytesIO()
    audio_data.export(mp3_buffer, format="mp3")
    mp3_buffer.seek(0)  # ストリームを巻き戻す

    # MP3データをクライアントにストリーミング
    return StreamingResponse(mp3_buffer, media_type="audio/mpeg")