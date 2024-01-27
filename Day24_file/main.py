# file = open("par.txt")  #  透過open function打開檔案，open會回傳資訊
# document = file.read()  #  利用read來讀取file裡面的訊息，並回傳字串
# 
# print(document)
# file.close()  #  每次檔案打開後，都需要手動關閉他，否則會吃CPU的效能

#  可以用另一種打開的方法，不用每次都手動關閉

# with open("par.txt") as file:  #  用with來打開檔案，並將其命名為file
#     document = file.read()
#     print(document)

with open("par.txt", mode="a") as file:  #  mode為a的話，表示append，把寫的內容加到後面
    file.write("\ngood")  #  如果想要寫東西進去檔案，可以用write，但要注意的是：在open的mode要讓它變成w，才可以覆寫

#  如果你打開的檔案不存在，可以用write來打開新的檔案，但mode要為"w"