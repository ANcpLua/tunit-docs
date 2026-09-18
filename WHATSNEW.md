# TUnit v1.67.0 → v1.68.4

Compare: https://github.com/thomhurst/TUnit/compare/v1.67.0...v1.68.4

## Releases

### v1.68.0

* chore: switch to fillable checkboxes for issue templates by @radmorecameron in https://github.com/thomhurst/TUnit/pull/6795
* Add functionality to TUnit.Playwright to easily record videos for tests by @dahlsailrunner in https://github.com/thomhurst/TUnit/pull/6799
* docs: clarify thread pool usage in parallel tests by @thomhurst in https://github.com/thomhurst/TUnit/pull/6817
* Fix mocking events with ref struct arguments by @thomhurst in https://github.com/thomhurst/TUnit/pull/6814
* Fix TUnit0023 false positives for disposal through casts by @thomhurst in https://github.com/thomhurst/TUnit/pull/6818
* @radmorecameron made their first contribution in https://github.com/thomhurst/TUnit/pull/6795
* @dahlsailrunner made their first contribution in https://github.com/thomhurst/TUnit/pull/6799

### v1.68.4

* Add installable TUnit documentation routing skill by @thomhurst in https://github.com/thomhurst/TUnit/pull/6823

## Public API

#### Playwright_Library

```diff
@@ -1,3 +1,4 @@
+[assembly: .(@", PublicKey=0024000004800000940000000602000000240000525341310004000001000100698a70398fa0b2230c5a72e3bd9d56b48f809f6173e49a19fbb942d621be93ad48c5566b47b28faabc359b9ad3ff4e00bbdea88f5bdfa250f391fedd28182b2e37b55d429c0151a42a98ea7a5821818cd15a79fef9903e8607a88304cf3e0317bf86ec96e32e1381535a6582251e5a6eed40b5a3ed82bc444598b1269cce57a7")]
 [assembly: .(".NETCoreApp,Version=v10.0", FrameworkDisplayName=".NET 10.0")]
 namespace 
 {
@@ -120,6 +121,17 @@ namespace
         public static . PlaywrightSetup() { }
         public static void SetDefaultExpectTimeout(float timeout) { }
     }
+    [(.Method)]
+    public class RecordVideoAttribute : .TUnitAttribute, ., ., .
+    {
+        public RecordVideoAttribute(string path = "playwright-artifacts", int width = 1280, int height = 1400) { }
+        public int Height { get; }
+        public int Order { get; }
+        public string Path { get; }
+        public int Width { get; }
+        public . OnTestDiscovered(.DiscoveredTestContext discoveredTestContext) { }
+        public . OnTestEnd(.TestContext context) { }
+    }
     public class TUnitPlaywrightSettings
     {
         public .BrowserNewContextOptions? DefaultBrowserNewContextOptions { get; set; }
```

## Library code (src/)

- `src/TUnit.Analyzers/DisposableFieldPropertyAnalyzer.cs` (+21 −13)
- `src/TUnit.Core/Interfaces/ITestAttemptInitializer.cs` (+12 −0)
- `src/TUnit.Core/ObjectInitializer.cs` (+10 −0)
- `src/TUnit.Core/Tracking/ObjectTracker.cs` (+3 −0)
- `src/TUnit.Engine/Services/EventReceiverOrchestrator.cs` (+13 −0)
- `src/TUnit.Mocks.SourceGenerator/Builders/EventRaiserBuilder.cs` (+63 −0)
- `src/TUnit.Mocks.SourceGenerator/Builders/MockImplBuilder.cs` (+27 −34)
- `src/TUnit.Mocks.SourceGenerator/Builders/MockMembersBuilder.cs` (+15 −4)
- `src/TUnit.Mocks.SourceGenerator/Discovery/MemberDiscovery.cs` (+4 −3)
- `src/TUnit.Mocks.SourceGenerator/Extensions/MethodSymbolExtensions.cs` (+22 −1)
- `src/TUnit.Mocks.SourceGenerator/Models/MockEventModel.cs` (+6 −0)
- `src/TUnit.Mocks.SourceGenerator/Models/MockParameterModel.cs` (+8 −0)
- `src/TUnit.Playwright/BrowserFixture.cs` (+1 −1)
- `src/TUnit.Playwright/BrowserTest.cs` (+43 −19)
- `src/TUnit.Playwright/ContextFixture.cs` (+28 −10)
- `src/TUnit.Playwright/ContextTest.cs` (+2 −7)
- `src/TUnit.Playwright/PageFixture.cs` (+20 −5)
- `src/TUnit.Playwright/PlaywrightContextOptions.cs` (+36 −0)
- `src/TUnit.Playwright/PlaywrightFixtureLifecycle.cs` (+78 −0)
- `src/TUnit.Playwright/PlaywrightRecordingScope.cs` (+56 −0)
- `src/TUnit.Playwright/PlaywrightVideoRecorder.cs` (+148 −0)
- `src/TUnit.Playwright/RecordVideoAttribute.cs` (+57 −0)
- `src/TUnit.Playwright/TUnit.Playwright.csproj` (+1 −0)
- `src/TUnit.Templates/content/TUnit.Aspire.Starter/ExampleNamespace.AppHost/ExampleNamespace.AppHost.csproj` (+3 −3)
- `src/TUnit.Templates/content/TUnit.Aspire.Starter/ExampleNamespace.WebApp/ExampleNamespace.WebApp.csproj` (+1 −1)

## Commits

25 commits; dependency bumps not listed.

- chore: switch to fillable checkboxes for issue templates (#6795)
- chore: update benchmark results (#6797)
- chore: update mock benchmark results (#6798)
- chore: update mock benchmark results (#6802)
- chore: update mock benchmark results (#6810)
- Add functionality to TUnit.Playwright to easily record videos for tests (#6799)
- docs: clarify thread pool usage in parallel tests (#6817)
- Support Playwright video recording with composition fixtures (#6816)
- Fix mocking events with ref struct arguments (#6814)
- +semver:minor - fix: recognize cast disposal in TUnit0023 (#6818)
- chore: update mock benchmark results (#6820)
- Add installable TUnit documentation routing skill (#6823)
