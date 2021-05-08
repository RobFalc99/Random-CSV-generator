import random
import string

names = ["Andrea","Francesco","Marco","Giuseppe","Alessandro","Maria","Luca","Anna","Antonio","Francesca","Giovanni","Paolo","Stefano","Matteo","Roberto","Elena","Davide","Giulia","Sara","Laura","Paola","Chiara","Lorenzo","Daniela","Luigi","Daniele","Simone","Gabriele","Riccardo","Salvatore","Massimo","Alberto","Silvia","Federico","Claudio","Cristina","Monica","Federica","Valentina","Elisa","Fabio","Martina","Vincenzo","Giorgio","Franco","Lucia","Patrizia","Giovanna","Pietro","Angela","Mauro","Mattia","Alessandra","Michele","Mario","Barbara","Domenico","Giuseppina","Maurizio","Stefania","Roberta","Antonella","Alessia","Simona","Filippo","Luciano","Claudia","Carla","Alice","Enrico","Carlo","Sofia","Elisabetta","Franca","Sergio","Giorgia","Leonardo","Angelo","Fabrizio","Gianluca","Caterina","Cristian","Nicola","Luisa","Anna Maria","Rita","Tommaso","Gianni","Eleonora","Silvana","Rosa","Emanuele","Marta","Marisa","Marina","Ilaria","Giuliano","Giacomo","Valeria","Beatrice","Teresa","Cinzia","Tiziana","Rosanna","Corrado","Massimiliano","Raffaele","Annalisa","Giuliana","Bruno","Veronica","Manuela","Annamaria","Giancarlo","Arianna","Samuele","Margherita","Matilde","Loredana","Carmela","Luciana","Antonietta","Sabrina","Ivan","Nicolo'","Aurora","Nadia","Emanuela","Cecilia","Greta","Gabriella","Emma","Sonia","Alex","Adriana","Mohamed","Christian","Pasquale","Giada","Irene","Mirella","Alessio","Graziella","Vittorio","Gianfranco","Marcello","Mara","Giulio","Diego","Liliana","Loretta","Tiziano","Edoardo","Ciro","Fausto","Gaetano","Manuel","Marianna","Umberto","Lidia","Maria Grazia","Enrica","Carmine","Sandra","Dario","Raffaella","Letizia","Serena","Nicole","Mirco","Vittoria","Alfredo","Isabella","Camilla","Lina","Lorena","Benedetta","Silvano","Bruna","Erika","Enzo","Deanna","Guido","Gaia","Gennaro","Ivano","Filomena","Jessica","Aldo","Adele","Maura","Lisa","Maria Teresa","Noemi","Rossella","Daniel","Maria Luisa","Edda","Romano","Rossana","Marzia","Rebecca","Linda","Valerio","Adriano","Gino","Bianca","Olga","Concetta","Jacopo","Gloria","Carlotta","Vanna","Renzo","Lara","Rosaria","Thomas","Rosario","Emilio","Viola","Maddalena","Carmen","Tatiana","Carolina","Natalia","Debora","Danilo","Grazia","Ahmed","Vincenza","Maria Cristina","Cesare","Donatella","Mariagrazia","Domenica","Lorenza","Renato","Emilia","Agnese","Gianna","Nicoletta","Eugenio","Clara","Katia","Samuel","Vito","Catia","Asia","Morena","Ivana","Michela","Omar","Fatima","Elia","Ettore","Miriam","Khadija","Antonia","Diana","Armando","Gabriel","Alfonso","Ida","Mirko","Mariya","Sandro","Virginia","Assunta","Graziano","William","Rina","Susanna","Ginevra","Rocco","Angelica","Ermanno","Loris","Marialuisa","Milena","Monia"]

