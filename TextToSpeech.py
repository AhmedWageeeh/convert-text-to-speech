#This Program Reading a text as speaking. GoodLuck!

print('Created By : ')
print('''
    _    _                        _  __        __               _     
   / \  | |__  _ __ ___   ___  __| | \ \      / /_ _  __ _  ___| |__  
  / _ \ | '_ \| '_ ` _ \ / _ \/ _` |  \ \ /\ / / _` |/ _` |/ _ \ '_ \ 
 / ___ \| | | | | | | | |  __/ (_| |   \ V  V / (_| | (_| |  __/ | | |
/_/   \_\_| |_|_| |_| |_|\___|\__,_|    \_/\_/ \__,_|\__, |\___|_| |_|
                                                     |___/           

C	O	P	Y	R	I	G	H	T	©	2019
''')



import os 
try:
    import pyttsx3
except:
    print('Wait for installing the lib.')
    os.system('pip install pyttsx3')


def main():
    rec = pyttsx3.init(debug=True)

    inp = input('Enter the text : ')
    rec.say(inp)
    rec.runAndWait()

    def rate():
        rate = rec.getProperty('rate')
        print('Current rate : ',rate)
        speedrate = int(input('Enter rate speed : '))
        rec.setProperty('rate',speedrate)
        main()

    def vol():
        volume  = rec.getProperty('volume')
        print('Current volume  : ',volume )
        urvol = float(input('Enter volume as u want `Note > setting up volume level  between 0 and 1` : '))
        rec.setProperty('volume',urvol)
        main()

    def gen():
        voices = rec.getProperty('voices')
        #print('Current voice : ',voice)
        print('Press[0] for male. or [1] for female.')
        gen = int(input('Enter a gender as u want : '))
        if gen==0 or gen==1:
            rec.setProperty('voice',voices[gen].id)
        else:
            print('Error')
        main()

    while True:
        print('*_* if u need to change rate/speed press[r] , volume press[v] , gender of voice press[g] , Exit press[x]')
        ch = input('Enter ur choice : ')
        if ch=='r':
            rate()
        elif ch=='v':
            vol()
        elif ch=='g':
            gen()
        elif ch=='x':
            quit()
        else:
            print('Incorrect choice')
        
    rec.stop()      
        
main()
