# README

## Systems Design
Design a metrics system that can be used for collecting response times for a hypothetical app.
Each instance of the app would send messages to a collection service. Each message would
contain a value that represents the response time for each request the app receives. Another
part of this system is a query service that can return aggregate values of metrics sent to the
collection service. As a starting point, imagine a scenario in which messages would be sent from 10 different apps
at the rate of 10,000 messages per second.

You can choose off-the-shelf software or decide to build the components you would need. In
either case, highlight the main characteristics of each component that satisfy the system
requirements.
Express your design visually or in pseudo-code. If you create a sketch, it doesn’t have to be
neat, just legible. Include justifications for your design decisions and trade-offs you may have
made. You don’t need to actually implement this service​.
After you present the design, comment on where you think it would break as we increase
utilization of the system by 10x, 100x, 1000x. How would you need to change it to adapt to that
failure mode ?

## System Requirements

### Collection Service
* The collection service should accept messages in the format: (key,value)
* If an instance of the collection service is not available:
* It should not affect the client
* It should not affect the collection service’s ability to respond to requests
* It should not affect the query service’s ability to respond to requests

### Query Service
* The query service should expose a JSON endpoint that returns aggregates of metrics by
hour for a particular instance of an app. Hours are non-overlapping. (ie. tumbling
windows, not sliding windows)
* The format of the JSON endpoint URI should be: ```http://hostname/<key>/<stat_type>/<date>/<hour>```
* stat_type is one of the following aggregate functions: average, min, max, median
* Users should be able to interact with the endpoint using curl