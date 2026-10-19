import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
NOTES = (
    "* Fixed by @ForNeVeR and @org/team.\n"
    "* @someone made their first contribution.\n"
    "Email first.last+docs@example.org\n"
    "[@ForNeVeR](https://github.com/ForNeVeR) and `@someone`\n\n"
    "An unmatched `backtick.\n\nThanks @ForNeVeR.\n\nAnother `backtick.\n"
)


class PrDescriptionTests(unittest.TestCase):
    def test_release_creation_and_update(self):
        for existing in (False, True):
            with self.subTest(existing=existing):
                self.check_description(existing=existing)

    def test_release_without_doc_changes(self):
        self.check_description(docs_changed=False)

    def test_docs_refresh(self):
        self.check_description(release=False)

    def check_description(self, existing=False, release=True, docs_changed=True):
        workflow = (ROOT / ".github/workflows/weekly-tunit.yml").read_text()
        step = workflow.split("      - name: Open or update the PR\n", 1)[1]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            folder = Path(directory)
            repo = folder / "repo"
            repo.mkdir()

            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=repo, check=True, capture_output=True, text=True
                ).stdout

            remote = folder / "remote.git"
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            git("init", "-b", "main")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            git("config", "commit.gpgsign", "false")
            git("remote", "add", "origin", str(remote))
            (repo / "docs").mkdir()
            (repo / "docs/page.md").write_text("Before\n")
            (repo / "VERSION").write_text("v1\n")
            (repo / "WHATSNEW.md").write_text(NOTES)
            git("add", "-A")
            git("commit", "-m", "Initial")
            if release:
                (repo / "VERSION").write_text("v2\n")
            if docs_changed:
                (repo / "docs/page.md").write_text("After\n")

            bin_dir = folder / "bin"
            bin_dir.mkdir()
            gh = bin_dir / "gh"
            gh.write_text(
                "#!/usr/bin/env bash\nset -eu\n"
                'if [ "$1 $2" = "pr view" ]; then\n'
                '  if [ "$TUNIT_EXISTING" = 1 ]; then echo OPEN; exit 0; fi\n'
                "  exit 1\nfi\n"
                'printf "%s\\n" "$2" > "$TUNIT_ACTION"\n'
                'for ((i=1; i<=$#; i++)); do\n'
                '  if [ "${!i}" = "--body-file" ]; then\n'
                '    j=$((i+1)); cp "${!j}" "$TUNIT_CAPTURE"\n'
                '  fi\ndone\n'
            )
            gh.chmod(0o755)
            capture = folder / "captured.md"
            action = folder / "action.txt"
            env = dict(
                os.environ, OLD="v1", NEW="v2" if release else "v1",
                GITHUB_SERVER_URL="https://github.com", GITHUB_REPOSITORY="ANcpLua/tunit-docs",
                TUNIT_EXISTING="1" if existing else "0", TUNIT_CAPTURE=str(capture),
                TUNIT_ACTION=str(action), PATH=str(bin_dir) + os.pathsep + os.environ["PATH"],
            )
            subprocess.run(
                ["bash", "-e", "-o", "pipefail", "-c", script.replace("/tmp/pr-body.md", str(folder / "body.md"))],
                cwd=repo, env=env, check=True, capture_output=True, text=True,
            )
            body = capture.read_text()
            self.assertNotIn("@", body)
            self.assertEqual(NOTES, git("show", "HEAD:WHATSNEW.md"))
            self.assertEqual("edit" if existing else "create", action.read_text().strip())
            if release:
                self.assertIn(f"/blob/{git('rev-parse', 'HEAD').strip()}/WHATSNEW.md", body)
            else:
                self.assertIn("No new TUnit release", body)
                self.assertNotIn("WHATSNEW.md", body)
            self.assertIn("docs/page.md" if docs_changed else "No page changed.", body)


if __name__ == "__main__":
    unittest.main()
