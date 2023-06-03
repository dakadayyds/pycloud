import requests
import ast
import os

def connecttxt(l,m):
    con=open(l,m,encoding="UTF-8")
    return con

def make_res(name=None,cmd=None,data=None):
	p = {}
	p["cmd"] = cmd
	p["name"] = name
	p["data"] = data
	f = requests.post("https://dakada.pythonanywhere.com/pycloud", data=p)
	return f.json()

class cloud():
    def __init__(self,name=None,data=None):
        self.name=name
        self.data=data
    def cload(self):
        res = make_res(self.name,"load",None)
        return (res["type"],res["msg"])
    def csave(self):
        res = make_res(self.name,"load",None)
        return (res["type"],res["msg"])
    def cadd(self):
        res = make_res(self.name,"load",None)
        return (res["type"],res["msg"])

class local():
    def __init__(self,name=None,data=None,cmd=None):
        self.name=name
        self.data=data
        self.cmd=cmd
    def pycloud(self):
        try:
            global json1
            name=self.name
            cmd=self.cmd
            data2=self.data
            f=connecttxt("data.json","r")
            if cmd=="add":
                f=connecttxt("data.json","a+")
                f.seek(0, 0)
                list1=f.readlines()
                for json2 in list1:
                    json1=ast.literal_eval(json2.split("\n")[0])
                    if json1.get("name")==name:
                        return ("err","空间名已存在")
                json3={"name":name,"data":data2}
                if os.path.getsize("data.json"):
                    f.write('\n')
                f.write(str(json3))
                f.close()
                return ("su","创建成功！")
            else:
                f=connecttxt("data.json","r")
                f.seek(0, 0)
                list1=f.readlines()
                find=0
                i=0
                for json2 in list1:
                    json1=ast.literal_eval(json2.split("\n")[0])
                    if json1.get("name")==name:
                        find=1
                        if cmd=="save":
                            list1[i]=str({"name":name,"data":data2})
                        break
                    i+=1
                f.close()
                if find==0:
                    return ("err","空间名不存在")
                if cmd=="load":
                    return {"type":"su","msg":json1.get("data")}
                elif cmd=="save":
                    f=connecttxt("data.json","w")
                    i=0
                    for str1 in list1:
                        if not i==0:
                            f.write('\n')
                        f.write(str1)
                        i+=1
                    return ("su","更新成功！")
                else:
                    return ("err","无效的指令")
            f.close()
        except Exception as e:
            return {"type":"pythonerr","msg":e}
    def get_all(self):
        f=connecttxt("data.json","r")
        return f.read()