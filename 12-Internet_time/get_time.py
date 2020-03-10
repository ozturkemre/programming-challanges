import ntplib
from time import ctime


def request_from_ntp(s):
    c = ntplib.NTPClient()
    # Provide the respective ntp server ip in below function
    response = c.request(s, version=3)
    return ctime(response.tx_time)


def print_servers(sl):
    for k, v in sl.items():
        print(k)


# These servers are only Europe countries. See for more https://www.pool.ntp.org/zone/@
servers = {'Andorra': 'ad.pool.ntp.org',
           'Albania': 'al.pool.ntp.org',
           'Austria': 'at.pool.ntp.org',
           'Aland Islands': 'ax.pool.ntp.org',
           'Bosnia and Herzegovina': 'ba.pool.ntp.org',
           'Belgium': 'be.pool.ntp.org',
           'Bulgaria': 'bg.pool.ntp.org',
           'Belarus': 'by.pool.ntp.org',
           'Switzerland': 'ch.pool.ntp.org',
           'Czech Republic': 'cz.pool.ntp.org',
           'Germany': 'de.pool.ntp.org',
           'Denmark': 'dk.pool.ntp.org',
           'Estonia': 'ee.pool.ntp.org',
           'Spain': 'es.pool.ntp.org',
           'Finland': 'fi.pool.ntp.org',
           'Faroe Islands': 'fo.pool.ntp.org',
           'France': 'fr.pool.ntp.org',
           'Guernsey': 'gg.pool.ntp.org',
           'Gibraltar': 'gi.pool.ntp.org',
           'Greece': 'gr.pool.ntp.org',
           'Croatia': 'hr.pool.ntp.org',
           'Hungary': 'hu.pool.ntp.org',
           'Ireland': 'ie.pool.ntp.org',
           'Isle of Man': 'im.pool.ntp.org',
           'Iceland': 'is.pool.ntp.org',
           'Italy': 'it.pool.ntp.org',
           'Jersey': 'je.pool.ntp.org',
           'Liechtenstein': 'li.pool.ntp.org',
           'Lithuania': 'lt.pool.ntp.org',
           'Luxembourg': 'lu.pool.ntp.org',
           'Latvia': 'lv.pool.ntp.org',
           'Monaco': 'mc.pool.ntp.org',
           'Moldova': 'md.pool.ntp.org',
           'Republic of Montenegro': 'me.pool.ntp.org',
           'Macedonia': 'mk.pool.ntp.org',
           'Malta': 'mt.pool.ntp.org',
           'Netherlands': 'nl.pool.ntp.org',
           'Norway': 'no.pool.ntp.org',
           'Poland': 'pl.pool.ntp.org',
           'Portugal': 'pt.pool.ntp.org',
           'Romania': 'ro.pool.ntp.org',
           'Republic of Serbia': 'rs.pool.ntp.org',
           'Russian Federation': 'ru.pool.ntp.org',
           'Sweden': 'se.pool.ntp.org',
           'Slovenia': 'si.pool.ntp.org',
           'Svalbard and Jan Mayen': 'sj.pool.ntp.org',
           'Slovakia': 'sk.pool.ntp.org',
           'San Marino': 'sm.pool.ntp.org',
           'Turkey': 'tr.pool.ntp.org',
           'Ukraine': 'ua.pool.ntp.org',
           'United Kingdom': 'uk.pool.ntp.org',
           'Holy See (Vatican City State)': 'va.pool.ntp.org',
           'Yugoslavia': 'yu.pool.ntp.org'}

print_servers(servers)
print("Type your server: ")
server = input()
time = request_from_ntp(servers[server])
print("Time is {}" .format(time))
