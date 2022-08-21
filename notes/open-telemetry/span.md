# Spans
**Span** represents an operation (unit of work) in a trace. A span could be a remote procedure call (RPC), a database query, or an in-process function call. A span has:

* Parent Span
* Span name (operation name)
* Span kind
* Start and end time
* A status that reports whether the operation succeeded or failed
* A set of key-value attributes describing the operation
* A timeline of events
* A list of links to other spans
* A span context that propagates trace ID and other data between different services

## Span names
To group spans properly, give them short and concise names. The total number of unique span names should be less than 1000.

## Span kind
**Span kind** must have one of the following values:
* server — for server operations, for example, HTTP server handler
* client — for client operations, for example, HTTP client requests
* producer — for message producers
* consumer — for message consumers and async processing in general
* internal — for internal operations

## Status Code
**Status code** indicates whether an operation succeeded or failed. It must have one of the following values:
* `Ok` — Success
* `Error` — Failure
* `Unset` — the default value which allows backends to assign the status

A status will be attached to a span. Typically, you will set a span status when there is a known error in the application code such as an exception. When an exception is handled, a Span status can be set to `Error`. Otherwise, a Span status is in the Unset state.

## Attributes
To record contextual information, you can annotate spans with attributes that carry information specific to the operation. You can name attributes as you want, but for common operations, you should use [semantic attributes](https://uptrace.dev/opentelemetry/attributes.html) convention.

**Attributes** are key-value pairs that contain metadata that you can use to annotate a Span to carry information about the operation it is tracking. Attributes have the following rules that each language SDK implements:
* Keys must be non-null string values
* Values must be non-null string, boolean, floating point value, integer, or an array of these values

## Events
You can also annotate spans with events that have a start time and an arbitrary number of attributes. The main difference between events and spans is that events don't have an end time (and therefore no duration). **Events** usually represent exceptions, errors, logs, and messages, but you can create custom events as well.

A Span Event can be thought of as a structured log message (or annotation) on a Span, typically used to denote a meaningful, singular point in time during the Span's duration.

## Links
Links exist so that you can associate one span with one or more spans, implying a casual relationship. Links are optional but serve as a good way to associate trace spans with one another.

## Context
Trace/span context is a request-scoped data such as:
* **Trace ID** — unique trace identification
* **Span ID** — unique span identification
* **Trace flags** — various flags such as sampled, deferred, and debug

**Span Context** is the part of a span that is serialized and propagated alongside Distributed Context and Baggage. Because Span Context contains the Trace DI, it is used when creating Span Links.

## Reference
* [Traces](https://opentelemetry.io/docs/concepts/signals/traces/#span-context)
* [Trace Semantic Conventions](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/)
* [OpenTelemetry Distributed Tracing](https://uptrace.dev/opentelemetry/distributed-tracing.html)