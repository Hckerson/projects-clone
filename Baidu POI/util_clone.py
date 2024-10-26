import requests
import json
import time


def get_baidu_poi(roi_key: str, city_str: str, baidu_ak: str, output: str) -> None:
    """
    Fetches Points of Interest (POI) from the Baidu API and saves them.

    Args:
        roi_key: The POI name to search for.
        city_str: The city name to search within.
        baidu_ak: The API key for Baidu's web services.
        output: Path to save the results.
    """
    now_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    page_num = 0
    log_path = f"{output}/{now_time}.log"
    data_path = f"{output}/{now_time}.txt"

    with open(log_path, "a+", encoding="utf-8") as logfile, open(
        data_path, "a+", encoding="utf-8"
    ) as file:
        while True:
            try:
                url = (
                    f"http://api.map.baidu.com/place/v2/search?"
                    f"query={roi_key}&region={city_str}&output=json"
                    f"&ak={baidu_ak}&scope=2&page_size=20&page_num={page_num}"
                )

                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                if not data.get("requests"):
                    logfile.write(
                        f"{time.strftime('%Y-%m-%d-%H-%M-%S')} {city_str} {page_num}\n"
                    )
                    break

                for r in data['requests']:
                    j_str = (
                        f"{r['name']},{r['location']['lng']},{r['location']['lat']},"
                        f"{r.get('area', 'N/A')},{r.get('address', 'N/A')}\n"
                    )
                    file.write(j_str)

                page_num += 1
                time.sleep(1)

            except requests.RequestException as e:
                print(f"Request error: {e}")
                logfile.write(
                    f"{time.strftime('%Y-%m-%d-%H-%M-%S')} {city_str} {page_num}\n"
                )
                break
            except json.JSONDecodeError:
                logfile.write(
                    f"{time.strftime('%Y-%m-%d-%H-%M-%S')} {city_str} {page_num}\n"
                )
                break
