# TUnit v1.68.17 → v1.76.28

Compare: https://github.com/thomhurst/TUnit/compare/v1.68.17...v1.76.28

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
- `src/TUnit.Analyzers.CodeFixers/TwoPhase/XUnitTwoPhaseAnalyzer.cs` (+11 −10)
- `src/TUnit.Analyzers.Internal/CultureSensitiveFormattingAnalyzer.cs` (+465 −0)
- `src/TUnit.Analyzers.Internal/TUnit.Analyzers.Internal.csproj` (+26 −0)
- `src/TUnit.Analyzers/AbstractTestClassWithDataSourcesAnalyzer.cs` (+40 −32)
- `src/TUnit.Analyzers/AnalyzerReleases.Shipped.md` (+2 −39)
- `src/TUnit.Analyzers/AnalyzerReleases.Unshipped.md` (+3 −1)
- `src/TUnit.Analyzers/AssemblyTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/BeforeHookAsyncLocalAnalyzer.cs` (+5 −1)
- `src/TUnit.Analyzers/ClassDataSourceConstructorAnalyzer.cs` (+3 −5)
- `src/TUnit.Analyzers/ClassHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/CombinedDataSourceAnalyzer.cs` (+18 −7)
- `src/TUnit.Analyzers/ConflictingExplicitAttributesAnalyzer.cs` (+4 −4)
- `src/TUnit.Analyzers/ConsoleOutAnalyzer.cs` (+1 −1)
- `src/TUnit.Analyzers/DependsOnConflictAnalyzer.cs` (+7 −0)
- `src/TUnit.Analyzers/DiagnosticIds.cs` (+2 −0)
- `src/TUnit.Analyzers/DisposableFieldPropertyAnalyzer.cs` (+92 −22)
- `src/TUnit.Analyzers/Extensions/AttributeExtensions.cs` (+37 −25)
- `src/TUnit.Analyzers/Extensions/CompilationExtensions.cs` (+295 −0)
- `src/TUnit.Analyzers/Extensions/MethodExtensions.cs` (+9 −16)
- `src/TUnit.Analyzers/Extensions/ParameterExtensions.cs` (+27 −14)
- `src/TUnit.Analyzers/Extensions/PropertyExtensions.cs` (+1 −1)
- `src/TUnit.Analyzers/Extensions/SymbolExtensions.cs` (+3 −3)
- `src/TUnit.Analyzers/Extensions/SyntaxExtensions.cs` (+0 −21)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.GloballyQualified.cs` (+129 −0)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.cs` (+5 −15)
- `src/TUnit.Analyzers/ForbidRedefiningAttributeUsageAnalyzer.cs` (+4 −2)
- `src/TUnit.Analyzers/Helpers/TUnitSymbols.cs` (+228 −0)
- `src/TUnit.Analyzers/Helpers/WellKnown.cs` (+2 −0)
- `src/TUnit.Analyzers/InheritsTestsAnalyzer.cs` (+14 −3)
- `src/TUnit.Analyzers/InstanceTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/InstanceValuesInTestClassAnalyzer.cs` (+19 −24)
- `src/TUnit.Analyzers/MatrixAnalyzer.cs` (+10 −2)
- `src/TUnit.Analyzers/Migrators/Base/BaseMigrationAnalyzer.cs` (+71 −20)
- `src/TUnit.Analyzers/Migrators/Base/MigrationHelpers.cs` (+3 −3)
- `src/TUnit.Analyzers/Migrators/Base/MigrationNamespaceHelper.cs` (+122 −0)
- `src/TUnit.Analyzers/Migrators/MSTestMigrationAnalyzer.cs` (+2 −2)
- `src/TUnit.Analyzers/Migrators/NUnitMigrationAnalyzer.cs` (+5 −3)
- `src/TUnit.Analyzers/Migrators/XUnitMigrationAnalyzer.cs` (+64 −25)
- `src/TUnit.Analyzers/MissingTestAttributeAnalyzer.cs` (+8 −1)
- `src/TUnit.Analyzers/MultipleConstructorsAnalyzer.cs` (+10 −11)
- `src/TUnit.Analyzers/PublicMethodMissingTestAttributeAnalyzer.cs` (+33 −1)
- `src/TUnit.Analyzers/Resources.Designer.cs` (+3 −3)
- `src/TUnit.Analyzers/Resources.resx` (+33 −6)
- `src/TUnit.Analyzers/Rules.cs` (+19 −4)
- `src/TUnit.Analyzers/SingleTUnitAttributeAnalyzer.cs` (+7 −1)
- `src/TUnit.Analyzers/TUnit.Analyzers.csproj` (+2 −0)
- `src/TUnit.Analyzers/TestDataAnalyzer.cs` (+434 −46)
- `src/TUnit.Analyzers/TestMethodParametersAnalyzer.cs` (+1 −1)
- `src/TUnit.Analyzers/TimeoutCancellationTokenAnalyzer.cs` (+97 −4)
- `src/TUnit.AspNetCore.Analyzers/WebApplicationFactoryAccessAnalyzer.cs` (+35 −67)
- `src/TUnit.AspNetCore.Core/Http/TUnitHttpClientFilter.cs` (+53 −0)
- `src/TUnit.AspNetCore.Core/Interception/HttpExchangeCaptureExtensions.cs` (+21 −1)
- `src/TUnit.AspNetCore.Core/TUnit.AspNetCore.Core.csproj` (+1 −10)
- `src/TUnit.AspNetCore.Core/TestWebApplicationFactory.cs` (+28 −9)
- `src/TUnit.AspNetCore.Core/TracedWebApplicationFactory.cs` (+12 −3)
- `src/TUnit.AspNetCore.Core/WebApplicationTest.cs` (+182 −39)
- `src/TUnit.Aspire.Core/AspireFixture.cs` (+15 −5)
- `src/TUnit.Aspire.Core/TUnit.Aspire.Core.csproj` (+4 −0)
- `src/TUnit.Assertions.Analyzers.CodeFixers/XUnitAssertionCodeFixProvider.cs` (+8 −2)
- `src/TUnit.Assertions.Analyzers/AnalyzerReleases.Shipped.md` (+2 −14)
- `src/TUnit.Assertions.Analyzers/AwaitAssertionAnalyzer.cs` (+16 −9)
- `src/TUnit.Assertions.Analyzers/AwaitValueTaskAssertThatAnalyzer.cs` (+22 −8)
- `src/TUnit.Assertions.Analyzers/CollectionIsEqualToAnalyzer.cs` (+10 −9)
- `src/TUnit.Assertions.Analyzers/CompilerArgumentsPopulatedAnalyzer.cs` (+78 −30)
- `src/TUnit.Assertions.Analyzers/ConstantInAssertThatAnalyzer.cs` (+14 −4)
- `src/TUnit.Assertions.Analyzers/DynamicInAssertThatAnalyzer.cs` (+14 −4)
- `src/TUnit.Assertions.Analyzers/Extensions/NamespaceExtensions.cs` (+24 −0)
- `src/TUnit.Assertions.Analyzers/Extensions/TypeExtensions.cs` (+1 −7)
- `src/TUnit.Assertions.Analyzers/GenerateAssertionAnalyzer.cs` (+2 −1)
- `src/TUnit.Assertions.Analyzers/Helpers/AssertionSymbols.cs` (+63 −0)
- `src/TUnit.Assertions.Analyzers/Helpers/TypeSymbolSet.cs` (+170 −0)
- `src/TUnit.Assertions.Analyzers/IsNotNullAssertionSuppressor.cs` (+189 −53)
- `src/TUnit.Assertions.Analyzers/MixAndOrOperatorsAnalyzer.cs` (+95 −21)
- `src/TUnit.Assertions.Analyzers/ObjectBaseEqualsMethodAnalyzer.cs` (+2 −3)
- `src/TUnit.Assertions.Analyzers/PreferIsNullAnalyzer.cs` (+3 −4)
- `src/TUnit.Assertions.Analyzers/PreferIsTrueOrIsFalseAnalyzer.cs` (+3 −4)
- `src/TUnit.Assertions.Analyzers/TUnit.Assertions.Analyzers.csproj` (+4 −0)
- `src/TUnit.Assertions.Analyzers/XUnitAssertionAnalyzer.cs` (+37 −3)
- `src/TUnit.Assertions.Should.SourceGenerator/ShouldExtensionGenerator.cs` (+434 −98)
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
- `src/TUnit.Assertions/Attributes/AssertionFromAttribute.cs` (+0 −0)
- `src/TUnit.Assertions/Attributes/AssertionFromAttribute`1.cs` (+0 −0)
- `src/TUnit.Assertions/Conditions/DirectoryInfoAssertionExtensions.cs` (+0 −0)
- `src/TUnit.Assertions/Conditions/EqualsAssertion.cs` (+0 −0)
- `src/TUnit.Assertions/Conditions/FileInfoAssertionExtensions.cs` (+0 −0)
- `src/TUnit.Assertions/Conditions/FileSystemAssertions.cs` (+0 −0)
- `src/TUnit.Assertions/Conditions/NotEqualsAssertion.cs` (+0 −0)
- `src/TUnit.Assertions/Conditions/SpanAssertionExtensions.cs` (+0 −0)
- `src/TUnit.Assertions/Extensions/ImplicitConversionCache.cs` (+0 −0)
- `src/TUnit.Assertions/Extensions/ImplicitConversionEqualityExtensions.cs` (+0 −0)
- `src/TUnit.Assertions/TUnit.Assertions.props` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Analyzers/ITestAnalyzer.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Analyzers/TestMethodAnalyzer.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerationHelpers.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/DynamicTestsGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Equality/PreventCompilationTriggerOnEveryKeystrokeComparer.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Formatting/TypedConstantFormatter.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/DataSourceAttributeHelper.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/GenericTypeHelper.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/InstanceFactoryGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/TupleArgumentHelper.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/InfrastructureGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/StaticPropertyInitializationGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Writers/AttributeWriter.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Writers/SourceInformationWriter.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Enums/HookLocationType.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/AttributeDataExtensions.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/ExactTypeExtensions.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/ObjectExtensions.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/TypeExtensions.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/TypeSymbolExtensions.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/TypedDataSourceInference.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/AotConverterGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/AttributePolyfillGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/DynamicDependencyPolyfillGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/HookMetadataGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/ModuleInitializerPolyfillGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/PropertyInjectionSourceGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/TestMetadataGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Helpers/FileNameHelper.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Helpers/IdentifierHelper.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/ClassTestGroup.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/DataSourceModel.cs` (+0 −0)

