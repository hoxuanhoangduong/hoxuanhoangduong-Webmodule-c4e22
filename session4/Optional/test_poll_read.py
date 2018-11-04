from poll import Poll
import mlab

# 1.Connect
mlab.connect()

# 2.Read all
poll_list = Poll.objects()  #page, lazy loading
p = poll_list[0]
# print(p.question) #p.question : p cua quest
# print(p.options)
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)
    print("*****")
