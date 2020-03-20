import requests

class HttpRequest:

    def http_request(self,url,data,http_method,header=None,cookie=None):

        try:
            if http_method.upper == "GET":
                res = requests.get(url,data,headers=header,cookies=cookie)
            elif http_method.upper == "POST":
                res = requests.post(url,data,headers=header,cookies=cookie)
            elif http_method.upper == "PUT":
                res = requests.put(url,data,headers=header,cookies=cookie)
            else:
                print("请求方式错误，请检查！")
        except Exception as e:
            print("报错信息为：{0}".format(e))
            raise e
        return res