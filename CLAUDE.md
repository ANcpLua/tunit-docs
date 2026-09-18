# TUnit docs — local Markdown copy

Every page of https://tunit.dev/docs as Markdown, one file per page, same tree as the site.
Mirrored from `https://tunit.dev/llms.txt`; latest TUnit release at refresh time: `v1.68.4` (see `VERSION`).

## How to use this folder

- Find the topic below, open **one** file, read it. Don't load the whole folder.
- Paths are relative to this folder. `grep -ril <term> docs/` when the index doesn't name it.
- Docs are not proof: the showcase repo (`../TUnit-*/CHANGELOG.md`, *Divergences from docs*) lists places where the real behaviour differs.
- `WHATSNEW.md` (when present) is the delta between the previous and the current `VERSION`.

## Refresh

- `python3 scripts/refresh_docs.py` — re-download every page, strip heading anchors, rebuild this file.
- `scripts/whats-new.sh <old-tag> <new-tag>` — release notes, public API diff and `src/` changes between two TUnit tags.
- `.github/workflows/weekly-tunit.yml` runs both every Monday and opens a PR with the result.

This file is generated — edit `scripts/refresh_docs.py`, not this file.

## Index

### `docs/`

- `docs/benchmarks.md` — **Performance Benchmarks**: Real-world performance comparisons between TUnit and other .NET testing frameworks
- `docs/intro.md` — **Intro**: TUnit is another testing framework for C# / .NET.
- `docs/troubleshooting.md` — **Troubleshooting & FAQ**: FAQ

### `docs/assertions/`

