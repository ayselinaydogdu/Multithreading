
import threading
import requests 
import time
import os

def downloading_file(url, name):
    try:
        print("The file " , name, " is downloading.")
        response = requests.get(url)
        with open(name, 'wb') as f:
            f.write(response.content)
        
        print("The file " , name, " is downloaded.")
    except Exception as hata:
        print(f"{name} hatası: {str(hata)}")


if __name__ == "__main__":
    dosya_list = [
        ("https://aad216.a-cdn.akinoncloud.com/products/2024/10/07/11917890/2b454b9b-c291-4de6-9a0e-a04df0859128_size568x568_cropCenter.jpg", "futbol-topu.png"),
        ("https://narasport.com/image/cache/catalog/Helix/Icon/Voleybol%20İcon%202-1500x1500.jpg", "voleybol-topu.png"),
        ("https://minio.yalispor.com.tr/sneakscloud/blog/basketbol-topu-ozellikleri-01_6053563b5b58a.jpg", "basketbol-topu.png")
    ]

    threads = []
    start = time.time()

    for url, name in dosya_list:
        thread = threading.Thread(target=downloading_file, args=(url, name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    finish = time.time()
    total_time = finish-start
    print(f"Total time: {total_time:.2f} seconds")


