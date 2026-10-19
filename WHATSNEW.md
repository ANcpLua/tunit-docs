# TUnit v1.68.17 → v1.75.0

Compare: https://github.com/thomhurst/TUnit/compare/v1.68.17...v1.75.0

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
- `src/TUnit.Analyzers/AnalyzerReleases.Unshipped.md` (+2 −1)
- `src/TUnit.Analyzers/AssemblyTestHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/BeforeHookAsyncLocalAnalyzer.cs` (+5 −1)
- `src/TUnit.Analyzers/ClassDataSourceConstructorAnalyzer.cs` (+3 −5)
- `src/TUnit.Analyzers/ClassHooksAnalyzer.cs` (+8 −8)
- `src/TUnit.Analyzers/CombinedDataSourceAnalyzer.cs` (+18 −7)
- `src/TUnit.Analyzers/ConflictingExplicitAttributesAnalyzer.cs` (+4 −4)
- `src/TUnit.Analyzers/ConsoleOutAnalyzer.cs` (+1 −1)
- `src/TUnit.Analyzers/DependsOnConflictAnalyzer.cs` (+7 −0)
- `src/TUnit.Analyzers/DiagnosticIds.cs` (+1 −0)
- `src/TUnit.Analyzers/DisposableFieldPropertyAnalyzer.cs` (+92 −22)
- `src/TUnit.Analyzers/Extensions/AttributeExtensions.cs` (+37 −25)
- `src/TUnit.Analyzers/Extensions/MethodExtensions.cs` (+9 −16)
- `src/TUnit.Analyzers/Extensions/ParameterExtensions.cs` (+4 −4)
- `src/TUnit.Analyzers/Extensions/PropertyExtensions.cs` (+1 −1)
- `src/TUnit.Analyzers/Extensions/SymbolExtensions.cs` (+3 −3)
- `src/TUnit.Analyzers/Extensions/SyntaxExtensions.cs` (+0 −21)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.GloballyQualified.cs` (+129 −0)
- `src/TUnit.Analyzers/Extensions/TypeExtensions.cs` (+5 −15)
- `src/TUnit.Analyzers/ForbidRedefiningAttributeUsageAnalyzer.cs` (+4 −2)
- `src/TUnit.Analyzers/Helpers/TUnitSymbols.cs` (+228 −0)
- `src/TUnit.Analyzers/Helpers/WellKnown.cs` (+1 −0)
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
- `src/TUnit.Analyzers/PublicMethodMissingTestAttributeAnalyzer.cs` (+9 −1)
- `src/TUnit.Analyzers/Resources.Designer.cs` (+3 −3)
- `src/TUnit.Analyzers/Resources.resx` (+15 −6)
- `src/TUnit.Analyzers/Rules.cs` (+3 −0)
- `src/TUnit.Analyzers/SingleTUnitAttributeAnalyzer.cs` (+7 −1)
- `src/TUnit.Analyzers/TestDataAnalyzer.cs` (+33 −20)
- `src/TUnit.Analyzers/TimeoutCancellationTokenAnalyzer.cs` (+97 −4)
- `src/TUnit.AspNetCore.Analyzers/WebApplicationFactoryAccessAnalyzer.cs` (+35 −67)
- `src/TUnit.AspNetCore.Core/Http/TUnitHttpClientFilter.cs` (+53 −0)
- `src/TUnit.AspNetCore.Core/Interception/HttpExchangeCaptureExtensions.cs` (+21 −1)
- `src/TUnit.AspNetCore.Core/TUnit.AspNetCore.Core.csproj` (+1 −10)
- `src/TUnit.AspNetCore.Core/TestWebApplicationFactory.cs` (+28 −9)
- `src/TUnit.AspNetCore.Core/TracedWebApplicationFactory.cs` (+12 −3)
- `src/TUnit.AspNetCore.Core/WebApplicationTest.cs` (+182 −39)
- `src/TUnit.Assertions.Analyzers.CodeFixers/XUnitAssertionCodeFixProvider.cs` (+8 −2)
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
- `src/TUnit.Assertions.SourceGenerator/Generators/AssertionExtensionGenerator.cs` (+218 −176)
- `src/TUnit.Assertions.SourceGenerator/Generators/AssertionMethodGenerator.cs` (+266 −179)
- `src/TUnit.Assertions.SourceGenerator/Generators/CollectionShapeAssertionGenerator.cs` (+4 −3)
- `src/TUnit.Assertions.SourceGenerator/Generators/CollectionShapeRegistry.cs` (+2 −1)
- `src/TUnit.Assertions.SourceGenerator/Generators/CovarianceHelper.cs` (+2 −2)
- `src/TUnit.Assertions.SourceGenerator/Generators/MethodAssertionGenerator.cs` (+196 −82)
- `src/TUnit.Assertions.SourceGenerator/Shared/AttributeForwardingFormatters.cs` (+2 −1)
- `src/TUnit.Assertions.SourceGenerator/TUnit.Assertions.SourceGenerator.csproj` (+5 −0)
- `src/TUnit.Assertions/Conditions/DirectoryInfoAssertionExtensions.cs` (+1 −0)
- `src/TUnit.Assertions/Conditions/FileInfoAssertionExtensions.cs` (+2 −0)
- `src/TUnit.Assertions/Conditions/FileSystemAssertions.cs` (+25 −3)
- `src/TUnit.Assertions/TUnit.Assertions.props` (+0 −4)
- `src/TUnit.Core.SourceGenerator/Analyzers/ITestAnalyzer.cs` (+0 −36)
- `src/TUnit.Core.SourceGenerator/Analyzers/TestMethodAnalyzer.cs` (+0 −132)
- `src/TUnit.Core.SourceGenerator/CodeGenerationHelpers.cs` (+6 −192)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/DynamicTestsGenerator.cs` (+6 −7)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Equality/PreventCompilationTriggerOnEveryKeystrokeComparer.cs` (+0 −39)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Formatting/TypedConstantFormatter.cs` (+18 −18)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/GenericTypeHelper.cs` (+0 −65)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/InstanceFactoryGenerator.cs` (+2 −1)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Helpers/TupleArgumentHelper.cs` (+11 −10)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/InfrastructureGenerator.cs` (+134 −11)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/StaticPropertyInitializationGenerator.cs` (+144 −69)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Writers/AttributeWriter.cs` (+49 −30)
- `src/TUnit.Core.SourceGenerator/CodeGenerators/Writers/SourceInformationWriter.cs` (+1 −43)
- `src/TUnit.Core.SourceGenerator/Enums/HookLocationType.cs` (+0 −8)
- `src/TUnit.Core.SourceGenerator/Extensions/AttributeDataExtensions.cs` (+53 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/ObjectExtensions.cs` (+6 −0)
- `src/TUnit.Core.SourceGenerator/Extensions/TypeExtensions.cs` (+1 −1)
- `src/TUnit.Core.SourceGenerator/Generators/AotConverterGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/AttributePolyfillGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/DynamicDependencyPolyfillGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/HookMetadataGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/ModuleInitializerPolyfillGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/PropertyInjectionSourceGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Generators/TestMetadataGenerator.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Helpers/FileNameHelper.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/ClassTestGroup.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/DataSourceModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/DynamicTestModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/HookClassGroup.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/HookModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/TestMethodModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/Extracted/TypedConstantModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/HooksDataModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/TestDescriptorModel.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/TestMetadataGenerationContext.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/TestMethodGenerationResult.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/TestMethodMetadata.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Models/TestMethodSourceCode.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Properties/AssemblyInfo.cs` (+0 −0)
- `src/TUnit.Core.SourceGenerator/Utilities/MetadataGenerationHelper.cs` (+0 −0)
- `src/TUnit.Core/AmbientContexts.cs` (+0 −0)
- `src/TUnit.Core/Attributes/TestData/MatrixDataSourceAttribute.cs` (+0 −0)
- `src/TUnit.Core/Attributes/TestData/PairwiseDataSourceAttribute.cs` (+0 −0)
- `src/TUnit.Core/Attributes/TestMetadata/ExcludeOnAttribute.cs` (+0 −0)
- `src/TUnit.Core/Attributes/TestMetadata/RunOnAttribute.cs` (+0 −0)
- `src/TUnit.Core/ContextProvider.cs` (+0 −0)
- `src/TUnit.Core/Contexts/TestRegisteredContext.cs` (+0 −0)
- `src/TUnit.Core/Data/ThreadSafeDictionary.cs` (+0 −0)
- `src/TUnit.Core/Discovery/ObjectGraphDiscoverer.cs` (+0 −0)
- `src/TUnit.Core/EngineCancellationToken.cs` (+0 −0)
- `src/TUnit.Core/Executors/DedicatedThreadExecutor.cs` (+0 −0)
- `src/TUnit.Core/Executors/STAThreadExecutor.cs` (+0 −0)
- `src/TUnit.Core/Helpers/ClassConstructorHelper.cs` (+0 −0)
- `src/TUnit.Core/Helpers/LazyAttributeDictionary.cs` (+0 −0)
- `src/TUnit.Core/Helpers/MatrixParameterValues.cs` (+0 −0)
- `src/TUnit.Core/Helpers/PairwiseStrategy.cs` (+0 −0)
- `src/TUnit.Core/Hooks/AfterAssemblyHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/AfterClassHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/AfterTestDiscoveryHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/AfterTestHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/AfterTestSessionHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/BeforeAssemblyHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/BeforeClassHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/BeforeTestDiscoveryHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/BeforeTestHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/BeforeTestSessionHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/HookBodyInvoker.cs` (+0 −0)
- `src/TUnit.Core/Hooks/InstanceHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Hooks/StaticHookMethod.cs` (+0 −0)
- `src/TUnit.Core/Models/AssemblyHookContext.cs` (+0 −0)
- `src/TUnit.Core/Models/ClassHookContext.cs` (+0 −0)
- `src/TUnit.Core/Models/TestBuildContext.cs` (+0 −0)
- `src/TUnit.Core/Models/TestDiscoveryContext.cs` (+0 −0)

## Commits

191 commits; dependency bumps not listed.

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
- perf: lighter per-test trace bookkeeping for the HTML report (-12% allocations at 10k tests) (#6910)
- perf(html-report): serialize large report arrays in parallel and optimize hot writers (#6911)
- perf: emit source-generated test types after user code to avoid slow Defender scans (#6908)
- perf(source-gen): bound generated test-entry methods (data-driven startup JIT -45%) (#6909)
- fix: avoid blocking waiting callers during IAsyncInitializer initialization (#6906)
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

> Truncated by the GitHub compare API; the compare link above has the full list.
