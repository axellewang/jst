import requests
import json

class fund_scripts:
    def batch(self,batchNo):
        header = {'cookie':'Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; SSO-AUTH-HEADER=LONG41ce88b83662462a8bbf2532dc97b7d6; td_cookie=18446744072504736465'}
        url = 'http://172.25.33.1:30531/resource/sum-no?batchNo=%s'%batchNo
        print(url)
        req = requests.get(url=url,headers=header)
        print(req.text)

    def store(self):
        header = {'cookie':'Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; SSO-AUTH-HEADER=LONG7096c0f13aa74bdca6198113af1b53d2; td_cookie=18446744071280889774'}
        url = 'http://172.25.33.1:30531/resource/sync-store'
        req = requests.get(url=url,headers=header)
        print(req.text)
    def download(self):
        url = 'http://weaward-uat.bestwehotel.com/store/asset/assets/download?batchNo=2020-03-29'
        header = {
            'cookie': 'Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; SSO-AUTH-HEADER=LONG7096c0f13aa74bdca6198113af1b53d2; td_cookie=18446744071280889774'}
        req = requests.post(url=url,headers=header)

    def search(self):
        url = 'http://weaward-uat.bestwehotel.com/store/asset/assets'
        header =  {'cookie': 'Hm_lvt_ebd658446a937c986befd8173e8285e5=1585301886,1585545182,1585548911,1585552265; SSO-AUTH-HEADER=LONG7a3209a9a60e467ca1882eb53cff561e; td_cookie=18446744071111108224; Hm_lpvt_ebd658446a937c986befd8173e8285e5=1585553003; STORE-PLAT-TOKEN=LONG7a3209a9a60e467ca1882eb53cff561e','Content-Type':'application/json;charset=UTF-8'}
        data = {'batchNo': "2020-03-21", "brandCodes": [], 'pageSize': 100, 'pageNum': 0}
        req = requests.post(url=url,headers = header,json= data)
        print(req.text)



if __name__ == '__main__':
  #  fund_scripts().batch('2020-03-30')
  #  fund_scripts().store()
    fund_scripts().download()
    #fund_scripts().search()