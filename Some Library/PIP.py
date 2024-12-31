# PIP - Python Package Manager

# PIP нь Python програмчлалын хэлний нэмэлт модуль болон сан удирдах хэрэгсэл юм .
# PIP хувилбар шалгахдаа pip --version 
# Одоогийн минийх pip 24.3.1  (python 3.13)

# Нэмэлт сан суулгахдаа pip install camelcase
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt)) # Hello World

# Cуулгасан сангаа усгахдаа pip uninstall camelcase 

# Сангуудын жагсаалт харахдаа pip list