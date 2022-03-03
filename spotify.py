import csv
from random import randint

EN_TETE = [{"Artiste": '', "Titre": '', "Durée": ''}for i in range (250)] ##

with open('/home/techfront2/Bureau/musique.txt') as file_txt: # ajoùter un module pour truover le fichier
    # v. 1.0
    file_list=[]
    j=0
    for line in file_txt:
        file_list.append(EN_TETE[j]) # trouver un moyen de cut le lien avec EN_TETE sans j
        line = line.replace("\n", "").split('--') # replaceONE(' ', '') [::-1] et []
        for i in range (2):
            if line[i].startswith(' '): # logiquement, on est deja dans i ==1
                out = line[i][1:]
            elif line[i].endswith(' '): # i ==0
                out = line[i][:-1]
            if i==0:
                file_list[j]['Artiste'] = out # voir premier if
            elif i==1:
                file_list[j]['Titre'] = out #       ' '
        j+=1
        # v.0.0 file_list.append(line.replace("\n", "").split("--"))

rand_list=[randint(0,len(file_list)) for i in range(len(file_list))]
for i in range (len(file_list)):
    while(rand_list[i] in rand_list[:i]):
        rand_list[i]= randint(0, len(file_list))












class Music(): 
    '''Fiche pour chaque musique'''
    
    def __init__(self, title, artist, length=None):
        self.title=title
        self.artist=artist
        self.length=length

    def __str__(self):
        return f'Vous écoutez {self.title} de {self.artist}'

class Playlist():
    '''Liste de toutes les musiques'''

    def __init__(self, size):
        self.size=size
        self.playlist=[[] for i in range(self.size)]

    def fill_playlist(self, file):
        pass

    def show_music(nb, self):
        return f' {self.playlist[nb]}'

    def start_playlist(self, length):
        '''àremplir'''
        pass
    
    def __str__(self):
        print (f'')



# -------------------------------------------------------------------------------------------------
# with open('temp.csv', 'w') as fichier_csv:
#    # Créer un objet writer (écriture) avec ce fichier
#    writer = csv.writer(fichier_csv, delimiter=',')
#    writer.writerow(EN_TETE
#    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
#    for titre, description in zip(titres, descriptions):
#       # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
#       ligne = [titre.string, description.string]
#       writer.writerow(ligne)


# with open("/home/techfront2/Bureau/musique.txt") as csv_file:
#    reader = csv.DictReader(csv_file, delimiter='-')
#    for ligne in reader:
#       print(ligne, "test2") 