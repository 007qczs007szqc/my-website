'''我的主页'''
import streamlit as st
from PIL import Image
import base64
import time
page = st.sidebar.radio('💡友情导航', ['主页', '图片处理 Tools','飞花令游戏','计算器','MarkLatex编辑器','排序简介','留言板'])

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('mybg1.jpg')

def img_cg(img1,r_,g_,b_):
    w,h = img1.size
    imga = img1.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][r_]
            g = imga[x,y][g_]
            b = imga[x,y][b_]
            imga[x,y] = (r,g,b)
            
    return img1

def img_rm(img):
    w,h = img.size
    img.save("tp.png")
    img = Image.open("tp.png")
    imga = img.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][0]
            g = imga[x,y][1]
            b = imga[x,y][2]
            if(r >= 230 and g >= 230 and b >= 230):
                imga[x,y] = (0,0,0,255)
            
    return img

def img_rt(img):
    r = st.slider('旋转角度:', 0, 360, 180)
    img = img.rotate(r,expand = True)
    return img

def img_rs(img):
    h = st.number_input("图片高度:",min_value = 1)
    w = st.number_input("图片宽度:",min_value = 1)
    img = img.resize((w,h))
    return img

def img_cp(img):
    ex = st.number_input("裁剪终点X坐标:",min_value = 1)
    ey = st.number_input("裁剪终点Y坐标:",min_value = 1)
    sx = st.number_input("裁剪起点X坐标:",min_value = 0,max_value = ex-1)
    sy = st.number_input("裁剪起点Y坐标:",min_value = 0,max_value = ey-1)
    img = img.crop((sx,sy,ex,ey))
    return img

def img_cc(img1):
    w,h = img1.size
    imga = img1.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][0]
            g = imga[x,y][1]
            b = imga[x,y][2]
            imga[x,y] = (255-r,255-g,255-b)
            
    return img1

def img_a(img):
    w,h = img.size
    a = st.slider('透明度:', 1, 255, 100)
    img = img.convert("RGBA")
    imga = img.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][0]
            g = imga[x,y][1]
            b = imga[x,y][2]
            imga[x,y] = (r,g,b,a)
            
    return img

#视频
#def show_vedio(v):
#    if v != "":
#        with open(f"vedios/{v}.mp4","rb") as f:
#            mymp4 = f.read()
#        st.video(mymp4)

#音乐
#with open("sounds/bgm.mp3","rb") as f:
#        mymp3 = f.read()
#    st.audio(mymp3,format = "audio/mp3",start_time = 0)

