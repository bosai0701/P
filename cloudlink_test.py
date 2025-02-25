import asyncio
from cloudlink import CloudLink

async def main():
    cl = CloudLink()
    await cl.connect()  # Scratchのクラウド変数に接続
    print("Scratch に接続しました！")

    # クラウド変数 "shindo" を 5 に変更
    await cl.set_var("shindo", 5)
    print("☁ shindo を 5 に設定しました！")

    await asyncio.sleep(10)  # 10秒待機
    await cl.close()  # 接続を閉じる
    print("接続を終了しました")

asyncio.run(main())
