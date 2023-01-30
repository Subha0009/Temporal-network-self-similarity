wiki_config = {'FILENAME': 'wiki-talk-temporal.txt',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 1003638700 + 12*3600*24*30,
                'Delta': 36*3600*24*30,
                'TS': 3600*24*30,
                'boxlist': [(0.5, 1), (1, 2), (1.5, 3), (2, 4), (2.5, 5), (3, 6), (3.5, 7), (4, 8), (4.5,9)],
                'save_path': 'wiki-boxes'
               }

ia_email_config = {'FILENAME': 'ia-enron-email-dynamic-sorted.edges',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 937612800,
                'Delta': 24*3600*24*30,
                'TS': 3600*24*30,
                'boxlist': [(4, 8)], #[(0.5, 1), (1., 2), (1.5, 3), (2, 4), (2.5, 5), (3, 6), (4, 8)],
                'save_path': 'ia-email-boxes'
               }

superuser_config = {'FILENAME': 'sx-superuser.txt',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 1247667441 + 8*3600*24*30,
                'Delta': 72*3600*24*30,
                'TS': 3600*24*30,
                'boxlist': [(0.5, 1), (1., 2), (1.5, 3), (2, 4), (2.5, 5), (3, 6), (3.5,7), (4, 8), (4.5, 9)],
                'save_path': 'superuser-boxes'
               }

fb_config = {'FILENAME': 'ia-facebook-wall-wosn-dir-sorted.edges',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 1095135831 + 24*3600*24*30,
                'Delta': 24*3600*24*30,
                'TS': 3600*24*30,
                'boxlist': [(0.5, 1), (1., 2), (1.5, 3), (2, 4), (2.5, 5), (3, 6), (4, 8)],
                'save_path': 'fb-boxes'
               }


ca_config = {'FILENAME': 'ca-cit-HepPH-sorted.edges',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 793926000,
                'Delta': 24*3600*24*90,
                'TS': 3600*24*90,
                'boxlist': [(0.5, 1), (1., 2), (1.5, 3), (2, 4), (2.5, 5), (3, 6), (4, 8)],
                'save_path': 'ca-cit-boxes'
               }

babu_config = {'FILENAME': 'DPPIN/DPPIN-Babu/Dynamic_PPIN.txt',
                'DELIM': ',',
                'LINELEN': 4,
                'TPOS': 2,
                'S': 0,
                'Delta': 36,
                'TS': 1,
                'boxlist': [(1, 1), (2, 2), (3, 3), (4, 4), (5,5), (6, 6), (7,7)],
                'save_path': 'babu-boxes'
               }

msg_config = {'FILENAME': 'CollegeMsg.txt',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 1082040961,
                'Delta': 24*3600*24*8,
                'TS': 3600*24*8,
                'boxlist': [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9,9)],
                'save_path': 'msg-boxes'
               }
email_eu_config = {'FILENAME': 'email-Eu-core-temporal.txt',
                'DELIM': ' ',
                'LINELEN': 3,
                'TPOS': 2,
                'S': 0,
                'Delta': 36*3600*24*7,
                'TS': 3600*24*7,
                'boxlist': [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9,9)],
                'save_path': 'email-eu-boxes'
               }