surnames = ["Abbondanza","Abu","Accadia","Acunzo","Adorno","Agostini","Aguila","Ahamed","Ahmed El Ghandor","Aiello","Alam","Albanese","Albanese","Alfano","Alpi","Amato","Amato","Andronico","Andruccioli","Angelicchio","Angiuli","Anklin","Antonelli","Antonelli","Antosh","Apa","Apreda","Arena","Arlati","Armaroli","Assal","Attendoli","Avello","Avendato","Azzarri","Bagnaia","Bagnato","Baiano","Baldari","Baldi","Baldinotti","Balice","Balloni","Balta","Baragliu","Barbieri","Bardi","Barone","Barone","Baronti","Barruga","Barsanti","Bartolini","Bartolucci","Basile","Basile","Bassani","Bassano","Bassolino","Battaglia","Battelli","Bazhanova","Bazzocchi","Bellaneve","Bellettini","Bellini","Bellino","Bellinzoni","Bello","Bencivenga","Benedetti","Benhadda","Bennada Epse Herichi","Bentivegna","Bento Da Silva","Berardi","Bernacci","Bernardi","Bernardi","Bertini","Bevilacqua","Bianchi","Bianchi","Bianco","Biondini","Blasi","Blasi ","Boes","Boncompagni","Bonn","Bonomo","Bonsignore","Bonventre","Borgat-Wohlbang","Borghini","Borkowska","Borrelli","Boschi","Botnariu","Boubaker","Bragioto","Brambilla","Brizi","Brunetti","Bruni","Bruni","Bruno","Buccolieri","Bugli","Buongrazio","Burla","Bushulli","Caccamo","Cagnotti","Calabrese","Caldironi","Caligari","Caligiuri","Callegarini","Campana","Campanella","Cangini","Canichella","Caniglia ","Cannizzaro","Capanna","Capelli","Capitani","Capone ","Caporilli","Caputo","Caraballo","Carbone","Cardinetti","Carina","Carpi Marasco","Carrara","Carucci","Carullo","Caruso","Casadei","Casali","Casella","Castagna","Castagnoli","Castaldi","Castaldo","Castelli","Catalano","Cataldi","Cattaneo","Cauteruccio","Cavallo","Cavaterra","Ceccarelli","Ceccaroni","Cecchetti","Cecere","Cellini","Celotti","Cenciarelli","Ceraldi","Cerchierini","Cerilli","Chaibi","Charaf","Cheikh Talibouya","Chesti","Chiricozzi","Ciampaglia","Ciarla","Ciarlariello","Cicconi","Cichon","Ciervo","Cipollone","Cirillo","Clementucci","Clesceri","Coccia","Colle","Colli","Colombo","Colombo ","Colongi","Colonna","Coluccia","Coluccio","Comini","Conflitti","Conte","Conte","Conti","Contiu","Coppola","Corrado","Corraretti","Corrias","Cospito","Costa","Costa","Costantini","Costantini","Coulier","Covato","Cozzolino","Crepaldi","Croce","Crognale","Curcio","Cusin","Cutillo","D'achille","D'agapito","D alessandro","Dallago","D ambrosio","D amico","D amora","D amore","De Angelis","De Bacco","De Cataldo","De Domenico ","De Filippis","De Florio","De Freitas Sousa Tavares","De La Cruz","De Luca","De Matteo","De Peppe","De Rosa","De Santis","De Santis","De Simone","De Simone","De Stefano","De Sterlich","Deiana","Del Aguila Rosario","Delgadillo Vargas","Delgado","D emilia","Di Benimeo","Di Carlo","Di Lena","Di Maio","Di Marco","Di Mario","Di Menna","Di Paolo","Di Pasquale","Di Renna","Di Ruzza","Di Santo","Di Sipio","Di Stefano","Di Tuoro ","Diacetti","Diamantini","Disabato","Dolciotti","Domenicali","Donatantonio","Donati","Donati","Donatini","Donnhauser","Dorascenzi","D ottavio ","Dotti","Ducci","Eichenberger","El Falaki","El Hallaf","El Haqaoui","El Kaaba  Armit","Emili","Emumwen","Ercolani","Ermeti","Errahmani","Errichetti","Esposito","Esposito","Fabbri","Fabbrizi","Fabiani","Fadda","Farazi","Farina","Fasano","Fassbender","Fazi","Felici","Ferrante","Ferrara","Ferrarese","Ferrari","Ferrari","Ferraro","Ferrero","Ferretti","Ferri","Ferro","Fiadone ","Fico","Filagna","Filipek","Filippelli","Filippi","Finiti","Fiordigigli","Fiore","Fiumi","Fiuzzi","Focaccia","Fontana","Fontana","Fontanella","Fontanilla","Fontolan","Forcina","Forcina ","Fortini","Fossaroli","Fralassi","Franco","Frasca","Fraticelli","Fratini","Freschi ","Fumagalli","Fusco","Fusini","Gagliardi","Galli","Galli","Gallo","Galotti","Gamberini","Gargiulo","Garofalo","Gasmi","Gatti","Gatti","Gealapu","Gentile","Gentili","Gentilini","Ghazi","Ghini","Giannetti","Gigante","Gindre","Giordano","Giorgetti","Giorgi","Giorgio","Giuliani","Giuliani","Giura","Giurgola","Gnani","Gori","Graffiedi","Grande","Grassi","Grasso","Grebenea","Greco","Grimaldi","Gromala","Grossi Pavia","Guaman","Gubinelli","Guerra","Guida","Guidi","Guidi","Guillen Crespo","Gutjahr","Guzman Soriano","Haji","Hajji","Harasymiuk","Harroud","Haryadi","Hijjoui","Hossain","Huaman Lopez","Hushchyna","Iachini","Iacoangeli","Iacobelli","Ianne","Iatalese","Infante","Iuliano","Jagmin","Jaschke ","Jebrane","Jianu","Kamal","Karim","Kazi","Kellmann","Kosek","Kovacs","La Bella","La Sorda","Labella","Lacerenza","Laita","Lanconelli","Lanzoni","Latini","Lattanzi","Laurenti","Lazar","Lazazzera","Lecca","Lelli","Lena","Leone","Leonetti","Lesniewska","Liberto ","Linzi","Lippi","Lombardi","Lombardo","Longo","Lopez","Lorusso","Lucani","Lucarini","Lucchesini","Lucchi","Lunerti","Luzietti","Luzzi","Magalotti","Mahu","Malagigi","Maldini","Mamone","Manchia","Mancini","Mane","Mane'","Mangano","Manzi","Marano","Marata","Marchesini","Marchetti","Marchi","Marchi","Mariani","Mariani","Marini","Marino","Marocchini","Maroncelli","Marra","Martellini ","Martinelli","Martini","Martino","Martino","Martys","Mascali Zeo","Masetti","Massa","Mathlouthi","Mattioni","Mauro","Mazza","Medda","Mele","Meloni","Mena","Mercantini","Messina","Metozzi","Meucci","Mezzogori","Michilli","Milani","Milenov","Milutinovic","Mincuzzi","Minelli","Minestrini ","Minnella","Minuz","Mirante","Mohammed","Moiano","Mollica","Monaco","Monsone ","Monsorno","Montanari","Montevecchi","Monti","Montuori","Morelli","Moretti","Moro","Morselli","Morsiani","Moschetti","Moukrim","Mucci","Mugione","Muratori","Mussinelli","Naci","Napoli","Napolitano","Narducci","Neri","Niane","Nicastro","Nini","Nizzi","Nurul","Nuti","Odigwe","Oliva","Olivelli","Olivieri","Orlandi","Orlando","Ortu","Ossati","Pace","Pacini","Paduano","Pagano","Paglia","Pal Ionut","Palatano","Palazzari","Palma ","Palmieri","Palumbo","Panchetti","Panichi","Panza","Paolini","Papaleo","Paradisi","Parini","Parisi","Parravani","Pascale","Pascucci","Pasolini","Pasquini","Passitto","Pastore","Patruno","Patwary","Paul","Pellegrini","Pellegrino","Pelliccia","Pello'","Pelo","Pepe","Pereira De Castro","Perrone","Petritoli","Pezzuco","Pia","Piacentini","Piani","Piazza","Piccoli","Piccolo","Piersanti","Pierucci","Pierucci ","Piga","Pinna","Pinna","Piras","Piro","Pisacane","Placidi ","Planta","Poli","Policarpo","Polidori","Polyzopoulos","Pompili","Pongetti","Poni","Popescu","Popovici","Porcu","Porta","Potalivo ","Pozzi","Pozzi","Pracucci","Prelati","Proietti","Pucciotti","Pulsoni","Quadalti Noferini","Quadrini","Quartarone","Rainesi","Ranfi","Ranucci","Raqabi","Rebeccato","Renzoni","Renzulli","Resende Azevedo","Riboloni","Ricci","Ricci","Ricciardi","Ricciolino","Rifilato","Rimoldi","Rinaldi","Riva","Rizzelli","Rizzi","Rizzo","Robbio","Rocchi","Romagnoli ","Romani Bergonzo","Romano","Romano","Romeo","Rosata","Rosati","Rosato","Rossetti","Rossi","Rossi","Rotella","Rucci","Rudel","Ruggeri","Ruggieri","Ruggiero","Russo","Russo","Saccone","Sala","Sala","Salamone ","Salvemini","Salvini","Sanges","Sanna","Sanna","Santana Moscato","Santini","Santoro","Santucci","Sarpieri","Sartori","Sartori","Sassetti","Sassi","Sasvari","Satta","Sbreni","Scarale","Scardone","Scipioni","Scotti","Sebastiani","Sementilli","Sepe ","Serban","Seri","Serra","Sestito","Settembrini","Severi","Sgrigna","Siapian","Silvestri","Simonetti","Simoni","Sipio","Siracusa","Soldati","Sorbalo","Sorgentone","Soro","Sorrentino","Sorrentino","Spalletta","Speziale","Spoletini","Sposato","Stazzone","Stefanovich","Steffanina","Steffenoni","Stefoni","Strazzanti","Succi","Tabane","Taifi","Tambini","Tarani","Tarnogrodzki","Tarozzi","Taurone","Tazzari","Teodorani","Terracciano","Testa","Tiglio","Tioni","Tiranno","Tisba","Toader","Tomassi","Torraca","Toso","Tosolini","Totaro ","Tranquilli","Trasforini","Trombino","Tronconi","Tufano","Tulli","Turci","Urbini","Urzo","Usami","Vaccaro","Valbonesi","Valdinosi","Valente","Valentini","Valvano","Vandenbulcke","Vanni","Vannozzi","Vassura","Vella","Veneziani","Veneziano","Verastegui Pereyra","Vidanalage","Villa","Villa","Villani","Vincenzi","Vinciguerra","Vitale","Vitali","Vitor","Volpe","Von Oppen","Wally","Wenz","Wicher","Williams","Wilmer","Wirth","Wozniak","Wozniczka","Zaccaria","Zak","Zamberlan","Zandoli","Zanella","Zanellati","Zanelli","Zanetti","Zapalski","Zaratti","Zavalloni","Zavoli","Zecchini","Zenina","Zeolla","Zepponi","Zinnamosca","Zito","Zivkovic","Zolea","Zolnowski","Zuccherelli","Zurzolo"]

