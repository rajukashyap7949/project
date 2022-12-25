#!/usr/bin/env python
# coding: utf-8

# DBMS

# In[1]:


import sqlite3


# create database

# In[2]:


db=sqlite3.connect('student_detail_database20aug.db')


# create cursor

# In[3]:


cur=db.cursor()


# In[4]:


cur.execute('create table student(id int primary key,name text,marks int)')


# In[5]:


cur.execute("insert into student(id,name,marks) values(110,'alon',80)")


# In[6]:


db.commit()


# In[7]:


cur.execute("insert into student(id,name,marks) values(111,'mick',60)")

db.commit()


# In[8]:


cur.execute("insert into student(id,name,marks) values(112,'john',70)")

db.commit()


# In[10]:


result=cur.execute("select * from student")

for i in result:
    print(i)


# In[11]:


cur.execute("insert into student(id,name,marks) values(113,'robat',50)")

db.commit()


# In[12]:


cur.execute("insert into student(id,name,marks) values(114,'dany',70)")

db.commit()


# In[13]:


cur.execute("insert into student values(115,'maxi',50),(116,'neck',40),(117,'niel',75),(118,'jully',50)")
db.commit()


# In[14]:


result=cur.execute("select * from student")

for i in result:
    print(i)


# In[15]:


result=cur.execute("select * from student")

result.fetchall()


# In[16]:


result=cur.execute("select id from student")

for i in result:
    print(i)


# In[17]:


result=cur.execute("select name from student")

for i in result:
    print(i)


# In[18]:


result=cur.execute("select marks from student")

for i in result:
    print(i)


# In[19]:


result=cur.execute("select id,name from student")

for i in result:
    print(i)


# In[20]:


result=cur.execute("select * from student where id=110")
for i in result:
    print(i)


# In[21]:


result=cur.execute("select * from student where id=111")
for i in result:
    print(i)


# In[22]:


result=cur.execute("select * from student where id=112")
for i in result:
    print(i)


# In[23]:


result=cur.execute("select * from student where id=113")

result.fetchone()


# In[1]:


result=cur.execute("select * from student where name='dany'")

result.fetchone()


# In[ ]:




