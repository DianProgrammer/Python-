# for be in sorat hast ke miad mige to majmoe ke man sakhtam ke inja alan range 1 ta 10 bya moteghayere i ro negah kon.
for i in range(1, 10):
    # badesh bya dastorat mored nazar ro barash anjam bede ke inja mishe print kardan.
    print (i)
    # range inja ta ghabl as 10 hasr hamishe ghabl as one.

for i in range(1, 10):
    print (i, i*i)

for i in range(1, 10):
    print (i, i*i)
    if i ==5:
        break 

for i in range(1, 10):
    print (i , i*i)
    if i == 5:
        print (' i reached 5')
        break 

# for be onvane halghei ke be tedad moshakhsi ke man midonam ghara ye kari ro anjam bede.
# total structure = for + variable + in + set : rules 

friends = [1, 10, 20]
for thisone in friends:
    print(thisone)
    # result in program be in sorat mishe ke 1 va 10 va 20 ro miad print migire.

friends = ['hasan', 'mirza', 'tahmine']
for thisone in friends:
    print ('salam', thisone)
    # result in program in mishe ke miad mige salam hasan, salam mirza, salam tahmine.

# Count Rule : baraye in ke bebinim chand bar yek program anjam shode.
friends = ['hasan', 'mirza', 'tahmine']
count = 0
for thisone in friends:
    print ('salam', thisone)
    count = count + 1
    # baraye in ghazie bayad havasemon be in bashe ke inaro daghighan koja mizarim yani inke aval as hame count = 0
    # va badesh bad az ejraye loop tedad count mire bala.
print(' i said', count, 'hellos')
# alan inja mige ke chand bar salam karde be ebarati inja count yek varaiable ke ma tarif kardim. 




