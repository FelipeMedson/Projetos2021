#!/usr/bin/env python
# coding: utf-8

# # Projeto Final de Tópicos Especiais de Estruturas 2 - Confiabilidade Estrutural

# # Otimização da area de aço de uma laje a partir do método Euro Code(JCSS)

# ## Definindo as variáveis do problema

# In[1]:


import matplotlib.pyplot as plt
import random
import math

N=1000000
L=6.0
b=1.0
Nf=0.0
As=0.000735
m_a=As
dp_a= 0.05*As
List_G=[]
#Listas auxiliares para verificação da distribuição das variáveis e plot dos histogramas
teta_1=[]
teta_2=[]
fy_=[]
fc_ =[]
d_ =[]
q_ =[]
g_ =[]
As_ =[]


# In[2]:


m_teta1 = 1;
dp_teta1=0.1
mu_teta1 = math.log((m_teta1**2)/math.sqrt(dp_teta1**2+m_teta1**2));
sigma_teta1 = math.sqrt(math.log((dp_teta1**2/(m_teta1**2)+1)));
print(mu_teta1)
print(sigma_teta1)


# In[3]:


m_teta2 = 1;
dp_teta2=0.2;
mu_teta2 = math.log((m_teta2**2)/math.sqrt(dp_teta2**2+m_teta2**2));
sigma_teta2 = math.sqrt(math.log((dp_teta2**2/(m_teta2**2)+1)));
print(mu_teta2)
print(sigma_teta2)


# In[4]:


m_fy = 560000;
dp_fy=30000
mu_fy = math.log((m_fy**2)/math.sqrt(dp_fy**2+m_fy**2));
sigma_fy = math.sqrt(math.log((dp_fy**2/(m_fy**2)+1)));
print(mu_fy)
print(sigma_fy)


# In[5]:


m_fc = 30000;
dp_fc=5500
mu_fc = math.log((m_fc**2)/math.sqrt(dp_fc**2+m_fc**2));
sigma_fc = math.sqrt(math.log((dp_fc**2/(m_fc**2)+1)));
print(mu_fc)
print(sigma_fc)


# In[6]:


m_q=0.8
dp_q=0.48
a_q=(m_q/dp_q)**2;
b_q=dp_q**2/m_q;
print(a_q)
print(b_q)


# ## Simulações de Monte Carlo para a Função da Falha G

# In[7]:


for i in range(N):
    
    teta1=random.lognormvariate(mu_teta1,sigma_teta1)
    teta_1.append(teta1)
    teta2=random.lognormvariate(mu_teta2, sigma_teta2)
    teta_2.append(teta2)
    fy=random.lognormvariate(mu_fy,sigma_fy)
    fy_.append(fy)
    fc=random.lognormvariate(mu_fc,sigma_fc)
    fc_.append(fc)
    q=random.gammavariate(a_q,b_q)
    q_.append(q)
    As=random.normalvariate(m_a,dp_a)
    As_.append(As)
    d=random.normalvariate(0.23,0.01)
    d_.append(d)
    g=random.normalvariate(7,0.7)
    g_.append(g)
    L=6.0
    b=1.0
    
    G= teta1*As*fy*(d-((As*fy)/(2*fc*b)))-(teta2*(g+q)*(b*L**2)/8)
    List_G.append(G)
    


# In[13]:


plt.hist(List_G)


# In[9]:


for i in List_G:
  if i<=0:
    Nf = Nf + 1


# In[10]:


print(Nf)


# In[11]:


pF = Nf/N
print(pF)


# In[ ]:





# In[ ]:




