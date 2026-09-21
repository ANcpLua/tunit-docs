# TUnit v1.68.4 → v1.68.17

Compare: https://github.com/thomhurst/TUnit/compare/v1.68.4...v1.68.17

## Releases

### v1.68.17

* fix(mocks): emit init accessors for init-only properties and indexers by @thomhurst in https://github.com/thomhurst/TUnit/pull/6833
* fix(mocks): let one type be mocked regularly and wrapped in one compilation by @thomhurst in https://github.com/thomhurst/TUnit/pull/6835
* fix(mocks): keep editors in sync with publicized project references (#6836) by @thomhurst in https://github.com/thomhurst/TUnit/pull/6837

## Public API

No public API change.

## Library code (src/)

- `src/TUnit.Mocks.SourceGenerator/Builders/MockImplBuilder.cs` (+31 −14)
- `src/TUnit.Mocks.SourceGenerator/Builders/MockMembersBuilder.cs` (+5 −1)
- `src/TUnit.Mocks.SourceGenerator/Builders/MockWrapperTypeBuilder.cs` (+46 −10)
- `src/TUnit.Mocks.SourceGenerator/Discovery/GeneratedNameCollisionDetector.cs` (+1 −6)
- `src/TUnit.Mocks.SourceGenerator/Discovery/MemberDiscovery.cs` (+69 −5)
- `src/TUnit.Mocks.SourceGenerator/Discovery/MockTypeIdentity.cs` (+17 −0)
- `src/TUnit.Mocks.SourceGenerator/Discovery/SharedMemberSurfaceResolver.cs` (+57 −0)
- `src/TUnit.Mocks.SourceGenerator/MockGenerator.cs` (+21 −3)
- `src/TUnit.Mocks.SourceGenerator/Models/MockExplicitInterfaceSlot.cs` (+5 −1)
- `src/TUnit.Mocks.SourceGenerator/Models/MockMemberModel.cs` (+18 −0)
- `src/TUnit.Mocks.SourceGenerator/Models/MockTypeModel.cs` (+12 −0)
- `src/TUnit.Mocks/TUnit.Mocks.InternalsAccess.targets` (+25 −0)
- `src/TUnit.Templates/content/TUnit.Aspire.Starter/ExampleNamespace.ServiceDefaults/ExampleNamespace.ServiceDefaults.csproj` (+2 −2)

## Commits

13 commits; dependency bumps not listed.

- chore: update mock benchmark results (#6826)
- chore: update mock benchmark results (#6830)
- fix(mocks): emit init accessors for init-only properties and indexers (#6833)
- fix(mocks): let one type be mocked regularly and wrapped in one compilation (#6835)
- fix(mocks): keep editors in sync with publicized project references (#6836) (#6837)
