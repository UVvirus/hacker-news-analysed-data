#!/usr/bin/env python
# coding: utf-8

# In[18]:


from csv import reader
opened_file=open('hacker_news.csv')
read_file=reader(opened_file)
hn=list(read_file)
# Printing to see what is in the first 5 rows
for i in hn[:5]:
    print(i)
    print("\n")


# In[19]:


headers = hn[:1] #Extracting the first row of data,
hn = hn[1:] #Removing the header 

# Confirms header is gone
for i in hn[:5]:
    print(i)
    print("\n")


# In[20]:


ask_posts=[]
show_posts=[]
other_posts=[]

for row in hn:
    title=row[1]
    if title.lower().startswith('ask hn'):
         ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# In[21]:


total_ask_comments=0
for row in ask_posts:
    #num_comments=int(row[4])
    total_ask_comments+=int(row[4])
avg_ask_comments=total_ask_comments/len(ask_posts)
print(avg_ask_comments)

total_show_comments=0
for row in show_posts:
    # num_comments=int(row[4])
    total_show_comments+=int(row[4])
avg_show_comments=total_show_comments/len(show_posts)
print(avg_show_comments)
    
    


# In[22]:


#ask posts receive average comments


# In[23]:


import datetime as dt
result_list=[]
for row in ask_posts:
    result_list.append([row[6],int(row[4])])
count_by_hour={}
comments_by_hour={}
for row in result_list:
    row[0]=dt.datetime.strptime(row[0],"%m/%d/%Y %H:%M")
    if row[0].hour not in count_by_hour:
        count_by_hour[row[0].hour]=1
        comments_by_hour[row[0].hour]=row[1]
    else:
        count_by_hour[row[0].hour]+=1
        comments_by_hour[row[0].hour]+=row[1]


# In[24]:


#""""avg_by_hour=[]
#for row in comments_by_hour:
    #avg_by_hour.append(row,comments_by_hour[row]/count_by_hour[row]
    #print(avg_by_hour)
    #""""
avg_by_hour = []

for row in comments_by_hour:
    avg_by_hour.append([row, comments_by_hour[row] / count_by_hour[row]])

avg_by_hour


# In[25]:


swap_avg_by_hour=[]

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1],row[0]])
print(swap_avg_by_hour)




# In[26]:


sorted_swap=sorted(swap_avg_by_hour,reverse=True)
print("Top 5 Hours for Ask Posts Comments")

for avg, hr in sorted_swap[:5]:
     print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(str(hr), "%H").strftime("%H:%M"),avg
        )
    )

