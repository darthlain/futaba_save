from a_import import *

class Tsumanne:

    root = 'https://tsumanne.net'

    def __init__(self):
        self.session = requests.session()

    @staticmethod
    def tsuma_mid(url):
        if 'may' in url:
            return 'my'
        else:
            return 'si'

    # つまんね。に保存する
    def input(self, url):
    
        param = { 'url': url, 'sbmt': '追加' }
        
        a = self.session.post(self.root + f'/{self.tsuma_mid(url)}/input.php?format=json', param,
                allow_redirects = False)

        b = json.loads(a.text[a.text.index('{') - 1:])

        if not b['success']:
            for i in b['messages']:
                print(f'[つまんね。] {i}')
    
    # つまんね。に保存されていればブラウザで開く
    def exist(self, url):
        s = self.root + f'/{self.tsuma_mid(url)}/indexes.php'
    
        s += f'?w={url}&sbmt=URL&format=json'

        a = self.session.get(s, allow_redirects = False)

        if a.status_code == 200:
            j = a.json()

            if j['success']:
                s = self.root + j['path']
                webbrowser.open(s)
            else:
                for i in j['messages']:
                    print(f'[つまんね。] {i}')
        else:
            print(f'[つまんね。] Responce: {a.status_code}')

# 保存&開く
def ftbucket(url):
    a = f'https://dev2.ftbucket.info/scdev2/scrapshot.php?rooturl={url}'
    webbrowser.open(a)

def double(url):
    tsuma = Tsumanne()
    tsuma.input(url)
    time.sleep(1)
    tsuma.exist(url)

    time.sleep(1)
    ftbucket(url)

if __name__ == '__main__':
    double(sys.argv[1])
