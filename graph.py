from math import*

def get_station_graph():
    station_graph = {
                    'kogalniceanu': {'trolleybuses' : [2, 3, 10, 24], 'passengers' : 2370},
                    'puskin' : {'trolleybuses' : [3], 'passengers': 490},
                    'casa-presei' : {'trolleybuses' : [2, 10, 24], 'passengers' : 1890},
                    'emin-theatre' : {'trolleybuses' : [2], 'passengers' : 630},
                    'stefan_cel_mare' : {'trolleybuses' : [7, 10, 24, 25], 'passengers' : 2240},
                    'asem' : {'trolleybuses' : [7, 10, 24, 25], 'passengers' : 2240},
                    'circul' : {'trolleybuses' : [7, 10, 24, 25], 'passengers' : 2100},
                    'vladimirescu' : {'trolleybuses' : [7], 'passengers' : 300},
                    'central_typography' : {'trolleybuses' : [25], 'passengers' : 520},
                    'kiev' : {'trolleybuses' : [10, 24], 'passengers' : 1300}
    }
    return station_graph

def get_terminal_stations():
    terminal = ['puskin', 'emin-theatre', 'vladimirescu', 'central_typography', 'kiev']
    return terminal
