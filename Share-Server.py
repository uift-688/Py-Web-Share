import asyncio
import websockets
import os

async def send_file(websocket, path):
    file_path = 'path/to/your/file'  # 送信するファイルのパス
    file_size = os.path.getsize(file_path)
    chunk_size = 1024 * 1024  # 1MB のチャンクサイズ
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            await websocket.send(chunk)

    print(f"Sent file: {file_path}")

async def main():
    async with websockets.serve(send_file, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # サーバーを永遠に実行する

if __name__ == "__main__":
    asyncio.run(main())
