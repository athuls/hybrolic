'''
Created on Dec 8, 2015

@author: umang
'''
import sys
import inspect

class Error:            
        @staticmethod
        def error(msg, estream = None):
            error_stream = None
            if estream == None:
                error_stream = sys.stderr
            else:
                error_stream = estream
            _,filename,line_number,_,_,_ = inspect.stack()[1]
            e_msg = 'Error at '
            e_msg = e_msg + str(filename) + ' (' + str(line_number) + ') : ' 
            e_msg = e_msg + msg
            e_msg = e_msg + '\n'
            error_stream.write(e_msg)
            exit()
            
#Error.error("hey",sys.stdout)
#Error.error("you")