- Ora lavoreremo in un contesto sincrono, il che significa che come assunzioni abbiamo che 
	- ogni entità manda un messaggio al tick del clock
	- per ogni tick può inviare un solo messaggio allo stesso vicino
	- ogni nodo ha lo stesso clock e si conosce la frequenza
	- conosciamo un upper bound del ritardo dei canali di comunicazione
	- La comunicazione avviene in un unità di tempo che è così definita
		- $$u = \Delta/\delta $$
	- Abbiamo un upper bound sulla dimensione del messaggio
## Elezione in anello sincrono
- Idea: come nell'algoritmo AS-FAR id grandi verranno stoppati e gli ID piccoli andranno avanti
- Il vantaggio è che possiamo mandare messaggi con velocità differenti, possiamo farlo per la sincronizzazione del tempo
	- ID piccoli viaggiano a velocità maggiori e viceversa
	- Per farlo aggiungo un **delay**, cioè se ricevo una i minore del proprio ID allora attendo una quantità di tempo pari a f(i) time units
	- Se un nodo riceve il proprio ID allora elegge se stesso come **LEADER**. 
	- L'idea è che l'ID del leader viaggi più velocemente degli altri
- **delay function**
	- Una possibilità è questa
		- $$2^i$$
		- ci siamo fermati prima, la domanda che ha posto è, ci abbiamo guadagnato inserendoci in questo contesto? (si ma ho aggiunto un tempo esponenziale)
- Quando un entità riceve un messaggio contenente i questo aspetta f(i) unità di tempo, con f definito come sopra.
	- Se un entità riceve il proprio identificativo allora elegge se stesso come **leader** e invia una notifica nell'anello, che non viene rallentato.
- **Qunate unità di tempo deve aspettare l'id minore?**
	- Il più piccolo identificativo aspetta $$2^{min} * n + n$$
- Quanto tempo ci mette il secondo identificativo più piccolo?
	- Assumendo che il secondo id più piccolo sia uguale a min + 1 il che significa che il tempo di attesa sarà di $$2^{min} * n+ n /2^{min+1} $$
	- Questo è il mio upperboud
		- $$ \frac{2^{min} * n+ n}{2^{min+1}}\le \frac{n}{2}+ \frac{n}{2} = n < n \space\space links$$
- Man mano che aumenta l'identificativo allora dimezza la strada percorribile nel tempo in cui il minore esegue un giro completo dell'anello
- **Numero messaggi**
	- $$n+n+\frac{n}{2} + \frac{n}{4} + \frac{n}{8} +\frac{n}{2^{n-2}}$$
	- $$ = n + n*\sum\limits^{n-2}_{i=0}{\frac{1}{2^{i}}}\in O(n)$$
	- **number of bits**
		- $$O(n\log{(Max)})$$
- **Time units**
	- $$O(2^{min}n)$$
### Silenzio espressivo
- Usando il silenzio possiamo inviare dati di grandi dimensioni anche con solo 2 bit indipendentemente dal numero da rappresentare. Ovviamente tutti devono poter contare il tempo nello stesso modo.
	- Se A vuole inviare un valore a B allora quello che farà è
		- A invia un bit al tempo t (dice a B di iniziare a contare a B)
		- B riceve il bit al tempo t' = t +1
		- A attende X ticks
		- A invia un'altro bit al tempo t+X
		- B riceve un bit al tempo t'' = t + X + 1
		- B calcola X = t'' - t'
	- Ovviamente senza uno stesso riferimento temporale questo non può essere fatto.
	- Ovviamente utilizzo solo 2 bit ma utilizzo anche X unità di tempo
#### Elezione usando il silenzio
- Ogni entità aspetta una certa quantità di tempo se non succede nulla allora diventa leader e lo notifica agli altri
- Come definisco la funzione di attesa?
	- sia d(x,y) la distanza di x e y in un anello orientato
	- ogni entità con ID = i deve aspettare f(i,n)
		- il leader deve notificare tutte le entità mentre stanno ancora aspettando
		- Un problema è il secondo minimo nel caso in cui si trovi nel punto più distante così che la notifica impieghi molto tempo a raggiungerlo
			- la nostra funzione di attesa deve soddisfare la seguente proprietà $$f(x+1,n) - f(x,n) > n-1$$
				- Significa che il tempo di attesa del secondo più piccolo meno il tempo di attesa del leader sia strettamente maggiore del numero di nodi -1 (cioè il tempo di inviare la notifica da parte del leader)
			- Funziona solo se $$f(i,n) = i*n$$
