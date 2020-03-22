import requests

class HttpRequest:

    @staticmethod
    def http_request(url,data,method,header=None,cookie=None):
        try:
            if method.upper() == "GET":
                res = requests.get(url,data,headers=header,cookies=cookie)
            elif method.upper() == "POST":
                res = requests.post(url,data,headers=header,cookies=cookie)
            elif method.upper() == "PUT":
                res = requests.put(url,data,headers=header,cookies=cookie)
            else:
                print("请求方式错误，请检查！")
        except Exception as e:
            print("报错信息为：{0}".format(e))
            raise e
        return res