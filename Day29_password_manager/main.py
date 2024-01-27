import json
from tkinter import *
#  messagebox不是class, constant，所以用*沒辦法import
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]


    random.shuffle(password_list)

    # 利用join()來達到下面的目的，讓list變成字串
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_input.insert(END, password)
    #  當密碼一產生時，就會自動複製
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():
    website = website_input.get()
    email = email_input.get()
    pas = password_input.get()
    # store_info = f"{website} | {email} | {pas}"
    # data_file = open("data.txt", "a")
    # data_file.write(f"{store_info}\n")
    # data_file.close()
    new_data = {
        website: {
            "email": email,
            "password": pas,
        }
    }

    #  使用者不能沒有輸入，就按Add按鈕
    if website == "" or len(pas) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        #  跳出popup，讓使用者知道自己輸入的資訊
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
        #                                                   f"Email: {email} \nPassword: {pas} \n"
        #                                                   f"Is it ok to save?")
        #  如果回傳的是True
        # if is_ok:
        # with open("data.txt", "a") as data_file:
        #     data_file.write(f"{store_info}\n")
        try:
            with open("data.json", "r") as data_file:
                #  Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                #  可以寫入資訊到file裡，將new_data的資訊存到data_file裡
                json.dump(new_data, data_file, indent=4)
        else:
            #  Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #  Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            #  不管如何都要執行的
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')

# ---------------------------- SEARCH SETUP ------------------------------- #
def find_password():
    website = website_input.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in the website!")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
                print(data)
        except FileNotFoundError:
            messagebox.showinfo(title="Alert", message="No Data File Found, please build up first")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \n"
                                                                      f"Password: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Alert", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=300, height=300, pady=50, padx=50, bg="white")

#  建立畫布，讓img可以放上去
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
keeper = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=keeper)
canvas.grid(row=0, column=1)

#  建立Label
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

#  建立輸入
website_input = Entry(width=20)
website_input.grid(row=1, column=1)
#  讓鼠標一開始就在這個Entry裡，讓使用者可以直接輸入
website_input.focus()

#  建立Search Button
search_button = Button(text="Search", width=15, bg="white", command=find_password)
search_button.grid(row=1, column=2)

#  建立Email label
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

#  建立email input
email_input = Entry(width=36)
email_input.grid(row=2, column=1, columnspan=2)
#  0跟END的差別在於，0將鼠標放在第一個字元，而END是放在原本預設文字後面
email_input.insert(END, "lavouver96@gmail.com")

#  建立Password label
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

#  Create password input
password_input = Entry(width=20)
password_input.grid(row=3, column=1)

#  Create generate password button
password_button = Button(text="Generate Password", bg="white", width=15, command=password_generator)
password_button.grid(row=3, column=2)

#  Create Add button
add_button = Button(text="Add", width=36, bg="white", command=store_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()