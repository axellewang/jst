import requests


def currency_service():
    url = 'http://172.25.33.1:30519/currency-services/rest/currencyServices/enjoyCurrencyByOrderCode'
    header = {'Content-Type': 'application/json','X-AUTH-HEADER': 'A2CCDB0EAEC29EF89EBF2B0104F85458'}
    data = {
            "busType":0,
            "mebId":185382602,
            "remark":"创新中心储值联调测试扣款",
            "specRemark":"创新中心储值联调测试扣款",
            "oprtId":224466,
            "createAppId":1034,
            "orderCode":'185382603',
            "amount":0.02

            }
    res = requests.post(url=url,headers=header,data=data)
    print(res.text)

currency_service()