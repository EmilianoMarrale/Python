import pandas as pd
from sklearn.tree import DecisionTreeClassifier #Semplice algoritmo per il training e il testing
from sklearn.model_selection import train_test_split # Funzione che permette di splittare il dataset in training e testing
from sklearn.metrics import accuracy_score # Importa la funzione per vedere l'accuracy del nostro algoritmo
from sklearn.externals import joblib # Metodi per salvare e caricare modelli trainati
from sklearn import tree # Ha metodi per esportare il modello in formato grafico


music_data = pd.read_csv('music.csv') # Legge il file csv (comma separated values)
music_data.describe() # Mostra interessanti informazioni riguardo il dataset (es dati mancanti)

X = music_data.drop(columns=['genre']) # Genero a partire da music_data un altro "DB" contenente tutte le colonne di music_data tranne la colonna "genre"ù
y = music_data['genre'] # Genero a partire da music_data tutte le colonne di tipo "genre"

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# X_train sarà l'input dataset per il training mentre y_train l'output dataset per il training
# X_test sarà l'input dataset per il testing mentre y_train l'output dataset per il training
# train_test_split consente di dividere il "DB" in queste quattro variabili, inoltre sceglie i valori da splittare in modo casuale
# test_size = 0.2 indica che vogliamo riservare il 20% del "DB" per il testing

model = DecisionTreeClassifier() # Crea il modello con l'algoritmo DecisionTreeClassifier

model.fit(X_train, y_train) #Esegue il training sui due input training dataset

predictions = model.predict(X_test) # Esegue le predizioni sul dataset di testing

score = accuracy_score(y_test, predictions) # Mostra l'accuratezza calcolandola tra l'output test set e le predizioni effettuate sull'input test dataset

joblib.dump(model, 'nome_file.joblib') # Permette di salvare il modello trainato in un file

joblib.load('nome_file.joblib') # Permette di caricare il modello trainato dal file specificato

predictions = model.predict([[21,1], [22,0]]) # Si testa se funziona il joblib.load


tree.export_graphviz(model, out_file='music-recommender.dot', 
                        feature_names=['age', 'gender'], 
                        class_names= sorted(y.unique()),
                        label='all',
                        rounded=True,
                        filled=True)
                        # Crea un file che permette di visualizzare graficamente i dati in grafici
                        # Bisogna installare un graphviz su VSCode

                    # filled: ogni nodo lo voglio riempito
                    # rounged: i bordi rotondi su ogni bordo
                    # label: ogni nodo ha etichette da leggere
                    # class_names = lista unica dei generi: mostrare la classe per ogni nodo
                    # feature_names=['age', 'gender']: così ci mostra le regole di scelta nei nodi
                    