city = ["Torino","Vercelli","Novara","Cuneo","Asti","Alessandria","Biella","Verbano-Cusio-Ossola","Valle d'Aosta","Varese","Como","Sondrio","Milano","Bergamo","Brescia","Pavia","Cremona","Mantova","Lecco","Lodi","Monza e della Brianza","Bolzano","Trento","Verona","Vicenza","Belluno","Treviso","Venezia","Padova","Rovigo","Udine","Gorizia","Trieste","Pordenone","Imperia","Savona","Genova","La Spezia","Piacenza","Parma","Reggio nell'Emilia","Modena","Bologna","Ferrara","Ravenna","Forli-Cesena","Rimini","Massa-Carrara","Lucca","Pistoia","Firenze","Livorno","Pisa","Arezzo","Siena","Grosseto","Prato","Perugia","Terni","Pesaro e Urbino","Ancona","Macerata","Ascoli Piceno","Fermo","Viterbo","Rieti","Roma","Latina","Frosinone","L'Aquila","Teramo","Pescara","Chieti","Campobasso","Isernia","Caserta","Benevento","Napoli","Avellino","Salerno","Foggia","Bari","Taranto","Brindisi","Lecce","Barletta-Andria-Trani","Potenza","Matera","Cosenza","Catanzaro","Reggio Calabria","Crotone","Vibo Valentia","Trapani","Palermo","Messina","Agrigento","Caltanissetta","Enna","Catania","Ragusa","Siracusa","Sassari","Nuoro","Cagliari","Oristano","Sud Sardegna"]

