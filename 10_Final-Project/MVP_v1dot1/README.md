# Minimum Viable Product version 1.1
Version 1.1 is currently under construction. Version 1.0 is released and can be viewed [here](/10_Final-Project/MVP_v1dot0/).  
<br>

## V1.1 Provisional Architecture design
![v1.1 provisional architecture diagram](/10_Final-Project/MVP_v1dot1/includes/diagram_v1dot1.drawio.png)
*v1.1 provisional architecture diagram*  
<br>

## Requirements V1.1
The requirements for version 1.1 are:

|  | Requirements |
| - | - |
| 1 | The web server must no longer be "naked" on the internet. The customer would prefer to see a proxy intervene. The server will also no longer need to have a public IP address. |
| 2 | If a user connects to the load balancer via HTTP, this connection should be automatically upgraded to HTTPS. |
| 3 | The connection must be secured with at least TLS 1.2 or higher. |
| 4 | The web server must undergo a health check on a regular basis. If the web server fails this health check, the server should be automatically restored. |
| 5 | If the web server comes under persistent load, a temporary additional server should be started. |
| 6 | Make sure the customer can understand how to use the application. Make sure it is clear what the customer must configure before the deployment can start and which arguments the program needs. |
| 7 | The customer wants to test your architecture internally before using the code in production. Ensure that configuration is available that allows the customer to deploy an MVP. |