- `docs/assertions/awaiting.md` — **Awaiting**: In TUnit you await your assertions, and this serves two purposes
- `docs/assertions/boolean.md` — **Boolean Assertions**: TUnit provides simple, expressive assertions for testing boolean values.
- `docs/assertions/collections.md` — **Collection Assertions**: TUnit provides comprehensive assertions for testing collections, including membership, count, ordering, and equivalency checks.
- `docs/assertions/combining-assertions.md` — **Combining Assertions**: TUnit provides several ways to combine multiple assertions within a single test: chaining with .And and .Or, and grouping with Assert.Multiple().
- `docs/assertions/datetime.md` — **DateTime and Time Assertions**: TUnit provides comprehensive assertions for date and time types, including DateTime, DateTimeOffset, DateOnly, TimeOnly, and TimeSpan, with support for toler…
- `docs/assertions/delegates.md` — **Delegates**: TUnit can execute your delegates for you, and this allows you to assert on the data returned (if any was) - Or on any exceptions thrown
- `docs/assertions/dictionaries.md` — **Dictionary Assertions**: TUnit provides specialized assertions for testing dictionaries (IReadOnlyDictionary), including key and value membership checks.
- `docs/assertions/equality-and-comparison.md` — **Equality and Comparison Assertions**: TUnit provides comprehensive assertions for testing equality and comparing values.
- `docs/assertions/exceptions.md` — **Exception Assertions**: TUnit provides comprehensive assertions for testing that code throws (or doesn't throw) exceptions, with rich support for validating exception types, message…
- `docs/assertions/extensibility/custom-assertions.md` — **Custom Assertions**: The TUnit Assertions can be easily extended so that you can create your own assertions.
- `docs/assertions/extensibility/extensibility-chaining-and-converting.md` — **Chaining and Converting**: TUnit allows you to chain assertions that change the type being asserted, enabling fluent and expressive test code.
- `docs/assertions/extensibility/extensibility-returning-items-from-await.md` — **Returning Data via await**: Sometimes, you may want your assertion to return a value, such as an item found in a collection, so you can use it in further assertions or logic.
- `docs/assertions/extensibility/source-generator-assertions.md` — **Source Generator Assertions**: TUnit provides source generators to simplify creating custom assertions.
- `docs/assertions/fsharp.md` — **FSharp**: As awaiting doesn't work quite the same in F#, the syntax instead looks like this
- `docs/assertions/getting-started.md` — **Getting Started with Assertions**: TUnit provides a comprehensive, fluent assertion library that makes your tests readable and expressive.
- `docs/assertions/library.md` — **Assertions Library**: Searchable library of all TUnit assertions
- `docs/assertions/member-assertions.md` — **Member Assertions**: The .Member() method allows you to assert on object properties while maintaining the parent object's context for chaining.
- `docs/assertions/null-and-default.md` — **Null and Default Value Assertions**: TUnit provides assertions for testing null values and default values.
- `docs/assertions/numeric.md` — **Numeric Assertions**: TUnit provides comprehensive assertions for testing numeric values, including specialized assertions for positive/negative values and comparison assertions w…
- `docs/assertions/regex-assertions.md` — **Regex Assertions**: The .Matches() method allows you to validate strings against regular expressions and assert on capture groups, match positions, and match lengths.
- `docs/assertions/should-syntax.md` — **Should Syntax**: FluentAssertions-style value.Should().BeEqualTo() syntax via the optional TUnit.Assertions.Should NuGet package.
- `docs/assertions/specialized-types.md` — **Specialized Type Assertions**: TUnit provides assertions for many specialized .NET types beyond the common primitives.
- `docs/assertions/string.md` — **String Assertions**: TUnit provides rich assertions for testing strings, including substring matching, pattern matching, length checks, and various string comparison options.
- `docs/assertions/tasks-and-async.md` — **Task and Async Assertions**: TUnit provides specialized assertions for testing Task and Task objects, including state checking, completion timeouts, and async exception handling.
- `docs/assertions/type-checking.md` — **Type Checking**: TUnit assertions check types at compile time wherever possible.
- `docs/assertions/types.md` — **Type Assertions**: TUnit provides comprehensive assertions for testing types and type properties.

### `docs/benchmarks/`

- `docs/benchmarks/engine/AsyncTests.md` — **AsyncTests Benchmark**: Performance benchmark results for AsyncTests
- `docs/benchmarks/engine/BuildTime.md` — **Build Performance Benchmark**: Compilation time benchmark results
- `docs/benchmarks/engine/DataDrivenTests.md` — **DataDrivenTests Benchmark**: Performance benchmark results for DataDrivenTests
- `docs/benchmarks/engine/MassiveParallelTests.md` — **MassiveParallelTests Benchmark**: Performance benchmark results for MassiveParallelTests
- `docs/benchmarks/engine/MatrixTests.md` — **MatrixTests Benchmark**: Performance benchmark results for MatrixTests
- `docs/benchmarks/engine/ScaleTests.md` — **ScaleTests Benchmark**: Performance benchmark results for ScaleTests
- `docs/benchmarks/engine/SetupTeardownTests.md` — **SetupTeardownTests Benchmark**: Performance benchmark results for SetupTeardownTests
- `docs/benchmarks/methodology.md` — **Benchmark Methodology**: How TUnit's performance benchmarks are measured and compared
- `docs/benchmarks/mocks.md` — **Mock Library Benchmarks**: Performance comparisons between TUnit.Mocks, Imposter, Mockolate, Moq, NSubstitute, FakeItEasy
- `docs/benchmarks/mocks/Callback.md` — **Callback Benchmark**: Callback registration and execution — TUnit.Mocks vs Imposter vs Mockolate vs Moq vs NSubstitute vs FakeItEasy
- `docs/benchmarks/mocks/CombinedWorkflow.md` — **CombinedWorkflow Benchmark**: Full workflow: create → setup → invoke → verify — TUnit.Mocks vs Imposter vs Mockolate vs Moq vs NSubstitute vs FakeItEasy
- `docs/benchmarks/mocks/Invocation.md` — **Invocation Benchmark**: Calling methods on mock objects — TUnit.Mocks vs Imposter vs Mockolate vs Moq vs NSubstitute vs FakeItEasy
- `docs/benchmarks/mocks/MockCreation.md` — **MockCreation Benchmark**: Mock instance creation performance — TUnit.Mocks vs Imposter vs Mockolate vs Moq vs NSubstitute vs FakeItEasy
- `docs/benchmarks/mocks/Setup.md` — **Setup Benchmark**: Mock behavior configuration (returns, matchers) — TUnit.Mocks vs Imposter vs Mockolate vs Moq vs NSubstitute vs FakeItEasy
- `docs/benchmarks/mocks/Verification.md` — **Verification Benchmark**: Verifying mock method calls — TUnit.Mocks vs Imposter vs Mockolate vs Moq vs NSubstitute vs FakeItEasy

### `docs/comparison/`

- `docs/comparison/attributes.md` — **Attributes**: Here are TUnit's equivalent attributes to other test frameworks.
- `docs/comparison/framework-differences.md` — **Framework Differences**: TUnit is inspired by NUnit and xUnit — they're excellent frameworks that have served the .NET community well.

### `docs/examples/`

- `docs/examples/aspire.md` — **Aspire Integration Testing**: TUnit provides first-class support for Aspire integration testing through the TUnit.Aspire package.
- `docs/examples/aspnet.md` — **ASP.NET Core Integration Testing**: TUnit provides first-class support for ASP.NET Core integration testing through the TUnit.AspNetCore package.
- `docs/examples/complex-test-infrastructure.md` — **Complex Test Infrastructure Orchestration**: TUnit provides a property injection system that can help orchestrate complex test infrastructure setups.
- `docs/examples/filebased-csharp.md` — **File based C# application**: application
- `docs/examples/fscheck.md` — **FsCheck (Property-Based Testing)**: FsCheck is a property-based testing framework for .NET.
- `docs/examples/fsharp-interactive.md` — **F# Interactive**: Interactive
- `docs/examples/instrumenting-global-test-ids.md` — **Instrumenting: Global Test IDs**: There are plenty use cases for having a unique identifier for each test in your test suite.
- `docs/examples/opentelemetry.md` — **OpenTelemetry Tracing**: TUnit emits System.Diagnostics.Activity trace spans at every level of the test lifecycle.
- `docs/examples/playwright.md` — **Playwright**: There is a NuGet package to help with Playwright: TUnit.Playwright
- `docs/examples/tunit-ci-pipeline.md` — **TUnit in CI/CD Pipelines**: When using TUnit in a CI/CD pipeline, you'll want to run tests, collect results, and publish reports for visibility.

### `docs/execution/`

- `docs/execution/cancellation.md` — **Cancelling a Test**: Call TestContext.Execution.Cancel() to request cooperative cancellation of the current test without affecting other tests or the test session
- `docs/execution/ci-cd-reporting.md` — **CI/CD Reporting**: TUnit provides built-in integration with continuous integration and deployment platforms, automatically detecting and adapting to various CI environments.
- `docs/execution/engine-modes.md` — **Engine Modes**: TUnit supports two execution modes, providing flexibility for different development and deployment scenarios.
- `docs/execution/parallelism.md` — **Controlling Parallelism**: TUnit runs all tests in parallel by default.
- `docs/execution/parameters.md` — **Test Parameters**: TUnit allows you to pass custom key-value parameters to your tests at runtime using the --test-parameter command-line option.
- `docs/execution/repeating.md` — **Repeating**: If you want to repeat a test, add a [Repeat] attribute onto your test method or class.
- `docs/execution/retrying.md` — **Retrying**: Unfortunately sometimes our tests hit issues.
- `docs/execution/test-filters.md` — **Test Filters**: Running TUnit via dotnet run supports test filters.
- `docs/execution/timeouts.md` — **Timeouts**: If you want to stop a test after a specified amount of time, add a [Timeout] attribute onto your test method or class.

### `docs/extending/`

- `docs/extending/argument-formatters.md` — **Argument Formatters**: When writing data-driven tests, especially with custom classes as arguments, the test explorer may only show the class name, making it hard to distinguish te…
- `docs/extending/built-in-extensions.md` — **Extensions**: As TUnit is built on top of Microsoft.Testing.Platform, it can tap into generic testing extension packages.
- `docs/extending/code-coverage.md` — **Code Coverage**: TUnit includes built-in code coverage support via Microsoft.Testing.Extensions.CodeCoverage, which is automatically included when you install the TUnit meta…
- `docs/extending/data-source-generators.md` — **Data Source Generators**: TUnit provides several base classes for creating custom data source generators
- `docs/extending/display-names.md` — **Display Names**: If you want simple control over the name of a test, you can use the [DisplayName(...)] attribute.
- `docs/extending/dynamic-tests.md` — **Dynamically Created Tests**: TUnit offers the ability to create your tests via dynamic code, as opposed to the standard [Test] attribute and data attributes.
- `docs/extending/exception-handling.md` — **Exception Handling**: When a test fails, TUnit throws an exception.
- `docs/extending/extension-points.md` — **Extension Points**: TUnit provides several extension points that allow you to customize and extend the framework's behavior.
- `docs/extending/libraries.md` — **Libraries**: When building a reusable library that defines shared hooks, custom attributes, base classes, or data sources for TUnit, reference TUnit.Core instead of the m…
- `docs/extending/logging.md` — **Logging**: TUnit provides a flexible logging system that captures all test output and routes it to configurable destinations called "log sinks".

### `docs/getting-started/`

- `docs/getting-started/installation.md` — **Installing TUnit**: Quick Start
- `docs/getting-started/running-your-tests.md` — **Running your tests**: As TUnit is built on-top of the newer Microsoft.Testing.Platform, and combined with the fact that TUnit tests are source generated, running your tests is ava…
- `docs/getting-started/writing-your-first-test.md` — **Writing your first test**: Quick Start: Complete Example

### `docs/guides/`

- `docs/guides/best-practices.md` — **Tips & Pitfalls**: TUnit-specific tips to avoid common mistakes.
- `docs/guides/distributed-tracing.md` — **Distributed Tracing**: This page is for users wiring TUnit up to a tracing backend like Seq, Jaeger, Tempo, or the Aspire dashboard.
- `docs/guides/html-report.md` — **HTML Test Report**: TUnit automatically generates a rich HTML test report after every test run.
- `docs/guides/performance.md` — **Performance Best Practices**: This guide provides recommendations for optimizing test performance and ensuring your TUnit test suite runs efficiently.
- `docs/guides/philosophy.md` — **Philosophy**: TUnit does some things differently from other .NET testing frameworks.
- `docs/guides/report-aggregation.md` — **Aggregated Reports (Multiple Test Projects)**: When you run several test projects with a single command — dotnet test on a solution, or one dotnet run per microservice test suite — each project runs in it…

### `docs/migration/`

- `docs/migration/mstest.md` — **Migrating from MSTest**: Migrating from MSTest to TUnit can improve test execution speed.
- `docs/migration/nunit.md` — **Migrating from NUnit**: Migrating from NUnit to TUnit can improve test execution speed.
- `docs/migration/testcontext-interface-organization.md` — **TestContext Interface Organization Migration Guide**: Overview
- `docs/migration/xunit.md` — **Migrating from xUnit.net**: Migrating from xUnit to TUnit can improve test execution speed.

### `docs/reference/`

- `docs/reference/command-line-flags.md` — **Command Line Flags**: Please note that for the coverage and trx report, you need to install additional extensions
- `docs/reference/environment-variables.md` — **Environment Variables**: TUnit supports configuration through environment variables, allowing you to set defaults without modifying command-line arguments.
- `docs/reference/programmatic-configuration.md` — **Programmatic Configuration**: Overview
- `docs/reference/test-configuration.md` — **Test Configuration**: TUnit supports having a testconfig.json file within your test project.

### `docs/writing-tests/`

- `docs/writing-tests/aot.md` — **AOT Compatibility and Generic Tests**: TUnit's source generation mode provides compile-time safety and performance benefits, but requires specific patterns for advanced scenarios like generic test…
- `docs/writing-tests/arguments.md` — **Data Driven Tests**: Inject compile-time known data via [Arguments(...)] attributes.
- `docs/writing-tests/artifacts.md` — **Test Artifacts**: Test artifacts are files (screenshots, logs, videos, JSON dumps, etc.) that you can attach to your tests.
- `docs/writing-tests/class-data-source.md` — **Injectable Class Data Source**: The ClassDataSource attribute is used to instantiate and inject in new classes as parameters to your tests and/or test classes.
- `docs/writing-tests/combined-data-source.md` — **CombinedDataSources**: Overview
- `docs/writing-tests/culture.md` — **Culture**: The Culture] attribute sets the [current Culture for the duration of a test.
- `docs/writing-tests/data-driven-overview.md` — **Choosing a Data Approach**: TUnit offers several ways to provide data to your tests.
- `docs/writing-tests/defer-enumeration.md` — **Deferring Data Source Enumeration**: By default, data sources are enumerated during test discovery — every row becomes its own test node, so a data source that produces thousands of cases produc…
- `docs/writing-tests/dependency-injection.md` — **Dependency Injection**: TUnit provides two mechanisms for controlling how test classes are constructed: the low-level IClassConstructor interface and the higher-level DependencyInje…
- `docs/writing-tests/event-subscribing.md` — **Event Subscribing**: Objects associated with your tests have the ability to subscribe to lifecycle events generated by TUnit.
- `docs/writing-tests/explicit.md` — **Explicit**: If you want a test to only be run explicitly (and not part of all general tests) then you can add the [Explicit] attribute.
- `docs/writing-tests/generic-attributes.md` — **Generic Attributes**: TUnit provides generic versions of several attributes that offer enhanced type safety and better IDE support.
- `docs/writing-tests/hooks.md` — **Hooks**: Hooks let you run code at specific points in the test lifecycle using [Before] / [BeforeEvery] and [After] / [AfterEvery] attributes.
- `docs/writing-tests/lifecycle.md` — **Test Lifecycle Overview**: TUnit provides multiple mechanisms for hooking into the test lifecycle
- `docs/writing-tests/matrix-tests.md` — **Matrix Tests**: The Matrix data source is a way to specify different arguments per parameter, and then generate every possible combination of all of those arguments.
- `docs/writing-tests/method-data-source.md` — **Method Data Sources**: A limitation of passing data in with [Arguments(...)] is that the data must be constant values.
- `docs/writing-tests/mocking.md` — **TUnit.Mocks**: TUnit.Mocks is a source-generated, AOT-compatible mocking framework.
- `docs/writing-tests/mocking/advanced.md` — **Advanced Features**: Events
- `docs/writing-tests/mocking/argument-matchers.md` — **Argument Matchers**: Argument matchers control which calls a setup or verification matches.
- `docs/writing-tests/mocking/http.md` — **HTTP Mocking**: TUnit.Mocks.Http provides MockHttpHandler — a drop-in HttpMessageHandler replacement for testing code that uses HttpClient.
- `docs/writing-tests/mocking/logging.md` — **Logging**: TUnit.Mocks.Logging provides MockLogger — a simple ILogger implementation that captures log entries for inspection and verification.
- `docs/writing-tests/mocking/setup.md` — **Setup & Stubbing**: Methods are called directly on Mock — the chain method (.Returns(), .Throws(), etc.) makes it a setup.
- `docs/writing-tests/mocking/verification.md` — **Verification**: Verification uses the same methods as setup — the chain method (.WasCalled(), .WasNeverCalled()) makes it a verification instead of a setup.
- `docs/writing-tests/nested-data-sources.md` — **Nested Data Sources with Initialization**: When writing integration tests, you often need complex test fixtures that depend on other initialized resources.
- `docs/writing-tests/ordering.md` — **Test Ordering & Dependencies**: Ordering with [Order]
- `docs/writing-tests/property-injection.md` — **Property Injection**: TUnit's AOT-compatible property injection system makes it easy to initialize properties on your test class with compile-time safety and excellent performance.
- `docs/writing-tests/skip.md` — **Skipping Tests**: If you want to simply skip a test, just place a [Skip(reason)] attribute on your test with an explanation of why you're skipping it.
- `docs/writing-tests/test-context.md` — **Test Context**: All tests have a TestContext object available to them.
- `docs/writing-tests/test-data-row.md` — **Test Data Row Metadata**: When using data sources like [MethodDataSource] or [ClassDataSource], you may want to customize individual test cases with specific display names, skip reaso…
- `docs/writing-tests/things-to-know.md` — **Things to know**: TUnit has made some decisions by design.