nation = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antartide","Antigua e Barbuda","Arabia Saudita","Argentina","Armenia","Aruba","Australia","Austria","Azerbaigian","Bahamas","Bahrein","Bangladesh","Barbados","Belgio","Belize","Benin","Bermuda","Bhutan","Bielorussia","Birmania","Bolivia","Bosnia ed Erzegovina","Botswana","Brasile","Brunei","Bulgaria","Burkina Faso","Burundi","Cambogia","Camerun","Canada","Capo Verde","Ciad","Cile","Cina","Cipro","Citt","Colombia","Comore","Corea del Nord","Corea del Sud","Costa d'Avorio","Costa Rica","Croazia","Cuba","Cura","Danimarca","Dominica","Ecuador","Egitto","El Salvador","Emirati Arabi Uniti","Eritrea","Estonia","Etiopia","Figi","Filippine","Finlandia","Francia","Gabon","Gambia","Georgia","Georgia del Sud","Germania","Ghana","Giamaica","Giappone","Gibilterra","Gibuti","Giordania","Grecia","Grenada","Groenlandia","Guadalupa","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guinea Equatoriale","Guyana","Guyana francese","Haiti","Honduras","Hong Kong","India","Indonesia","Iran","Iraq","Irlanda","Islanda","Isola Bouvet","Isola di Man","Isola di Natale","Isola Norfolk","Isole ","Isole BES","Isole Cayman","Isole Cocos (Keeling)","Isole Cook","Isole Falkland","Isole Heard e McDonald","Isole Marianne Settentrionali","Isole Marshall","Isole Pitcairn","Isole Salomone","Isole Vergini britanniche","Isole Vergini americane","Israele","Italia","Jersey","Kazakistan","Kenya","Kirghizistan","Kiribati","Kuwait","Laos","Lesotho","Lettonia","Libano","Liberia","Libia","Liechtenstein","Lituania","Lussemburgo","Macao","Macedonia","Madagascar","Malawi","Malesia","Maldive","Mali","Malta","Marocco","Martinica","Mauritania","Mauritius","Mayotte","Messico","Micronesia","Moldavia","Mongolia","Montenegro","Montserrat","Mozambico","Namibia","Nauru","Nepal","Nicaragua","Niger","Nigeria","Niue","Norvegia","Nuova Caledonia","Nuova Zelanda","Oman","Paesi Bassi","Pakistan","Palau","Palestina","Panam","Papua Nuova Guinea","Paraguay","Polinesia Francese","Polonia","Porto Rico","Portogallo","Monaco","Qatar","Regno Unito","RD del Congo","Rep. Ceca","Rep. Centrafricana","Rep. del Congo","Rep. Dominicana","Romania","Ruanda","Russia","Sahara Occidentale","Saint Kitts","Santa Lucia","Sant Elena","Saint Vincent","Saint-Barth","Saint-Martin","Miquelon","Samoa","Samoa Americane","San Marino","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Sint Maarten","Siria","Slovacchia","Slovenia","Somalia","Spagna","Sri Lanka","Stati Uniti","Sudafrica","Sudan","Sudan del Sud","Suriname","Svalbard","Svezia","Svizzera","Swaziland","Taiwan","Tagikistan","Tanzania","Thailandia","Timor Est","Togo","Tokelau","Tonga","Trinidad","Tunisia","Turchia","Turkmenistan","Turks e Caicos","Tuvalu","Ucraina","Uganda","Ungheria","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Wallis e Futuna","Yemen","Zambia","Zimbabwe"]

