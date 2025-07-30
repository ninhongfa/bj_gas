import asyncio
from aiohttp import ClientSession
from gas import GASData

async def main():
    token = "6da103ab-1f27-4823-94a8-2dbb51038b21"          # 你必须从 configuration.yaml 中拿这个
    user_code ="95566151083" # 一般是燃气账户

    async with ClientSession() as session:
        gas = GASData(session, token, user_code)
        data = await gas.async_get_data()
        print("获取成功:", data)
        try:
            data = await gas.async_get_data()
            print("获取成功:", data)
        except Exception as e:
            print("获取失败:", repr(e))

if __name__ == "__main__":
    asyncio.run(main())
