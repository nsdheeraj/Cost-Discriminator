#from chatapp import aocd,Links 


def url_extract(s):
    print("hghghg")
    #input_data = json.loads(request.body.decode('utf-8'))
    #costD =aocd.AOCD(reqq)
    #print(costD,reqq)
    if '$' in s:
        d=dict()
        a = s.split('$')
        b=a[1]
        a[1]=b[1:] 
        d['text']=a[0]
        d['url']=a[1]
        return d
    else:
        c=dict()
        c['text']=s
        return c