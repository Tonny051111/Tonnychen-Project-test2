from tkinter import *
import tkinter.messagebox as tm
import random
def play():
    a=random.randint(2,99)
    start,end=1,100
    for j in range(100):
        try:
            root=Tk()
            root.title("猜数字-数字炸弹")
            Label(root,text="请输入%d到%d之间的整数："%(start,end),font=("Arial",35)).grid(row=0,column=0)
            num=Entry(root,width=20)
            num.grid(row=0,column=1)
            Button(root,text="Yes",command=root.quit,font=("Arial",30)).grid(row=1,column=1)
            root.mainloop()
            b=int(num.get())
            if b==a:
                tm.showinfo("提示","恭喜您猜中了")
                break
            elif b<start or b>end:
                tm.showinfo("提示","对不起，不能输入边界外的值，请重新输入。")
            elif b==start or b==end:
                tm.showinfo("提示","对不起，不能输入边界上的值，请重新输入。")
            elif b>a:
                end=b
                root.quit()
            else:
                start=b
                root.quit()
        except:
            tm.showinfo("提示","您输入的不是整数，请重新输入！")
if __name__=='__main__':
    play()
