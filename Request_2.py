import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.URL = 'https://cloud-api.yandex.net:443/'
        self.headers = {
            'accept': 'application/json',
            'Authorization': f'OAuth {token}',
        }

    def upload(self, file_path: str):
        url_downloads = requests.get(self.URL + 'v1/disk/resources/upload', params={'path': file_path}, headers=self.headers).json()['href']
        requests.put(url_downloads, headers=self.headers, files={'file': open(file_path, 'rb')})
        print("Файл загружен")


if __name__ == '__main__':
    uploader = YaUploader()
    result = uploader.upload()
