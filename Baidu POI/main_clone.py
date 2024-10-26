import os
from util_clone import get_baidu_poi
import argparse

def run(args:argparse.Namespace) -> None:
    baidu_web_ak = args.ak
    city_str = args.city
    roi_key = args.poi
    output = args.save

    os.makedirs(output, exist_ok=True)
    get_baidu_poi(roi_key, city_str, baidu_web_ak, output)
    print("Current area completed.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="input parameters")
    parser.add_argument("--ak", type=str, required=True, help="Baidu web AK")
    parser.add_argument('--city', type=str, required=True, help="city, name")
    parser.add_argument("--poi", type=str, required=True, help="POI key")
    parser.add_argument("--save", type=str, default="output", help="Save path")
    
    args = parser.parse_args()
    run(args)