def generate_int(init=0, fin=100):
    return random.randrange(init, fin)

def generate_name():
    return names[random.randrange(280)]

def generate_surname():
    return surnames[random.randrange(802)]

def generate_cf():
    st = ''
    for x in range(6):
        st+=random.choice(string.ascii_uppercase)
    for x in range(2):
        st+= str(random.randrange(0,10))
    st+=random.choice(string.ascii_uppercase)
    for x in range(2):
        st+= str(random.randrange(0,10))
    st+=random.choice(string.ascii_uppercase)
    for x in range(3):
        st+= str(random.randrange(0,10))
    st+=random.choice(string.ascii_uppercase)
    return st
    

def generate_city():
    return city[random.randrange(107)]

def generate_nation():
    return nation[random.randrange(243)]

def generate_boolean():
    r = random.randrange(0,2)
    if r==0:
        return 't'
    elif r==1:
        return 'f'

def generate_float(init=0, fin=100):
    intero = random.randrange(init, fin+1)
    decimal = random.randrange(0,100)
    return intero+(decimal/100)

def generate_date(init, fin):
    y = random.randrange(init, fin+1)
    m = random.randrange(1, 13)
    if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        d = random.randrange(1, 32)
    elif (m==4 or m==6 or m==9 or m==11):
        d = random.randrange(1,31)
    else:
        d = random.randrange(1, 29)
    return str(y)+'-'+str(m)+'-'+str(d)

