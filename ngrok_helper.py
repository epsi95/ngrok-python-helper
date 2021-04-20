#!/usr/bin/env python
# coding: utf-8



# import pygrok
# install it via
# pip install pyngrok
# or
# conda install -c conda-forge pyngrok
# more about it here https://pyngrok.readthedocs.io/en/latest/index.html#installation

from pyngrok import conf,ngrok



# configure tunnel location ex: india 'in'
# tunnels at the same time
# you get this authtoken by signing up
# to ngrok portal here https://dashboard.ngrok.com/
# if you don't have AUTH_TOKEN your tunnel will be closed
# after fixed amount of time
# so auth token is recommended

ngrok.set_auth_token("<NGROK_AUTH_TOKEN>")
conf.get_default().region = "in"

# stopping monitoring thread as I don't need it
# it eats up resource
conf.get_default().monitor_thread = False




# this code starts monitoring
# if you don't need this don't use it
# as it can eat some resources

# def log_event_callback(log):
#     print(str(log))

# conf.get_default().log_event_callback = log_event_callback

# to stop the monitoring

# conf.get_default().monitor_thread = False

# for running process

# ngrok.get_ngrok_process().stop_monitor_thread()




http_tunnel = ngrok.connect(addr='8080', proto='http', bind_tls=True)




def start_a_tunnel(port= 8080):
    """
    This function will start a tunnel in port given port, default is 8080
    By default ngrok opens two tunnels 1. http 2. https
    I don't need http
    bind_tls=True tells ngrok to open only https tunnel
    """
    # first I will check if there is any tunnel active
    # if there is any active tunnel we will disconnect it
    for each_tunnel in ngrok.get_tunnels():
        print('Shutting down: ' + each_tunnel.public_url)
        ngrok.disconnect(each_tunnel.public_url)
        
    # now that it is made sure that there is no tunnels
    # we can open a new_tunnel
    tunnel = ngrok.connect(addr=port, proto='http', bind_tls=True)
    
    return tunnel.public_url




start_a_tunnel()




# to shutdown ngrok process

# ngrok.kill()






