# Introduction

**OpenTelemetry** (OTel for short) is a collection of APIs and SDKs that allows us to collect, export, and generate traces, logs, and metrics (also known as the three pillars of observability). **Open** stands for *open-source*. **Telemetry** comes from the greek word **Tele** which means *remote* and **metry** means *measurement*. So OpenTelemetry is an open-source technology allowing you to collect remote measurements.

In fact it comes from two existing open-source projects that merged and it is **[OpenTracing](https://github.com/opentracing)** and **[OpenCensus](https://github.com/census-instrumentation)**. It doesn't provide any observability back-end solution like Prometheus or Jaeger. It is defining a standard.

It is a CNCF (Cloud Native Computing Foundation) community-driven open-source project. OpenTelemetry enables us to **instrument** our cloud-native applications. Instrumenting your code means collecting **telemetry data** from the events that happen in your systems, which ultimately helps us understand our software's performance and behavior.

When you are dealing with OpenTelemetry it requires two steps. First, you need to generate data from your applications. Second, you need to store and consume the data collected.

---
**NOTE**

1. Generate measurement

   Instrument your code

2. Store the data

   Consume the data
---

## Three Types of Telemetry
**Telemetry** is the data we use to monitor our applications. It is a term meant to cover a wide range of data types, such as metrics, logs, and traces.

### Traces
**Distributed Trace**, more commonly known as a **Trace**, records the paths taken by requests (made by an application or end-user) as they propagate through multi-service architectures, like microservice and serverless applications. Tracing is essential for distributed systems, which commonly have nondterministic problems or are too complicated to reproduce locally.

It is a context of what and why things are happening and the story of the communication between services. Traces allows us to visualize the progression of requests as they move throughout your system. Traces specify how requests are propagated through your services. It solves a lot of the gaps that you had when you relied solely on metrics and logs.

A Trace is made of one or more **Spans**. The first Span represents the Root Span. Each Root Span represents a request from start to finish. The Spans underneath the parent provide a more in-depth context of what occurs during a request (or what steps make up a request). Traces tell us how long each request took, which components and services it interacted with, and the latency during each step, giving you a complete picture, end-to-end.

#### Spans
A **span** is a description of an event that occurs in your system. For example, and HTTP request or a database operation that spans over time (start at X and has a duration of Y milliseconds). Usually, it will be the parent and/or child of another span.

It represents a unit of work or operation. It tracks specific operations that a request makes, painting a picture of what happened during the time in which that operation was executed. A Span contains name, parent span ID (empty for root spans), time-related (start and end) data, structured log messages, and other metadata (i.e. Attributes) to provide information about the operation it tracks.

### Logs
A **Log** is a timestamped message emitted by a service or other components. Logs are the trail of breadcrumbs we leave within your application to read them later and understand how the application is behaving.

### Metrics
**Metrics** provide us with a high-level view of your system's health and if it behaves within your desired boundaries. They are great at showing you when behaviour has changed. It is a simple measurement that you can capture during runtime and there are three types of metrics.

Three types of metrics:
* **Counter**
   * It is a value that will sum and that will just grow over time
* **Measure**
   * A value that will be aggregated over time
* **Observer**
   * Capture the current set of values at a given time like a gauge

Similar to Traces, Metrics will have context and it will also be important for the metric information. Metric has a name, description, unit, kind (it is the type of metric), a lable (type of aggregation), and time.

## Reference
* [Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
* [Documentation](https://opentelemetry.io/docs/)
* [Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)
* [Introduction to OpenTelemetry](https://www.youtube.com/watch?v=dfpGU9al_i4)
* [How to Get Started with OpenTelemetry Go](https://www.aspecto.io/blog/opentelemetry-go-getting-started/)
* [What is OpenTelemetry? A Straightforward Guide](https://www.aspecto.io/blog/what-is-opentelemetry-the-infinitive-guide/)