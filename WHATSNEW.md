# TUnit v1.68.17 → v1.70.1

Compare: https://github.com/thomhurst/TUnit/compare/v1.68.17...v1.70.1

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

## Public API

#### Core_Library

```diff
(patch too large — open the compare link)
```

## Library code (src/)

- `src/TUnit.Analyzers/AbstractTestClassWithDataSourcesAnalyzer.cs` (+3 −3)
- `src/TUnit.Analyzers/AnalyzerReleases.Unshipped.md` (+2 −1)
- `src/TUnit.Analyzers/AssemblyTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/BeforeHookAsyncLocalAnalyzer.cs` (+5 −1)
- `src/TUnit.Analyzers/ClassDataSourceConstructorAnalyzer.cs` (+3 −5)
- `src/TUnit.Analyzers/ClassHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/CombinedDataSourceAnalyzer.cs` (+2 −2)
- `src/TUnit.Analyzers/ConflictingExplicitAttributesAnalyzer.cs` (+4 −4)
- `src/TUnit.Analyzers/ConsoleOutAnalyzer.cs` (+1 −1)
- `src/TUnit.Analyzers/DiagnosticIds.cs` (+1 −0)
- `src/TUnit.Analyzers/Extensions/AttributeExtensions.cs` (+1 −2)
- `src/TUnit.Analyzers/Extensions/MethodExtensions.cs` (+1 −2)
- `src/TUnit.Analyzers/Extensions/ParameterExtensions.cs` (+4 −4)
- `src/TUnit.Analyzers/Extensions/PropertyExtensions.cs` (+1 −1)
- `src/TUnit.Analyzers/Extensions/SymbolExtensions.cs` (+3 −3)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.GloballyQualified.cs` (+116 −0)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.cs` (+3 −11)
- `src/TUnit.Analyzers/ForbidRedefiningAttributeUsageAnalyzer.cs` (+3 −1)
- `src/TUnit.Analyzers/InheritsTestsAnalyzer.cs` (+2 −2)
- `src/TUnit.Analyzers/InstanceTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/MissingTestAttributeAnalyzer.cs` (+2 −1)
- `src/TUnit.Analyzers/PublicMethodMissingTestAttributeAnalyzer.cs` (+3 −1)
- `src/TUnit.Analyzers/Resources.resx` (+10 −1)
- `src/TUnit.Analyzers/Rules.cs` (+3 −0)
- `src/TUnit.Analyzers/SingleTUnitAttributeAnalyzer.cs` (+7 −1)
- `src/TUnit.Analyzers/TestDataAnalyzer.cs` (+3 −3)
- `src/TUnit.Analyzers/TimeoutCancellationTokenAnalyzer.cs` (+97 −4)
- `src/TUnit.Assertions.Analyzers/AwaitAssertionAnalyzer.cs` (+8 −0)
- `src/TUnit.Assertions.Analyzers/AwaitValueTaskAssertThatAnalyzer.cs` (+3 −5)
- `src/TUnit.Assertions.Analyzers/CompilerArgumentsPopulatedAnalyzer.cs` (+14 −18)
- `src/TUnit.Assertions.Analyzers/Extensions/TypeExtensions.cs` (+1 −7)
- `src/TUnit.Assertions.Analyzers/GenerateAssertionAnalyzer.cs` (+2 −1)
- `src/TUnit.Assertions.Analyzers/MixAndOrOperatorsAnalyzer.cs` (+3 −3)
- `src/TUnit.Assertions.Analyzers/ObjectBaseEqualsMethodAnalyzer.cs` (+2 −3)
- `src/TUnit.Assertions.Analyzers/TUnit.Assertions.Analyzers.csproj` (+4 −0)
- `src/TUnit.Assertions.Analyzers/XUnitAssertionAnalyzer.cs` (+19 −0)
- `src/TUnit.Core.SourceGenerator/CodeGenerationHelpers.cs` (+2 −189)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Writers/AttributeWriter.cs` (+24 −23)
- `src/TUnit.Core.SourceGenerator/Extensions/AttributeDataExtensions.cs` (+53 −0)
- `src/TUnit.Core.SourceGenerator/Generators/TestMetadataGenerator.cs` (+243 −60)
- `src/TUnit.Core.SourceGenerator/Models/TestMethodSourceCode.cs` (+3 −1)
- `src/TUnit.Core/AmbientContexts.cs` (+120 −0)
- `src/TUnit.Core/Contexts/TestRegisteredContext.cs` (+28 −0)
- `src/TUnit.Core/Data/ThreadSafeDictionary.cs` (+12 −0)
- `src/TUnit.Core/Discovery/ObjectGraphDiscoverer.cs` (+88 −1)
- `src/TUnit.Core/EngineCancellationToken.cs` (+41 −2)
- `src/TUnit.Core/Executors/DedicatedThreadExecutor.cs` (+122 −105)
- `src/TUnit.Core/Helpers/ClassConstructorHelper.cs` (+5 −6)
- `src/TUnit.Core/Helpers/LazyAttributeDictionary.cs` (+73 −0)
- `src/TUnit.Core/Models/AssemblyHookContext.cs` (+3 −7)
- `src/TUnit.Core/Models/ClassHookContext.cs` (+3 −7)
- `src/TUnit.Core/Models/TestBuildContext.cs` (+8 −0)
- `src/TUnit.Core/Models/TestDiscoveryContext.cs` (+2 −3)
- `src/TUnit.Core/Models/TestSessionContext.cs` (+3 −7)
- `src/TUnit.Core/TUnit.Core.targets` (+1 −1)
- `src/TUnit.Core/TestBuilderContext.cs` (+69 −4)
- `src/TUnit.Core/TestContext.Dependencies.cs` (+3 −2)
- `src/TUnit.Core/TestContext.Events.cs` (+12 −7)
- `src/TUnit.Core/TestContext.Output.cs` (+45 −10)
- `src/TUnit.Core/TestContext.Parallelization.cs` (+5 −0)
- `src/TUnit.Core/TestContext.cs` (+22 −10)
- `src/TUnit.Core/TestDetails.cs` (+4 −0)
- `src/TUnit.Core/TestEntryFactory.cs` (+72 −0)
- `src/TUnit.Core/TestMetadata`1.cs` (+6 −1)
- `src/TUnit.Core/Tracking/ObjectTracker.cs` (+22 −10)
- `src/TUnit.Engine/Building/Interfaces/ITestBuilder.cs` (+2 −2)
- `src/TUnit.Engine/Building/TestBuilder.cs` (+263 −116)
- `src/TUnit.Engine/Building/TestBuilderPipeline.cs` (+2 −2)
- `src/TUnit.Engine/Events/EventReceiverRegistry.cs` (+39 −9)
- `src/TUnit.Engine/Extensions/TestContextExtensions.cs` (+14 −5)
- `src/TUnit.Engine/Extensions/TestExtensions.cs` (+19 −16)
- `src/TUnit.Engine/Framework/TUnitTestFramework.cs` (+10 −2)
- `src/TUnit.Engine/Helpers/DataSourceMetadataExtractor.cs` (+12 −5)
- `src/TUnit.Engine/Reporters/Aggregation/AtomicFile.cs` (+18 −0)
- `src/TUnit.Engine/Reporters/Aggregation/ReportAggregator.cs` (+17 −0)
- `src/TUnit.Engine/Reporters/Aggregation/ReportDataJson.cs` (+21 −6)
- `src/TUnit.Engine/Reporters/Aggregation/SegmentedBufferWriter.cs` (+125 −0)
- `src/TUnit.Engine/Reporters/Html/ActivityCollector.cs` (+104 −49)
- `src/TUnit.Engine/Reporters/Html/HtmlReportGenerator.cs` (+36 −13)
- `src/TUnit.Engine/Reporters/Html/HtmlReporter.cs` (+76 −24)
- `src/TUnit.Engine/Reporters/JUnitReporter.cs` (+3 −2)
- `src/TUnit.Engine/Services/EventReceiverOrchestrator.cs` (+16 −0)
- `src/TUnit.Engine/Services/ObjectLifecycleService.cs` (+31 −7)
- `src/TUnit.Engine/Services/PropertyInjector.cs` (+18 −1)
- `src/TUnit.Engine/Services/TestArgumentRegistrationService.cs` (+36 −16)
- `src/TUnit.Engine/Services/TestDependencyResolver.cs` (+32 −2)
- `src/TUnit.Engine/Services/TestExecution/RetryHelper.cs` (+1 −1)
- `src/TUnit.Engine/Services/TestExecution/TestContextRestorer.cs` (+20 −0)
- `src/TUnit.Engine/Services/TestExecution/TestCoordinator.cs` (+27 −13)
- `src/TUnit.Engine/Services/TestFilterService.cs` (+12 −6)
- `src/TUnit.Engine/TestExecutor.cs` (+27 −8)
- `src/TUnit.Engine/Utilities/ParallelMap.cs` (+19 −1)
- `src/TUnit.Mocks.SourceGenerator/Builders/MockDelegateFactoryBuilder.cs` (+88 −32)
- `src/TUnit.Mocks.SourceGenerator/Builders/MockImplBuilder.cs` (+12 −7)
- `src/TUnit.Mocks.SourceGenerator/Extensions/TypeSymbolExtensions.cs` (+29 −24)
- `src/TUnit.Reporting.Tool/TUnit.Reporting.Tool.csproj` (+1 −0)
- `src/TUnit.Templates/README.md` (+16 −1)
- `src/TUnit.Templates/content/TUnit.Aspire.Starter/ExampleNamespace.ServiceDefaults/ExampleNamespace.ServiceDefaults.csproj` (+5 −5)
- `src/TUnit.Templates/content/TUnit.FSharp/.template.config/dotnetcli.host.json` (+9 −0)
- `src/TUnit.Templates/content/TUnit.FSharp/.template.config/ide.host.json` (+9 −0)
- `src/TUnit.Templates/content/TUnit.FSharp/.template.config/template.json` (+10 −1)
- `src/TUnit.Templates/content/TUnit.FSharp/TestProject.fsproj` (+3 −0)
- `src/TUnit.Templates/content/TUnit.VB/.template.config/dotnetcli.host.json` (+9 −0)
- `src/TUnit.Templates/content/TUnit.VB/.template.config/ide.host.json` (+9 −0)
- `src/TUnit.Templates/content/TUnit.VB/.template.config/template.json` (+10 −1)
- `src/TUnit.Templates/content/TUnit.VB/TestProject.vbproj` (+3 −0)
- `src/TUnit.Templates/content/TUnit/.template.config/dotnetcli.host.json` (+9 −0)
- `src/TUnit.Templates/content/TUnit/.template.config/ide.host.json` (+9 −0)
- `src/TUnit.Templates/content/TUnit/.template.config/template.json` (+7 −0)
- `src/TUnit.Templates/content/TUnit/TestProject.csproj` (+4 −1)

