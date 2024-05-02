# Network-Socket-Chat-Program
___
## Set Up:
1. Download both server.py and client.py Python files.
2. Run the *server.py* file
3. Run the *client.py* file

## Sending Messages
There are 3 types of messages you can send:
* **Broadcast Message**
  Broadcast messages are sent to whoever is actively connected to the server.
> ALL  *message contents*
  
* **Private Message**
  Private messages can be sent to an individual who is actively connected to the server.
> PRIVATE **receiver's username**  *message contents*
  
* **Exit Message**
  Exit messages are used to disconnect from the server after communicating.
  When exiting the program, you will be prompted with a confirmation to leave and your connection will be disconnected.
> EXIT
