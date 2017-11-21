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

## Solution for collection service
![Design Doc](./collection_service.pdf)

### Serverless producer layer:
This layer accepts messages in (key, value) format and becomes a producer for the collection layer. Serverless architecture was chosen. Some of its pros and cons

***pros:***
* Easy to scale
* If AWS Lambda or Google Cloud Function is used, these services are managed and do not require lot of developer hours

***cons:***
* vendor lock in, ie the service is highly dependent on the vendor(eg google or AWS)

### Collection layer:
This layer accepts the (key, value) messages from the producers and queues them, which are collected by the consumers (in our case the processing and ingest layer). This layer can be implemented using kafka or google pub/sub or AWS services. Using an open source tool gives more control but requires lot of developer time, whereas using a managed service requires less developer time but provides us less control.

***pros:***
* Ensures message delivery downstream

***cons:***
* Managing the partitions among topics is time consuming (not applicable in case of managed services)
* expensive (not applicable in case of open source implementation)

### Processing and Ingest layer:
This is a consumer of the collection layer. We use spark streaming which is a consumer of the collection layer. Here we operate on a one hour window and for each hour windowed dataframe we perform a dedupe among the records, group by on key, date and hour_of_day(0-24) and get the following metrics at a key, date and hour_of_day level
* number of events
* sum of all the events
* min 
* max
* median
* average

Then the data at key, date and hour_of_day level is pushed into a database

***pros:***
* Data processed with an approximate one hour delay.

***cons:***
* Not exactly real time (eg, if the query service makes a request for data at time 5:55PM no data will be available for the 5 PM time)
* The hour level aggregation will only be performed after the hour is complete, which means that there is a lag time of more than an hour between real time and data in our database layer.

### Database layer:
The processing and ingest layer pushed data into this layer. We can store it in a highly available, distributed and scalable database (eg: bigquery, redshift)

## Solution for query service:
![Design Doc](./query_service.pdf)