## Commits

55 commits; dependency bumps not listed.

- chore: update benchmark results (#6845)
- chore: update mock benchmark results (#6846)
- docs: consolidate agent instructions in AGENTS.md
- chore: update mock benchmark results (#6849)
- chore: update mock benchmark results (#6852)
- feat(templates): add enableDotCover flag (#6714) (#6844)
- fix: don't request semantic models for attribute syntax from other compilations (DevKit crash) (#6855)
- fix(ci): restore net472 PublicAPI tests on Windows (#6857)
- perf(html-report): stream report JSON through pooled chunks and overlap sidecar serialization (#6860)
- chore(renovate): cap Microsoft.Build packages below 18.10.0 (#6863)
- perf: shrink generated per-class test source static constructors (~40% less startup JIT) (#6859)
- refactor: remove unreachable decimal source-text path from GenerateAttributeInstantiation (#6856)
- perf: cut per-test allocations in discovery and execution (-61% at 10k tests) (#6861)
- perf: stop hashing per-test event receivers during registration (data-driven tests 2.9x faster at 10k) (#6858)
- +semver:minor - perf(analyzers): cut TUnit analyzer build time ~60% on large test projects (#6862)
- chore: update mock benchmark results (#6865)
- chore: update mock benchmark results (#6875)
- chore: update mock benchmark results (#6880)
- fix: preserve TRX results when session cleanup fails (#6879)
- chore: update mock benchmark results (#6884)
- fix: preserve JUnit results after session cancellation (#6882)
- feat: warn when setup hooks pass the test execution token (#6883)
- fix: complete DedicatedThreadExecutor tests only after CleanUp() returns (#6886)
- fix: skip Ctrl+C handling where Console.CancelKeyPress is unsupported (#6889)
- chore: update benchmark results (#6894)
- chore: update mock benchmark results (#6895)
- feat: let registration receivers clear parallel constraints and limiter (#6897)
- +semver:minor - fix(mocks): emit valid lambdas for Task/ValueTask-returning delegate mocks (#6896)
- fix: don't run DedicatedThreadExecutor continuations inline on the dedicated thread (#6898)

> Truncated by the GitHub compare API; the compare link above has the full list.
