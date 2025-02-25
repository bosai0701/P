import asyncio
from cloudlink import CloudLink

async def main():
    cl = CloudLink()
    await cl.connect()  # Scratchのクラウドサーバーに接続
    print("接続しました！")

    # クラウド変数 "score" を100に設定
    await cl.set_var("score", 100)
    print("☁ score を 100 に設定しました！")

    await asyncio.sleep(10)  # 10秒待つ
    await cl.close()  # 接続を閉じる
    print("接続を終了しました")

asyncio.run(main())