def generate_year(init, fin):
    return random.randrange(init, fin+1)

def generate_code(dim):
    st = ''
    for x in range(dim):
        st+=random.choice(string.ascii_uppercase)
    return st

def generate_new(diz):
    return diz[random.randrange(len(diz))]

def populate():
    x=' '
    diz = []
    while x!='':
        x=(input('Insert dictonary\' term (ETNER to stop): '))
        if x!='':
            diz.append(x)
    return diz

def primary_key(mat, n_col):
    rem = []
    for x in mat:
        for y in mat[mat.index(x)+1:]:
            if x[:n_col] == y[:n_col]:
                mat.remove(y)
    return mat

def export(mat):
    print('\nExporting ...\n')
    file = open('EXPORT.csv', 'w')
    for x in range(len(mat)):
        for y in mat[x]:
            if type(y)==int or type(y)==float:
                file.write(str(y))
            else:
                file.write(str(y))
            if y!=mat[x][-1]:
                file.write(',')
        file.write('\n')
    file.close() 

row = int(input('Insert number of rows: '))
clm = int(input('Insert number of columns: '))

print('\nATTENTION: The last range will be taken for all same types ranges\n')

mat = [[] for x in range(row)]

types = list()


inf = 0
sup = 100

inf_date = 1975
sup_date = 2021

inf_year = 1990
sup_year = 2021

dim_code = 0

diz = []

i=0
print('Insert columns types')
print('name - surname - cf - city - nation - int - float - bool - date - year - code - new\n')
for x in range(clm):
    tipo=str(input('Column #' + str(x+1) + ' : '))
    if tipo == 'int':
        inf = int(input('INSERT MIN: '))
        sup = int(input('INSERT MAX: '))
    elif tipo == 'date':
        inf_date = int(input('INSERT MIN date\' YEAR: '))
        sup_date = int(input('INSERT MAX date\' YEAR: '))
    elif tipo == 'year':
        inf_year = int(input('INSERT MIN YEAR: '))
        sup_year = int(input('INSERT MIN YEAR: '))
    elif tipo == 'code':
        dim_code = int(input('INSERT CODE\' DIM: '))
    elif tipo == 'new':
        diz = populate()
    types.append(tipo)


for j in range(row):
    for x in types:
        if x=='name':
            mat[j].append(generate_name())
        elif x=='surname':
            mat[j].append(generate_surname())
        elif x=='int':
            mat[j].append(generate_int(inf, sup))
        elif x=='cf':
            mat[j].append(generate_cf())
        elif x=='city':
           mat[j].append(generate_city())
        elif x=='nation':
            mat[j].append(generate_nation())
        elif x=='float':
            mat[j].append(generate_float())
        elif x=='date':
            mat[j].append(generate_date(inf_date, sup_date))
        elif x=='year':
            mat[j].append(generate_year(inf_year, sup_year))
        elif x=='bool':
            mat[j].append(generate_boolean())
        elif x=='code':
            mat[j].append(generate_code(dim_code))
        elif x=='new':
            mat[j].append(generate_new(diz))
            

print('INSERT PRIMARY KEYS')
pk = int(input('0: nothing - n: PRIMARY KEY until column #n: '))
if pk!=0:
    mat = primary_key(mat, pk)

export(mat)

print('Table generated:')
for x in types:
    print(x, end=' ')
print('\nCon PK:', end=': ')
for x in range(pk):
    print(types[x], end=' ')

input('\n\nPRESS ENTER TO CLOSE THE WINDOWS ...')







        
