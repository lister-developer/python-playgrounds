import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 定义URL模板
url_template = "https://www.example.com/city?page={}"

# 初始化空列表来存储数据
data = []

# 遍历多个城市和页面
cities = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
for city in cities:
    for page in range(1, 6):  # 假设每个城市有5页数据
        url = url_template.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 假设每个房产条目的HTML结构如下：
        # <div class="property">
        #     <span class="city">CityName</span>
        #     <span class="sales">SalesNumber</span>
        #     <span class="inventory">InventoryNumber</span>
        #     <span class="price">PriceNumber</span>
        # </div>
        
        properties = soup.find_all('div', class_='property')
        
        for prop in properties:
            city = prop.find('span', class_='city').text
            sales = int(prop.find('span', class_='sales').text)
            inventory = int(prop.find('span', class_='inventory').text)
            price = float(prop.find('span', class_='price').text)
            
            data.append({
                'city': city,
                'sales': sales,
                'inventory': inventory,
                'price': price
            })
        
        # 等待一段时间以避免过于频繁的请求
        time.sleep(1)

# 转换为DataFrame
df = pd.DataFrame(data)

# 保存为CSV文件
df.to_csv('real_estate_data.csv', index=False)

print("Data has been saved to real_estate_data.csv")
