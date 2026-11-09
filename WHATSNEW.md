# TUnit v1.68.17 → v1.81.10

Compare: https://github.com/thomhurst/TUnit/compare/v1.68.17...v1.81.10

## Releases

### v1.69.0

* feat(templates): add enableDotCover flag (#6714) by @ForNeVeR in https://github.com/thomhurst/TUnit/pull/6844
* fix: don't request semantic models for attribute syntax from other compilations (DevKit crash) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6855
* fix(ci): restore net472 PublicAPI tests on Windows by @thomhurst in https://github.com/thomhurst/TUnit/pull/6857
* perf(html-report): stream report JSON through pooled chunks and overlap sidecar serialization by @thomhurst in https://github.com/thomhurst/TUnit/pull/6860
* chore(renovate): cap Microsoft.Build packages below 18.10.0 by @thomhurst in https://github.com/thomhurst/TUnit/pull/6863
* perf: shrink generated per-class test source static constructors (~40% less startup JIT) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6859
* refactor: remove unreachable decimal source-text path from GenerateAttributeInstantiation by @thomhurst in https://github.com/thomhurst/TUnit/pull/6856
* perf: cut per-test allocations in discovery and execution (-61% at 10k tests) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6861
* perf: stop hashing per-test event receivers during registration (data-driven tests 2.9x faster at 10k) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6858
* perf(analyzers): cut TUnit analyzer build time ~60% on large test projects by @thomhurst in https://github.com/thomhurst/TUnit/pull/6862
* @ForNeVeR made their first contribution in https://github.com/thomhurst/TUnit/pull/6844

### v1.69.16

* fix: preserve TRX results when session cleanup fails by @Sing303 in https://github.com/thomhurst/TUnit/pull/6879
* @Sing303 made their first contribution in https://github.com/thomhurst/TUnit/pull/6879

### v1.69.21

* fix: preserve JUnit results after session cancellation by @Sing303 in https://github.com/thomhurst/TUnit/pull/6882
* feat: warn when setup hooks pass the test execution token by @Sing303 in https://github.com/thomhurst/TUnit/pull/6883
* fix: complete DedicatedThreadExecutor tests only after CleanUp() returns by @glennawatson in https://github.com/thomhurst/TUnit/pull/6886
* @glennawatson made their first contribution in https://github.com/thomhurst/TUnit/pull/6886

### v1.69.24

* fix: skip Ctrl+C handling where Console.CancelKeyPress is unsupported by @glennawatson in https://github.com/thomhurst/TUnit/pull/6889

### v1.70.0

* feat: clear parallel constraints and limiter during test registration by @thomhurst in https://github.com/thomhurst/TUnit/pull/6897
* fix(mocks): emit valid lambdas for Task/ValueTask-returning delegate mocks by @thomhurst in https://github.com/thomhurst/TUnit/pull/6896

### v1.70.1

* fix: don't run DedicatedThreadExecutor continuations inline on the dedicated thread by @thomhurst in https://github.com/thomhurst/TUnit/pull/6898

### v1.71.0

* perf: lighter per-test trace bookkeeping for the HTML report (-12% allocations at 10k tests) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6910
* perf(html-report): parallel report serialization + optimized hot writers (-26% end-of-session time) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6911
* perf: emit source-generated test types after user code (Defender scan 5s → 0.2s at 10k tests) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6908
* perf(source-gen): bound generated test-entry methods (data-driven startup JIT -45%) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6909
* fix: avoid blocking waiting callers during IAsyncInitializer initialization by @Sing303 in https://github.com/thomhurst/TUnit/pull/6906
* perf(analyzers): cut binding and symbol lookups in analyzer hot paths (TUnit.Analyzers -89% on TestProject) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6917
* fix(source-gen): model equality covers every emitted field; infrastructure refreshes on reference changes by @thomhurst in https://github.com/thomhurst/TUnit/pull/6912
* perf(mocks): memoize generator discovery per compilation and decouple emitted source from call-site locations by @thomhurst in https://github.com/thomhurst/TUnit/pull/6913
* fix(packaging): skip the source generator when disabled and replace the broken Polyfill injection by @thomhurst in https://github.com/thomhurst/TUnit/pull/6915
* refactor(analyzers): address review feedback from #6917 by @thomhurst in https://github.com/thomhurst/TUnit/pull/6919
* perf(source-gen): remove whole-compilation scans from static property, property injection and AOT converter generators by @thomhurst in https://github.com/thomhurst/TUnit/pull/6914
* perf(assertions-source-gen): make assertion generators properly incremental by @thomhurst in https://github.com/thomhurst/TUnit/pull/6916
* perf(source-gen): make TestMetadataGenerator pipeline values equatable by @thomhurst in https://github.com/thomhurst/TUnit/pull/6918

### v1.72.0

* perf(source-gen): resolve parameter reflection info through a shared runtime helper by @thomhurst in https://github.com/thomhurst/TUnit/pull/6923
* perf(analyzers): trim remaining analyzer hot-path symbol lookups and binds by @thomhurst in https://github.com/thomhurst/TUnit/pull/6928
* perf(mocks): move shared MockCall wrapper plumbing into runtime base classes by @thomhurst in https://github.com/thomhurst/TUnit/pull/6929
* perf(source-gen): close incremental caching gaps in static property and property injection generators by @thomhurst in https://github.com/thomhurst/TUnit/pull/6925
* perf(source-gen): stop InfrastructureGenerator pinning an old Compilation by @thomhurst in https://github.com/thomhurst/TUnit/pull/6926
* perf(assertions-analyzers): cache assertion symbols and cut per-call work by @thomhurst in https://github.com/thomhurst/TUnit/pull/6927
* perf(source-gen): emit hooks per class with direct, non-async bodies by @thomhurst in https://github.com/thomhurst/TUnit/pull/6924
* test: fix flaky ObjectInitializer continuation-thread test by @thomhurst in https://github.com/thomhurst/TUnit/pull/6932
* fix: CI flakes from leaked hook contexts, ActivityCollector race and Repro5700 rendezvous by @thomhurst in https://github.com/thomhurst/TUnit/pull/6933
* fix(aspnetcore): honor WebApplicationFactoryClientOptions in CreateClient by @thomhurst in https://github.com/thomhurst/TUnit/pull/6931

### v1.72.4

* fix(source-gen): stop parameter resolver keeping every non-public test-class method (IL2111) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6937

### v1.72.10

* fix(source-gen): adapt ValueTask<T> test results by @zion-sati in https://github.com/thomhurst/TUnit/pull/6930
* @zion-sati made their first contribution in https://github.com/thomhurst/TUnit/pull/6930

### v1.72.16

* docs: add Moq, NSubstitute, and FakeItEasy migration guides for TUnit.Mocks by @thomhurst in https://github.com/thomhurst/TUnit/pull/6951

### v1.73.0

* fix(aspnetcore): initialize web application factories through services by @thomhurst in https://github.com/thomhurst/TUnit/pull/6956
* docs: give the site a green-bar identity by @thomhurst in https://github.com/thomhurst/TUnit/pull/6959
* docs: make examples work on Linux and macOS by @Quattordici in https://github.com/thomhurst/TUnit/pull/6964
* fix(runtime): correct Windows-shaped assumptions on Linux and macOS by @Quattordici in https://github.com/thomhurst/TUnit/pull/6962
* build: make the repo build, test and script cleanly on macOS and Linux by @Quattordici in https://github.com/thomhurst/TUnit/pull/6963
* fix(globalization): culture-invariant generators, analyzers and code fixers; enforce it by @Quattordici in https://github.com/thomhurst/TUnit/pull/6969
* chore: update NuGet dependencies and split versions per target framework by @Quattordici in https://github.com/thomhurst/TUnit/pull/6972
* feat: add [PairwiseDataSource] for all-pairs test case generation by @AArnott in https://github.com/thomhurst/TUnit/pull/6971
* @Quattordici made their first contribution in https://github.com/thomhurst/TUnit/pull/6964

### v1.73.5

* fix: Ignore default start timestamps in HTML report by @SnakyBeaky in https://github.com/thomhurst/TUnit/pull/6942
* fix(playwright): send trace context headers only to origins under test by @thomhurst in https://github.com/thomhurst/TUnit/pull/6993

### v1.73.19

* fix(fscheck): apply Verbose, QuietOnSuccess and Parallelism; validate Replay by @JesseKlaasse in https://github.com/thomhurst/TUnit/pull/7001
* @JesseKlaasse made their first contribution in https://github.com/thomhurst/TUnit/pull/7001

### v1.74.0

* fix(mocks): eliminate trim/AOT warnings on Native AOT publish by @thomhurst in https://github.com/thomhurst/TUnit/pull/7029
* feat(engine): raise thread pool minimum when blocking tests starve the pool by @thomhurst in https://github.com/thomhurst/TUnit/pull/7030
* feat(mocks): add ClearCalls, PassThrough toggle and string/type/reference matchers by @Quattordici in https://github.com/thomhurst/TUnit/pull/7018

### v1.75.0

* docs: explain when ClassDataSource instances are created by @thomhurst in https://github.com/thomhurst/TUnit/pull/7046
* feat(aspnetcore): add PerTestWebApplicationTest with per-test CreateFactoryAsync by @thomhurst in https://github.com/thomhurst/TUnit/pull/7047
* fix(aspnetcore): make WebApplicationTest.HttpCapture return the registered capture by @thomhurst in https://github.com/thomhurst/TUnit/pull/7048

### v1.76.0

* chore: add OSS scanner config, threat model and SECURITY.md by @thomhurst in https://github.com/thomhurst/TUnit/pull/7080
* fix(deps): patch MessagePack for Aspire and use per-TFM Microsoft.Extensions.Http by @Quattordici in https://github.com/thomhurst/TUnit/pull/7072
* fix: skip tests marked with an empty skip reason by @thomhurst in https://github.com/thomhurst/TUnit/pull/7083
* fix(engine): report the engine mode actually selected in the banner by @thomhurst in https://github.com/thomhurst/TUnit/pull/7085
* fix(engine): order keyed NotInParallel tests by priority, not hash code by @thomhurst in https://github.com/thomhurst/TUnit/pull/7090
* fix: remove root causes of flaky tests and the broken Apple smoke jobs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7095
* fix(engine): run synchronous keyed NotInParallel tests concurrently by @thomhurst in https://github.com/thomhurst/TUnit/pull/7087
* fix(sourcegen): run every [Arguments] row that infers the same generic type by @thomhurst in https://github.com/thomhurst/TUnit/pull/7100
* fix: same filter path and display name for generic tests in both engine modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7110
* fix(engine): apply max parallelism cap to keyed NotInParallel tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7084
* fix(ci): install only Chromium for Playwright and wait on dpkg lock by @thomhurst in https://github.com/thomhurst/TUnit/pull/6994
* fix(core): keep the engine-selected execution mode when late assemblies load by @thomhurst in https://github.com/thomhurst/TUnit/pull/7091
* fix(engine): end fail-fast runs without crashing the test host by @thomhurst in https://github.com/thomhurst/TUnit/pull/7115
* test: stop the AOT [EngineTest=Pass] run hitting its 5 minute budget by @thomhurst in https://github.com/thomhurst/TUnit/pull/7125
* fix(engine): align reflection-mode data sources and hooks with source-gen by @thomhurst in https://github.com/thomhurst/TUnit/pull/7094
* fix(pipeline): stop skipping the NuGet package tester modules by @thomhurst in https://github.com/thomhurst/TUnit/pull/7127
* ci: take AOT publishes and doc snippets off the Ubuntu critical path by @thomhurst in https://github.com/thomhurst/TUnit/pull/7128
* fix(analyzers): TUnit0001 false positive for MethodDataSource on generic type-parameter parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7109
* fix: report generic class constraint violations as failed tests in both modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7112
* ci: cut runner contention and the AOT publish off the critical path by @thomhurst in https://github.com/thomhurst/TUnit/pull/7131
* fix(assertions): make cross-type IsEqualTo work for numeric and nullable arguments on C# 12 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7086
* fix(engine): substitute class type arguments and array element types in build-time constraint checks by @thomhurst in https://github.com/thomhurst/TUnit/pull/7102
* ci: test the NuGet packages on Windows in their own job by @thomhurst in https://github.com/thomhurst/TUnit/pull/7130
* fix(sourcegen): bind params T[] on generic test methods by @thomhurst in https://github.com/thomhurst/TUnit/pull/7101
* fix(engine): run every [Arguments] row on generic test classes in both modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7111
* fix(engine): use last inferred type for repeated generic parameters by @theluckystrike in https://github.com/thomhurst/TUnit/pull/7134
* Make the test suite pass in every environment and run fully in CI by @Quattordici in https://github.com/thomhurst/TUnit/pull/7129
* fix(assertions): skip using directive for global-namespace assertion types by @thomhurst in https://github.com/thomhurst/TUnit/pull/7139
* fix(core): format numeric display-name arguments with the invariant culture by @thomhurst in https://github.com/thomhurst/TUnit/pull/7138
* fix(engine): dispose data-source objects of rows that end as failed tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7150
* Fix net472 compile gate failure in assertions source generator tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7170
* fix(sourcegen): close generic methods of generic classes on every class source by @thomhurst in https://github.com/thomhurst/TUnit/pull/7152
* fix(engine): infer object for null rows on generic test methods in reflection mode by @thomhurst in https://github.com/thomhurst/TUnit/pull/7142
* fix(engine): report every test once on fail-fast runs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7145
* test(engine): stop whole-process budgets killing healthy scheduling engine tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7177
* feat(analyzers): report MethodDataSource Arguments that fit two overloads equally (TUnit0076) by @thomhurst in https://github.com/thomhurst/TUnit/pull/7181
* fix(sourcegen): render top-level dynamic as object so typeof compiles by @thomhurst in https://github.com/thomhurst/TUnit/pull/7182
* fix(sourcegen): pair each GenerateGenericTest type only with its typed ClassDataSource<T> by @thomhurst in https://github.com/thomhurst/TUnit/pull/7188
* fix(engine): run untyped [Arguments(null)] rows on generic classes instead of dropping them by @thomhurst in https://github.com/thomhurst/TUnit/pull/7203
* fix(engine): report generic test classes by their generic type definition in TRX by @thomhurst in https://github.com/thomhurst/TUnit/pull/7200
* test(sourcegen): parse snapshot fixtures as a real build does by @thomhurst in https://github.com/thomhurst/TUnit/pull/7189
* refactor(engine): dedupe reflection generic discovery by @thomhurst in https://github.com/thomhurst/TUnit/pull/7183
* test: make TimeoutHelperTests deterministic under thread-pool load by @thomhurst in https://github.com/thomhurst/TUnit/pull/7180
* fix(analyzers): accept null MethodDataSource arguments for nullable parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7179
* test(assertions): make WaitsFor cancellation tests robust to slow CI runners by @thomhurst in https://github.com/thomhurst/TUnit/pull/7176
* fix(assertions): support [AssertionFrom] with unbound generic types by @thomhurst in https://github.com/thomhurst/TUnit/pull/7144
* fix(sourcegen): pass omitted optional defaults so calls bind to the test method by @thomhurst in https://github.com/thomhurst/TUnit/pull/7148
* fix(engine): reuse the first class-data fetch for the first test of a class row by @thomhurst in https://github.com/thomhurst/TUnit/pull/7195
* fix(engine): report [Arguments] rows that break constraints with [GenerateGenericTest] in reflection mode by @thomhurst in https://github.com/thomhurst/TUnit/pull/7196
* fix(generic): infer object when a type parameter gets null and a value-type value by @thomhurst in https://github.com/thomhurst/TUnit/pull/7198
* fix(engine): dispose data-source objects of skipped tests and rows by @thomhurst in https://github.com/thomhurst/TUnit/pull/7191
* fix(sourcegen): bind omitted optional parameters of generic tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7199
* fix(generic): infer method type arguments from typed data sources on generic classes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7186
* fix: restore main build and stop the macOS AOT publish timing out by @thomhurst in https://github.com/thomhurst/TUnit/pull/7216
* ci: stop heavy modules overlapping the AOT test-app publish by @thomhurst in https://github.com/thomhurst/TUnit/pull/7217
* ci: make the NuGet tester AOT publish's wait on the AOT test-app publish optional by @thomhurst in https://github.com/thomhurst/TUnit/pull/7219
* chore(sourcegen): fix CS8602 warning in InferTypesFromArgumentsAttribute by @thomhurst in https://github.com/thomhurst/TUnit/pull/7218
* fix(sourcegen): report generic test rows whose type arguments cannot be inferred by @thomhurst in https://github.com/thomhurst/TUnit/pull/7187
* fix(generic): explain declared-type inference for broad data source types by @thomhurst in https://github.com/thomhurst/TUnit/pull/7154
* fix(engine): run method rows only on the generic class instantiation they infer by @thomhurst in https://github.com/thomhurst/TUnit/pull/7149
* Fix TUnit0014 on interface implementations, Aspire exit-code culture and [AssertionFrom] expectation messages by @Quattordici in https://github.com/thomhurst/TUnit/pull/7135
* fix: bind a CancellationToken declared anywhere and keep a single tuple parameter whole by @thomhurst in https://github.com/thomhurst/TUnit/pull/7185
* test: fix Windows CI by lowering net472 expectation count guard by @thomhurst in https://github.com/thomhurst/TUnit/pull/7228
* fix(sourcegen): infer generic method types from any MethodDataSource row shape by @thomhurst in https://github.com/thomhurst/TUnit/pull/7143
* ci: move the AOT test-app publish and AOT engine tests into their own workflow by @thomhurst in https://github.com/thomhurst/TUnit/pull/7226
* @theluckystrike made their first contribution in https://github.com/thomhurst/TUnit/pull/7134

### v1.76.28

* Remove legacy JSON output implementation by @Saad-elnagar in https://github.com/thomhurst/TUnit/pull/7234
* fix(engine): drop row-scoped data sources from failed test metadata by @kenny-ish in https://github.com/thomhurst/TUnit/pull/7079
* Merge the analyzer release tables under one New Rules section (RS2007) by @bfs2021 in https://github.com/thomhurst/TUnit/pull/7174
* fix: release finished test instances before session end by @thomhurst in https://github.com/thomhurst/TUnit/pull/7262
* fix: never hand out a disposed shared data-source instance by @thomhurst in https://github.com/thomhurst/TUnit/pull/7248
* @Saad-elnagar made their first contribution in https://github.com/thomhurst/TUnit/pull/7234
* @kenny-ish made their first contribution in https://github.com/thomhurst/TUnit/pull/7079
* @bfs2021 made their first contribution in https://github.com/thomhurst/TUnit/pull/7174

### v1.76.45

* chore(docs): remark Forgejo test summary compatability by @koryphaee in https://github.com/thomhurst/TUnit/pull/7272
* fix(aspire): cancel and join startup waits (#7277) by @thomhurst in https://github.com/thomhurst/TUnit/pull/7279
* fix(aspire): follow DCP runtime instances when reading resource logs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7283

### v1.77.0

* fix(engine): invoke OnTestRegistered on property-injected data sources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7292
* fix(sourcegen): globally qualify type names in property injection output by @lucaxchaves in https://github.com/thomhurst/TUnit/pull/7291
* test(sourcegen): snapshot property injection output for Core.* namespaces by @thomhurst in https://github.com/thomhurst/TUnit/pull/7293
* fix(aspire): detach kept resources from removed resources in ResourcesToRemove by @thomhurst in https://github.com/thomhurst/TUnit/pull/7295
* feat(engine): report unobserved task exceptions in session results by @thomhurst in https://github.com/thomhurst/TUnit/pull/7296
* fix(mocks): rename method type parameters that collide with the mocked type's by @thomhurst in https://github.com/thomhurst/TUnit/pull/7303
* feat(mocks): TM010 analyzer + code fix for Mock.Of<T>() -> T.Mock() by @thomhurst in https://github.com/thomhurst/TUnit/pull/7307
* feat(playwright): failure screenshots/traces and shared-browser disconnect diagnostics by @thomhurst in https://github.com/thomhurst/TUnit/pull/7309

### v1.78.0

* fix: Should().HaveSingleItem() returns the single item by @mvanhorn in https://github.com/thomhurst/TUnit/pull/7035
* feat(mocks): TM011 analyzer + code fix to declare mocks with the generated mock type by @thomhurst in https://github.com/thomhurst/TUnit/pull/7311
* fix(sourcegen): skip [Obsolete(error: true)] conversion operators in AotConverterGenerator by @thomhurst in https://github.com/thomhurst/TUnit/pull/7317

### v1.79.0

* test(sourcegen): parse fixtures as a real build in all generator test harnesses by @thomhurst in https://github.com/thomhurst/TUnit/pull/7319
* test(sourcegen): fix net472 compile of AotConverterScanTests obsolete-conversion fixture by @thomhurst in https://github.com/thomhurst/TUnit/pull/7330
* fix(sourcegen): emit typeof(Nullable<>) for a T? parameter of a generic test method by @thomhurst in https://github.com/thomhurst/TUnit/pull/7322
* test: fix ClassDataSourceTupleTests to exercise class-level tuple unwrapping by @thomhurst in https://github.com/thomhurst/TUnit/pull/7318
* fix(fsharp): pin FSharp.Core in TUnit.Assertions.FSharp independent of the building SDK by @thomhurst in https://github.com/thomhurst/TUnit/pull/7321
* fix(sourcegen): pick MethodDataSource overloads declared on base types like reflection by @thomhurst in https://github.com/thomhurst/TUnit/pull/7323
* fix(reflection): close generic methods over a typed data source's declared types without [GenerateGenericTest] by @thomhurst in https://github.com/thomhurst/TUnit/pull/7324
* fix(engine): run every overload of a [Test] method in filtered runs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7332
* fix: bind a tuple row whole to a tuple parameter followed by optional parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7341
* fix(core): keep and dispose data-source roots when object-graph tracking throws by @thomhurst in https://github.com/thomhurst/TUnit/pull/7342
* fix(engine): lower default maximum parallel tests to 2x processor count by @thomhurst in https://github.com/thomhurst/TUnit/pull/7354
* ci: cut duplicate TFM and packaging work from the Windows and macOS jobs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7357
* ci: run engine tests in their own job and drop the per-child test-host relaunch by @thomhurst in https://github.com/thomhurst/TUnit/pull/7364
* fix(sourcegen): split untyped class data source rows by the generic class type they infer by @thomhurst in https://github.com/thomhurst/TUnit/pull/7339
* fix(engine): read a generic class's own class-level [MethodDataSource] member on the closed class by @thomhurst in https://github.com/thomhurst/TUnit/pull/7336
* fix(analyzers): TUnit0001 unwraps only the Func/TestDataRow layers the runtime removes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7347
* test: make SharedType.None leakage tests independent of build order by @thomhurst in https://github.com/thomhurst/TUnit/pull/7385
* fix(generic): infer method type arguments from [Arguments<T>] rows in both modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7343
* fix(generic): infer class type arguments through T[] constructor parameters from any class row by @thomhurst in https://github.com/thomhurst/TUnit/pull/7346
* fix(engine): await the Task of async runtime dynamic tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7363
* feat(engine): add dispose spans for shared data-source objects by @thomhurst in https://github.com/thomhurst/TUnit/pull/7396
* fix(engine): stop copying build-time output to TestSessionContext by @thomhurst in https://github.com/thomhurst/TUnit/pull/7397
* feat(mocks): argument-aware Returns for Task/ValueTask members by @thomhurst in https://github.com/thomhurst/TUnit/pull/7404
* fix(generic): a type-free class [Arguments] row lets method rows infer T, with matching constructor binding in both modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7392
* feat(scripts): finish open loop PRs before starting new issues by @thomhurst in https://github.com/thomhurst/TUnit/pull/7423
* fix(mocks): preserve nullable generic constraints by @thomhurst in https://github.com/thomhurst/TUnit/pull/7414
* Retain class sources sharing an inferred generic instantiation by @thomhurst in https://github.com/thomhurst/TUnit/pull/7420
* Fix reflection data source overloads with omitted optional arguments by @thomhurst in https://github.com/thomhurst/TUnit/pull/7421
* feat(playwright): honor HEADED and BROWSER environment variables by @thomhurst in https://github.com/thomhurst/TUnit/pull/7395
* docs: enable Windows long paths before worktree checkout by @thomhurst in https://github.com/thomhurst/TUnit/pull/7416
* Fix duplicate dynamic builder invocation in reflection mode by @thomhurst in https://github.com/thomhurst/TUnit/pull/7424
* fix(mocks): bind explicit method type arguments on Mock.Of<IGeneric<X>>() by @thomhurst in https://github.com/thomhurst/TUnit/pull/7406
* fix(mocks): Is<T>(predicate) passes T, not T?, for non-nullable T by @thomhurst in https://github.com/thomhurst/TUnit/pull/7405
* fix(engine): deliver row builder-context events to the test and raise OnDispose once per test (#7381) by @thomhurst in https://github.com/thomhurst/TUnit/pull/7384
* fix: report generic classes whose data cannot infer types at compile time by @thomhurst in https://github.com/thomhurst/TUnit/pull/7425
* fix(core): hold shared instances fetched while runtime tests register by @thomhurst in https://github.com/thomhurst/TUnit/pull/7391
* fix(mocks): match null literals in generated predicate overloads by @thomhurst in https://github.com/thomhurst/TUnit/pull/7415
* fix(mocks): qualify extern-aliased types with their alias in generated code by @thomhurst in https://github.com/thomhurst/TUnit/pull/7403
* fix(generic): fail wrongly sized [GenerateGenericTest] in source-generated mode by @thomhurst in https://github.com/thomhurst/TUnit/pull/7344
* fix(sourcegen): generate a data source factory for [InstanceMethodDataSource] (#7225) by @thomhurst in https://github.com/thomhurst/TUnit/pull/7348
* fix(aspire): preserve caller cancellation over startup cleanup faults by @thomhurst in https://github.com/thomhurst/TUnit/pull/7447
* fix(tests): remove polling throughput requirement on shared runners by @thomhurst in https://github.com/thomhurst/TUnit/pull/7448
* fix(html-reporter): scope report state per session when sessions overlap by @thomhurst in https://github.com/thomhurst/TUnit/pull/7400
* fix(analyzers): validate class data against TestConstructor by @thomhurst in https://github.com/thomhurst/TUnit/pull/7449
* Infer generic method types from typed array rows in both discovery modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7460
* Share generic method inference policy between discovery modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7455
* Wrap runtime registration holds in an async scope by @thomhurst in https://github.com/thomhurst/TUnit/pull/7458
* Preserve generic class source rows and distinguish null collections by @thomhurst in https://github.com/thomhurst/TUnit/pull/7453
* Fix TUnit0001 for reference tuple data source rows by @thomhurst in https://github.com/thomhurst/TUnit/pull/7457
* Raise issue-pr-loop open-PR limit to 15 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7483
* Await resultless ValueTask data sources consistently by @thomhurst in https://github.com/thomhurst/TUnit/pull/7478
* Fix internals-access task MSBuild dependency compatibility by @thomhurst in https://github.com/thomhurst/TUnit/pull/7479
* fix: dispose session-lifetime DI scopes at session end by @thomhurst in https://github.com/thomhurst/TUnit/pull/7459
* Await concurrent ASP.NET Core application disposal by @thomhurst in https://github.com/thomhurst/TUnit/pull/7470
* Fix source generation for one-element ValueTuple parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7467
* Preserve loadable types during dynamic reflection discovery by @thomhurst in https://github.com/thomhurst/TUnit/pull/7495
* Set Verify solution context for project-only builds by @thomhurst in https://github.com/thomhurst/TUnit/pull/7488
* Fix inherited constructor data in reflection discovery by @thomhurst in https://github.com/thomhurst/TUnit/pull/7491
* Fix constructor-order-dependent instance data source diagnostic by @thomhurst in https://github.com/thomhurst/TUnit/pull/7502
* Isolate shared disposal span capture by parent activity by @thomhurst in https://github.com/thomhurst/TUnit/pull/7492
* Fix preserved generic tuple binding in reflection mode by @thomhurst in https://github.com/thomhurst/TUnit/pull/7487
* Fix core generator test nullable and constant-assertion warnings by @thomhurst in https://github.com/thomhurst/TUnit/pull/7494
* Fix AutoFixture fixture trimming contracts by @thomhurst in https://github.com/thomhurst/TUnit/pull/7500

### v1.80.0

* Share evaluated constructor-row state across discovery modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7497
* Diagnose static data-source properties in inaccessible containing types by @thomhurst in https://github.com/thomhurst/TUnit/pull/7503
* Extract typed-row binding and verify invocation parity by @thomhurst in https://github.com/thomhurst/TUnit/pull/7507
* Accept omitted optional MethodDataSource arguments in TUnit0001 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7486
* Preserve null-containing tuples from static method data sources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7469
* Fix dependencies on deferred enumeration tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7471
* Preserve DI scope ownership and synchronize concurrent property registration by @thomhurst in https://github.com/thomhurst/TUnit/pull/7476
* Infer typed row generic arguments through interfaces and base classes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7508
* Keep session cleanup from disposing another session’s data sources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7509
* Fix recursive generated tuple argument conversions by @thomhurst in https://github.com/thomhurst/TUnit/pull/7515
* Share generic class row selection and pairing policy by @thomhurst in https://github.com/thomhurst/TUnit/pull/7498
* Raise data-source delegates at test lifecycle stages by @thomhurst in https://github.com/thomhurst/TUnit/pull/7521
* Fix class argument literals to use constructor parameter types by @thomhurst in https://github.com/thomhurst/TUnit/pull/7496
* Accept numeric widening for single reference-tuple data parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7510
* fix(core): preserve optional F# async support without AOT warnings by @thomhurst in https://github.com/thomhurst/TUnit/pull/7526
* Fix timeouts for synchronously blocking test bodies by @thomhurst in https://github.com/thomhurst/TUnit/pull/7527
* Fix Native AOT getters for generic test class property metadata by @thomhurst in https://github.com/thomhurst/TUnit/pull/7524
* Refresh stale core generator snapshots by @thomhurst in https://github.com/thomhurst/TUnit/pull/7549
* Infer generic class types from inherited literal arguments by @thomhurst in https://github.com/thomhurst/TUnit/pull/7544
* Make duplicate-stop cancellation regression independent of thread-pool scheduling by @thomhurst in https://github.com/thomhurst/TUnit/pull/7546
* Fix colliding generator diagnostic IDs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7538
* Fix generic array binding inside tuple data-source parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7541
* Discover AOT converters from method data source return types by @thomhurst in https://github.com/thomhurst/TUnit/pull/7547
* Check tuple conversion analyzer policy against runtime binding by @thomhurst in https://github.com/thomhurst/TUnit/pull/7559
* Deduplicate disposal span callbacks on .NET 8 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7557
* Preserve generic tuple rows from instance data sources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7548
* Expect source operators to bind in AOT in the tuple conversion matrix by @thomhurst in https://github.com/thomhurst/TUnit/pull/7580
* Preserve containing generic types in TUnit0001 diagnostics by @thomhurst in https://github.com/thomhurst/TUnit/pull/7563
* Populate reflection class property metadata by @thomhurst in https://github.com/thomhurst/TUnit/pull/7550
* Verify every generic class/method argument pair executes once by @thomhurst in https://github.com/thomhurst/TUnit/pull/7558
* Exclude indexers from generated class property metadata by @thomhurst in https://github.com/thomhurst/TUnit/pull/7560
* Fix synchronous factory timeout cancellation classification by @thomhurst in https://github.com/thomhurst/TUnit/pull/7561
* Add packaged F# async trimming smoke coverage by @thomhurst in https://github.com/thomhurst/TUnit/pull/7562
* Remove unused metadata generation entry points by @thomhurst in https://github.com/thomhurst/TUnit/pull/7570
* Remove unused streaming test builder path by @thomhurst in https://github.com/thomhurst/TUnit/pull/7535
* Isolate test registration callback failures by @thomhurst in https://github.com/thomhurst/TUnit/pull/7556
* Update mcr.microsoft.com/dotnet/sdk Docker tag to v11 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7513
* Update dependency Microsoft.Kiota.Abstractions to 2.1.6 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7512
* Update all non-major dependencies to 1.79.0 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7528
* Update all non-major dependencies by @thomhurst in https://github.com/thomhurst/TUnit/pull/7536

### v1.81.0

* Extract Windows engine hang dump stacks in CI by @thomhurst in https://github.com/thomhurst/TUnit/pull/7584
* Cut STAThreadTests repeats so the Windows reflection pass run fits its timeout by @thomhurst in https://github.com/thomhurst/TUnit/pull/7594
* Preserve expected-value semantics when migrating xUnit Assert.Single by @thomhurst in https://github.com/thomhurst/TUnit/pull/7586
* Capture Windows loader ownership and thread CPU times by @thomhurst in https://github.com/thomhurst/TUnit/pull/7603
* Isolate the full passing engine session from sibling test processes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7606
* Remove unused concrete metadata generation chain by @thomhurst in https://github.com/thomhurst/TUnit/pull/7569
* Avoid temporary arrays in singleton tuple binding by @thomhurst in https://github.com/thomhurst/TUnit/pull/7583
* Fix ParallelTests overlap assertion for late repetitions by @thomhurst in https://github.com/thomhurst/TUnit/pull/7600
* Fix nullable generic class method-row analyzer validation by @thomhurst in https://github.com/thomhurst/TUnit/pull/7613
* Fix generated property injection into boxed structs by @thomhurst in https://github.com/thomhurst/TUnit/pull/7612
* Make Playwright template navigation deterministic by @thomhurst in https://github.com/thomhurst/TUnit/pull/7604
* Release objects and complete teardown for dependency-skipped tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7605
* Support typed tuple rows before optional parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7608
* Cover null rows in generic class type inference by @thomhurst in https://github.com/thomhurst/TUnit/pull/7621
* Skip certificate trust preparation for HTTP-only Aspire test resources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7618
* Accept convertible typed rows before optional test parameters by @thomhurst in https://github.com/thomhurst/TUnit/pull/7619
* Preserve nullable class discovery parity and constructor precedence by @thomhurst in https://github.com/thomhurst/TUnit/pull/7614
* Preserve whole tuple rows before omitted trailing arrays by @thomhurst in https://github.com/thomhurst/TUnit/pull/7625
* Fix reflection inference for concrete params arrays by @thomhurst in https://github.com/thomhurst/TUnit/pull/7627
* Remove obsolete nullable method-row analyzer suppression by @thomhurst in https://github.com/thomhurst/TUnit/pull/7626
* Infer generic method arguments from instance data sources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7630
* test: cover discarded method-row lifecycle isolation (#7373) by @thomhurst in https://github.com/thomhurst/TUnit/pull/7632
* Allow DI scopes to opt out of resolved object ownership by @thomhurst in https://github.com/thomhurst/TUnit/pull/7633
* Give TestBuilder rows explicit cleanup owners by @thomhurst in https://github.com/thomhurst/TUnit/pull/7637
* Preserve whole-tuple inference across wrapped and async sources by @thomhurst in https://github.com/thomhurst/TUnit/pull/7641
* Fix reported compiler warnings in regression fixtures by @thomhurst in https://github.com/thomhurst/TUnit/pull/7645
* fix(core): track external ownership per row scope by @thomhurst in https://github.com/thomhurst/TUnit/pull/7635
* Fix remaining regression fixture compiler warnings by @thomhurst in https://github.com/thomhurst/TUnit/pull/7646
* Fix generic class argument row edge cases by @thomhurst in https://github.com/thomhurst/TUnit/pull/7647
* Preserve sole-tuple inference and runtime conversion parity by @thomhurst in https://github.com/thomhurst/TUnit/pull/7643
* Match method data source attributes by fully qualified identity by @thomhurst in https://github.com/thomhurst/TUnit/pull/7649
* Treat null method data sources as empty in both execution modes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7652
* Fix xUnit proper-set migration operands and strictness by @thomhurst in https://github.com/thomhurst/TUnit/pull/7653
* Fix mock setup identifier collisions by @thomhurst in https://github.com/thomhurst/TUnit/pull/7658
* fix(generator): qualify built-in data-source row classification by @thomhurst in https://github.com/thomhurst/TUnit/pull/7651
* Capture macOS native runtime crashes for diagnosis by @thomhurst in https://github.com/thomhurst/TUnit/pull/7659
* Restore nullable diagnostics in mock generated-code regression guards by @thomhurst in https://github.com/thomhurst/TUnit/pull/7661
* Avoid mock predicate conversion local name collisions by @thomhurst in https://github.com/thomhurst/TUnit/pull/7655
* Install browsers with the resolved .NET Playwright package by @thomhurst in https://github.com/thomhurst/TUnit/pull/7673
* Remove nullable and assertion warnings from unit tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/7670
* Preserve keyword escapes in generated attribute factory type names by @thomhurst in https://github.com/thomhurst/TUnit/pull/7669
* Fix default mock argument matching by @thomhurst in https://github.com/thomhurst/TUnit/pull/7676
* Preserve category and property filters on generic discovery failures by @thomhurst in https://github.com/thomhurst/TUnit/pull/7663
* Preserve keyword escapes in generated type expressions by @thomhurst in https://github.com/thomhurst/TUnit/pull/7675
* Encapsulate row lifetime and constructor state replay by @thomhurst in https://github.com/thomhurst/TUnit/pull/7678
* Diagnose unsupported span params on test methods by @thomhurst in https://github.com/thomhurst/TUnit/pull/7679
* Honor inherited tests on generic classes in reflection discovery by @thomhurst in https://github.com/thomhurst/TUnit/pull/7665
* Update all non-major dependencies by @thomhurst in https://github.com/thomhurst/TUnit/pull/7593

### v1.81.5

* feat(sourcegen): inherit XML docs from [GenerateAssertion] source methods by @JohnVerheij in https://github.com/thomhurst/TUnit/pull/7687
* fix(mocks): stop verification leaving setups on void-shaped members by @thomhurst in https://github.com/thomhurst/TUnit/pull/7688
* Update all non-major dependencies by @thomhurst in https://github.com/thomhurst/TUnit/pull/7681
* Update dependency OpenTelemetry.Instrumentation.AspNetCore to 1.20.2 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7685

### v1.81.10

* Preserve private type values in generated executable test attributes by @thomhurst in https://github.com/thomhurst/TUnit/pull/7667
* feat(sourcegen): inherit XML docs from [AssertionExtension] classes by @JohnVerheij in https://github.com/thomhurst/TUnit/pull/7692
* Update all non-major dependencies to 1.81.5 by @thomhurst in https://github.com/thomhurst/TUnit/pull/7690

## Public API

No public API change.

## Library code (src/)

- `src/TUnit.Analyzers.CodeFixers/Base/AssertionRewriter.cs` (+5 −5)
- `src/TUnit.Analyzers.CodeFixers/Base/BaseMigrationCodeFixProvider.cs` (+3 −2)
- `src/TUnit.Analyzers.CodeFixers/Base/TestAttributeEnsurer.cs` (+3 −2)
- `src/TUnit.Analyzers.CodeFixers/Base/TwoPhase/MigrationAnalyzer.cs` (+5 −5)
- `src/TUnit.Analyzers.CodeFixers/Base/TwoPhase/MigrationTransformer.cs` (+3 −2)
- `src/TUnit.Analyzers.CodeFixers/MSTestMigrationCodeFixProvider.cs` (+1 −1)
- `src/TUnit.Analyzers.CodeFixers/MatrixDataSourceCodeFixProvider.cs` (+23 −6)
- `src/TUnit.Analyzers.CodeFixers/NUnitMigrationCodeFixProvider.cs` (+1 −1)
- `src/TUnit.Analyzers.CodeFixers/TwoPhase/MSTestTwoPhaseAnalyzer.cs` (+2 −2)
- `src/TUnit.Analyzers.CodeFixers/TwoPhase/NUnitTwoPhaseAnalyzer.cs` (+4 −4)
- `src/TUnit.Analyzers.CodeFixers/TwoPhase/XUnitTwoPhaseAnalyzer.cs` (+63 −33)
- `src/TUnit.Analyzers.Internal/CultureSensitiveFormattingAnalyzer.cs` (+465 −0)
- `src/TUnit.Analyzers.Internal/TUnit.Analyzers.Internal.csproj` (+26 −0)
- `src/TUnit.Analyzers/AbstractTestClassWithDataSourcesAnalyzer.cs` (+40 −32)
- `src/TUnit.Analyzers/AnalyzerReleases.Shipped.md` (+2 −39)
- `src/TUnit.Analyzers/AnalyzerReleases.Unshipped.md` (+4 −1)
- `src/TUnit.Analyzers/AssemblyTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/BeforeHookAsyncLocalAnalyzer.cs` (+5 −1)
- `src/TUnit.Analyzers/ClassDataSourceConstructorAnalyzer.cs` (+3 −5)
- `src/TUnit.Analyzers/ClassHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/CombinedDataSourceAnalyzer.cs` (+18 −7)
- `src/TUnit.Analyzers/ConflictingExplicitAttributesAnalyzer.cs` (+4 −4)
- `src/TUnit.Analyzers/ConsoleOutAnalyzer.cs` (+1 −1)
- `src/TUnit.Analyzers/DependsOnConflictAnalyzer.cs` (+7 −0)
- `src/TUnit.Analyzers/DiagnosticIds.cs` (+3 −0)
- `src/TUnit.Analyzers/DisposableFieldPropertyAnalyzer.cs` (+92 −22)
- `src/TUnit.Analyzers/Extensions/AttributeExtensions.cs` (+37 −25)
- `src/TUnit.Analyzers/Extensions/CompilationExtensions.cs` (+470 −0)
- `src/TUnit.Analyzers/Extensions/MethodExtensions.cs` (+9 −16)
- `src/TUnit.Analyzers/Extensions/ParameterExtensions.cs` (+27 −14)
- `src/TUnit.Analyzers/Extensions/PropertyExtensions.cs` (+1 −1)
- `src/TUnit.Analyzers/Extensions/SymbolExtensions.cs` (+11 −4)
- `src/TUnit.Analyzers/Extensions/SyntaxExtensions.cs` (+0 −21)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.GloballyQualified.cs` (+129 −0)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.cs` (+7 −16)
- `src/TUnit.Analyzers/Extensions/TypedRowParameterBinding.cs` (+79 −0)
- `src/TUnit.Analyzers/ForbidRedefiningAttributeUsageAnalyzer.cs` (+4 −2)
- `src/TUnit.Analyzers/Helpers/TUnitSymbols.cs` (+228 −0)
- `src/TUnit.Analyzers/Helpers/WellKnown.cs` (+2 −0)
- `src/TUnit.Analyzers/InheritsTestsAnalyzer.cs` (+14 −3)
- `src/TUnit.Analyzers/InstanceTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/InstanceValuesInTestClassAnalyzer.cs` (+19 −24)
- `src/TUnit.Analyzers/MatrixAnalyzer.cs` (+10 −2)
- `src/TUnit.Analyzers/Migrators/Base/BaseMigrationAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/Migrators/Base/MigrationHelpers.cs` (+0 −0)
- `src/TUnit.Analyzers/Migrators/Base/MigrationNamespaceHelper.cs` (+0 −0)
- `src/TUnit.Analyzers/Migrators/MSTestMigrationAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/Migrators/NUnitMigrationAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/Migrators/XUnitMigrationAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/MissingTestAttributeAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/MultipleConstructorsAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/PublicMethodMissingTestAttributeAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/Resources.Designer.cs` (+0 −0)
- `src/TUnit.Analyzers/Resources.resx` (+0 −0)
- `src/TUnit.Analyzers/Rules.cs` (+0 −0)
- `src/TUnit.Analyzers/SingleTUnitAttributeAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/TUnit.Analyzers.csproj` (+0 −0)
- `src/TUnit.Analyzers/TestDataAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/TestMethodParametersAnalyzer.cs` (+0 −0)
- `src/TUnit.Analyzers/TimeoutCancellationTokenAnalyzer.cs` (+0 −0)
- `src/TUnit.AspNetCore.Analyzers/WebApplicationFactoryAccessAnalyzer.cs` (+0 −0)
- `src/TUnit.AspNetCore.Core/DisposalCoordinatingHost.cs` (+0 −0)
- `src/TUnit.AspNetCore.Core/Http/TUnitHttpClientFilter.cs` (+0 −0)
- `src/TUnit.AspNetCore.Core/Interception/HttpExchangeCaptureExtensions.cs` (+0 −0)
- `src/TUnit.AspNetCore.Core/TUnit.AspNetCore.Core.csproj` (+0 −0)
- `src/TUnit.AspNetCore.Core/TestWebApplicationFactory.cs` (+0 −0)
- `src/TUnit.AspNetCore.Core/TracedWebApplicationFactory.cs` (+0 −0)
- `src/TUnit.AspNetCore.Core/WebApplicationTest.cs` (+0 −0)
- `src/TUnit.Aspire.Core/AspireFixture.cs` (+0 −0)
- `src/TUnit.Aspire.Core/AspireFixtureOptions.cs` (+0 −0)
- `src/TUnit.Aspire.Core/ResourceRemoval.cs` (+0 −0)
- `src/TUnit.Aspire.Core/ResourceStartupWaiter.cs` (+0 −0)
- `src/TUnit.Aspire.Core/TUnit.Aspire.Core.csproj` (+0 −0)
- `src/TUnit.Assertions.Analyzers.CodeFixers/XUnitAssertionCodeFixProvider.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/AnalyzerReleases.Shipped.md` (+0 −0)
- `src/TUnit.Assertions.Analyzers/AwaitAssertionAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/AwaitValueTaskAssertThatAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/CollectionIsEqualToAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/CompilerArgumentsPopulatedAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/ConstantInAssertThatAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/DynamicInAssertThatAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/Extensions/NamespaceExtensions.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/Extensions/TypeExtensions.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/GenerateAssertionAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/Helpers/AssertionSymbols.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/Helpers/TypeSymbolSet.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/IsNotNullAssertionSuppressor.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/MixAndOrOperatorsAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/ObjectBaseEqualsMethodAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/PreferIsNullAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/PreferIsTrueOrIsFalseAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.Analyzers/TUnit.Assertions.Analyzers.csproj` (+0 −0)
- `src/TUnit.Assertions.Analyzers/XUnitAssertionAnalyzer.cs` (+0 −0)
- `src/TUnit.Assertions.FSharp/TUnit.Assertions.FSharp.fsproj` (+0 −0)
- `src/TUnit.Assertions.Should.SourceGenerator/ShouldExtensionGenerator.cs` (+0 −0)
- `src/TUnit.Assertions.Should/Core/ShouldSingleItemAssertion.cs` (+0 −0)
- `src/TUnit.Assertions.Should/Extensions/ShouldHasSingleItemAssertionExtensions.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/AssertionExtensionGenerator.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/AssertionMethodGenerator.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/CollectionShapeAssertionGenerator.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/CollectionShapeRegistry.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/CovarianceHelper.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/MethodAssertionGenerator.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Generators/NamespaceHelper.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Models/DiagnosticInfo.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/Shared/AttributeForwardingFormatters.cs` (+0 −0)
- `src/TUnit.Assertions.SourceGenerator/TUnit.Assertions.SourceGenerator.csproj` (+0 −0)

## Commits

535 commits; dependency bumps not listed.

- test: lower built-in expectation count guard so net472 passes (#7228)
- fix(sourcegen): infer generic method types from any MethodDataSource row shape (#7143)
- +semver:minor- ci: move the AOT test-app publish and AOT engine tests into their own workflow (#7226)
- Remove legacy JSON output implementation (#7234)
- fix(engine): drop row-scoped data sources from failed test metadata (#7079)
- fix(analyzers): merge the category tables under one New Rules section (#7174)
- chore: update mock benchmark results (#7239)
- fix(agents): give agent evidence a well-known home and stop lock markers leaking into new worktrees
- fix(agents): treat root-level MSBuild binary logs as disposable worktree output
- chore: update benchmark results (#7254)
- chore: update mock benchmark results (#7255)
- fix: release finished test instances and per-test objects before session end (#7260) (#7262)
- fix: never hand out a disposed shared data-source instance (#7248)
- chore(docs): remark Forgejo test summary compatability (#7272)
- fix(aspire): cancel and join startup waits (#7277) (#7279)
- fix(aspire): follow DCP runtime instances when reading resource logs (#7283)
- fix(engine): invoke OnTestRegistered on property-injected data sources (#7292)
- fix(sourcegen): globally qualify type names in property injection output (#7291)
- test(sourcegen): snapshot property injection output for Core.* namespaces (#7293)
- fix(aspire): detach kept resources from removed resources in ResourcesToRemove (#7295)
- feat(engine): report unobserved task exceptions in session results (#7296)
- fix(mocks): rename method type parameters that collide with the mocked type's (#7303)
- feat(mocks): TM010 analyzer + code fix for Mock.Of<T>() -> T.Mock() (#7307)
- docs(agents): check review threads and conversation comments every review cycle
- +semver:minor - feat(playwright): failure screenshots/traces and shared-browser disconnect diagnostics (#7309)
- fix: Should().HaveSingleItem() returns the single item (#7035)
- chore(agents): add the issue-pr-loop skill and its scripts
- chore: update benchmark results (#7314)
- chore: update mock benchmark results (#7315)
- feat(mocks): TM011 analyzer + code fix to declare mocks with the generated mock type (#7311)
- +semver:minor - fix(sourcegen): skip [Obsolete(error: true)] conversion operators in AotConverterGenerator (#7317)
- test(sourcegen): parse generator test fixtures with preview language version in all harnesses (#7190) (#7319)
- test(sourcegen): avoid record struct in AotConverterScanTests fixture so net472 compiles (#7329) (#7330)
- fix(sourcegen): emit typeof(Nullable<>) for a T? parameter of a generic test method (#7197) (#7322)
- test: exercise class-level tuple unwrapping in ClassDataSourceTupleTests (#7184) (#7318)
- fix(fsharp): pin FSharp.Core in TUnit.Assertions.FSharp independent of the building SDK (#7193) (#7321)
- fix(sourcegen): pick MethodDataSource overloads declared on base types like reflection (#7323)
- fix(reflection): close generic methods over a typed data source's declared types without [GenerateGenericTest] (#7324)
- ci: skip CI jobs on draft pull requests (#7345)
- docs(issue-pr-loop): draft PRs skip CI since #7345
- docs(agents): do not run TUnit.Engine.Tests locally
- fix(engine): run every overload of a [Test] method in filtered runs (#7332)
- fix: bind a tuple row whole to a tuple parameter followed by optional parameters (#7341)
- fix(core): keep and dispose data-source roots when object-graph tracking throws (#7342)
- chore: delete agent evidence of closed work items in the worktree sweep
- fix(engine): lower default maximum parallel tests to 2x processor count (#7354)
- chore: remove worktrees of closed work items in the sweep, retaining their work
- chore: retain leftover changes of merged checkouts instead of keeping them
- chore: lease the work item before saving a dirty merged checkout
- ci: cut duplicate TFM and packaging work from the Windows and macOS jobs (#7357)
- ci: run engine tests in their own job and drop the per-child test-host relaunch (#7364)
- fix(sourcegen): split untyped class data source rows by the generic class type they infer (#7339)
- fix(engine): read a generic class's own class-level [MethodDataSource] member on the closed class (#7336)
- fix(analyzers): TUnit0001 unwraps only the Func/TestDataRow layers the runtime removes (#7227) (#7347)
- test: assert distinct SharedType.None instance IDs instead of build order (#7250) (#7385)
- fix(generic): infer method type arguments from [Arguments<T>] rows in both modes (#7343)
- fix(generic): infer class type arguments through T[] constructor parameters from any class row (#7346)
- fix(engine): await the Task of async runtime dynamic tests (#7363)
- feat(engine): add dispose spans for shared data-source objects (#7396)
- fix(engine): stop copying build-time output to TestSessionContext (#7297) (#7397)
- feat(mocks): argument-aware Returns/ReturnsAsync for Task and ValueTask members (#7301) (#7404)
- docs: require issues that readers outside TUnit can understand
- chore(scripts): make PowerShell scripts directly executable
- fix(generic): a type-free class [Arguments] row lets method rows infer T, with matching constructor binding in both modes (#7392)
- docs(issue-pr-loop): finish open PRs before claiming new issues
- feat(scripts): finish open loop PRs before starting new issues (#7423)
- ci: cancel superseded runs on main pushes and key PR groups by number
- fix(mocks): preserve nullable generic constraints (#7305) (#7414)
- Fix #7335: retain typed class sources sharing inferred generic types (#7420)
- Fix reflection data source overloads with omitted optional arguments (#7421)
- feat(playwright): honor HEADED and BROWSER environment variables (#7395)
- docs: enable Windows long paths before worktree checkout (#7416)
- Fix duplicate dynamic builder invocation in reflection mode (#7424)
- fix(mocks): bind explicit method type arguments on Mock.Of<IGeneric<X>>() (#7406)
- fix(mocks): Is<T>(predicate) passes T, not T?, for non-nullable T (#7405)
- fix(engine): deliver row builder-context events to the test and raise OnDispose once per test (#7381) (#7384)
- fix: report generic classes whose data cannot infer types at compile time (#7425)
- fix(core): hold shared instances fetched while runtime tests register (#7391)
- fix(mocks): match null literals in generated predicate overloads (#7415)
- fix(mocks): qualify extern-aliased types with their alias in generated code (#7403)
- fix(generic): fail wrongly sized [GenerateGenericTest] in source-generated mode (#7344)
- fix(sourcegen): generate a data source factory for [InstanceMethodDataSource] (#7225) (#7348)
- Fix #7282: preserve caller cancellation over startup cleanup faults (#7447)
- fix(tests): remove polling throughput requirement on shared runners (#7448)
- fix(html-reporter): scope report state per session when sessions overlap (#7400)
- fix(analyzers): validate data against TestConstructor (#7370) (#7449)
- Infer generic method types from typed array rows in both discovery modes (#7460)
- Share generic method inference policy between discovery modes (#7455)
- Wrap runtime registration holds in an async scope (#7458)
- Preserve generic class source rows and distinguish null collections (#7453)
- Fix reference tuple method data source analysis (#7374) (#7457)
- Raise issue-pr-loop open-PR limit to 15
- Fix resultless ValueTask data source awaiting (#7411) (#7478)
- Fix MSBuild dependency compatibility for internals-access task (#7413) (#7479)
- fix: dispose session-lifetime DI scopes at session end (#7459)
- Await concurrent ASP.NET Core application disposal (#7470)
- Fix source generation for one-element ValueTuple parameters (#7467)
- Preserve loadable types during dynamic reflection discovery (#7495)
- Fix Verify solution context for project builds (#7419) (#7488)
- Fix inherited constructor data in reflection discovery (#7426) (#7491)
- Fix constructor-order-dependent data source diagnostic (#7456) (#7502)
- Isolate shared disposal span capture by parent activity (#7492)
- Fix preserved generic tuple binding in reflection mode (#7487)
- Fix core generator test warnings (#7428) (#7494)
- Fix AutoFixture fixture trimming contracts (#7452) (#7500)
- +semver:minor
- Share evaluated constructor-row state across discovery modes (#7443) (#7497)
- Diagnose static data-source properties in inaccessible containing types (#7503)
- Extract typed-row binding and verify invocation parity (#7507)
- Accept omitted optional MethodDataSource arguments in TUnit0001 (#7486)
- Update mcr.microsoft.com/dotnet/sdk Docker tag to v11 (#7513)
- Update dependency Microsoft.Kiota.Abstractions to 2.1.6 (#7512)
- ci: stop newer main pushes cancelling the AOT run the NuGet publish gate needs (#7519)
- Preserve null-containing tuples from static method data sources (#7469)
- Fix dependencies on deferred enumeration tests (#7471)
- Preserve DI scope ownership and synchronize concurrent property registration (#7476)
- Infer typed row generic arguments through interfaces and base classes (#7508)
- Fix session ownership of object tracker cleanup (#7475) (#7509)
- Fix recursive generated tuple argument conversions (#7515)
- Share generic class row selection and pairing policy (#7498)
- Raise data-source delegates at test lifecycle stages (#7521)
- Update all non-major dependencies to 1.79.0 (#7528)
- Fix class argument literals to use constructor parameter types (#7496)
- Accept numeric widening for single reference-tuple data parameters (#7510)
- fix(core): preserve optional F# async support without AOT warnings (#7526)
- Fix timeouts for synchronously blocking test bodies (#7527)
- Fix AOT-compatible generic property metadata getters (#7499) (#7524)
- Refresh core generator snapshots for #7537 (#7549)
- Infer generic class types from inherited literal arguments (#7544)
- Fix hosted-service cancellation test scheduling (#7506) (#7546)
- Fix colliding generator diagnostic IDs (#7538)
- Fix generic array binding inside tuple data-source parameters (#7541)
- Discover AOT converters from method data source return types (#7547)
- Check tuple conversion analyzer policy against runtime binding (#7559)
- Deduplicate repeated activity stop callbacks in tests (#7435) (#7557)
- Preserve generic tuple rows from instance data sources (#7548)
- Expect source operators to bind in AOT in the tuple conversion matrix (#7580)
- ci: run one general macOS job per pull request push (#7578)
- ci: restore analyzer-test reference packs and write heap hang dumps on macOS (#7576)
- Fix nested type names in test data diagnostics (#7534) (#7563)
- Populate reflection class property metadata (#7550)
- Strengthen generic class and method pairing regression (#7529) (#7558)
- Exclude indexers from generated class property metadata (#7531) (#7560)
- Fix synchronous factory timeout cancellation classification (#7561)
- Add packaged F# async trimming smoke coverage (#7562)
- Update all non-major dependencies (#7536)
- ci: run only OS-specific work on Windows and macOS pull request jobs (#7582)
- Fix unfinished dependency regression scheduling race (#7564) (#7567)
- Isolate crashed Aspire probe from certificate setup (#7555) (#7566)
- Remove unused metadata generation entry points (#7568) (#7570)
- Remove unused streaming test builder path (#7327) (#7535)
- Isolate test registration callback failures (#7556)
- +semver:minor - Capture the stalled Windows reflection test process before timeout (#7565)
- Extract Windows engine hang dump stacks in CI (#7584)
- Cut STAThreadTests repeats so the Windows reflection pass run fits its timeout (#7594)
- Preserve expected-value semantics when migrating xUnit Assert.Single (#7586)
- Capture Windows loader ownership and thread CPU times (#7603)
- Isolate the full passing engine session from sibling children (#7554) (#7606)
- Remove unused concrete metadata generation chain (#7194) (#7569)
- Avoid singleton tuple null-check arrays (#7552) (#7583)
- Fix parallel overlap assertion for late repetitions (#7581) (#7600)
- Fix nullable generic class row validation for #7610 (#7613)
- Fix generated property injection into boxed structs (#7612)
- Make Playwright template navigation deterministic (#7601) (#7604)
- Release objects and complete teardown for dependency-skipped tests (#7605)
- Support typed tuple rows before optional parameters (#7608)
- Cover null rows in generic class type inference (#7621)
- Skip certificate trust preparation for HTTP-only Aspire test resources (#7618)
- Accept convertible typed rows before optional test parameters (#7619)
- Preserve nullable class discovery parity and constructor precedence (#7614)
- Preserve whole tuple rows before omitted trailing arrays (#7625)
- Fix reflection inference for concrete params arrays (#7624) (#7627)
- Remove obsolete nullable method-row analyzer suppression (#7626)
- Infer generic method arguments from instance data sources (#7630)
- test: cover discarded method-row lifecycle isolation (#7373) (#7632)
- Allow DI scopes to opt out of resolved object ownership (#7633)
- Give TestBuilder rows explicit cleanup owners (#7637)
- Preserve whole-tuple inference across wrapped and async sources (#7641)
- Fix reported compiler warnings in regression fixtures (#7645)
- fix(core): track external ownership per row scope (#7635)
- Fix remaining regression fixture compiler warnings (#7646)
- Fix generic class argument row edge cases (#7647)
- Preserve sole-tuple inference and runtime conversion parity (#7643)
- Fix method data source attribute identity checks (#7648) (#7649)
- Treat null method data sources as empty in both execution modes (#7652)
- Fix xUnit proper-set migration operands and strictness (#7653)
- Fix mock setup identifier collisions (#7657) (#7658)
- fix(generator): qualify built-in data-source row classification (#7651)
- Capture macOS native runtime crashes for diagnosis (#7659)
- Enforce generated nullable diagnostics in mock regression guards (#7436) (#7661)
- Avoid mock predicate conversion local name collisions (#7655)
- Use package-matched Playwright browser installer (#7672) (#7673)
- Remove unit-test nullable and assertion diagnostics (#7438) (#7670)
- Fix escaped attribute type names in generated factories (#7668) (#7669)
- Fix default mock argument matching (#7441) (#7676)
- Preserve category and property filters on generic discovery failures (#7663)
- Update all non-major dependencies (#7593)
- Preserve keyword escapes in generated type expressions (#7675)
- Encapsulate row lifetime and constructor state replay (#7454) (#7678)
- Diagnose unsupported span params on test methods (#7679)
- +semver:minor - Honor inherited tests on generic classes in reflection discovery (#7665)
- Update all non-major dependencies (#7681)
- chore: update mock benchmark results (#7682)
- Update dependency OpenTelemetry.Instrumentation.AspNetCore to 1.20.2 (#7685)
- feat(sourcegen): inherit XML docs from [GenerateAssertion] source methods (#7687)
- fix(mocks): stop verification leaving setups on void-shaped members (#7688)
- docs(issue-pr-loop): slim SKILL.md and move repo specifics to repository guidance
- ci: stop the tvOS smoke test depending on one pinned simulator (#7689)
- Update all non-major dependencies to 1.81.5 (#7690)
- Preserve private type values in generated executable test attributes (#7667)
- feat(sourcegen): inherit XML docs from [AssertionExtension] classes (#7692)

> Truncated by the GitHub compare API; the compare link above has the full list.
