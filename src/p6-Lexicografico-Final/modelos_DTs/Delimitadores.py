def dt_delimitadores( self, lexema ):
    
    if lexema == " ":

        return {
                    "token": "DELIMITADOR",
                    "lexema": lexema
                }

    if lexema == "\n":

        return {
                    "token": "DELIMITADOR",
                    "lexema": lexema
                }
    if lexema == "\t":

        return {
                    "token": "DELIMITADOR",
                    "lexema": lexema
                }
    if lexema == "\b":

        return {
                    "token": "DELIMITADOR",
                    "lexema": lexema
                }
        
    