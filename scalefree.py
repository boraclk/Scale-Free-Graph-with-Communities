import networkx as nx 
from networkx.algorithms import community
import matplotlib.pyplot as plt 

# 1.Genereating network 

G= nx.barabasi_albert_graph(100,3) 

# 2.Drawing degree distribution

pos = nx.spring_layout(G)
nx.draw_networkx(G,pos, with_labels=True)
plt.show() 

# 3.Finding all communities    (I used Louvain Modularity Algorithm.)

communities = list(community.greedy_modularity_communities(G))

# 4.Number of communities

print(f"There are {len(communities)} communities.")

# 5.Naming communities    (I assigned all the communities that I created into a array called community. When I want to access it, I will do this using the index value.)

community=[]
for frozenset in communities:
   community.append(list(frozenset))

# 6.Print the size and the node labels in each community

i=1
print("community name     community size     nodes in the community")
for a in community:
   print("community",i,"      ",len(a),"               ",list(a))
   i+=1

# 7. Coloring communities    (Since the number of ensembles to be formed is not certain, I decided to use the same color for values above 7.)

colorlist=[]
for node in G:
   i=0
   while i<len(community):
      for comnode in community[i]:
         if comnode==node and i==0:
            colorlist.append('blue')
         elif comnode==node and i==1:
            colorlist.append('red')
         elif comnode==node and i==2:
            colorlist.append('green')
         elif comnode==node and i==3:
            colorlist.append('yellow')
         elif comnode==node and i==4:
            colorlist.append('pink')
         elif comnode==node and i==5:
            colorlist.append('aqua')
         elif comnode==node and i==6:
            colorlist.append('purple')
         elif comnode==node and i==7:
            colorlist.append('brown')   
         elif comnode==node and i>7:
            colorlist.append('gray')   
      i+=1         
       
nx.draw_networkx(G,pos,node_color=colorlist ,with_labels=True)
plt.show()

# 8. Assaign subnetworks    (As in step 5, I created an array called sub_network here.)

sub_network=[]
for comnode in community:
   sub_network.append(G.subgraph(comnode))

# 9. Drawing subnetworks

i=0
color={}
for sub in sub_network:
   if i==0:
      color='blue'
   elif i==1:
      color='red'
   elif i==2:
      color='green'
   elif i==3:
      color='yellow'
   elif i==4:
      color='pink'
   elif i==5:
      color='aqua'
   elif i==6:
      color='purple'
   elif i==7:
      color='brown'
   elif i>7:
      color='gray'                         
   nx.draw_networkx(sub,pos,node_color=color ,with_labels=True)
   plt.show()
   i=i+1

   # Sonuç olarak ödevde benden istenileni yaptığıma inanıyorum. Şekillerdeki community'ler pek de beklediğim gibi oluşmadı.
   # Ancak yine de oluşturmak istediğim community'leri tam olarak olmasa da görebiliyorum. 
   # Grafın kenarlarında oluşan community'ler daha doğru bir şekilde oluşmuşken içeriye doğru ilerledikçe oluşumların daha düzensiz hale geldiğini farkettim.
   # Bunun sebebinin grafın içerisindeki edge sayısının oldukça fazla olmasından ve dolayısıyla çok fazla komşuluk ilişkisi barındırdığından kaynaklı olduğunu düşünüyorum.