def temp(word):
    with open("temp.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    words_list = set(words_list)
    words_list = list(words_list)
    if(" " not in word and word != ""):
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        for i in words_list:
            if word in i:
                st.write(i)

op = []
num = []

def cal():
    ch = op[-1];
    op.pop(-1);
    r = num[-1];
    num.pop(-1);
    l = num[-1];
    num.pop(-1);
    if(ch=='+'):num.append(l+r);
    elif(ch=='-'):num.append(l-r);
    else:num.append(l*r);

def cal_expr(expr):
    now = 0;
    s = " ("+expr+")";
    length = len(s)-1;
    i = 1
    while(i<=length):
        if(s[i]==' '):
            i+=1
            continue
        if(str.isdigit(s[i])):
            now = 0
            while(str.isdigit(s[i])):
                now = now*10+int(s[i])
                i+=1
            num.append(now)
            i-=1
        else:
            if(s[i]=='-' and s[i-1]=='('):num.append(0);
            if(s[i]=='(' or len(op)==0):op.append(s[i]);
            elif(s[i]==')'):
                while(op[-1]!='('):cal()
                op.pop(-1)
            elif(s[i]=='*'):
                while(op[-1]=='*'):cal()
                op.append(s[i])
            else:
                while(op[-1]!='(' and len(op)>0):cal();
                op.append(s[i])
        i+=1
    return num[-1]

def page_1():
    st.title("qczs007的主页")
    st.image("img1.gif")
    t1,t2 = st.tabs(["首页","飞花令"])
    with t1:
        st.write("<span style='font-size:30px; color:blue'>:sunglasses: 欢迎来到qczs007的网站！", unsafe_allow_html=True)
        st.link_button('前往作者洛谷主页',"https://www.luogu.com.cn/user/1649274")
        st.link_button('前往qczs007 2222团队',"https://www.luogu.com.cn/team/106697")
        st.write("<span style='font-size:20px; color:Blue'>:heart_eyes: 图片处理Tools：", unsafe_allow_html=True)
        st.write("在线图片处理工具，可免费处理并下载！（如抠图、反色、旋转等）")
        st.write("<span style='font-size:20px; color:Blue'>:heart_eyes: 有趣的飞花令：", unsafe_allow_html=True)
        st.write("左侧导航下有飞花令游戏，现在可以之间点击上方Tabs栏试玩！")
        st.write("<span style='font-size:20px; color:Blue'>:heart_eyes: 多功能计算器：", unsafe_allow_html=True)
        st.write("不仅可以进行不同计算，还能计算进制转换和计算表达式！")
        st.write("<span style='font-size:20px; color:Blue'>:heart_eyes: MarkLatex编辑器：", unsafe_allow_html=True)
        st.write("本编辑器结合了Markdown和Latex的效果，输入后点一下旁边空白处，下方会出现Markdown+Latex对应的内容。")
    with t2:
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:飞花令小游戏", unsafe_allow_html=True)
        a1,a2,a3 = False, False, False
        q1,q2,q3 = False, False, False
        st.image("img3.gif")
        c0,c1,c2,c3,c4 = st.columns([0.8,1,1,1,2.2])
        with c1:
            a1 = st.button("花")
        with c2:
            a2 = st.button("月")
        with c3:
            a3 = st.button("春")
        if(q1 != a1):
            q1 = a1
            a2,a3 = False, False
            q2,q3 = False, False
        if(q2 != a2):
            q2 = a2
            a1,a3 = False, False
            q1,q3 = False, False
        if(q3 != a3):
            q3 = a3
            a2,a1 = False, False
            q2,q1 = False, False
        if a1:
            st.write("")
            st.write("飞花之字:花")
            st.write("")
            temp("花")
            st.snow()
        if a2:
            st.write("")
            st.write("飞花之字:月")
            st.write("")
            temp("月")
            st.balloons()
        if a3:
            st.write("")
            st.write("飞花之字:春")
            st.write("")
            temp("春")

def page_2():
    st.title("图片处理 Tools")
    st.image("img2.gif")
    st.write("<span style='font-size:30px; color:blue'>:smile:图片处理小程序:smile:</span>", unsafe_allow_html=True)
    up_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if up_file:
        fn = up_file.name
        ft = up_file.type
        img = Image.open(up_file)
        fs = img.size
        st.write(f"图片宽度：{fs[0]}")
        st.write(f"图片高度：{fs[1]}")
        t1,t2,t3,t4,t5,t6,t7,t8 = st.tabs(["原图","改色","抠图","旋转","缩放","裁剪","反色","透明度"])
        si = 0
        new_img = img
        with t1:
            st.image(img)
            new_img = img
            si = new_img
            n1 = st.columns(1)
            if(n1):
                b1 = st.button("下载原图")
            if(b1):
                new_img.save(r"C:\Users\86158\Downloads\Original_img.png")
        with t2:
            img1 = img
            new_img = img_cg(img1,1,2,0)
            si = new_img
            st.image(new_img)
            n2 = st.columns(2)
            if(n2):
                b2 = st.button("下载改色")
            if(b2):
                new_img.save(r"C:\Users\86158\Downloads\Recoloring_img.png")
        img = Image.open(up_file)
        with t3:
            new_img = img_rm(img)
            si = new_img
            st.image(new_img)
            n3 = st.columns(3)
            if(n3):
                b3 = st.button("下载抠图")
            if(b3):
                new_img.save(r"C:\Users\86158\Downloads\Cutout_img.png")
        img = Image.open(up_file)
        with t4:
            new_img = img_rt(img)
            si = new_img
            st.image(new_img)
            n4 = st.columns(4)
            if(n4):
                b4 = st.button("下载旋转")
            if(b4):
                new_img.save(r"C:\Users\86158\Downloads\Rotation_img.png")
        img = Image.open(up_file)
        with t5:
            new_img = img_rs(img)
            si = new_img
            st.image(new_img)
            n5 = st.columns(5)
            if(n5):
                b5 = st.button("下载缩放")
            if(b5):
                new_img.save(r"C:\Users\86158\Downloads\Zoom_img.png")
        img = Image.open(up_file)
        with t6:
            new_img = img_cp(img)
            si = new_img
            st.image(new_img)
            n6 = st.columns(6)
            if(n6):
                b6 = st.button("下载裁剪")
            if(b6):
                new_img.save(r"C:\Users\86158\Downloads\Cropping_img.png")
        img = Image.open(up_file)
        with t7:
            new_img = img_cc(img)
            si = new_img
            st.image(new_img)
            n7 = st.columns(7)
            if(n7):
                b7 = st.button("下载反色")
            if(b7):
                new_img.save(r"C:\Users\86158\Downloads\Negative_img.png")
        img = Image.open(up_file)
        with t8:
            new_img = img_a(img)
            si = new_img
            st.image(new_img)
            n8 = st.columns(8)
            if(n8):
                b8 = st.button("下载透明度")
            if(b8):
                new_img.save(r"C:\Users\86158\Downloads\Transparency‌_img.png")

def page_3():
    st.title("飞花令游戏")
    st.image("img3.gif")
    
    st.write(":smile:我可是很强的，快来给我出题吧~")
    word = st.text_input('请输入要飞花的字（只能输入一个字）')
    if(len(word)>1):
        st.write("不可以问多个字哦！")
    else:
        temp(word)

def page_4():
    st.title("计算器")
    st.image("img4.gif")
    t1,t2,t3 = st.tabs(["普通计算","进制转换","表达式计算"])
    with t1:
        num1 = st.number_input("输入第一个数字",value = 0.000)
        num2 = st.number_input("输入第二个数字",value = 0.000)
        f = st.selectbox("运算符", ["+","-","*","/","%"])
        if(st.button("运算")):
            if f == "+":
                res = num1+num2
            if f == "-":
                res = num1-num2
            if f == "*":
                res = num1*num2
            if f == "/":
                res = num1/num2
            if f == "%":
                res = num1%num2
            st.write(f"<span style='font-size:30px; color:blue'>{num1}{f}{num2}={res}</span>",unsafe_allow_html=True)
    with t2:
        mode = int(st.selectbox("模式选择",["1.  10进制转2进制","2.  10进制转8进制","3.  10进制转16进制"])[0])
        num = st.number_input("输入数字",value = 1)
        ans = 0
        if mode == 1:
            ans = bin(num)[2:]
        if mode == 2:
            ans = oct(num)[2:]
        if mode == 3:
            ans = hex(num)[2:]
        st.write(f"<span style='font-size:30px; color:blue'>{ans}</span>",unsafe_allow_html=True)
    with t3:
        st.write("输入必须只包含+ - * 和括号，暂时不支持除法。可以输入负数，但输入时需要用括号包裹。")
        exp = st.text_input("输入第一个表达式")
        if(st.button("计算")):
            try:
                if('/' in exp):
                    n = 1/0
                st.write(f"<span style='font-size:30px; color:blue'>{cal_expr(exp)}</span>",unsafe_allow_html=True)
            except:
                st.write("输入算式不合法！")

qczs007team_rules = """# qczs007 2222 团队规则（必读）

1. 遵守法律与相关法规：一切违反法律法规的行为在都是绝对禁止的。

- 违反本条规则直接踢团

2. 尊重他人，待人友善：友善的氛围是qczs007 2222维持活力与亲和力的重要因素。

- 违反本条规则，每违反一次扣除 $100$S值，违反 $\geqslant 3$ 次直接踢团

3. 遵守学术诚信：对于构建一个良好的学术交流氛围，起着至关重要的作用。

- 不允许赛中作弊，发现第一次关入米奇妙妙屋并获得 `LZ` 称号 $30$ 天，第二次直接踢团
    
- 不允许恶意使用 AI 或大模型刷题，发现关入米奇妙妙屋并获得 `LZ` 称号 $5\sim 20$ 天，情节严重直接踢团
    
- 如果是真的不会，需要AI来研究代码或提交，请在代码最后一行标注 ```//AIGC for learning use```，这种情况我们会取消比赛成绩但不做出惩罚

4. 在此团队不能乱调自己/别人的的身份（除团主同意）。

- 发现撤销管理员，情节严重直接踢团

5. 在此团队不能乱改团队公告（非让勿动）。

6. 管理员需要维护好团队，禁止滥用职权。

7. 若发现违反规则屡教不改的成员可以向团队管理员汇报。

8. 所有管理员须要听团主的要求，谢谢。不要私自删改东西，可以**为团队提供**题目、题单。

- 有一定贡献可以减免其他惩罚

9. 本团可以贴广告，不限制次数，但不可随意刷屏。

- 刷屏严重的撤销管理员+米奇妙妙屋

10. 团队比赛题目代码，和推荐的题目，应发到 qczs 工作室中。

11. 不可抄袭代码题解，发送到月赛或其他比赛上，请坚守你的**学术诚信**。

12. **严禁骂人/说脏话**

- 恶劣直接踢团

13. 严禁上传/发送涉政（如纳粹相关）或淫秽擦边的信息，否则将会删除并**永久踢团**。

注意：若被封号无论封多久都直接踢除！

## 希望大家遵守团队规则！
"""

def page_5():
    st.title("MarkLatex编辑器")
    st.image("img5.gif")
    template = int(st.selectbox("模板选择",["1.  空白","2.  二次公式","3.  qczs007团队规则","4.  P4005 小 Y 和地铁"])[0])
    mode = ""
    if(template==1):
        mode = ""
    elif(template==2):
        mode = "$x = \\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$是方程式$ax^2+bx+c=0$的根。"
    elif(template==3):
        mode = qczs007team_rules
    else:
        mode = """# P4005 小 Y 和地铁

## 题目描述

小 Y 是一个爱好旅行的 OIer。一天，她来到了一个新的城市。由于不熟悉那里的交通系统，她选择了坐地铁。

她发现每条地铁线路可以看成平面上的一条曲线，不同线路的交点处一定会设有换乘站 。通过调查得知，没有线路是环线，也没有线路与自身相交。任意两条不同的线路只会在若干个点上相交，没有重合的部分，且没有三线共点的情况。即，如图所示的情况都是不存在的：

 ![](https://cdn.luogu.com.cn/upload/pic/12055.png) 

小 Y 坐着地铁 $0$ 号线，路上依次经过了 $n$ 个换乘站。她记下了每个换乘站可以换乘的线路编号，发现每条线路与她所乘坐的线路最多只有 $2$ 个换乘站。现在小 Y 想知道，除掉她经过的换乘站以外，这个城市里最少有几个换乘站。只有你告诉她正确的答案，她才会答应下次带你去玩呢。

## 输入格式

**请注意本题有多组输入数据。**

输入数据的第一行是一个整数 $T$，表示输入数据的组数。接下来依次给出每组数据。

对于每组数据，第一行是一个整数 $n$，表示小 Y 经过的换乘站的数目。第二行为 $n$ 个用空格隔开的整数，依次表示每个换乘站的可以换乘的线路编号。这些编号都在 $1\sim n$ 之内。

## 输出格式

对于每组输入数据，输出一行一个整数，表示除掉这 $n$ 个换乘站之外，最少有几个换乘站。

## 输入输出样例 #1

### 输入 #1

```
4 4
1 2 1 2
8
1 2 3 4 1 2 3 4
5
5 4 3 3 5
8
1 2 3 4 1 3 2 4
```

### 输出 #1

```
0 
0 
0 
1
```

## 说明/提示

【样例 1 解释】

对于样例的前两组数据，一种可能的最优答案如下图所示。

 ![](https://cdn.luogu.com.cn/upload/pic/12053.png) 

【子任务】

一共有 $50$ 个测试点，每个测试点 $2$ 分。你只有在答案完全正确时才能得到该测试点的全部分数，否则不得分。

对于所有测试点，以及对于样例， $1 \leq T \leq 100$, $1 \leq n \leq 44$。对于每个测试点， $n$ 的范围如下表：

![](https://cdn.luogu.com.cn/upload/pic/12054.png)
"""
    content = st.text_area("",mode,700,8000)
    st.markdown(content)

def page_6():
    st.title("排序简介")
    st.image("img6.gif")
    st.markdown("""
| 排序名称 | 排序方式(核心) | 时间复杂度 | 空间复杂度 | 综合评价 | 稳定性 |
| :----------: | :----------: | :----------: | :----------: | :----------: | :----------: |
| 冒泡排序 | `if a[i]>a[j]swap(a[i],a[j]);` | $O(n^2)$ | $O(n)$ | 初学者专用 | 稳定 |
| 选择排序 | `get max;swap(a[nmax],a[n-i]);` | $O(n^2)$ | $O(n)$ | 稳定在$O(n^2)$的时间复杂度 | 不稳定 |
| 快速排序 | `sort();` | $O(n\; log \;n)$（最坏$O(n^2)$） | $O(n)$ | 直接上sort！ | 不稳定 |
| 归并排序 | `void merge while i,j if(b[j] < a[i])c[k] = b[j++] else c[k] = a[i++];++k;for(i,k)c[k]=a[i];for(j,k)c[k]=b[j];};` | $O(n\; log \;n)$ | $O(n)$ | 稳定的$O(n\; log \;n)$时间复杂度 | 稳定 |
| 桶排序（计数排序） | `cnt[a[i]]++;for(1~m)while(cnt[i]--)cout<<i;` | $O(n+m)$，这里$m$指所有数的范围 | $O(n+m)$ | 数的范围小，要比sort好！ | 稳定 |
""")

def page_8():
    st.title("留言板")
    st.image("img7.gif")
    st.write("留言板")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    name = st.selectbox("我是......", ["guanxin55","22","大fw","自定义"])
    if name == "自定义":
        name = st.text_input("我是......")
    ex = st.selectbox("表情:", ["🌈","❄️","⭐","❤️"])
    new_message = st.text_input("想要说的话......")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message,ex])
        with open("leave_messages.txt","w",encoding='utf-8') as f:
            message = ""
            for i in  messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "#" + i[3] + "\n"
            message = message[:-1]
            f.write(message)
    st.write("")
    st.write("")
    st.write("")
    choice = st.radio(
        '调查:你最喜欢的栏目',
        ['图片处理 Tools','飞花令游戏','计算器','MarkLatex编辑器']
    )
    st.write(f"我最喜欢:{choice}")
    if st.button("提交"):
        with open("leave_messages.txt","w",encoding='utf-8') as f:
            message = ""
            messages_list.append([str(int(messages_list[-1][0])+1), name, f"我最喜欢{choice}",ex])
            for i in  messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "#" + i[3] + "\n"
            message = message[:-1]
            f.write(message)
    st.write("")
    st.write("")
    st.write("")
    for i in messages_list:
        with st.chat_message(i[3]):
            st.write(i[1],":",i[2])
        
if (page == '主页'):
    page_1()
elif (page == '图片处理 Tools') :
    page_2()
elif (page == '飞花令游戏') :
    page_3()
elif(page == '计算器') :
    page_4()
elif(page == 'MarkLatex编辑器') :
    page_5()
elif(page == '排序简介') :
    page_6()
elif(page == '留言板') :
    page_8()
else :
    pass