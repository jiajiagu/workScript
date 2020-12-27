import json
import asyncio
import requests_async as requests

# requests.packages.urllib3.disable_warnings()

host = "https://xxx.com"
token = 'xxx'
headers = {
    'Host': 'xxx',
    'accesstoken': token,
    'Content-Type': 'application/json'
}

async def gerOrder(orderNumber: str):
    orderUrl = host + "/xxx/api/v2/xxx?order_search_number=" + orderNumber + "&xxx=1"

    # 获取amount_cents、item_unit_id
    orderResponse = await requests.get(url=orderUrl, headers=headers, verify=False)

    if orderResponse.status_code == 200:
        print(orderNumber + "获取amount_cents、item_unit_id成功")
    else:
        print(orderNumber + "获取amount_cents、item_unit_id失败: " + orderResponse.txt)

    id = json.loads(orderResponse.text)['item_units'][0]['id']
    amount_cents = json.loads(orderResponse.text)['item_units'][0]['amount_cents']

    return {'id': id, 'amount_cents': amount_cents}


async def getRefund(id: str, amount_cents: str, orderNumber: str):
    refundsUrl = host + "/xxx/api/v2/order_refunds"
    refundable_item_units = [{
        "xxx_amount_cents": amount_cents,
        "item_unit_id": id
    }]

    payload = {
        "refundable_item_units": refundable_item_units,
        "reason": "test",
        "payment_mode": 9,
        "refund_mode": 1,
        "xxx_amount_cents": 1
    }
    # 函数是将一个Python数据类型列表进行json格式的编码
    payload_json = json.dumps(payload, ensure_ascii=False)
    refundsResponse = await requests.request("POST", refundsUrl, headers=headers, data=payload_json, verify=False)

    if refundsResponse.status_code == 200:
        print(orderNumber + "申请退款状态成功")
    else:
        print(orderNumber + "申请退款状态失败:" + refundsResponse.text)


async def main():
    file = open("./orderNumberList", 'r', encoding='UTF-8')
    orderNumberList = []
    for line in file:
        # 将空格作为分隔符将一个字符切割成一个字符数组
        orderNumberList.extend([str(i) for i in line.split()])
    file.close()

    for orderNumber in orderNumberList:
        refunds = await gerOrder(orderNumber)
        await getRefund(refunds['id'], refunds['amount_cents'], orderNumber)


asyncio.run(main())
