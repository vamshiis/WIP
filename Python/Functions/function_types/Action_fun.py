# Task : Store Application log message in a file
def write_log(message):
    with open(r"C:\Users\vamshi\Demo\app.log",'a') as file:
        file.write(message + '\n')

# write_log('App started')
# write_log('user logged in')
write_log('App Stopped')