- Questa funzione di attesa funziona solo con l'inizio simultaneo, senza allora dobbiamo definire una nuova funzione di attesa.
- la funzione f(i,n) deve essere (x è il leader e y è una qualsiasi altra entità) $$t(x) + f(x,n) + d(x,y) < t(y) + f(y,n)$$
	- Quindi il tempo in cui si è svegliato più il tempo di attesa più la distanza di notifica a y deve essere minore del tempo in cui si è svegliato y più il suo tempo di attesa
		- Quello che vale sempre è che $$t(x) - t(y) + f(x,n) + d(x,y) < f(x,n) + 2n$$
		- Sappiamo che t(x) -t(y) < n
		- sappiamo che d(x,y) < n 
		- Da qui abbiamo che la quantità a sinistra è minore uguale a f(x,n) + 2n
	- Quello che cerchiamo è una funzione di attesa per cui valga $$f(i,n) = f(x,n) + 2n \le f(y,n)$$
	- $$f(x,n) + 2n \le f(x+1,n)$$
	- Con queste condizioni allora è vero anche che $$t(x) - t(y) + f(x,n) + d(x,y) < f(x,n) + 2n \le f(y,n)$$
		- Il che significa che il leader farà in tempo a svegliarsi e attendere che tanto questo valore sarà sempre minore o uguale al tempo di attesa di un qualsiasi nodo
	- Una funzione di attesa per cui vale tutto ciò è $$f(i,n) = 2n*i$$
- **Complexity**
	- **Message**
		- 1 notifica per ogni link O(n)
	- **Time**
		- t(min) + f(min,n) + n < 2n * min +2n
		- O(n*min) unità di temp

### Universal waiting

- La tecnica di attesa può essere utilizzata da qualsiasi rete connessa G per determinare l'ID minimo
- Algoritmo
	- Wake Up: viene mandato un messaggio start 

## Randomized leader election
- Cosa posso fare se non ho identificativi univoci? Posso cambiare il protocollo.
	- Protocollo randomizzato
		- Ovviamente non abbiamo garanzie come ne abbiamo nei protocolli deterministici per ovvie ragioni
			- **Montecarlo**: terminano sempre ma il risultato è corretto con una data probabilità
			- **Las Vegas**: terminano sempre correttamente ma terminano con una data probabilità
	- LasVegas: l'idea è che si ragiona in rounds in cui in ognuni si scelgono dei valori casualmente, se ho un solo minimo allora lo definisco leader altrimenti inizia un nuovo round.
		- **Assunzioni:**
			- ogni nodo conosce n
		- Tutit quelli che hanno il minimo inviano una notifica, ma come facciamo a sapere se siamo gli unici ad avere il minimo, non ho un identificativo che mi faccia capire di chi è la notifica
			- uso il tempo che è sincronizzato, so dopo quanto tempo devo ricevere il mio messaggio.
		- Una volta che ho capito che sono leader allora mando una notifica di leader election.
		- **Protocol Complexity**
			- **Singolo round**
				- **Message**
					- O(n) bits
				- **Time**
					- O(n * min_id + n) and min_id < b --> O(n*b)
					- b identifica l'intervallo entro il quale io scelgo il mio identificativo casualmente, più è grande maggiore sarà il tempo di elezione del leader.
			- **Quanti round ho bisogno**:
				- Dipende dal criterio di selezione random
					- se utilizzo distribuzione uniforme allora se ho 2 valori ad esempio risulta difficile che il protocollo termini rapidamente
					- una possibilità può essere
						- 0 con probabilità 1/n
						- 1 con probabilità (n-1)/n
					- Il protocollo termina quando esattamente una sola entità sceglie 0 questo accade con probabilità $$\frac{1}{n} * \frac{n-1}{n}^{n-1}$$
					- Ovviamente a me va bene che chiunque possa diventare leader quindi devo moltiplicate tutto per n $$n*\frac{1}{n} * \frac{n-1}{n}^{n-1} = \frac{1}{e}_{n\rightarrow \inf}$$
					- Se io voglio sapere la probabilità di successo non dopo 1 round ma dopo r round allora ho $$\frac{1}{e} * (1-\frac{1}{e})^{r-1} = e$$
					- In media ci aspettiamo che termini entro 3 round circa, si parla di risultati attesi
					