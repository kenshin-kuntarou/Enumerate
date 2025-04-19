import argparse
import requests 
from concurrent.futures import ThreadPoolExecutor

class Enumeration:
    def __init__ (self, url_name, file_name):
        self.url = url_name
        self.file = file_name
        self.result = list()
        self.ascii_art = f"""
-----------------------------------------------------------------
 _______                                         __              
|    ___|.-----.--.--.--------.-----.----.---.-.|  |_.-----.----.
|    ___||     |  |  |        |  -__|   _|  _  ||   _|  _  |   _|
|_______||__|__|_____|__|__|__|_____|__| |___._||____|_____|__|  

------------------------------------------------------------------
| Url: {self.url} | File: {self.file}                            
------------------------------------------------------------------"""

    def file_reader(self):
        try:
            with open(self.file, encoding="utf-8", errors="ignore") as f:
                self.result = [line.strip() for line in f]

        except IndexError:
            print("| Não foi possível ler o arquivo ou ele não exisite.")

    def url_request(self, numerator):
        try: 
            request = requests.get(f"{self.url}/{numerator}")

            if request.status_code == 200:
                print(f"| {self.url}{numerator} - status: {request.status_code}")
            else:
                pass

        except ConnectionRefusedError:
            print("| Erro de conexão")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-url', type=str, required=True, help="The domain that will be listed")
    parser.add_argument('-file', type=str, required=True, help="The Wordlist that will be used")
    parser.add_argument('-threads', type=int, required=False, help="The number of threads used (default = 5)")

    args = parser.parse_args()
    
    enumerator = Enumeration(args.url, args.file) 
    print(enumerator.ascii_art)
    enumerator.file_reader()

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = executor.map(enumerator.url_request, enumerator.result)
    print("------------------------------------------------------------------")
