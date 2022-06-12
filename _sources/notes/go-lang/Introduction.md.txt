# Introduction

### GO (golang)
* Strong and statically typed
* Excellent community
* Key features
   * Simplicity
   * Fast compile times
   * Garbage collected
   * Built-in concurrency
   * Compile to standalone binaries

#### What is a "Garbage Collected"?
The primary purpose of Garbage Collection is to reduce memory leaks. Garbage implementation requires 3 primary approaches as follows:
* Mark-and-sweep
   - In process when memory runs out, the Garbage Collector locates all accessible memory and then reclaims available memory
* Reference counting
   - Allocated objects contain a reference count of the referencing number. When the memory count is zerom the object is garbage and is then destroyed. The freed memory returns to the memory heap.
* Copy collection
   - There are two memory partitions. If the first partition is full, the Garbage Collector locates all accessible data structures and copies them to the second partition, compacting memory after Garbage Collector process and allowing continuous free memory.

## Resources
* [GO Programming Language](https://golang.org)
* [Documentation](https://go.dev/doc/)
* [Effective Go](https://go.dev/doc/effective_go)
* [Playground](https://go.dev/play/)
* [Packages](https://pkg.go.dev/std)
* [Roadmap](https://roadmap.sh/golang)

## Blog / Article
* [Garbage Collection (GC)](https://www.techopedia.com/definition/1083/garbage-collection-gc-general-programming)
* [An overview of memory management in Go](https://medium.com/safetycultureengineering/an-overview-of-memory-management-in-go-9a72ec7c76a8#:~:text=To%20do%20this%2C%20Go%20relies,new%20objects%20to%20the%20heap.)
* [Understanding Garbage Collection in Go](https://www.developer.com/languages/garbage-collection-go/)
* [Getting to Go: The Journey of Go's Garbage Collector](https://go.dev/blog/ismmkeynote)