## Commits

316 commits; dependency bumps not listed.

- perf(analyzers): cut binding and symbol lookups in analyzer hot paths (TUnit.Analyzers -89% on TestProject) (#6917)
- fix(source-gen): model equality covers every emitted field; infrastructure refreshes on reference changes (#6912)
- perf(mocks): memoize generator discovery per compilation and decouple emitted source from call-site locations (#6913)
- fix(packaging): skip the source generator when disabled and replace the broken Polyfill injection (#6915)
- refactor(analyzers): address review feedback from #6917 (#6919)
- perf(source-gen): remove whole-compilation scans from static property, property injection and AOT converter generators (#6914)
- perf(assertions-source-gen): make assertion generators properly incremental (#6916)
- +semver:minor - perf(source-gen): make TestMetadataGenerator pipeline values equatable (#6918)
- chore: update mock benchmark results (#6922)
- perf(source-gen): resolve parameter reflection info through a shared runtime helper (#6923)
- perf(analyzers): trim remaining analyzer hot-path symbol lookups and binds (#6928)
- perf(mocks): move shared MockCall wrapper plumbing into runtime base classes (#6929)
- perf(source-gen): close incremental caching gaps in static property and property injection generators (#6925)
- perf(source-gen): stop InfrastructureGenerator pinning an old Compilation (#6926)
- perf(assertions-analyzers): cache assertion symbols and cut per-call work (#6927)
- perf(source-gen): emit hooks per class with direct, non-async bodies (#6924)
- test: compare Thread identity in ObjectInitializer continuation test (#6932)
- fix: CI flakes from leaked hook contexts, ActivityCollector race and Repro5700 rendezvous (#6933)
- +semver:minor - fix(aspnetcore): honor WebApplicationFactoryClientOptions in CreateClient (#6931)
- chore: update benchmark results (#6935)
- chore: update benchmark results (#6936)
- fix(source-gen): stop parameter resolver keeping every non-public test-class method (IL2111) (#6937)
- ci: key Claude review concurrency on PR number
- Fix generated invokers for ValueTask<T> tests (#6930)
- chore: update mock benchmark results (#6947)
- chore: update mock benchmark results (#6950)
- docs: add Moq, NSubstitute, and FakeItEasy migration guides for TUnit.Mocks (#6951)
- fix(aspnetcore): initialize web application factories through services (#6956)
- chore: update mock benchmark results (#6957)
- docs: give the site a green-bar identity (#6959)
- chore: update benchmark results (#6960)
- chore: update mock benchmark results (#6961)
- chore: update mock benchmark results (#6967)
- docs: make examples work on Linux and macOS (#6964)
- fix(runtime): correct Windows-shaped assumptions on Linux and macOS (#6962)
- build: make the repo build, test and script cleanly on macOS and Linux (#6963)
- chore: update mock benchmark results (#6970)
- fix(globalization): culture-invariant generators, analyzers and code fixers; enforce it (#6969)
- chore: update NuGet dependencies and split versions per target framework (#6972)
- chore: update mock benchmark results (#6984)
- +semver:minor - feat: add [PairwiseDataSource] for all-pairs test case generation (#6971)
- fix: Ignore default start timestamps in HTML report (#6942)
- fix(playwright): send trace context headers only to origins under test (#6993)
- docs: resolve review threads once fixed or pushed back
- chore: update mock benchmark results (#6998)
- fix(fscheck): apply Verbose, QuietOnSuccess and Parallelism; validate Replay (#7001)
- chore: update mock benchmark results (#7009)
- chore: update mock benchmark results (#7017)
- chore: update benchmark results (#7026)
- chore: update mock benchmark results (#7028)
- fix(mocks): eliminate trim/AOT warnings on Native AOT publish (#7029)
- feat(engine): raise thread pool minimum when blocking tests starve the pool (#7030)
- +semver:minor - feat(mocks): add ClearCalls, PassThrough toggle and string/type/reference matchers (#7018)
- docs: document IKeyedDataSource for per-key fixture configuration
- docs: explain when ClassDataSource instances are created (#7046)
- feat(aspnetcore): add PerTestWebApplicationTest with per-test CreateFactoryAsync (#7047)
- +semver:minor - fix(aspnetcore): make WebApplicationTest.HttpCapture return the registered capture (#7048)
- chore: update mock benchmark results (#7070)
- chore: add OSS scanner config, threat model and SECURITY.md (#7080)
- fix(deps): patch MessagePack for Aspire and use per-TFM Microsoft.Extensions.Http (#7072)
- docs: list security contact email in SECURITY.md
- fix: skip tests marked with an empty skip reason (#7083)
- fix(engine): report the engine mode actually selected in the banner (#7085)
- fix(engine): order keyed NotInParallel tests by priority, not hash code (#7090)
- fix: remove root causes of flaky tests and the broken Apple smoke jobs (#7095)
- chore: update benchmark results (#7114)
- fix(engine): run synchronous keyed NotInParallel tests concurrently (#7087)
- fix(sourcegen): run every [Arguments] row that infers the same generic type (#7100)
- fix: same filter path and display name for generic tests in both engine modes (#7110)
- fix(engine): apply max parallelism cap to keyed NotInParallel tests (#7084)
- fix(ci): install only Chromium for Playwright and wait on dpkg lock (#6994)
- fix(core): keep the engine-selected execution mode when late assemblies load (#7091)
- fix(engine): end fail-fast runs without crashing the test host (#7115)
- test: stop the AOT [EngineTest=Pass] run hitting its 5 minute budget (#7125)
- fix(engine): align reflection-mode data sources and hooks with source-gen (#7094)
- fix(pipeline): stop skipping the NuGet package tester modules (#7127)
- fix(agents): detach junctions before removing worktrees
- ci: take AOT publishes and doc snippets off the Ubuntu critical path (#7128)
- fix(analyzers): TUnit0001 false positive for MethodDataSource on generic type-parameter parameters (#7109)
- fix: report generic class constraint violations as failed tests in both modes (#7112)
- ci: cut runner contention and the AOT publish off the critical path (#7131)
- fix(assertions): make cross-type IsEqualTo work for numeric and nullable arguments on C# 12 (#7086)
- fix(sourcegen): report generic constraint violations instead of dropping rows (#7102)
- ci: test the NuGet packages on Windows in their own job (#7130)
- fix(sourcegen): bind params T[] on generic test methods (#7101)
- fix(engine): run every [Arguments] row on generic test classes in both modes (#7111)
- docs: add autonomous self-improvement guidance to AGENTS.md
- fix(engine): use last inferred type for repeated generic parameters (#7134)
- docs: link to other libraries from navbar and footer
- Make the test suite pass in every environment and run fully in CI (#7129)
- fix(assertions): skip using directive for global-namespace assertion types (#7139)
- fix(core): format numeric display-name arguments with the invariant culture (#7138)
- fix(engine): dispose data-source objects of rows that end as failed tests (#7150)
- Fix net472 compile gate failure in assertions source generator tests (#7170)
- fix(sourcegen): close generic methods of generic classes on every class source (#7152)
- fix(engine): infer object for null rows on generic test methods in reflection mode (#7142)
- fix(engine): report every test once on fail-fast runs (#7145)
- test(engine): stop whole-process budgets killing healthy scheduling engine tests (#7177)
- feat(analyzers): report MethodDataSource Arguments that fit two overloads equally (TUnit0076) (#7181)
- fix(sourcegen): render top-level dynamic as object so typeof compiles (#7182)
- fix(sourcegen): pair each GenerateGenericTest type only with its typed ClassDataSource<T> (#7188)
- fix(engine): run untyped [Arguments(null)] rows on generic classes instead of dropping them (#7203)
- fix(engine): report generic test classes by their generic type definition in TRX (#7200)
- test(sourcegen): parse snapshot fixtures as a real build does (#7189)
- refactor(engine): remove dead streaming reflection discovery and share generic instantiation code (#7183)
- test: make TimeoutHelperTests deterministic under thread-pool load (#7180)
- fix(analyzers): accept null MethodDataSource arguments for nullable parameters (#7179)
- test(assertions): make WaitsFor cancellation tests robust to slow CI runners (#7176)
- fix(assertions): support [AssertionFrom] with unbound generic types (#7144)
- fix(sourcegen): pass omitted optional defaults so calls bind to the test method (#7148)
- fix(engine): reuse the first class-data fetch for the first test of a class row (#7195)
- fix(engine): report [Arguments] rows that break constraints with [GenerateGenericTest] in reflection mode (#7196)
- fix(generic): infer object when a type parameter gets null and a value-type value (#7198)
- fix(engine): dispose data-source objects of skipped tests and rows (#7191)
- fix(sourcegen): bind omitted optional parameters of generic tests (#7199)
- fix(generic): infer method type arguments from typed data sources on generic classes (#7186)
- fix: restore main build and stop the macOS AOT publish timing out (#7216)
- ci: stop heavy modules overlapping the AOT test-app publish (#7217)
- docs(agents): pass -OwnerId to every AgentLocks verb
- ci: make the NuGet tester AOT publish's wait on the AOT test-app publish optional (#7219)
- chore(sourcegen): drop redundant null-conditionals that raise CS8602 (#7218)
- fix(sourcegen): report generic test rows whose type arguments cannot be inferred (#7187)
- fix(generic): explain declared-type inference for broad data source types (#7154)
- fix(engine): run method rows only on the generic class instantiation they infer (#7149)
- Fix TUnit0014 on interface implementations, Aspire exit-code culture and [AssertionFrom] expectation messages (#7135)
- fix: bind a CancellationToken declared anywhere and keep a single tuple parameter whole (#7185)
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

> Truncated by the GitHub compare API; the compare link above has the full list.
