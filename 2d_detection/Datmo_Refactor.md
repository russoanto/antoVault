- **Datmo_Node**
	- Interfaccia ros per prendere in input le scan e l'odometria e fornire in **output** i cluster
- datmo
	- Rappresentava la classe che effettuava la detection in se, mi sembra abbia poco senso mantenere questa classe visto che la parte di features extraction può essere mantenuta nella classe cluster
- cluster
	- classe che identifica un singolo cluster è caratterizzato da informazioni come id(fornito durante la data association) nuvola di punti che lo definiscono 