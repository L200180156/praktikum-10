####Kegiatan 1. Data diri dari server
####
####import socket
####s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
####s.bind(("", 50009))
####s.listen (5)
####print "Program komunikasi tentang diri anda"
####data = ''
####kamus = {'nama' : 'aulia putri r',
####         'NIM' : 'L200180156',
####         'keluar' : ' Siapp !!' }
####while data.lower() != 'keluar' :
####    komm, addr = s.accept()
####    while data.lower () != 'keluar' :
####        data = komm.recv(1024)
####        if data.lower() == 'keluar' :
####            s.close()
####            break
####        print 'perintah: ', data
####        if kamus.has_key(data) :
####            komm.send(kamus[data])
####        else :
####            komm.send('Maaf, perintah tidak dimengerti')


###Kegiatan 2. Informasi tentang server
##
##import socket
##import platform
##s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.bind(("", 50008))
##s.listen (5)
##print "Program komunikasi tentang diri anda"
##baba = ''
##masukan = {'machine' : platform.machine(),
##         'release' : platform.release(),
##         'system' : platform.system(),
##         'version' : platform.version(),
##         'node'    : platform.node(),
##         'quit' : ' Siapp !!!' }
##while baba.lower() != 'quit' :
##    komm, addr = s.accept()
##    while baba.lower () != 'quit' :
##        baba = komm.recv(1024)
##        if baba.lower() == 'quit' :
##            s.close()
##            break
##        print 'Command: ', baba
##        if masukan.has_key(baba) :
##            komm.send(masukan[baba])
##        else :
##            komm.send('unknown command')

#Kegiatan 3. Server menghitung luas bangun geometri

            
import socket

def jajargenjang(a=0, t=0):
    L=a*t
    return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',50006))
s.listen(5)
print 'server sudah siap'
data=''

while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        print 'pesan:',data
        if data.find('parameter1') != -1:
            param, value=data.split('-')
            if param == 'parameter alas':
                a=float(value)
                x=value
                komm.send('parameter dicatat')
            elif param == 'parameter tinggi':
                t=float(value)
                y=value
                komm.send('parameter dicatat')
        elif data == 'hitung':
            komm.send('luas jajar genjangdengan alas {} dan tinggi {} adalah {}.')
        else:
            komm.send('tidak ada')
