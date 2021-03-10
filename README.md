# hw1
目的: 找出 staion_id C0A880, C0F9A0, C0G640, C0R190, C0X260 的最高氣溫

# part1
先把 csv檔 import進來到python3

# part2
打開 <107061122.csv> 將資料存入mycsv，然後再以 for 迴圈，把 mycsv的數據以 append的方式丟入 list型態的data

# part3
以下以 station_id :'C0X260' 為例，其餘 C0A880, C0F9A0, C0G640, C0R190皆是仿此方法:
1.外層的 filter()函式 呼叫data，過濾掉data裡面 station_id 不是C0X260的資料，並將是 'C0X260' 的資料返回名叫first_data的list；
而在filter內層的 lambda 作為一個表示式，則是表達我們的 filter只要station_id 是'C0X260'的資料。
2.接著用len()函式，計算first_data的長度，並把這一結果指定給變數length1。
3.再然後，我用for迴圈將first_data裡面跟'TEMP'有關的數據以append的方式，傳入data1這個list。
4.最後用sorted()函示，把data1裡的資料，由大到小扔入我的新list data1_1。

# part4
因為 data1_1已經是被sorted()函式以由大到小的方式排列，所以我們只要將station_id: 'C0X260'和data1_1的第一筆資料print出來，就可以得到該站的最高氣溫了!
station_id C0A880, C0F9A0, C0G640, C0R190採取同樣的方法，得出以下各站的最高氣溫:
C0A880: 17.100
C0F9A0: 24.800
C0G640: 22.100
C0R190: 27.200
C0X260: 24.700
